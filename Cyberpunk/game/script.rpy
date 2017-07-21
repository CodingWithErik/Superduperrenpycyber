# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# Characters
define e = Character("Test", color="#ffffff")
        
# Backgrounds
image bg0 = "images/testbg0.jpg"
image bg1 = "images/testbg1.jpg"
image bg2 = "images/testbg2.jpg"


# Ambience


label start:

    scene bg0
    with fade

    # Prologue

    "The highway has some solitary cars driving along above the neon lit city at breakneck speeds. You’ve been driving this route home for so long it’s second nature."
    
    "You’ve been overworked lately and worry that you will be too tired to do anything but go directly to sleep when you get home, much to your wife’s chagrin."
    
    "You heave a sigh, fingers tightening on the steering wheel as you briefly look down as you drive on a straight stretch of road, thumb and forefinger moving to massage the bridge of your nose."
    
    "Something strikes the wheel and you hear a loud pop and the sound of metal against asphalt. The car begins to veer right and in a panic you turn it in the opposite direction to compensate."
    
    "A few tense moments later and the car is spinning out, going off the side of the autobahn and plunging into the dark streets below."
    
    "As if it is happening to someone else, you sense the weight of the car slam and roll, before darkness overtakes you."

    # Scene 2
    
    scene bg1
    
    e"Scene2"
    
    return