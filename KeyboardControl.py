import cv2
from djitellopy import tello
import webcolors
import keypress as kp
import time
from PIL import Image
from collections import Counter

kp.init()
drone = tello.Tello()
drone.connect()
drone.streamon()
# global img
# global x_pressed
clicked = False

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
    
    # if kp.getKey("x") and not x_pressed:
    #     filename = f"Resources/Images/{i}.jpg"
    #     cv2.imwrite(filename, img)
    #     writetofile(filename)
    #     i += 1
    #     x_pressed = True
    
    # if not kp.getKey("x") and x_pressed:
    #     x_pressed = False
    
    return[lr, fb, up, yv]

# def find_dominant_color(filename):
#     width, height = 150, 150
#     try:
#         # Open and resize the image
#         image = Image.open(filename)
#         image = image.resize((width, height), resample=0)
        
#         # Get the list of pixels
#         pixels = image.getcolors(width * height)
        
#         # Use Counter to count the frequencies of each color
#         pixel_counts = Counter([pixel[1] for pixel in pixels])
        
#         # Find the most common color
#         dominant_color = pixel_counts.most_common(1)[0][0]
        
#         # Get the name of the dominant color
#         dominant_color_name = get_colour_name(dominant_color)
        
#         return dominant_color_name
#     except Exception as e:
#         print(f"Error processing the image: {e}")
#         return None

# def writetofile(filename):
#     dominant_color = find_dominant_color(filename)
#     if dominant_color:
#         with open("colour.txt", "a") as f:
#             f.write(f"{dominant_color}\n")

# def get_colour_name(rgb_triplet):
#     try:
#         hex_value = webcolors.rgb_to_hex(rgb_triplet)
#         return webcolors.hex_to_name(hex_value)
#     except ValueError:
#         return closest_colour(rgb_triplet)

# def closest_colour(requested_colour):
#     min_colours = {}
#     for name in webcolors.names("css3"):
#         r_c, g_c, b_c = webcolors.name_to_rgb(name)
#         rd = (r_c - requested_colour[0]) ** 2
#         gd = (g_c - requested_colour[1]) ** 2
#         bd = (b_c - requested_colour[2]) ** 2
#         min_colours[(rd + gd + bd)] = name
#     return min_colours[min(min_colours.keys())]

while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (720,480))
    cv2.imshow("Feed", img)
    time.sleep(0.05)