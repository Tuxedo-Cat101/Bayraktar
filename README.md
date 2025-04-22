This is a project where we take a Tello Drone, fly it through hulahoops and it detects the color of said hulahoop.

Team Members: Connor, Teagan, Logan(Logiebear)

Instructions: Before running, ensure pandas is installed by running the following prompt(without the parantheses) in the Visual Studio terminal:
                "pip install pandas"
              Turn on the drone, wait for a flashing yellow light on said drone, then connect your device to the drone.
              Run the code
              Running the code should automatically connect the drone, you should get two tabs to pop-up, the pygame and camera feed.
              The pygame tab must be selected to do controls for the drone.
    Controls:
             Arrow Keys: Move the drone along the x-axis(forward, backward, left, right)
             W/S Keys: W moves the drone up, S moves the drone down
             A/D Keys: A rotates the drone left, D rotates the drone right
             L/T Keys: L automatically lands the drone and turns it off, T automatically takeoffs the drone
             F Key: F causes the drone to execute a flip forward
             Double clicking in the live feed tab will get the color of the double clicked area and put the name of the color in colour.txt
             Pressing the Escape Key in the live feed tab will close all tabs and end the program
