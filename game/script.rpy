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
    black "{color=#E34234}Vermilion.{/color} An assertive man, stubborn in his ideals. He holds his heart tightly so only those closest to him see it."
    black "{color=#04b75a}Turine.{/color} A wealthy man, calm in his demeaner. He looks after the sort of people that catch his attention."
    black "{color=#007FFF}Azure.{/color} An intelligent woman, determined in her passions."
    black '"Warning: You may forget the reason you entered depending on who you choose. This allows optimal immersion."'
    black "They really went all out for this, huh..."
    black "Well then, I think I'll choose-"
    menu:
        "Who {i}will{/i} you choose?"
        "Vermillion":
            jump verRoute
        "Turine":
            jump turineRoute
        "Azure":
            jump azureRoute

label verRoute:
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
    red "Would you rather just follow the rules or be with me?"
    black "I..."
    menu:
        "I need to go back.":
            jump verGood
        "I'll stay here.":
            jump verBad

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
        "{color=#E34234}RED ROUTE: GOOD!{/color}"
        "{color=#E34234}Wanna see how else things could have turned out?{/color}"
        "{color=#E34234}Or maybe how things would go if you chose someone else.{/color}"
        return

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
        "{color=#E34234}RED ROUTE: BAD.{/color}"
        "{color=#E34234}Wanna see how else things could have turned out?{/color}"
        "{color=#E34234}Or maybe how things would go if you chose someone else.{/color}"
        return

#label maizeRoute:
    #Yellow

label turineRoute:
    #Setting: A quiet, elegant garden on the school campus. It’s after hours, and Turine is seated
    #on a bench, surrounded by manicured hedges and expensive decor. The player notices him looking
    #out into the distance, lost in thought. There’s something magnetic about him, though he’s always
    #surrounded by an air of mystery.
    black "(Who is that? I’ve seen him around, but he’s never really talked to anyone...)"
    mystery "Ah, you. I’ve seen you around. You seem… interesting."
    black "Oh, um, hi. Do I know you?"
    mystery "Perhaps not, but you’ve piqued my curiosity."
    green "My name is {color=#04b75a}Turine.{/color}"
    green "It’s not every day someone as… captivating as you walks by."
    black "I’m not sure what you mean…"
    green "I think you do. But you’re more modest than I expected."
    black "(What is this feeling?)"
    black "(It's like he knows more about me than I know about myself.)"
    #Class
    "--The next day--"
    green "You’re stressed, aren’t you? I noticed you’ve been overworking yourself lately."
    green "It’s not good for you, you know. You should rest."
    black "What? How do you even—?"
    green "I have my ways of paying attention. You can’t hide everything from someone who’s paying close attention."
    green "And you know, there are things I could do to help."
    green "I could take care of those little problems in your life… you wouldn’t have to worry about a thing."
    green "I’m sure you’d like that, wouldn’t you?"
    black "(It'd be nice...)"
    black "(But...)"
    black "(It feels almost too nice.)"
    black "I… I don’t need help. I’m fine."
    green "Of course, you are. But sometimes, it’s okay to let someone take care of you. You wouldn’t have to lift a finger."
    green "Just think about it, okay?"
    black "(Somehow, I get the feeling just saying no wouldn't be enough for him.)"
    menu:
        "I'll think about it":
            jump turineGood
        "I'm fine on my own":
            jump turineBad

    label turineGood:
        "--A few weeks later--"
        green "You know, I’ve arranged something special for you. You’ve been working too hard, and you need to relax."
        green "You’re going to come to the party tonight, and you won’t worry about anything. Just trust me."
        black "(It's funny, I've gotten so used to him saying things like that.)"
        black "Turine, I appreciate everything you’ve done for me… but sometimes, I feel like you’re doing too much."
        black "I don’t know if I can always rely on you."
        green "You don’t need to worry about that. You’ll always have me, and I’ll take care of you. You’re mine, after all."
        black "(Mine?)"
        black "(It feels like a weight's fallen on me.)"
        black "(I just can't find it in me to pull away from his warmth though...)"
        green "You’ll see, everything will fall into place soon. I’ll make sure of it."
        #Balcony
        green "I’ve been thinking a lot about us, lately. I know I can’t keep pretending to just be your friend. I want more than that."
        green "I want you to be with me, fully. No more doubts, no more running away."
        black "Turine, I—"
        green "Shh… Just listen."
        green "I can offer you everything. I’ve already arranged things so you’ll never have to worry again."
        green "You’ll have the world, as long as you stay with me. All I ask is that you trust me."
        black "(God, when he looks at me like that, how am I supposed to say anything but yes?)"
        green "I’ll protect you. I’ll make you happy. We belong together, don’t you think?"
        black "I… I think so."
        "{color=#04b75a}GREEN ROUTE: GOOD?{/color}"
        "{color=#04b75a}Wanna see how else things could have turned out?{/color}"
        "{color=#04b75a}Or maybe how things would go if you chose someone else.{/color}"
        return
    
    label turineBad:
        "--A few weeks later--"
        black "(It's so wonderful here. It's everything I could ever ask for.)"
        black "(Comfort, wealth, and Turine's attention.)"
        black "(Was it... worth it?)"
        green "I told you… everything would fall into place. You and I, we were always meant to be together."
        black "(That's what he said. That's what he always said.)"
        black "(It didn't feel right though.)"
        black "(I thought it would go away with time, but things only got worse.)"
        black "(He started to hate when I talked with anyone else.)"
        black "(Or he'd get jealous over small things.)"
        black "(And now...)"
        black "(I don't know how much more my heart can take.)"
        black "Turine, you’re acting a bit strange lately. You’re controlling my every move. This isn’t healthy."
        green "You think so? I’m just making sure nothing gets in the way of us. You’re mine, and no one will take you away from me."
        green "Not even you."
        black "What do you mean?"
        green "I mean that if you can’t see what’s best for you, I’ll just have to make the decision for you."
        green "No one else can have you."
        black "Turine?"
        green "You’ll learn to love me. In time. I’ll make sure of it."
        "{color=#04b75a}GREEN ROUTE: BAD!{/color}"
        "{color=#04b75a}Wanna see how else things could have turned out?{/color}"
        "{color=#04b75a}Or maybe how things would go if you chose someone else.{/color}"
        return

label azureRoute:
    black "Wait… what is Azure building? That doesn’t look like it’s for the competition."
    blue "..."
    black ""