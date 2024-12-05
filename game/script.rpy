# Characterrs
define protag = False # True=black, false=white
define red = Character(_("Vermilion"), color="#E34234")
define orange = Character(_("Persimmon"), color="#EC5800")
define yellow = Character(_("Maize"), color="#FBEC5D")
define green = Character(_("Aventurine"), color="#04b75a")
define blue = Character(_("Aoi/Azure"), color="#007FFF")
define purple = Character(_("Orchid"), color="#DA70D6")
define grey = Character(_("Ash"), color="#B2BEB5")
define mystery = Character(("???"), color="#804103")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    #Note: It'll be clarified who's actually talking where when sprites are added
    mystery "You ready to go inside?" #White
    mystery "Eh, might as well." #Black
    mystery "First we gotta figure out who's heading this." #White
    mystery "Then they gotta make a choice." #black

    menu:
        "Chose Your Protagonist"
        "The White One":
            $ protag = False
            define black = Character(_("Onyx"), color="#000000") # Support
            define white = Character("[povname]", color="#ffffff")
            python:
                povname = renpy.input("What is your name?", length=32)
                povname = povname.strip()

                if not povname:
                    povname = "Quartz"

            black "Come on, let's go [povname]."
            jump charIntro
        "The Black One":
            $ protag = True
            define white = Character(_("Quartz"), color="#ffffff") # Support
            define black = Character("[povname]", color="#000000")
            python:
                povname = renpy.input("What is your name?", length=32)
                povname = povname.strip()

                if not povname:
                    povname = "Onyx"

            white "You ready [povname]?"
            jump charIntro

    label charIntro:



    # This ends the game.
    return
