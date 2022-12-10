'''The entire script file was made from scratch, files referenced in game were also made both by myself (Riley) and my partner (Nia)'''
'''In-game, all notes are displayed using #, this is due to the engine reading the apostrophe as a part of the dialogue'''

'''Character names and the colors that they are displayed as'''
define y = Character("You")
define r1 = Character("Alex", color="#365e6b")
define r2 = Character("Nelson", color="#990000")
define r3 = Character("May", color="#800080")

'''Background images to use for different scenes'''
image bg_nel_room = "room 1.png"
image bg_alex_room = "room 2.png"
image bg_room_1 = "room 0 a.png"
image bg_room_2 = "room 0 b.png"
image bg_kitchen = "room 3.png"
image bg_end_1 = "end scene 1.png"
image bg_end_2 = "end scene 2.png"

'''Character sprites and their names, categorized by expression and name assigned'''
image r1 happy = "Green_happy.png"
image r1 nervous = "Green_worried.png"
image r1 thinking = "Green_thinking.png"

image r2 happy = "Red_happy.png"
image r2 nervous = "Red_worried.png"
image r2 thinking = "Red_thinking.png"

image r3 happy = "Purple_happy.png"
image r3 nervous = "Purple_worried.png"
image r3 thinking = "Purple_thinking.png"
image note = "note.png"
image dog = "dog.png"
'''The game starts here'''
#set scene room 1 bedroom
label start:
    scene bg_room_1
    "BEEP BEEP BEEP BEEP BEEP-"
    "Uh oh"
    "That’s the omen of doom to wake you up every morning"
    "Yet again on its conquest to rob you of that most important thing:"
    "Sleep"
    "No matter! You rise and, although you wouldn’t quite say you were shining, get ready for today."
    "A day like any other day, get up get dressed"
    "Grunt “Mornin’” to your fellow roommates, and then quickly exit to your car with your-"
    "..."
    "You seem to be unable to find your keys."
    #menu pop up option for user interaction
    menu:
        "Check Counter":
            jump counter
label counter:
    $ counter_flag = True
    "Yes, still nothing- however! Therein lies the first clue!"
    "There is a note on the counter."
    menu:
        "Check Note":
            jump note
label note:
    #New scene/change in background
    #Note flag set for potential later use
    $ note_flag = True
    scene bg_room_2
    show note
    "Today is Day! :) Have surprise 4 you! <3"
    hide note
    "You have fallen victim to one of your traitorous roommate’s favorite past times:"
    "Wasting your time."
    "A surprise could be anything, from a candy bar to a burger king coupon"
    "to a bucket full of water sitting on top of your door."
    "Either way, you should probably see which one of your roommates snagged your keys"
    #Flags are set in the menu so that during later choices, the characters dialogue changes based off where you went first
    menu:
        "Nel's Room":
            $ nel_flag = True
            $ alex_flag = False
            jump nel_room
        "Alex's Room":
            $ alex_flag = True
            $ nel_flag = False
            jump alex_room
label nel_room:
    scene bg_nel_room
    show r2 happy
    #The show function displays whatever image it is assigned to in the center of the screen
    "You knock on the door, your usually sleeping-in-at-this-time-in-the-day roommate answers"
    r2 "Hm?"
    y "Where are my keys?"
    show r2 nervous
    r2 "Hate to break it to ya but how am I supposed to know?"
    #The way the if function works in Renpy is by saying if == True, so instead of if alex_flag = True, its just if alex_flag

    if alex_flag:
        y "Because Alex said you were up weirdly early this morning"
    else:
        y "Because YOU took them fiend!"
    show r2 thinking
    r2 "Do I get a lawyer for this conversation? Can I appease the jury?"
    y "Very suspicious thing for you to say, sounds like something a key thief would say in fact!"
    show r2 nervous
    r2 "come back with a warrant!"
    r2 "Until then, you’ll find the one truly guilty of your charges is in fact closer than you think!"
    show r2 happy
    r2 "Andisprobablymakingbreakfastinthekitchen-"
    "Ok, that is strange, usually at this time in the morning, at least one of your roommates are already out the door!"

    #This whole part here makes sure users cant jump back and forth between the two rooms repeatedly
    if alex_flag:
        menu:
            "Kitchen?":
                jump kitchen
    else:
        menu:
            "Alex's Room":
                jump alex_room
            "Kitchen?":
                jump kitchen

label alex_room:
    scene bg_alex_room
    "Alex's room is in the same place it always is, and as hard to see through as possible"
    "All these plants really show off how much of a green thumb they have, and also show how many devious hiding places that could now be holding your keys"
    "Luckily your roommate is here to interrogate."
    show r1 happy
    y "Have you seen my keys?"
    r1 "Good morning to you too!"
    y "Yes ok good morning key-stealer"
    show r1 nervous
    r1 "What makes you think I stole your keys? I’ve only left my room to go get some water for these little guys"
    y "If you didn’t take them, who did?"
    show r1 thinking
    #The logic for this room is a little different than that of the first room,
    #it will only ever give you one option for where to go based on where you were before
    if nel_flag:
        r1 "Hm, ya know, I think I heard someone in the kitchen!"
        menu:
            "Kitchen?":
                jump kitchen
    else:
        r1 "huh, I’m not sure? It sounded like Nel was up awfully early this morning, especially given their sleep schedule"
        show r1 happy
        r1 "why don’t you check with them? Verrrrry suspicious if you ask me!"
        menu:
            "Nel's Room":
                jump nel_room
label kitchen:
    scene bg_kitchen
    "You enter stage left to the little kitchenette in your apartment, where you find, lo and behold"
    show r3 happy
    r3 "Oh! Morning!"
    y "Suspicious…"
    show r3 nervous
    r3 "Suspicious? What could possibly be suspicious about me? Maybe I should be suspicious of you!"
    y "No way! Don’t try to flip this on me! You are the only remaining suspect! Where are my keys!"
    show r3 thinking
    r3 "Your… Keys…. Hmmmmmmmmmmmmmmmmmm"
    y "hey now-"
    r3 "mmmmmmmmmmmmmmmmmm"
    y "May-"
    show r3 happy
    r3 "I think I saw them in the living room!"
    y "W-"
    r3 "Yup! Definitely the living room! In the box next to the door!"
    menu:
        "Go Living room????":
            jump living_room
label living_room:
    scene bg_end_1
    "There is a box at the door"
    "It is Large"
    menu:
        "Open box?":
            jump box
label box:
    #the following shows how to position characters in more specific places on screen
    scene bg_end_2
    show r1 happy at left
    show r2 happy at right
    show r3 happy:
        xalign .75
        yalign 1.0
    show dog at center
    "Everyone" "Surprise! Happy Birthday!"
    y "A DOG?!?!"
    jump end
label end:
    "THE END"
    # This ends the game.

    return
