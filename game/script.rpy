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
    black "{color=#E34234}Vermilion.{/color}"
    black "{color=#04b75a}Turine.{/color}"
    black "{color=#007FFF}Azure.{/color}"
    menu:
        "Who will you talk?"
        "Vermillion":
            jump verRoute
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
        "Stay Outside With Ver":
            jump verBad
        "Go Back To Class":
            jump verGood

    label verBad:
        black "I want to stay with you."
        red "What?"
        black "Don't look so shocked!"
        black "I told you, you mean a lot to me."
        red "..."
        black "(His face is all red. Did I make him mad?)"
        red "Thank you."
        black "Huh?"
        red "S-sorry it's just... no one has ever done that for me before."
        red "Or stick around really."
        black "I can't believe that."
        black "You're worth it for me."
        red "St-stop saying that!"
        black "Why? It's true."
        red "..."
        black "(I guess he's not mad.)"
        black "(I didn't realize he'd be easy to tease like this.)"
        black "Hehe."
        #hide
        black "(It was nice.)"
        black "(But nice times don't last forever.)"
        black "Hey Ver?"
        red "Yeah?"
        black "This might be a weird question but..."
        black "What color is your jacket?"
        red "Red, duh."
        red "It's the same one I always wear."
        black "It is?"
        black "Sorry, I must have just not slept well."
        red "You good?"
        black "I'm sure it'll be fine."
        black "It must just be the lighting."
        red "What color did you think it was?"
        black "Haha, this is gonna sound stupid."
        black "To me it looks almost..."
        black "Grey?"
        red "Grey? Weird."
        black "It is. It's not just that though."
        black "For some reason, when I look around, everything looks off."
        black "It's likely every color is fading."
        red "Oh- Oh no-"
        red "This wasn't supposed to happen-"
        black "What?"
        red "I didn't realize it would affect you oh my god-"
        black "What are you talking about?"
        red "You don't deserve this-"
        black "Ver!"
        red "I thought it was just a myth-"
        black "VER!"
        red "Sorry, I'm sorry."
        red "You deserved better than me. You always did."
        red "I wish I could love you better."
        black "Wait- where are you going?"
        red "I'm sorry [pov]."
        black "Ver?"
        black "Ver!"
        black "{b}VER! PLEASE!{/b}"
        black "(No matter what I said, no matter what I did, no matter how much I turned my heart, things never went back to normal.)"
        black "(It all simply faded to grey.)"
        "{color=#E34234}RED ROUTE: BAD{/color}"
        "{color=#E34234}Wanna see how else things could have turned out?{/color}"
        "{color=#E34234}Or maybe how things would go if you chose someone else.{/color}"
        return
    
    label verGood:
        black "I'm sorry, but I can't ignore school."
        red "Fine. Whatever. Do what you want."
        black "I'll see you later?"
        red "We'll see."
        black "(Why do I have such a bad feeling in my throat?)"
        #class
        black "(If I stop by the library, I should be able to grab a pod and study for an hour there.)"
        black "(Then I can work-)"
        black "Ah!"
        red "Cmon [pov], I thought you'd be harder to surprise."
        black "Ver???"
        red "Yeah. Turns out our classrooms are right next to each other."
        black "Wait- your class?"
        black "You went to class?"
        red "Yep."
        red "Annoyingly enough, you do have a point. I need to get my life together."
        black "I'm glad you're trying."
        red "I owe it to you."
        black "To me?"
        red "Do I have to repeat it? Without you, I don't know if I would've shown up today."
        red "So..."
        red "Thanks."
        black "Of course!"
        black "Hey, how about we pick somewhere a little less risky to hang out at?"
        red "Sure."
        black "I have an idea in mind already!"
        "{color=#E34234}RED ROUTE: GOOD{/color}"
        "{color=#E34234}Wanna see how else things could have turned out?{/color}"
        "{color=#E34234}Or maybe how things would go if you chose someone else.{/color}"
        return

#label maizeRoute:
    #Yellow

label turineRoute:
    #Green

label azureRoute:
    #Blue