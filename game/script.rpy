﻿# Characterrs
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
    mystery "Yeah! But... aren't you forgetting something?" #Black
    mystery "Right, first we gotta figure out who's heading this." #White
    mystery "Then they gotta make a choice." #black 

    menu:
        "Chose Your Protagonist"
        "The White Twin":
            $ protag = False
            define black = Character(_("Onyx"), color="#000000") # Support
            define white = Character("[povname]", color="#ffffff")
            python:
                povname = renpy.input("So... what's your name?", length=32)
                povname = povname.strip()
                if not povname:
                    povname = "Quartz"
            black "Come on, let's go [povname]!"
            jump charIntro
        "The Black Twin":
            $ protag = True
            define white = Character(_("Quartz"), color="#ffffff") # Support
            define black = Character("[povname]", color="#000000")
            python:
                povname = renpy.input("What is your name?", length=32)
                povname = povname.strip()
                if not povname:
                    povname = "Onyx"
            white "Alright, are you actually ready now [povname]?"
            jump charIntro

    label charIntro:
        if protag == True:
            white "It looks like we're the last ones to arrive."
            white "If only you were a little faster."
            black "Sorry..."
            white "Whatever. They should all be decent."
        if protag == False:
            black "Shoot, we're late!"
            white "I'm sure it'll be fine."
            black "But I don't wanna make a bad first impression..."
        #Ver
        mystery "Tch, there's still more people coming?"
        #Simeon
        mystery "Don't be like that. It's always nice to see new faces!"
        #Maize
        mystery "They better be interesting."
        #Turine
        mystery "I'm sure at least one of the two is."
        #Azure
        mystery "As long as they don't bother my work, I don't care."
        #Orchid
        mystery "D-don't you think we should try talking?"
        #Ash
        mystery "..."
        if protag == True:
            white "Go say hi to someone."
            black "What are you going to do?"
            white "Follow you, duh."
            menu:
                "Who will you talk to first?"
                "Red":
                    jump verRoute
                "Orange":
                    jump perRoute
                "Yellow":
                    jump maizeRoute
                "No One":
                    jump ashRoute
        if protag == False:
            black "Come on, let's go talk!"
            white "Fine."
            menu:
                "Who Will You Approach?"
                "Green":
                    jump turineRoute
                "Blue":
                    jump azureRoute
                "Purple":
                    jump orchidRoute
                "No One":
                    jump ashRoute
    
    label verRoute:
        #Red
    
    label perRoute:
        #Orange
    
    label maizeRoute:
        #Yellow
    
    label turineRoute:
        #Green
    
    label azureRoute:
        #Blue
    
    label orchidRoute:
        #Purple
    
    label ashRoute:
        #Grey
