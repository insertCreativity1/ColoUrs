# Characterrs
define protag = True # True=black, false=white
default pov = "A"
define red = Character(_("Vermilion"), color="#E34234")
define orange = Character(_("Persimmon"), color="#EC5800")
define yellow = Character(_("Maize"), color="#FBEC5D")
define green = Character(_("Turine"), color="#04b75a")
define blue = Character(_("Azure"), color="#007FFF")
define purple = Character(_("Orchid"), color="#DA70D6")
define grey = Character(_("Ash"), color="#B2BEB5")
define mystery = Character(("???"), color="#804103")

# The game starts here.

label start:
    scene bg room
    mystery '"Meet the love of your life here!"'
    mystery "I can't believe I'm really doing this..."
    mystery "Well, my twin said it was a good idea."
    mystery "I just need to write my name."
    define black = Character("[pov]", color="#000000")
    python:
        pov = renpy.input("What is your name?", length=32)
        pov = pov.strip()
        if not pov:
            pov = "Onyx"
    black "Alright, let's do this."
    jump charIntro

label charIntro:
    black "It looks like there's a few options."
    black "I'm glad. Hopefully, one of them will be the right one."
    black "Let's see..."
    menu:
        "Who will you talk?"
        "Vermillion":
            jump verRoute
        "Maize":
            jump maizeRoute
        "Turine":
            jump turineRoute
        "Azure":
            jump azureRoute

label verRoute: # Passionate Assertive Tsun -- Bitter End
    #Setting: At the side of the school, a lone man sits on the floor. His backpack
    #is thrown aside, spilling open to show a variety of textbooks and half-filled notebooks.
    #He leans back, not realizing someone else had come near. 
    mystery "Ha..."
    black "(Huh? I didn't realize I would find anyone here.)"
    black "(I wonder if he's lonely.)"
    black "Hey there."
    mystery "What the-"
    mystery "The hell are you doing here?"
    black "I-I was just walking around!"
    mystery "Tch, whatever."
    black "Um... I'm {color=#000000}[pov].{/color} It's nice to meet you."
    red "{color=#E34234}Vermilion.{/color}"
    black "That's a really long name."
    red "Got a problem with that?"
    black "No! I mean- not with you. I mean-"
    black "Sorry, I'm rambling."
    black "I mean if it's okay if I just called you Ver."
    red "!-"
    red "Yeahsurewhatever."
    black "(Was that a blush I saw?)"
    black "(He's kinda cute like that.)"
    black "Hehe."
    red "What are you laughing about?"
    black "N-nothing!"
    black "Class is starting soon. We should head back inside."
    red "Eh. I'll go in eventually."
    red "I know that there's nothing important going on today though."
    black "So?"
    red "So it wouldn't be the worst day to skip."
    black "Skip?! Are you insane?!"
    red "Calm your pants down. It'll be fine."
    black "What makes you so sure?"
    red "I've done it before?"
    black "Well... if you think it's a good idea..."
    black "I'll do it once, okay?"
    black "I wanna get to know you."
    red "You're weird."
    black "So are you!"
    "--A few weeks later--"
    red "What's up [pov]?"
    black "Oh! Hey Ver."
    black "Can I ask you about something?"
    red "Sure."
    black "Why are you always skipping?"
    red "Tch, I'm not {i}always{/i} skipping."
    black "When was the last time you actually went to class?"
    red "I don't see how that's any of your business."
    black "I care about you though."
    red "!-"
    red "You..."
    red "You what?"
    black "I care about you. Was that not obvious?"
    black "We've been talking outside here for weeks, of course I care."
    red "If you care so much, then leave my habits alone."
    red "Or you can just go back to class. See if I care."
    black "Ver!"
    red "What?"
    red "Would you rather spend time out here with me or just follow the rules?"
    black "I..."
        menu:
            "Spend time with Ver":
                jump verBad
            "Go back to class":
                jump verGood

    label verBad:
        black "I want to stay with you."
    
    label verGood:
        black "I'm sorry, but I can't ignore school."

label maizeRoute:
    #Yellow

label turineRoute:
    #Green

label azureRoute:
    #Blue