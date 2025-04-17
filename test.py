import cv2
import pandas as pd
from djitellopy import tello
import time
import keypress as kp
from collections import Counter
from PIL import Image
import webcolors

kp.init()
drone = tello.Tello()
drone.connect()
drone.streamon()
img = drone.get_frame_read().frame
img = cv2.resize(img, (480,480))

# declaring global variables (are used later on)
clicked = False
r = g = b = x_pos = y_pos = 0

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

#Get keyboard input for drone control
def getKeyboardInput():
    lr, fb, up, yv = 0, 0, 0, 0
    speed = 50
    i = 0
    x_pressed = False
    
    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed
    
    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed
    
    if kp.getKey("w"): up = speed
    if kp.getKey("s"): up = -speed
    
    if kp.getKey("a"): yv = -speed
    if kp.getKey("d"): yv = speed
    
    if kp.getKey("l"): drone.land()
    if kp.getKey("t"): drone.takeoff()
    if kp.getKey("f"): drone.flip()
    
    return[lr, fb, up, yv]

# function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

def displayColorName(img, text):
    cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    
def closest_colour(r, g, b):
    min_colours = {}
    for name in webcolors.names("css3"):
        r_c, g_c, b_c = webcolors.name_to_rgb(name)
        rd = (r_c - r) ** 2
        gd = (g_c - g) ** 2
        bd = (b_c - b) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(r, g, b):
    try:
        hex_value = webcolors.rgb_to_hex((r,g,b))
        return webcolors.hex_to_name(hex_value)
    except ValueError:
        return closest_colour(r, g, b)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
    vals = getKeyboardInput()
    img = drone.get_frame_read().frame
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    cv2.imshow("image", img)
    time.sleep(0.05)
    if clicked:

        # cv2.rectangle(image, start point, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        # Creating text string to display( Color name and RGB values )
        text = get_colour_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        displayColorName(img, text)

        # For very light colours we will display text in black colour
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        with open("colour.txt", "a") as f:
            f.write(f"{text}\n")

        clicked = False
        
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()