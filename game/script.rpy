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
define e = Character("Eileen")
define k = Character("Keichi")
define m = Character("Mion")
define re = Character("Rena")
define ri = Character("Rika")
define s = Character("Satoko")



#Keiichi 

image k school happy1 = "char:images/Characters/kei/k_sch_h1.png"


#Rena
image re school happy1 = "char:images/Characters/rena/re_sch_h1.png"

#Mion
image m school happy1 = "char:images/Characters/rena/mi_sch_h1.png"




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
    scene blood1
    play sound kswing
    play sound down
    "{i}*thwack*{/i}"
    pause 1.0
    play sound kswing
    play sound down
    "{i}*thwack*{/i}"
    pause 1.0 
    play sound kswing
    play sound down
    "{i}*thwack*{/i}"
    pause 1.0
    play sound kswing
    play sound down
    "{i}*thwack*{/i}"
    pause 2.0 

    "Where...?"
    "Where did those happy times 
    go?"

    pause 2.0
    play sound kswing
    play sound down
    "{i}*thwack*{/i}"

    pause 1.0 
    play sound kswing
    play sound down
    "{i}*thwack*{/i}"

    pause 2.0
    "How did it come to this...?"
    "Why did it come to this...?!"
    pause 1.0 
    
    play sound kswing
    play sound down
    "{i}*thwack*{/i}"
   
    pause 1.0 
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

    show re school happy1

    voice rena_kei
    re "Keiichi-kun! Good morning!"

    voice kei_grunt
    k "Why are you always here so early? You know you can sleep in every so often."

    voice rena_hau
    re "But if I slept in, I would keep you waiting."

    voice kei_grunt
    k "I wouldn't wait for you."

    voice rena_hau
    re "W-wha...? Keiichi-kun is so mean!"

    voice kei_grunt
    k "I'd leave you in the dust and kick you to the curb."

    voice rena_hau
    re "Keiichi-kun! But I always wait for you..."

    voice kei_grunt
    k "Don't care. I'd ditch you in a heartbeat if you were late."

    voice rena_hau
    re "Why are you being so cold to me, Keiichi-kun? Why?"

    "I acted as if I was bothered by Rena, but in truth every morning I was excited to walk to school with her."
    "That being said, someone this fun to tease is a rare occurance. I have to take advantage of it when I can."

    voice kei_grunt
    k "Just kidding. I would never ditch you."

    voice rena_hau
    re "Th-thanks."

    voice kei_grunt
    k "Yep. I would definitely wait for you. No matter how long it took, I would wait for you forever, Rena-chan."

    voice rena_hau
    re "F...f...forever...? Hauuuuu~"

    "Blushing profusely, Rena was at a loss for words. Fortunately for her, the awkward silence was soon shattered as we arrived at our next stop."

    scene hi2_day with dissolve
    
    show rena school happy1 at right

    pause 2.0
    voice mion_ohayo
    m "There you all are! You guys sure took your sweet time getting to me! Any longer and I would have left without you!"
    "Rena and I made eye contact, wondering, if perhaps, Mion had psychically been listening in on our previous conversation."
    show mion school happy1 at left

    voice kei_ja
    k "You're the one who is usually late Mion..."

    "This perky girl is Sonozaki Mion. She's my senior and pretty much the leader of our class."

    voice rena_mion
    re "Good morning Mii-chan!"

    


    scene black with slowdissolve




    
    return

#label splashscreen:
#    $renpy.movie_cutscene("op.ogv")
#    return

