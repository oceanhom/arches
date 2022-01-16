label day11morning:
    $ currentDay = 11
    scene day11 with fade
    $ renpy.pause (3.0)
    scene black with dissolve
    if MASSACRE == True:
        jump Day11CGoodMorning
    "What sleep I got was restless. Despite the comfort of the bed, everything running through my head kept me from staying down for too long."
    scene bedroom with dissolve
    if MASSACRE == False:
        #Path C
        play music dark fadein 2.0
        "I sat up suddenly in bed, having heard a crash somewhere in the house."
        if wolfroute == True:
            show wolf underwear annoyed with dissolve
            "Ty yawned and sat up next to me, shooting me an annoyed look."
            wolf "What?"
            mc "Shh... Listen."
            show wolf underwear scared
            "The next moment we heard a scream, a panicked yell coming from somewhere in the mansion."
            wolf "The fuck...?"
            "Ty and I jumped out of bed and rushed out of the room to join the others."
        elif bearroute == True:
            "My heart was beating in my chest, and I scanned the dark wondering if I'd just imagined it."
            show bear underwear pout with dissolve
            "Dean yawned, sitting up next to me almost in a daze."
            bear "Everything alright? What happened?"
            mc "I don't know... I thought I heard..."
            show bear underwear scared
            "The words were barely out of my mouth when we both heard a scream, coming from somewhere in the mansion."
            show bear underwear mad
            bear "Stay here. I'll go check it out."
            mc "No you don't! I'm coming too!"
            "There was no arguing, as we both jumped out of bed and rushed out of the room."
        elif dragonroute == True:
            show dragon underwear sad with dissolve
            "It woke Orlando too, or I did as I sat up. He did much the same, wondering what had happened."
            mc "Did you...?"
            show dragon pantsless sad with dissolve
            "I looked over to Orlando putting his shirt back on while I wondered if what I'd heard was just a figment of my imagination. "
            show dragon pantsless scared
            extend "But that's when we heard the scream."
            dragon "What was that...?"
            mc "I'm going to go check it out."
            show dragon pantsless mad
            dragon "Not alone you're not!"
            pass
        elif boarroute == True:
            "I scanned the dark, wondering what it was that I'd heard and went to settle back down before I noticed Roswell was missing."
            mc "Huh...?"
            "Fruitlessly I patted the spot where I remembered him laying before, half expecting my hand to collide with something as if he were invisible."
            "But no sooner had my hand passed through the space where he shouldn't been, I heard it. "
            extend "The unmistakable sound of a scream coming from somewhere in the mansion."
            "Doing a double take between the empty space of bed next to me and the door to the room, I jumped out of bed in order to investigate."
            pass
        elif lionroute == True:
            show lion shirtless mad with dissolve
            "I looked to Hoss who was already sitting up, looking tense."
            mc "Hoss...?"
            "He gave me a quick look over his shoulder before looking back at the door."
            mc "Did you hear..."
            "The sentence wasn't even entirely out of my mouth when I heard it. The unmistakable sound of someone screaming from somewhere in the mansion."
            "Hoss got up soon after, heading for the door. Assuming he was going to check it out, I followed suit."
            pass
        scene foyer with dissolve
        mc "What's happening!?"
        "There was no sense in asking but my panic prompted the question in any case. It seemed a few of us were in shock of what we were seeing."
        show boar shirtless cry at right
        show croc shirtless dazed at left
        with dissolve
        "Roswell was on the ground, trembling and he looked injured. Sal on the other hand looked to be in a trance, hands gripping an axe dripping with something viscous and red."
        mc "Is that..."
        show bear underwear scared at center with moveinright
        bear "Whoa, Sal! What are you doing?"
        "As Dean made a go for the axe, Sal shoved him back, but Dean didn't budge."
        show bear underwear mad
        bear "Sal! The hell do you think you're doing!?"
        "I was frozen in place, eyes looking to Roswell. The longer I noticed, the more I noticed he was bleeding and quite a bit too."
        hide boar
        hide bear
        hide croc
        show dragon pantsless scared at left
        show lion shirtless scared at right
        with dissolve
        mc "Guys! How do we... What should we..."
        show lion shirtless yell
        lion "Help Roswell, obviously!"
        "But before any of us could move, Dean yelled out in pain."
        scene salrampage with dissolve
        "He was stumbling back, clutching his shoulder where it seemed Sal had bitten him, blood dripping from the wound on Dean's shoulder and from Sal's teeth."
        "I was frozen, watching as Sal reared back with the axe. And in the next moment..."
        scene black
        "A pained yell echoed through the foyer, drowned out by the sickening squelch as the axe was removed from Dean's neck. He fell to the floor in a heap, heavy, but most importantly right on top of Roswell."
        "Dean's yell was replaced by the panicked squealing from Roswell as he tried to scramble away but was now pinned by Dean's corpse."
        $ DeanDead = True
        "Ty held me behind him, acting as a shield between me and Sal. Hoss and Orlando were holding each other's hands, with Orlando clinging further to Hoss's arm both horrified to what they'd just seen."
        show foyer with dissolve
        "When Sal turned back to Roswell something in me broke, freeing my feet so I could move. I shoved Tyson aside and scrambled to close the distance. He made to grab out for me but the shock gave me enough time to get out of reach."
        mc "Roswell!"
        "I reached out and he reached out for me as Sal raised the axe."
        boar "[mcname]!"
        "But it was the last thing he said as the axe came down and silenced him for good."
        $ RoswellDead = True
        "I stood there shaking, partially covered in the spray of blood that rose from the impact. As calmly as he'd done to Dean, Sal withdrew the axe from Roswell before turning to me."
        show wolf underwear yell at right
        show dragon pantsless cry at left
        with dissolve
        "Sal said nothing, but Tyson was soon to cross the floor and stand in front of me again, working himself up for a fight. Orlando shuffled forward having peeled himself away from Hoss closer to Sal."
        dragon "S-Sal...? Sal why... Why did you...?"
        "As much as I tried to reach out to Orlando, Tyson was much better at keeping me away this time but it seemed as though Sal made no effort to pursue me or even Orlando."
        hide wolf with moveoutright
        show dragon pantsless cry at right with ease
        show croc shirtless dazed at left with moveinleft
        "Silence. Nothing but silence. For the faintest of moments I thought maybe Sal would raise his axe against Orlando but instead it slipped from his hand, landing with a clatter on the floor."
        dragon "Sal...?"
        "He stared through Orlando and sure enough... "
        hide croc with dissolve
        "He wandered away. Heading outside through the back door and into the yard beyond."
        hide dragon with moveoutbottom
        "Orlando collapsed in a heap on the floor, passing out."
        show lion shirtless scared at right with moveinright
        show wolf underwear yell at left with moveinleft
        "There were no words. Sal had just killed Dean and Roswell. It was all I could smell, and as I wiped my face I looked at my hand, covered in Roswell's blood."
        "My eyes went to their bodies still on the floor and all I could do was stare at the carnage. A massacre indeed."
        lion "What... What do we..."
        wolf "Call the fuckin' cops! Now!"
        lion "R-Right!"
        scene conservatory with dissolve
        "While Hoss fumbled with his phone and Tyson was busy yelling at him for something, I wandered off. I let my body go on auto pilot to head towards the only other person I knew existed in the house that might know something if they weren't already watching."
        if BensonAround == True:
            show otter neutral with dissolve
            "When I arrived though, Benson was there as if waiting for me. His face didn't budge, but I got the impression he knew what was happening, or rather what had happened."
            otter "...Please follow me."
            scene black with dissolve
            "He led the way forward through the passage towards the library, not breaking stride once. As for me, I followed quietly until the library came into view."
            scene library
            show otter neutral at right
            show oz neutral at left
            with dissolve
            otter "...Sir."
            show oz pout
            oz "Yes, thank you Benson. That will be all."
            mc "No..."
            show oz neutral
            oz "No?"
            mc "Which... Which one of you..."
            "I was shaking but I noticed Benson and Oswin looking at one another."
            show oz annoyed
            oz "You're distressed from what you just watched. Believe me if I was the one behind this we'd not be talking right now."
            show oz pout
            oz "Honestly, I just wished to come out myself to confirm their passing."
            show otter pout
            otter "But sir..."
            show oz neutral
            oz "Right. And another thing. [mcname], it'd best the rest of your friends hear this too."
            hide oz with dissolve
            "Without waiting for either of us, Oz started walking back the way we'd come. As I made to follow, Benson placed a hand on my shoulder."
            show otter neutral
            otter "[mcname]. Are you alright?"
            "I brushed his hand away, glowering. What did he expect me to say to that? Two of my friends were dead. I was terrified. To top it all off Oswin just up and left, more interested in corpses than those still alive."
            otter "Very well. Shall we?"
            scene foyer with dissolve
            "By the time Benson and I had reached the foyer..."
            show oz pout at left
            show wolf underwear yell at right
            with dissolve
            wolf "Who the fuck is this!?"
            oz "Benson, would you mind? He's being awfully loud."
            wolf "[mcname]! Where'd you run off to?"
            "He wandered over and pulled me close by the arm, tight enough that his grip was digging in to the point it hurt."
            mc "I just went... I thought he could help!"
            show oz neutral
            oz "I can help somewhat. Not these two though, but for the rest of you perhaps."
            hide wolf
            show otter neutral at right
            with dissolve
            otter "Sir, two are unaccounted for. But-"
            show oz pout
            "I tried to tug myself free of Tyson's grip, not sure I wanted to look. Part of me was curious as to what Oz was doing but I also didn't want to see the corpses of my friends."
            oz "They'll show up eventually. This is a tragedy, and must be dealt with properly. The other two..."
            show otter annoyed
            otter "{i}Sir{/i}. Perhaps we should assist Master Noble who is unconscious on the floor."
            show oz neutral
            oz "Fine. I'll tend do him, can you arrange something for the other two?"
            hide otter with dissolve
            mc "Ty! Let me go!"
            "I yanked my arm free and scowled at him, wandering over to where Oswin was kneeling on the ground."
            show oz pout
            oz "He's breathing, and may have a bump on his head but otherwise he's physically fine. "
            show oz neutral
            extend "Mentally... we'll see. I might have to mix up something for him to take."
            show lion shirtless scared at right with moveinright
            lion "We have a problem!"
            "Hoss ran in through the front door, locking eyes with Oswin before flicking over to Tyson and I."
            lion "Uhh... Who are you?"
            show oz pout
            oz "Oswin Hammond. "
            show oz neutral
            extend "I live here.{w=0.2} This is {i}my{/i} house."
            lion "Uh... Sure. Okay."
            show lion shirtless sad
            lion "Anyway... There's a problem. No signal."
            oz "What do you mean no signal?"
            lion "I tried calling the police. Nothing. Even tried going outside to see if it was just a dead spot. Nothing."
            show oz pout
            oz "There's likely a landline we could try when Benson returns."
            hide lion with dissolve
            "Orlando groaned, sitting up and rubbing his head."
            mc "Orlando!"
            show dragon pantsless sad at right with dissolve
            dragon "Oh... My head..."
            show oz neutral
            oz "Do you know where you are? What about your name?"
            dragon "Me? I'm... my name's Orlando. I'm... at a mansion, with my friends."
            show oz pout
            oz "Good..."
            "As callous as Oswin was in the library, his voice was soft and calming as he supported Orlando while he came to."
            show oz neutral
            oz "Well you're at least not as disoriented as you could be."
            dragon "I... What happened?"
            show dragon pantsless scared
            dragon "Wait... Who are you!?"
            show oz annoyed
            oz "This is going to be a running problem, isn't it? "
            show oz pout
            extend "[mcname]. Take care of your friend. I'm going to go find Benson."
            hide oz with dissolve
            show lion shirtless sad at left with moveinleft
            lion "Orlando. Let's... uh... Let's get you outside."
            dragon "Alright..."
            hide lion
            hide dragon
            with dissolve
            "Hoss led Orlando out towards the back door and they disappeared into the back yard."
            "When I turned away my eyes were drawn to Roswell and Dean still on the floor."
            "There was something about seeing a corpse. Something deeply unsettling that you can't quite place. Maybe it was the smell of blood, or how they were living and breathing only a short time ago."
            "As I made to move, Ty let me go. Everything felt surreal, like I was underwater but I was able to walk towards my friends."
            play music sad fadein 2.0
            "I flinched, stopping in my tracks as my foot stepped in the blood pooling on the ground. The smell was stronger here, and as I looked down to the red puddle at my feet it started to hit me harder."
            "They were dead."
            show wolf underwear sad with dissolve
            wolf "Hey... come on. Let's get you outside."
            "All I could do was stare. If I didn't know better they were just sleeping."
            scene black with dissolve
            "Ty pulled me in close, most importantly turning me away from Roswell and Dean. Before I knew it, he was guiding me towards the back door in the direction that Hoss and Orlando went."
        else:
            # Find Oz Dead
            $ OswinDead = True
            "I made a beeline for the bookshelf, pulling the two books to the passage and heading down into the dark."
            scene black with dissolve
            "I was thoroughly on auto-pilot, retracing my steps from when Hoss had showed me the way here the first time."
            scene library with dissolve
            "Making my way down to the lower level of the library, I stopped by the table that we'd had our chat. I wasn't sure if I was going to blame Oswin for what had happened, or if I just wanted information."
            "As I looked over to the vault door though... it was open."
            mc "Huh..."
            "There was nothing stopping me from moving forward, so I pulled the door open and headed on inside."
            scene black with dissolve
            "The hallway was dark and it smelt musty. How often did this get used, anyway? I kept my hand on one of the walls as I made my way down, feeling for any light switch or something to make my walk easier."
            "I must've put more weight than intended on part of the wall, as I felt something give, and fondling the dark for what I'd found, I gripped the handle of a large door, opening it carefully."
            scene laboratory with dissolve
            "What lights that were on gave off a soft glow, ambience more than anything else. I wasn't really sure where I was until my eyes adjusted a bit more."
            "A hunched figure sat in a chair against the far wall, lit only from the dull glow from the monitor."
            "But there was that familiar smell again. I thought I'd escaped it from the foyer but it was here too. Edging forward I reached out to the hunched figure sitting at the desk."
            scene ozdead with dissolve
            "But when I spun the chair around it was just as I thought, Oswin had been killed too. The knife was still sticking out of his chest but everything was dry. He hadn't been killed recently."
            "Either way, he wasn't behind what Sal did, but it was one less person we could rely on for help."
            show conservatory with dissolve
            "I left him there. There was no point in moving him and to be honest, Roswell and Dean took priority. I could deal with his body later."
            show wolf underwear yell
            wolf "The {i}fuck{/i} did you go!?"
            "Ty snapped me out of my daze be grabbing me and yelling at me at point blank. The next moment he was hugging me, sighing out and growling at the same time."
            mc "...Nowhere. Sorry, Ty."
            "I could hear the hollow tone in my own voice. A tiredness I had forgotten I was capable of."
            show wolf underwear mad
            "He grabbed me by the arm and started leading me out of the conservatory and back downstairs."
            scene foyer
            show lion shirtless sad at left
            show wolf underwear mad at right
            with dissolve
            lion "You had me worried!"
            "Ty wasn't being gentle, dragging me down the stairs and holding onto me almost as insurance that I wouldn't go walkabout."
            show lion shirtless mad
            lion "Seriously, why did both of you run off on me?"
            mc "Sorry... I just thought..."
            show wolf underwear yell
            wolf "You shut your mouth and stay where I can keep an eye on you. Hoss, are the cops coming or what?"
            show lion shirtless sad
            lion "No reception. After I went outside to check I tried a few times in different spots but nothing. No signal anymore."
            wolf "Fuck! The hell are we supposed to do?"
            "At this point we looked over to Orlando who was starting to stir, picking himself up slowly off the ground."
            hide wolf with dissolve
            show dragon pantsless sad at right with moveinbottom
            dragon "Ugh... What happened...?"
            "As he was rubbing his head his eyes caught sight of Dean and Roswell still on the ground a ways, his eyes widening slowly as he came to realise what had happened."
            show dragon pantsless scared
            dragon "No, no, no, no, no no..."
            show dragon pantsless cry
            dragon "No! No, no!"
            "His cries devolved into wails and sobs as he turned away from the sight."
            show lion shirtless scared
            lion "Let's... let's get you outside, huh?"
            hide dragon
            hide lion
            with dissolve
            "He helped Orlando up and the pair of them headed towards the back yard, leaving Tyson and I alone in the foyer. His grip didn't budge though, and it started to get painful from how he had me pinned in place."
            mc "Ty..."
            show wolf underwear yell
            wolf "The fuck were you thinking, huh? Wandering off like that?"
            mc "I was just... I was just trying to..."
            show wolf underwear mad
            wolf "And what if something fucked up happened to you, huh? You saw what just happened."
            mc "I know... I just..."
            "His voice was lowered to a snarl, gripping me even tighter as he got up in my face."
            wolf "Get your ass into gear. We're going outside."
            "I stole a glance at Dean and Roswell, but found that my eyes were glued to them. "
            show wolf underwear sad
            "Ty's grip loosened off so I could wander closer, but I crossed half the distance before the smell of blood hit me hard and my eyes found its way to the growing pool of blood they lay in."
            wolf "Hey."
            "I didn't respond, taking this all in with some degree of fascination that couldn't have been healthy. If anything, the sight was so surreal that it just didn't seem real to begin with."
            "When Tyson wandered over, he turned me around carefully, easing me away from the scene."
            scene black with dissolve
            "Much in the same way that Hoss and Orlando had left the foyer, we followed suit into the back yard."
        scene mansionback with dissolve
        play audio night fadein 1.0
        "All four of us stood just outside the back door, wondering what was to happen next. The air was cold but fresh, if anything I felt bad for Tyson being only in his underwear but all of us were in varying levels of undress."
        show wolf underwear mad at right
        show lion shirtless sad at left
        with dissolve
        wolf "Okay. Gotta find that fucker and keep these two safe."
        lion "And find a way to contact the police."
        show wolf underwear annoyed
        "Ty's chest was heaving, and he was working himself up. I wasn't even sure if it was legitimate anger or fear, maybe worry spurring his actions."
        mc "Ty? What do we do?"
        wolf "You hang here and don't fuckin' wander off again. I'll be back."
        mc "Wait, no, please don't..."
        hide wolf with dissolve
        "He was already heading off towards the pool, looking around as if his head was on a swivel."
        lion "I might try and find a spot to get some signal. I could've sworn I had one every other day we've been here."
        show lion shirtless mad
        lion "You two stick together. Safety in numbers."
        mc "What about you? What about Tyson?"
        show lion shirtless sad
        lion "I'm going to go and follow him so he doesn't... Y'know. Stay safe that way, right?"
        mc "Okay..."
        lion "I won't be long. Trust me."
        hide lion with dissolve
        "And sure enough, with phone in hand, Hoss followed after Ty."
        show dragon pantsless cry with dissolve
        "Orlando had sat down on the steps leading down from the back porch, propping himself up with his hands as he massaged his knees."
        "I didn't know what to say, but he had his jaw clenched as the tears ran down his face. Every time he tried to open his eyes, he just stared forward before shutting them tight again a moment later."
        "As we sat there I stared off into the distance as well, taking it all in. It was a mistake, as the weight of what I'd witnessed first hand started to sink in. Maybe the shock of it all was finally wearing off."
        "My breath began to quicken, the tightness in my chest doubled down and made my stomach churn. I felt like I was going to be sick all the while hyperventilating. I put my head between my knees, groaning out and covering my head."
        show dragon pantsless scared
        "It was only when I saw him jolt that I lifted my head back up, following his gaze across to someone approaching."
        show dragon pantsless scared at right with ease
        show croc shirtless dazed at left with dissolve
        "He lumbered closer, mumbling something to himself. Even as he stopped before us, he continued mumbling but for the most part it just sounded like incoherent noise."
        "Was this it? Were we next? Once again I found myself frozen as his eyes settled upon me, and then Orlando. All the while his mouth moved as if he was talking to us but no sound escaped his mouth."
        "His presence lasted for minutes, maybe hours, it was hard to say with how I was feeling. But sure enough..."
        hide croc
        hide dragon
        with dissolve
        stop music fadeout 2.0
        "He continued forward, dragging himself up the steps and lazily heading back inside."
        "When he was gone, Orlando and I stared at one another in shock. A moment later and we were clinging to each other, terrified."
        show lion shirtless sad at left
        show wolf underwear mad at right
        with dissolve
        lion "You two... alright?"
        "Tyson kicked the ground, frustrated. Neither Orlando and I answered Hoss, huddling together."
        lion "Still no signal. At this rate I'll need to run down to the main road and try seeing if there's anyone on the road to try and ask for help. Or even see if there's better reception out that way."
        mc "You're... you're going to go down the driveway?"
        lion "When we've found Sal, yeah."
        mc "He... He was just here. He went inside."
        show wolf underwear yell
        wolf "That fucker better not have touched you."
        mc "No, but..."
        show wolf underwear mad
        wolf "So what's the plan?"
        show lion shirtless scared
        lion "The plan? Outside of calling the police?"
        wolf "Yeah. We making a run for it before he gets us too? We blocking him off somewhere until the cops rock up?"
        "No one seemed to have an answer. There were a few shared looks but overall none of us budged."
        if OswinDead == False:
            show lion shirtless scared
            lion "Wait! You said Sal went {i}inside{/i}, right? What about Benson, and that other guy?"
            mc "Oh no..."
            show wolf underwear annoyed
            wolf "Fuck 'em. We got enough to worry about."
            mc "Ty!"
            hide wolf
            hide lion
            with dissolve
            "No sooner has I cried out, the back door opened."
            show oz neutral at left
            show otter neutral at right
            with dissolve
            otter "Were you perhaps worried about us, Master Hoss?"
            show oz pout
            oz "Bah. We'd have been fine. He's back in his room now."
            mc "Really? He just... went back to bed?"
            show otter pout
            otter "It seems so. Perhaps his rampage is over for now, or at least that's the most we can hope for."
            show oz neutral
            oz "The landline is dead too. Have you managed to get in contact with the authorities?"
            "We seemed to all shake our heads even though the question was posed to Hoss."
            show oz pout
            oz "...Unfortunate."
            hide otter
            show wolf underwear mad at right
            with dissolve
            wolf "Hey, you."
            show oz neutral
            oz "What do you want?"
            wolf "What the fuck was that? Who the fuck are you?"
            oz "Were you not listening? I'll say it again, and I'm not going to repeat myself beyond this. My name is Oswin Hammond, and this is my house."
            wolf "And Sal? What'd you do to him?"
            show oz annoyed
            oz "I don't like what you're insinuating, boy. I did nothing, and I'd like to think you being witness to what he did to your friends would be enough to convince you of that."
            show oz neutral
            oz "But for the time being, the best we can do is seek out the police."
            mc "But why? There's no other options to pick from?"
            show oz pout
            oz "To remove you from my house, hopefully someplace safer. "
            show oz neutral
            extend "Unless you wished to stay, although I don't see any reason why you would after this. Beyond that, no. There are no immediate options."
        else:
            mc "...Where would we go? Is there anywhere we {i}could{/i} run to?"
            "I eased myself away from Orlando to almost collapse backwards. I wanted to scream. I wanted to lash out at something. All the emotions I was feeling at once was very quickly taking its toll."
            mc "...What do we do?"
        hide wolf
        hide oz
        hide lion
        with dissolve
        "We stood in silence wondering if there was any other option shy of finding a place we could call the police. Safety in numbers meant that whatever we chose to do, we'd all need to be present."
        scene woods2 with dissolve
        "Which was how we found ourselves all heading around the house towards the main road."
        if OswinDead == False:
            show oz pout at left with dissolve
            "Oswin looked as if he was lost in thought. Compared to Benson who seemed to be expressionless and the rest of us worried or on edge, I was curious as to why."
            mc "Oswin?"
            show oz neutral
            oz "What?"
            mc "What are you... thinking about?"
            oz "Nothing, really. Just... curious."
            "We kept walking, and a couple minutes later Benson spoke up."
            show otter neutral at right with dissolve
            otter "Sir, are you sure it's wise to be wandering the woods at night instead of remaining in the manor?"
            mc "Even with Sal back there?"
            show oz pout
            oz "It's fine. He's safe. I believe the worst of it is over, anyway."
            mc "Sal's safe? From what?"
            "He seemed to ignore me, instead talking directly to Benson."
            oz "I secured the lab, so nothing's getting in or out of there. For that reason I don't think I'm needed."
            otter "Very well."
            "It seemed as though I was getting ignored so I instead looked to the others."
            hide oz
            hide otter
            with dissolve
        show wolf underwear annoyed at left
        show dragon pantsless cry at right
        show lion shirtless sad
        with dissolve
        wolf "This fuckin' sucks. Fuckin' wandering around in my underwear..."
        lion "Yeah..."
        "Ty shivered, the cold starting to get to him. If I had a shirt or something I'd have offered it, but I was just as naked as he was."
        mc "Hopefully... We can get somewhere warm soon..."
        show wolf underwear sad
        "He gave me a look and threw an arm over my shoulder."
        wolf "Soon, pup."
        lion "Can we... talk about something real quick?"
        if OswinDead == False:
            "I looked from Hoss to Oswin and Benson, who seemed to be trudging along minding their own business."
        mc "Talk about what...?"
        lion "We're all in varying levels of not okay. But... does anyone actually know what happened?"
        show wolf underwear mad
        wolf "Sal went fuckin' nuts, murdered Roswell and Dean, you were there."
        show lion shirtless mad
        lion "I mean {i}why{/i}, asshole.{w=0.3} Have some tact."
        "As if to punctuate his point, Orlando sniffled and wiped his face. If Hoss wasn't guiding him forward by the hand, chances are we'd still be at the mansion."
        wolf "Who the fuck cares?"
        lion "{i}I{/i} do. Sal... Like..."
        "Hoss was worked up and it was interfering with his ability to put his thoughts into words."
        show dragon pantsless sad
        dragon "...Why would he kill two of our friends?"
        show lion shirtless scared
        dragon "...And why those two friends? Is that what you were wondering?"
        lion "I mean... it's odd, right?"
        "There was a pit in my stomach that was making itself known again, and I doubled over. Was it appropriate to throw up? To scream? Hoss's question hung in the air for a bit before Orlando answered."
        dragon "It was to protect us, right? It's got to be."
        lion "What...?"
        dragon "Sal was kind...{w=0.3} He {i}is{/i} kind. And nice and sweet, too. He had to have a reason... Right?"
        hide wolf
        hide dragon
        hide lion
        with dissolve
        if OswinDead == False:
            show oz neutral at left
            show otter neutral at right
            with dissolve
            otter "There are many reasons why one might kill, Master Noble. "
            show otter pout
            extend "As you say, it could be as a means to protect. But without questioning him further there isn't really much to go off."
            show oz pout
            oz "He could've made less of a mess of my foyer if he was being courteous. "
            extend "Granted, he looked out of it even on the security monitor."
            show dragon pantsless mad with dissolve
            "Orlando stomped over to Oswin and grabbed him by the collar of his coat, snarling."
            show oz neutral
            dragon "How dare you speak about Sal like that! You care more about your foyer over the two people that died there?"
            "Oswin seemed bored, quirking an eyebrow at Orlando while he clung to his front."
            show otter annoyed
            otter "{i}Master Noble{/i}, show some restraint!"
            dragon "No! For all I know he's happy they're dead! For all I know, he's the one that's behind it all!"
            show dragon pantsless cry
            "In a flash Benson moved forward, throwing his fist right into Orlando's gut. He was nimble and precise, knocking the wind out from Orlando so he let go of the coat he was clinging to."
            show oz pout
            "Orlando fell to his knees, gasping for air."
            otter "I'll say it plainly. It was a tragedy, but I will not allow you to throw accusations towards Master Oswin freely. {i}Especially{/i} from one such as yourself."
            hide dragon with dissolve
            "Hoss pulled Orlando off to the side, glaring daggers at Benson. Not that he seemed to pay much attention to him now that Orlando was removed."
            oz "Are we done?"
            show otter neutral
            otter "I believe so, sir."
            hide otter
            hide oz
            with dissolve
        stop music fadeout 2.0
        "While I tried to get my nausea under control, I just let things play out. Let people say what they needed to and hopefully getting to vent would help."
        "The next moment the world was rumbling, followed by the sound of an explosion somewhere in the distance."
        play music tense fadein 2.0
        show wolf underwear yell at left
        show dragon pantsless scared at right
        with dissolve
        wolf "The fuck was that?"
        dragon "I don't know! Is everyone okay?"
        "Hoss sped a little ways further down the driveway, looking around. He didn't say anything but he looked worried. Eventually he moved further on and out of sight. He was out of sight before I could ask if he was going to check."
        if OswinDead == False:
            hide wolf
            hide dragon
            show oz mad at left
            show otter annoyed at right
            with dissolve
            oz "Benson!"
            otter "Sir, do not start. I know just as much as you do."
            oz "Then find out, damn it!"
            hide otter
            hide oz
            with dissolve
            "Benson sped off down the driveway after Hoss, moving quicker than I expected him to."
        "And so we waited, Tyson huddling close to me on one side with Orlando on the other."
        if OswinDead == False:
            "Oswin was still standing where he was originally, arms folded and tapping his foot. He seemed anxious despite his frown, and who would blame him after what we heard?"
        "Time continued to pass, and as it did my worry grew. I didn't know how long this driveway was, but eventually..."
        if OswinDead == False:
            show lion shirtless sad at left
            show otter pout at right
            with dissolve
        else:
            show lion shirtless sad
            with dissolve
        mc "You're back!"
        "Despite the relief of seeing Hoss again, he looked even more troubled on his return."
        mc "What... What happened?"
        lion "The main road, part of it..."
        if OswinDead == False:
            show otter neutral
            otter "...it's gone."
            mc "What do you mean gone?"
            otter "Landslide perhaps, although I imagine it was the explosion that set it off. Part of the road is missing and a large part of it is covered in debris."
            mc "Wait, but that means..."
        else:
            mc "It's... what?"
            lion "It's gone!"
            "I looked between Ty and Orlando confused, but it seemed as though both of them were just as confused as me."
            mc "It can't just be gone! Where did it go?"
            lion "If I had to guess, that explosion we heard blew up part of the road along with causing a landslide. Either way, getting over that rubble seems... possible but..."
        hide otter
        hide lion
        with dissolve
        show dragon pantsless scared at left
        show wolf underwear sad at right
        with dissolve
        dragon "We're... we're trapped here?"
        wolf "Sounds like it..."
        show wolf underwear mad
        wolf "But fuck that. Come morning I'll just keep going until we find help."
        mc "But... what until then?"
        show dragon pantsless sad
        dragon "Do... Do we return to the mansion? It's cold out here and uh... I wouldn't mind some pants. But... then there's Sal..."
        wolf "I'm not scared. "
        show wolf underwear annoyed
        extend "Fuck. I'll go get you pants if that's all you're after."
        show lion shirtless sad with dissolve
        lion "Where does that leave us?"
        if OswinDead == False:
            hide lion
            hide wolf
            hide dragon
            with dissolve
            show oz pout at left
            show otter neutral at right
            with dissolve
            oz "Spending the night outdoors is unwise. "
            show oz neutral
            extend "For that reason I suggest we all take refuge inside the manor. Both for warmth, comfort, plus the dangers of unclaimed wilderness playing host to any number of things."
            mc "And... the... um..."
            show otter pout
            otter "You are concerned about your friends. "
            show otter neutral
            otter "I shall tend to them. Respectfully of course. At least until we can get in contact with the proper people so they can be buried properly."
            "I dropped my head, thinking it over."
        else:
            wolf "Well I'm not spending the night outside. I'll sleep in the greenhouse if I need to."
            dragon "But... we'll have to go inside at some point, right? And... how long will that be?"
            show wolf underwear mad
            wolf "Tomorrow."
            lion "That doesn't help us right now, and it's dark. Plus it's uh... well..."
            show wolf underwear annoyed
            wolf "Fine. What if I moved the bodies?"
            show lion shirtless scared
            lion "You'll... move them?"
            show wolf underwear mad
            wolf "Fuck it. I don't care. Having them just... {i}there{/i} is just..."
            "He trailed off, gesturing to the space before him. Although the meaning wasn't lost on us."
        scene mansionfront with dissolve
        "We trekked back the way we came. It was still late, and having nothing to show for it, the walk was spent in silence."
        "As the house came into view our pace slowed, knowing what still awaited us on the other side of the door."
        if OswinDead == False:
            "Benson wandered inside, poised and proper as he always was. We knew what he went in to do and after a long while of waiting he emerged, somewhat bloody, but ensuring us that the deed had been done."
            "Without hesitation, Oswin wandered inside ahead of us, leaving us out in the cold."
        else:
            "I looked to Ty who seemed reluctant to move, but upon looking at me he snapped his head forward. He was stiff, marching towards the door and out of sight."
            "And so we waited. Before long he appeared, looking disheveled and bloody, but the deed had been done."
        scene foyer with dissolve
        stop audio fadeout 2.0
        stop music fadeout 2.0
        "The moment I walked in, the smell of blood hit me. My eyes trailed to the floor, seeing the drag marks heading off to an adjoining room."
        play music sad fadein 2.0
        mc "I can't..."
        "Everyone else was moving around me, seemingly in a trance as they headed towards the stairs."
        "The smell of blood here was suffocating. My vision was going red and I felt as if I was drowning in the smell. So much so that I could taste it."
        show dragon pantsless sad with dissolve
        "Orlando reached out and took my hand, giving it a gentle squeeze."
        dragon "Come on..."
        mc "I... I want to see them..."
        if bearroute == True:
            mc "I want to say goodnight to my bear... I want..."
            "I felt sick, the conversation I had with Dean playing over in my head. The plans for tomorrow that would never happen."
            mc "We were... He..."
            "I wanted to cry, but it just wouldn't come. I just devolved into whining, almost clawing at my face to try and bring on the tears."
        elif boarroute == True:
            mc "I want... to say goodnight to Roswell..."
        "I felt his arms around me in a gentle hug before he broke away a second later."
        show dragon pantsless cry
        dragon "Tomorrow? Please? I... I'll come with you I just... need time to prepare myself..."
        scene bedroom
        show wolf shirtless sad at left
        show lion shirtless sad at right
        with dissolve
        "By the time we made it upstairs, Hoss corralled us into a single bedroom. Just so we were all in the same room."
        lion "It might be safer to stick together tonight. For what's left of it at least."
        mc "Yeah... that makes sense..."
        "Tyson handed me a shirt and I threw it on. I didn't even know who it belonged to but it was better than nothing."
        "Orlando and I watched as Hoss and Ty pushed stuff to block the door off. I could only imagine why."
        hide lion
        hide wolf
        with dissolve
        "All that was left was to settle in for whatever rest we could get."
        if wolfroute == True:
            "Ty settled in, pulling at his fur. He looked a mess, and no wonder. I sat down beside him, not sure of what to say and half expecting him to cuddle into me I just waited."
            "But nothing."
            mc "Ty... I-"
            "My voice was barely above a whisper but he shot me a pained look, gesturing for me to stop. It seemed he was mourning in his own way, or maybe he was finally breaking now that the immediate danger was over. Maybe part of it was the job to do tomorrow."
            "All I could do is nod, trying to find a spot to get comfortable in. As I closed my eyes I felt him shift behind me, resting his back against mine. It wasn't cuddling, but I got the impression this felt safer for him."
            scene black with dissolve
            "Eventually I passed out, the stress and fatigue catching up to me again. If only for a couple of hours, I was able to get something in the way of sleep."
        elif lionroute == True:
            pass
        elif dragonroute == True:
            "I looked to Orlando, and he took my hand in his. Wordlessly he guided me over to a corner of the room that the other two weren't occupying."
            "Ty looked like a mess and Hoss was rocking gently back and forth before he eventually just lay down."
            "As for Orlando and I, he lay me down and faced me towards the wall. He cuddled up behind me, almost using his body as a shield from the others in the room and resting his head atop mine."
            "I used his arm as a pillow and quietly sobbed despite no tears coming. I just couldn't manage it, but I wanted the tears to come all the same."
            scene black with dissolve
            "Maybe it was everything hitting me at once, but I passed out. While it was only going to be a couple hours of rest, it was all we were going to get."
        elif bearroute == True:
            "I watched as the others huddled in various spots in the room. They looked distant, afraid, and I felt the same."
            "I looked at the shirt I was wearing and sighed out, thankful that it wasn't immediately obvious as one of Dean's. I was unsure if wearing one of his shirts now was the right way to go."
            "Curling up, I tried to settle down enough to get some rest. But my eyes kept darting between the others in the room, all of them looking troubled."
            scene black with dissolve
            "Closing my eyes tight I willed sleep to come to me faster, and as difficult as it was, eventually I just passed out."
            "At best it'd only be a couple of hours, but at this point I needed all I could get."
        else:
            "Everything that had happened made my head spin. So much so that I found a spot away from the others and just collapsed."
            "I took the time to look at the others who all seemed to have done the same, a combination of exhausted and scared."
            scene black with dissolve
            "There wasn't anything we could do now, and as much as I'd started this night in my own bed, I was spending the rest of it on the floor by myself."
            "Closing my eyes helped lull me to sleep, but knowing I wouldn't get a lot of it kept me from drifting off comfortably."
        stop music fadeout 2.0
        jump Day11CMorning

label Day11CGoodMorning:
    return
