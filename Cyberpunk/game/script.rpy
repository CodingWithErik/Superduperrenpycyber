# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# Characters
define e = Character("Test", color="50d4ff")
        
# Backgrounds

image bg1 = "images/testbg1.jpg"
image bg2 = "images/testbg2.jpg"


# Ambience


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Hello, world. Lorem Ipsum, etc."


    jump scene1

label scene1:
    
    scene bg1
    
    e"This is a new scene."
    
    return