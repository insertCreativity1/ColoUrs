# Characterrs
define protag = True # True=black, false=white
default pov = "A"
define red = Character(_("Vermilion"), color="#E34234")
define orange = Character(_("Persimmon"), color="#EC5800")
define yellow = Character(_("Maize"), color="#FBEC5D")
define green = Character(_("Aventurine"), color="#04b75a")
define blue = Character(_("Azure"), color="#007FFF")
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
            define white = Character("[pov]", color="#ffffff")
            python:
                pov = renpy.input("So... what's your name?", length=32)
                pov = pov.strip()
                if not pov:
                    pov = "Quartz"
            black "Come on, let's go [pov]!"
            jump charIntro
        "The Black Twin":
            $ protag = True
            define white = Character(_("Quartz"), color="#ffffff") # Support
            define black = Character("[pov]", color="#000000")
            python:
                pov = renpy.input("What is your name?", length=32)
                pov = pov.strip()
                if not pov:
                    pov = "Onyx"
            white "Alright, are you actually ready now [pov]?"
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
        mystery "Hey there's more people coming."
        #Simeon
        mystery "Oh yay! It's always nice to see new faces!"
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
            white "Don't worry about it."
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
    
    label verRoute: # Passionate Assertive Tsun -- Bitter End
        mystery "You're... talking to me?"
        mystery "Nice."
        red "I'm {color=#E34234}Vermilion.{/color} It's nice to meet you or whatever."
        black "I'm [pov]. It's nice to meet you too!"
        red "Sure."
        black "It is. It's interesting meeting new people. And you seem interesting."
        red "Th-thanks..."
        black "(Is he blushing?)"
        black "(It's kinda cute.)"
        red "Tch, what are you laughing at?"
        black "It's nothing, you just... looked kinda cute there."
        red "!-"
        red "Th-that's-"
        red "Shut up!"
        black "Sorry..."
        black "I'm really sorry if I'm bothering you. I-I can go talk to someone else."
        red "No!"
        red "I mean, you don't have to."
        black "Oh- Oh!"
        black "Okay!"
        black "Maybe we can meet somewhere else to?"
        red "Why not?"
        "Five months later"
        black "Romance blah blah smooch"
    
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
