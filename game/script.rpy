# The script of the game goes in this file.
init -10 python:
    def shrink(s):
        return Transform(s, zoom=.5)

    config.displayable_prefix["small"] = shrink

    def char(s):
        return Transform(s, zoom=.66)

    config.displayable_prefix["char"] = char


# Declare characters used by this game. The color argument colorizes the
# name of the character.
#CHARACHTERS

define k = Character("Keichi")
define m = Character("Mion")
define re = Character("Rena")
define ri = Character("Rika")
define sa = Character("Satoko")
define sh = Character("Shion")



#Keiichi 

image k school happy1 = "char:images/Characters/kei/k_sch_h1.png"


#Rena
image re school happy1 = "char:images/Characters/rena/re_sch_h1.png"
image re school blush = "char:images/Characters/rena/re_sch_blsh.png"
image re school hau = "char:images/Characters/rena/re_sch_hau.png"
image re school kai = "char:images/Characters/rena/re_sch_kai.png"
image re school2 eh = "char:images/Characters/rena/re_sch2_eh.png"
#Mion
image m school happy1 = "char:images/Characters/mion/mi_sch_h1.png"




# The game starts here.

label start:
    stop music fadeout 1.0

    

    scene ch_op with intro_trans
    #Onidamashi-hen E1: 
    show onidamashi with dissolve 
    pause 7.0
    play sound cowbell
    show onidamashi-bern with slowdissolve
    play sound cowbell
    pause 10
    
    
    play music higurashi fadein 1.0 volume 0.66
    scene kei_room_black with slowdissolve
    scene blood1 with vpunch
    play sound kswing
    play sound down
    "{i}*thwack*{/i}"
    pause 1.0
    scene blood1 with vpunch
    play sound kswing
    play sound down
    "{i}*thwack*{/i}"
    pause 1.0 
    scene blood1 with vpunch
    play sound kswing
    play sound down
    "{i}*thwack*{/i}"
    pause 1.0
    scene blood1 with vpunch
    play sound kswing
    play sound down
    "{i}*thwack*{/i}"
    pause 2.0 

    "Where...?"
    "Where did those happy times 
    go?"

    pause 2.0
    scene blood1 with vpunch
    play sound kswing
    play sound down
    "{i}*thwack*{/i}"

    pause 1.0 
    scene blood1 with vpunch
    play sound kswing
    play sound down
    "{i}*thwack*{/i}"

    pause 2.0
    "How did it come to this...?"
    "Why did it come to this...?!"
    pause 1.0 
    
    scene blood1 with vpunch
    play sound kswing
    play sound down
    "{i}*thwack*{/i}"
   
    pause 1.0 
    scene blood1 with vpunch
    play sound kswing
    play sound down
    "{i}*thwack*{/i}"

    "I wish...that I could go 
    back and change things..."

    "I wish that I could go back to 
    before it all went wrong..."

    pause 2.0

    "Forgive me."

    scene kei_room_black with slowdissolve
    pause 3.0
    "The higurashi continued to sing their song."

    pause 3.0
    stop music fadeout 2.0
    scene black with slowdissolve
    stop sound fadeout 1.0
    pause 3.0
    
    
    "Mom" "Keiichi! Wake up!"

    scene kei_room_dark with slowdissolve

    pause 1.0 

    "I stirred from my slumber, yawning as I rubbed my eyes."
    "Slowly, the nightmare I had just awoken from faded from my mind."
    pause 1.0
    "{i}*grumble*{/i}"

    "I guess I should go down and eat breakfast. Rena-chan will be here soon to pick me up."

    play music daily_life_boppy fadein 1.0

    scene mae_dining_morn with dissolve

    pause 1.0

    "My mom laid breakfast out on the table. Seaweed, pickled vegetables, raw egg, and grilled salmon."
    "The platonic ideal of a Japanese breakfast. But my mother was not finished." 
    "To her, no breakfast would be complete without a steaming bowl of miso soup."
    "She walked over with the soup, eyes shining, all while humming a little tune."
    "She must be in a good mood today."

    pause 1.0

    "Mom" "You haven't skipped breakfast once since we moved to Hinamizawa. I'm so proud of you."
    scene black with dissolve
    "Let me explain."
    show k school happy1 with dissolve
    "My name is Maebara Keiichi."
    "It has been three weeks since my family moved to the small village of Hinamizawa, and, honestly, I can't believe it belongs to the same country as the city I used to live in."
    "In fact, I have a hard time believing that it belongs to the same time period..."

    scene mae_dining_morn with dissolve

    voice kei_grunt
    k "Yeah~ Your cooking is just that delicious!"

    "Back when we lived in the city, I was never a morning person. My parents were lucky if they saw me before I left for school."
    "Boycotting breakfast was my way of fighting back against my parents, who forced me to go to cram school."
    "Taking another bite of the grilled salmon, I sighed with satisfaction."
    "If I could go back in time, I would slap myself for ignoring all the hard work my mom put into those breakfasts."
    "Anyways, waking up early now was no issue, now that I no longer attended cram school."
    "I guess the country air helps too."

    "Mom" "Keiichi! Isn't it almost time for you to meet up with Rena-chan? Hurry, hurry!"

    "Mom seemed to enjoy the fact that I was walking to school with a girl."
    "That girl is named Ryuugu Rena. She is one of my classmates."
    "Every day since moving to Hinamizawa, Rena has shown up in the morning to walk me to school."
    "She and mom hit it off too. Rena would come over every so often with home-grown vegetables, and my mom was always appreciative of her kindness."

    "Mom" "Keiichi! Rena-chan is waiting!"

    "I shoveled the remainder of my breakfast down my throat and hopped up from the table."
    "After giving thanks to my mother, I ran out the door to meet up with Rena. As I left, my mom yelled out the door."

    scene mae_door_day with dissolve

    "Mom" "Have a safe trip! Don't forget to thank Rena-chan for the vegetables!"

    voice kei_grunt
    k "Haha, will do!"

    scene kei_house_sch with dissolve

    show re school happy1 with dissolve

    voice rena_kei
    re "Keiichi-kun! Good morning!"

    voice kei_ano
    k "Why are you always here so early? You know you can sleep in every so often."

    show re school blush with dissolve
    voice rena_cutelaugh
    re "But if I slept in, I would keep you waiting."

    voice kei_grunt
    k "I wouldn't wait for you."

    voice rena_cryout
    re "W-wha...? Keiichi-kun is so mean!"

    voice kei_eh
    k "I'd leave you in the dust and kick you to the curb."

    show re school hau with dissolve
    voice rena_squeal
    re "Keiichi-kun! But I always wait for you..."

    voice kei_ja
    k "Don't care. I'd ditch you in a heartbeat if you were late."

    show re school blush with dissolve
    voice rena_cryout
    re "Why are you being so cold to me, Keiichi-kun? Why?"

    "I acted as if I was bothered by Rena, but in truth every morning I was excited to walk to school with her."
    "That being said, someone this fun to tease is a rare occurance. I have to take advantage of it when I can."

    voice kei_eh
    k "Just kidding. I would never ditch you."

    voice rena_squeal
    re "Th-thanks."

    voice kei_ja
    k "Yep. I would definitely wait for you. No matter how long it took, I would wait for you forever, Rena-chan."

    show re school kai with dissolve
    voice rena_hau
    re "F...f...forever...? Hauuuuu~"

    "Blushing profusely, Rena was at a loss for words. Fortunately for her, the awkward silence was soon shattered as we arrived at our next stop."

    scene hi2_day with dissolve
    
    show re school happy1 at right with dissolve

    pause 2.0
    show m school happy1 with dissolve

    voice mion_ohayo
    m "There you all are! You guys sure took your sweet time getting to me! Any longer and I would have left without you!"
    "Rena and I made eye contact, wondering, if perhaps, Mion had psychically been listening in on our previous conversation."
    

    voice kei_ja
    k "You're the one who is usually late Mion..."

    pause 1.0

    "This perky girl is Sonozaki Mion. She's my senior and pretty much the leader of our class."

    voice rena_mion
    re "Good morning Mii-chan!"

    voice mion_ohrena
    m "Good morning Rena~!"

    voice mion_ahque
    m "Long time no see, Kei-chan! How many years has it been?"

    voice kei_grunt
    k "I was gone for two days, jeez! Besides, shouldn't I be asking that question to you, old man!?"

    "Mion leaned in to get a good look at me."
    
    
    show m school happy1:
        ease .5 zoom 3.0 yoffset 1000 #moves right 100px, bottom 50px. set to 0 when you return later.
        
    
    voice mion_mn
    m "You seem to be the same Kei-chan as when you left a few days ago..."
    pause 0.75
    show m school happy1:
        ease .25 zoom 1 yoffset 0
    voice mion_ahque
    m "Hm? What's this?"
    pause 1.0
    voice mion_laughcute
    m "Kei-chan, I see that your buddy is quite perky this morning."
    voice kei_ja 
    k "Yes, yes.{fast} He's always getting perky in the morning. It's actually a real pain. Wanna try saying hi to him?"

    show re school2 eh at right with dissolve                          
    voice rena_cryout
    re "Waa... What are you talking about? Mii-chan, Keiichi-kun?!"

    "As usual, Rena couldn't keep up with our early morning, crude banter. I can't blame her though. Most people would also be confused by Mion's morning antics."

    voice mion_do
    m "So! How was your trip, Kei-chan? Did you find that think I asked you about?"
    voice mion_laughcute
    m "You know, that Western game catalog I wanted?"

    voice kei_ano
    k "I went back to Tokyo for a funeral, so I was busy the whole time. I didn't really have time to look around for toy shops."

    voice mion_kyukyukyu
    m "Tsk tsk tsk... Toy shops are nothing like hobby shops. Western stuff in general is impossible to find in these parts, ya know..."


    scene school_d with dissolve
    "Laughing as we walked we soon arrived at school."
    "The students of Hinamizawa, all 30 of them, learn in a single classroom. It seems kind of strange at first, though I guess I got used to it pretty quickly."

    scene school_hall with dissolve
    "Mion reached out to open the classroom door but hesited for a moment."
    show m school happy1 with dissolve
    voice mion_laughcute
    m "Well, well... hehehe... After you, Kei-chan..."

    k "Are you trying to test my skills? I won't be defeated this time! Rena, get back!"

    show re school2 eh at right with dissolve 
    voice rena_squeal
    re "Huh..? What's going on guys?"

    #from here on out I am simply just scripting. Black screen as bg and no sounds or music
    scene black 
    stop music

    k "Stay back Rena! Its her!! She's at it again!"

    re "Eh..? By she, you mean...?"

    k "Look over there! Your trap is way too obvious, Houjo Satoko!!!!"

    "I pointed to the top of the doorway."
    "Suspended in the crack at the top of the door was an eraser."
    "If I had recklessly opened the door, it surely would have been my demise."

    m "Guess the game is on again today."
    m "Kei-chan keeps getting better and better at spotting Satoko-chan's traps."
    m "You may even defeat her today."

    k "No!" 
    k "Satoko isn't this naive."
    k "There must be some trick involved!"
    "I leaned in to get a closer look at the eraser."
    "To my eyes, it seemed to be an ordinary eraser."
    "When I first transfered here, Satoko had trapped the doorway in a similar manner to the way she had today."
    "However, the eraser that fell on my was not an ordinary eraser."
    "Satoko had put rocks in the eraser to make it heavier. Thanks to her, I left my first day at a new school covered in bruises."

    re "Why don't you just stand back and open the door?"
    re "I wonder if you can dodge the eraser, I wonder...?"

    k "Rena isn't thinking hard enough."
    k "The eraser is only one piece of Satoko's master trap."
    k "It is a red herring, a mere distraction meant to lure me into missing the greater threats!"

    "Rena looked dumbfounded and Mion simply laughed."

    m "Hehehe... I wonder who will win today...?"
    m "Kei-chan is in top form this morning."

    "I searched the rest of the door, looking for anything else that seemed remotely suspicious."
    "That's when I spotted it: the glint of thumbtacks taped to the inside of the door-handle."
    "Had I not found them, Satoko would surely have left me wounded and defeated, however, today was my day as the victor."

    k "Aha! Checkmate Satoko!"
    k "The real trap is the thumbtackes in the door-handle!"

    "Pulling the end of the tape, I masterfully stripped away all of the thumbtacks from the inside of the door-handle."

    k "You may have created a brilliant combination trap, but the mind of Maebara Keiichi is far superior!"

    "Excited to see the look on Satoko's face when she realized I had won, I rushed into the classroom at full speed."

    pause 1.0

    "<i>*twang*</i>"

    pause 1.0

    "What was that?"

    pause 1.0

    k "Waaaaaaaaaaaahhhhhhhh!!!???"

    pause 1.0 

    "Is that a rope? Why is the ground heading towards me so fast?"

    pause 1.0

    "<b><i>*CRASH*</i></b>"

    sa "Ohohohoho! What do we have here?"

    "There she is. Houjo Satoko, the cheeky little trap mistress herself."

    sa "Good morning to you, Keiichi-san."
    sa "Causing a ruckus at this early hour?"
    
    k "I'm impressed, Satoko. This was a step up from your ordinary traps!"
    
    sa "I haven't the faintest idea as to what you are refering to."

    k "Why, you little..."

    "I tried to stand up, but I had landed on my knee when I fell. I grunted involuntarily at the pain."
    "I felt a small hand rest and pat my head."

    ri "Pain, pain, go away!~"

    "The one petting my head is Furude Rika. Unlike Satoko, she is an absolute angel."

    re "Good morning, Rika-chan!"

    ri "Good morning, Rena!"
    ri "Good morning, everyone!"

    k "Wow, Rika-chan is a really good girl."
    k "The exact opposite of a certain someone."

    sa "Lies! Slander! Murder!"
    sa "You have no proof to back up any of your heinous words..."

    "I picked up Satoko by her uniform. She's only in middle school, so its like lifting a child."

    k "You better beware Satoko."
    k "My finger flick has been known to split plywood."

    sa "Ehhhh! Unhand me you brute!!!"

    k "Hey, quiet down, people will get the wrong idea!"

    sa "Waaaaaaaaahhhh!"

    "Satoko started crying."
    "Rika, being the sweet girl she is, walked over to comfort her."

    ri "No need to cry, Satoko!"
    ri "Fight-on!"

    ri "And next time, you will set up an even more amazing trap."
    ri "Then you can squich Keiichi like a pancake!~ Nipah!~"

    k "Gah!! Being betrayed by an angel hurts so much more..."

    re "Hauuuu!!"
    re "Satoko-chan is crying... but it's soo kyuute!!!"
    re "I wanna take her home!! Hauuuuuuuuuuuu!!!!!"

    #end scene wipe to Keiichi's Bedroom

    "Later that evening I recieved a knock on the door from Rena and Mion."

    re "Hey Keiichi-kun!"
    re "Tomorrow, Mii-chan and Rena were thinking that we'd like to show you all around Hinamizawa!"

    m "You'll be joining us, of course, right, Kei-chan?"

    k "I'll check my schedule."

    m "But you're being invited by two girls!!!"

    re "Keiichi-kun, I wonder are you free? Are you?"

    k "I am."

    m "Woah woah! Why do you treat Rena-chan differently than me!????"

    "Mion and Rena left soon after extending the invitation."
    "I thought it was really nice of them to give me a tour of Hinamizawa."
    "I knew how to get to school pretty well, but the rest of the village was a complete mystery."
    

    "*The next day*"

    "Mion and I met up at the usual spot. Rena, however, was nowhere to be seen."

    k "Hey, Mion. Where's Rena?"
    k "She's never late like this."


    m "She said she was going to make bento for you, so she's probably pulling out all the stops."
    m "Though I hope she doesn't go too much overboard."
    "I could hardly imagine the immense intricacies of a bento that would cause Ryuugu Rena to be late, but sure enough I soon could see Rena's figure approaching."
    "In her hands was a large wrapped bento."
    "Wait, at a second glance it should be described as many bento stacked together!"
    "How much food did Rena make?"
    re "Sorry I'm late!"
    re "Ok...1...2...3..."
    "*thud*"
    "Rena set down the large stack of bento, with a thud. Clearly, the food weighed a considerable amount."

    m "Hey, Kei-chan. Rena really went all out making you this bento. It's a shame that a delicate girl like Rena would get exhausted carrying it all day."

    k "I completely agree. I am a man of honor. I shall take responsibility for my actions and bear this load."

    re "Keiichi-kun...? Mii-chan..? What do you mean take responsibility...? Hauu..."

    "Fortunately for her, taking responsibility meant carrying around the food that Rena made."
    "Rena and Mion led me through the main shopping area of Hinamizawa."
    "We passed by kind villagers who all knew who I was, though they seemed to be complete strangers to me."
    "It was a beautiful day for a walk around the village. Days like these make me so glad that I live in Hinamizawa."

    "Eventually, Rena and Mion brought me to a steep outdoor stairway, appearing to lead to a shrine of some sort."















    


    scene black with slowdissolve




    
    return

#label splashscreen:
#    $renpy.movie_cutscene("op.ogv")
#    return

