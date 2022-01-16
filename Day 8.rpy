label day8morning:
    $ currentDay = 8
    scene day8 with fade
    $ renpy.pause (3.0)
    if BETRAYAL == False:
        scene bedroom with dissolve
        play music dark fadein 2.0
        show dragon cry with dissolve
        dragon "[mcname]! Wake up! Please!"
        "It was sudden, and I was being shaken by the shoulders by Orlando who had tears streaming down his face."
        if dragonroute == True or lionroute == True:
            dragon "Come on, hurry! I need your help!"
            "Was I dreaming, or was this actually happening?"
            if dragonroute == True:
                dragon "It happened again and I don't know what to do!"
            else:
                dragon "Something terrible has happened!"
            "A sinking feeling in my stomach came immediately after. I didn't want to move, but I was already half up from being concerned about how upset Orlando was."
            "I was scared to ask, scared to find out who was the next victim. In a daze I got up and stared at Orlando trying to figure anything out from his sobs."
            dragon "C-Come on, let... Let me show you. No one else is up yet so..."
            scene foyer with dissolve
            "Orlando started moving before I could protest, and we went down to the foyer."
            "We paused before the door to the dining room. Orlando went to open the door but shied away, looking to me. I knew what this meant. Whatever was on the other side of this door wasn't going to be good."
        else:
            mc "H-Hey, Orlando, what's wrong?"
            dragon "Something bad happened!"
            "My mind began to race, trying to place what could've happened. I immediately feared the worst, but pushed it back down in hopes that I was just still tired after the day before."
            mc "It's okay, just tell me what happened."
            "Orlando's breathing was all over the place, but he nodded to try and bring himself under control."
            dragon "I-I got up this morning. I couldn't sleep and... I went to the dining room and..."
            "His crying started up again, and I took the chance to see just how early it was. Early enough that even Sal wouldn't be up this early. Explained why it was still so dark, too; it was well before dawn."
            mc "Should... I go see what's in the dining room?"
            show dragon sad
            dragon "I... I think so. But you're not going to like it. At all."
            mc "Oh... Is it... bad?"
            show dragon cry
            dragon "I don't... Very bad, [mcname]. Very, very bad."
            "Orlando wandered over to my bedroom door, looking antsy. There was no avoiding it; at some point I was going to have to go to the dining room and for whatever reason Orlando had decided to come and grab me instead of anyone else."
            scene foyer with dissolve
            "The two of us made our way downstairs, Orlando lingering behind me as we headed towards the dining room. Just before the door, I reached out for the handle, shooting the dragon next to me one last look."
            "With a quick nod from him to indicate... something, I faced the door again, gulping. Whatever had set Orlando off like this wasn't going to be pretty."
        play music dark fadein 2.0
        scene diningroom with dissolve
        "I opened the door and took a step forward, with Orlando lingering by the entrance. Apparently whatever had happened spooked him enough that he didn't want to get closer than necessary."
        "It didn't take long before I could smell it though, the overbearing scent of iron and the faintest whiff of gunpowder. I froze, my heart catching in my chest. Somehow I was able to edge closer, taking it step by step."
        stop music
        "Nothing prepared me for what I saw when I rounded the edge of the table closest to the kitchen. Whether the tablecloth of something was the cause of how I didn't see it from the entrance, I didn't know."
        "But the moment I saw it, I yelled, anguished and confused."
        play sound heartbeat
        scene bensondead with dissolve
        "My eyes were glued to the scene before me on the floor. I heard Orlando scurry off while I took in everything before me."
        "He'd been so... scarce the past few days it was almost as if he'd literally disappeared. For him to show up here, like this, was almost a grim reminder that whoever had done this hadn't forgotten he was around."
        "My eyes settled on the gun in his hand, and I began to breathe hard and fast. I backed up until I was against the wall, still staring, hyper focused on the body before me."
        "Was it better that this wasn't one of my friends, or worse because the chances of them being the culprit had skyrocketed?"
        scene diningroom with dissolve
        show bear mad at left with dissolve
        show wolf mad at right with dissolve
        "I could hear the others pile in, catching Orlando asking someone else what they should do in the case of someone committing suicide. I think it was Hoss that was trying to calmly explain what he could despite the tones of panic in his voice too."
        "Dean and Tyson were eyeing each other off, having both rushed over to me to make sure I was okay."
        if PEACEKEEPER == True:
            "But I wasn't paying attention to either of them. I was focused on the gun."
            "Orlando gets shot. Was it about to happen? Was this the point I had to step in?"
            if dragonroute == True:
                "I looked to Orlando for a split second before I knew what I had to do."
            else:
                "There was no point risking it. If I didn't get there first, who knows what could happen?"
            show wolf scared
            show bear scared
            "I shoved Dean and Ty aside, only probably doing so because they'd been caught off guard. Scrambling forward I got to Benson's body and soon slipped, falling onto my butt just shy of landing in his blood."
            "But just looking at it made me pale. I began to panic before realizing what I'd done and why I'd done it. Shutting my eyes I spun around, voice cracking as I called out to the others."
            mc "G-Guys? Help..."
            wolf "R-Right. Dean, help me out here."
            bear "Sure."
            "I felt them both pull me away until I was propped against the wall, Tyson gently petting my head."
            show wolf neutral
            wolf "You good?"
            mc "Better, but..."
            show wolf pout
            wolf "Yeah, alright."
            bear "Can... someone explain what just happened?"
            wolf "You reckon you'd be alright getting close to a body like that? Come on, pup. Breathe for me."
            hide bear with dissolve
            hide wolf with dissolve
            "I nodded quickly, covering my eyes. Dean added a hand to my shoulder as Tyson continued to stroke my head."
            "When I opened my eyes, I could see Orlando having an equally hard time processing what was going on. Hyperventilating with his head resting against Sal's chest."
            show boar mad at left with dissolve
            show lion scared at right with dissolve
            lion "Everything alright over here? What..."
            "I looked up to Hoss as he looked over to where Benson lay on the ground, dead."
            lion "...Oh."
            jump Day8MurderTime
            #Dave gets the gun
        elif wolfroute == True:
            wolf "I fucking knew it!"
            "Before I could ask further, Tyson made a break for it, diving for Benson's body, hand reaching out for the gun on the floor."
            "Dean must've feared the worst, following suit."
        elif bearroute == True:
            "I looked at Dean, whose eyes shot from Tyson to the gun, then back at Tyson with the meanest scowl I'd ever seen him wear. In a flash, he was diving for Benson's body."
            "Almost immediately after, Tyson shoots me a look, coming to a revelation on his own part before he too dived after Dean, scrambling for the gun."
        elif boarroute == True:
            "In unison, their attention on me shifted to Benson's body, notably the gun still in his hand on the floor."
            "With one last look at one another, they both made to dive for it."
        else:
            "It didn't last long though, for the moment they had noticed the gun they both made a go to retrieve it, ending in them fumbling over one another."
        play music tense fadein 1.0
        scene deantysonfight with dissolve
        wolf "I knew I couldn't trust you, {i}bear{/i}! Stashing a gun just so you could fuckin' kill someone with it!"
        bear "Me!? Rich coming from you, mutt! Only one packing heat here would be you and I'll be damned if you think you can do in someone else too!"
        "My eyes were glued to the gun in their hands, them reaching fist over fist to have control over it. Shakily my hands made for my head and gripped what fur I could tight."

        if ARBITER == True:
            scene black
            "But then, amidst all the panic I had a moment of clarity. This is what the vault had shown me. This was an important junction, somehow, and I needed to stop it. I didn't know what was going to happen if I didn't but..."
            scene diningroom
            mc "Stop!"
            "My voice was cracking, tears now streaming down my face and I openly bawled. I'd apparently gotten back to my feet at some point only to fall onto my knees, crestfallen."
            mc "No... No fighting!"
            "The animalistic growls of Tyson and Dean had died down and before I knew it I had one of them hugging me. I had my eyes clenched too tightly to know which one, and my nose was too clogged to even identify them by smell before they pulled away."
            show croc mad with dissolve
            croc "What is wrong with you two?"
            show lion yell at left with dissolve
            lion "Do you {i}know{/i} what a gun of that caliber could do if it misfired? You're lucky you didn't drop it!"
            show dragon scared at right with dissolve
            dragon "So... are we safe? Nothing... nothing else wrong is going to happen, right?"
            "There was a tense silence around the room, all of us looking at one another. I wiped my eyes and got my breathing under control enough to try and ground myself against the wall."
            "Benson was dead, but... That was all. Heartless, but I barely knew the guy and I was facing two of mine playing with a gun."
            "Dean seemed to be putting the gun back when I noticed Roswell wandering closer to Benson's body with Hoss."
            hide croc with dissolve
            show boar mad with dissolve
            show lion scared with dissolve
            lion "It can't... but..."
            boar "...It is."
            #Dave stops the fight
        else:
            "No one else seemed to be saying anything, I know I wanted to but I was so scared, I was paralyzed in fear."
            "They bickered back and forth, the gun waving wildly above between them until it slipped from their grasp."
            scene black with dissolve
            stop music
            $ renpy.pause (1.0)
            "I watched it fall almost in slow motion. The only sound I could make out was my own breathing until everything else was broken by the single sound of it misfiring."
            $ renpy.pause (1.0)
            "My breath had caught in my chest, and as my hands scrambled over my body, expecting to feel a patch of wetness or a hole, or even a burning sensation, I let it out as a sigh of relief."
            "I looked to the others, a smile starting to form but it died soon after."
            show orlandoshot with dissolve
            "My mouth hung open, head shaking gently from side to side, denying what I'd just seen."
            dragon "I..."
            "Orlando was in shock, as was Sal who was hurriedly trying to do something about the wound in the dragon's chest."
            "My mind began to swim, having been thrown for a loop multiple times in quick succession."
            play sound heartbeat
            dragon "S-Sal... I don't... Why's it... so cold now?"
            croc "Hold on! {i}Please{/i} hold on! I won't let you die!"
            scene diningroom with dissolve
            "Hoss was running out of the room and into the foyer, I don't know why."
            "Dean and Tyson were still at each other's throats but I couldn't hear what they were saying."
            "Sal was tending to Orlando, trying to stop his bleeding with what little he had to work with. Orlando seemed to be hanging off every word he said, trying to stay conscious."
            "Then there was Roswell, who had wandered on over, seemingly in the same state as me, stopping just before Benson's body and looking down upon it."
            "I pushed myself off the wall to stand, wandering over to Roswell."
            boar "This... doesn't make sense."
            "It was almost like a mantra with how he seemed to repeat the line over and over, almost trying to piece together why."
            "Looking at Benson's body, I could only agree. Something was off about it, something that seemed so obvious but was just barely out of reach."
            scene black with dissolve
            play music sad fadein 2.0
            "At some point, the police and paramedics arrived, taking Orlando away."
            "We were questioned, but they let each of us go. We found our own ways home from there, what had happened creating a rift in the group that bred distrust as to who did what, and where the blame should be flung."
            "I blamed myself and my inability to keep things under control. Thankfully, no one else did."
            "A week later..."
            scene carpark with dissolve
            "I was at the hospital with flowers. Dean helped me pick some out, and with some careful planning I was able to find a time to come visit when Orlando's family wasn't around."
            "Various dragons in suits seemed to loiter around the place, and there was an air of oppression that lingered in the areas they were stationed."
            "Sal had given me the room number he was in, so thankfully I knew where to go and could make a beeline there instead of having to stop by reception."
            scene hospitalroom with dissolve
            "Funnily enough, despite the state of things outside the room, Orlando was sitting in a chair by the window, enjoying some sun while he played on a handheld gaming device."
            show dragon injured neutral with dissolve
            "Just seeing him alive and well set my mind at ease. I'd assumed that he'd be in bed unconscious or something. But no, there he was as if nothing had happened, shy of the bandages wrapped around his front."
            mc "Hey Orlando, how are you feeling?"
            dragon "Oh! [mcname]! It's good to see you!"
            "I set the flowers down on a table nearby and wandered over to take the other chair next to Orlando."
            dragon "Doing okay. The doctors reckon that I got really lucky."
            mc "Was the wound bad? I'm... I'm sorry that I couldn't... and didn't, help..."
            dragon "Don't be silly. I was convinced I was going to die when it happened, Sal talking to me up until the paramedics came, helped."
            show dragon injured sad
            dragon "Apparently that's an important thing. Your body can go into shock if it thinks you're going to die. It just... gives up."
            "I hung my head, ashamed."
            mc "I'm sorry it took so long to come visit. But I brought flowers!"
            show dragon injured neutral
            dragon "They're lovely! Thank you!"
            mc "And... I'm sorry you got shot."
            show dragon injured sad
            dragon "[mcname], it's not your fault. You didn't shoot me, no one did."
            dragon "Speaking of... How's Dean? And Tyson?"
            mc "Dean's good, he dropped me off here, actually. He's doubled down on some sleeping medication he'd been taking. Didn't sleep for a few days after it happened."
            if crocroute == True:
                dragon "By... medication..."
                mc "Bear tranquilizers, yeah."
            else:
                dragon "Wow... Poor guy. But so long as he's getting sleep now it's... fine, right?"
            "I nodded slowly, waiting to see if he had anything else he wanted to say. When he didn't, I continued."
            mc "Tyson... he's..."
            show dragon injured neutral
            dragon "He's...?"
            mc "Around. Still. He's been staying with me, something about not wanting to go back to his and also wanting to make sure I wasn't too beaten up about... y'know."
            show dragon injured sad
            dragon "It's not his fault either. It... hurt, sure, but..."
            mc "But...?"
            dragon "Well, I wish that... Well, that it didn't happen for starters."
            dragon "But I guess more importantly that I could tell him that in person?"
            dragon "Him {i}and{/i} Dean really. Maybe in a week when I'm discharged we can have lunch together. Something quiet just to settle everything."
            mc "That... that sounds good. I'll let them know and try and organize something. Maybe a picnic?"
            show dragon injured neutral
            dragon "There you go. A picnic sounds great."
            "I drummed my fingers on my knees, not really sure what I should be saying next. I still felt bad about what had happened despite Orlando telling me that it wasn't my fault."
            show dragon injured sad
            dragon "Y'know... This past week I've been wondering something."
            mc "What's that?"
            dragon "If you had a do-over. What... What would you do different?"
            mc "Oh geez, Orlando, I don't think..."
            show dragon injured neutral
            dragon "Humor me."
            mc "I'd... probably try and stop you getting shot for starters?"
            show dragon injured laugh
            dragon "Okay, but how?"
            mc "Oh, uh... I dunno?"
            show dragon injured neutral
            dragon "I think we were just missing something major in the group dynamic at that critical point is all. Maybe not necessarily a tank or something but..."
            show dragon injured sad
            dragon "How do I want to phrase it...?"
            "Orlando tapped his chin, stroked his beard, turning to look out the window before continuing his thought."
            dragon "Maybe... If we had someone that could arbitrate between Dean and Tyson?"
            mc "Don't I do that already?"
            dragon "You do, but... I mean in that point you would've really needed to put your foot down. Or interject enough that they'd stop. I imagine they'd both listen to you if you made a demand."
            mc "Demands are bad though."
            dragon "True, but how often do you, of all people, demand something? They'd be more than willing to comply if you spoke up with enough gusto I think."
            mc "I'm not like my dad, Orlando. I wish I was but he was just..."
            "I sighed out, falling further down the hole of shame I was digging for myself for being so inadequate."
            show dragon injured neutral
            dragon "Now, now. I'll have none of that. You have the makings of a great peacekeeper in your own way. Don't need to be a cop for that."
            mc "You really think so?"
            show dragon injured laugh
            dragon "I do!"
            dragon "Maybe it's something to consider just in case something like this happens again. Not that I'm volunteering to get shot again, but still."
            "I nodded slowly, looking out the window now too."
            "A peacekeeper, huh? The idea stuck with me, but I couldn't place why."
            show dragon injured neutral
            dragon "I'm glad you came to visit, [mcname]. It's... Well, I'm glad to know that things are still keeping together even after all this."
            if dragonroute == True:
                show dragon injured sad
                dragon "Granted... Might be a little different if it was one us killed instead of Benson..."
                dragon "Because... he was killed, right? It wasn't suicide?"
            else:
                show dragon injured sad
                dragon "To think... He committed suicide right there for us to find him. Right?"
            scene black with dissolve
            "I wasn't convinced either way, but last I heard it was ruled as such. Honestly I was just thankful that Dean and Tyson weren't getting thrown in jail for injuring Orlando."
            "But with Benson's suicide calling an end to our vacation things... became odd."
            "Roswell got really sick and had to be admitted into hospital, after I was done visiting Orlando I was going to pay him a visit too."
            "Dean... despite everything that happened, asked me out proper. Given the circumstances I took him up on it and we're... together, at least as a trial basis."
            "Tyson said he didn't mind, but left one day saying that he needed to sort some things out."
            "Sal stuck around too, ended up moving in with Hoss. The pair... seem to do alright? Keep mostly to themselves but they check in every now and again. Orlando moved in with them after he was cleared from hospital."
            $ renpy.pause (1.0)
            scene dayother with fade
            $ renpy.pause (3.0)
            scene street with dissolve
            "I was sitting outside waiting for Dean to get back from work with a glass of lemonade for the last hour. The weather was nice, and it was date night, so why not wait for my bear to get home and enjoy some sun?"
            "I pulled out my phone to check the time. He was late, sometimes it was just traffic but this was... getting a bit odd."
            "Rule was that he wouldn't check his phone while driving anyway, so even if I tried to call or send him a message he wouldn't be checking it until he pulled up."
            "As I was about to put it away, mid sigh it went off in my hand, causing me to jump and spill some of my lemonade on my shirt."
            mc "A-Ah! Cold!"
            "Setting the glass down and brushing off what moisture I could before it could seep into the fabric I looked at who was calling. I didn't recognize the number, so I ignored it under the assumption that if it was important they'd leave a message."
            mc "Hm... It stopped ringing. Guess it wasn't important afte-"
            "Then it started again. This time, it was Hoss calling. I looked out to the road quickly to see if Dean was pulling up before answering."
            mc "Hi Hoss! What's up?"
            lion "[mcname]."
            "His tone was serious, he sounded out of breath, and I could hear... something in the background, almost like a siren."
            lion "I need you to stay calm, and I need to know if you're able to meet me somewhere."
            mc "Is... Is everything okay?"
            "The next moment I was standing, abandoning my lemonade to wander to the fence and look out at the street. Not that I knew what I was looking for, but I did so anyway."
            lion "No. It's not. There's..."
            "I felt my chest tighten, dreading the worst given Dean's lateness."
            mc "Is Dean...?"
            lion "Huh?"
            mc "No, sorry, you first."
            lion "Uh... Look, maybe I should just..."
            "There was a sound of the phone being handed off to someone else before a familiar voice came through on the other side."
            bear "Hey, handsome!"
            mc "Dean! What's going on! Why are you with Hoss? Why were you late?"
            bear "So... about that."
            bear "I want you to sit down, and stay calm, okay?"
            "I did as he said, sitting down on the grass rather than wandering back to the steps leading up to the front door."
            mc "Okay, I'm sitting."
            bear "Okay... I'm going to come get you in a bit, but..."
            mc "Dean?"
            bear "Orlando's dead, [mcname]."
            "I almost dropped the phone in shock."
            mc "W-What? But... How? Why? {i}When{/i}?"
            bear "Just... hang tight. I'll come pick you up and explain."
            scene black with dissolve
            "But that wasn't the worst of it."
            "When Dean picked me up, I bombarded him with questions. He didn't answer at first, seemingly steeling himself before delivering more bad news."
            "It wasn't just Orlando. Roswell had been killed as well."
            "Sal was a wreck, having been shot as well but was only nicked in the shoulder. Given how big he was, it was a wonder the gunman missed as they did."
            "By sheer chance Dean was driving by Hoss's house when it happened, Roswell, Orlando, Hoss and Sal were all just in their front yard as a car pulled up and fired at them."
            "Hoss came to stay with Dean and I, with Sal joining us just so they weren't near the scene of two of their friends dead."
            "My faith had been rattled, the last conversation I had with Orlando in the hospital ringing through my mind."
            "Was there anything I could've done differently?"
            "Dean tried his best to help the police track the car from the license plate, but the investigation seemingly went cold."
            "Not to mention the streets became more dangerous soon after, you could see it whenever we went to the store. There were less police and more dragons in suits loitering about the place."
            "Our corner of the world went dark, something went wrong, and there wasn't anything we could do about it."
            $ renpy.pause (3.0)
            "{color=#EE2c2c}{b}BAD END: BENSON{/b}{/color}"
            return
        label Day8MurderTime:
        play music tense fadein 2.0
        "Hoss lingered back while Roswell stepped forward, almost steeling himself for what he was looking at."
        lion "How are you keeping your cool like this?"
        "Roswell shook his head, eyes narrowing as he continued to look before he backed back up."
        boar "...Okay."
        boar "...We have a problem."
        show lion mad
        lion "You're kidding, right?"
        show lion yell
        lion "Roswell, he's fucking {i}dead{/i}."
        "I hadn't heard Hoss swear before, typically he tried to keep that sort of stuff... well..."
        boar "I can {i}see{/i} that, Hoss."
        show lion mad
        boar "But the problem we have is much bigger than that. {i}Much{/i} bigger."
        "I got up, bracing myself against Tyson who was lingering nearby."
        mc "Roswell...? What... What's the problem?"
        show boar sad
        "Sal wandered over, guiding Orlando over too by the hand until we were all standing somewhat in a circle."
        boar "...This was murder."
        mc "But... he shot himself... didn't he?"
        hide dragon with dissolve
        show bear mad at right with dissolve
        bear "[mcname]. If you hadn't..."
        bear "It's not suicide."
        show boar annoyed
        boar "You noticed?"
        bear "I did."
        boar "Okay... Everyone...?"
        boar "One of us killed Benson."
        mc "W-What...?"
        hide bear with dissolve
        hide boar with dissolve
        "We looked around at each other, sizing each other up. Even Tyson, who I'd been supporting myself against had taken a step back to give me some space."
        mc "Are... you sure?"
        show lion mad at left with dissolve
        lion "I... can confirm that. Not only that... Someone's messed with the crime scene."
        mc "Wait, what? How? Why? I don't..."
        show dragon sad at right with dissolve
        dragon "It's... the wound, right?"
        show lion scared
        lion "Well... Maybe?"
        dragon "That wound... Think about... Think about the hand he's holding the gun in. And..."
        show dragon scared
        dragon "Y'know... Right?"
        lion "Oh damn, you're right."
        lion "Is that what you noticed, Dean?"
        hide dragon with dissolve
        show bear mad at right with dissolve
        bear "I did."
        show lion mad
        lion "What I noticed..."
        lion "That gun... Way too powerful to cause a wound like that. He'd have blown a lot more of his head off using something like that. Not just that, but... Reckon he could've used a gun that big given his size?"
        "I felt my stomach lurch, and I had to support myself on my knees without falling over."
        mc "So one of us..."
        show bear pout
        bear "Killed Benson..."
        show lion sad
        lion "...And then changed the crime scene. What I don't get, is why."
        hide bear with dissolve
        show boar pout at right with dissolve
        boar "What do you mean?"
        lion "If... Benson used a gun to kill himself. You wouldn't want to change the crime scene at all, would you?"
        boar "Oh, right, that's fair."
        lion "So if it's murder... why not still use the same gun? Why change guns?"
        boar "I... hadn't thought of that."
        scene diningroom with dissolve
        "I looked at the gun again, then immediately to Sal who seemed to be the only one big enough to handle something like that. With how he was still rubbing Orlando's back it was hard to throw an accusation that way."
        "Next up was Dean, who... I guess could have also handled a gun like that? He caught me looking at him and looked away just as quickly as he'd noticed, frowning."
        show boar sad with dissolve
        boar "So... That's it. One of us is a murderer."
        "The comment hung in the air before I realized that maybe... there was another option."
        mc "I..."
        "The moment I'd started speaking all eyes were on me. I had a choice to make. I had no proof, and no evidence of the fact, but... There was potentially one other person in this house that we hadn't considered."
        "One person that we hadn't seen, and that as far as I was aware, only Benson and I knew about."
        menu:
            "Reveal Oz":
                "I breathed in one more, putting on my best brave face, believing that there was someone else that could have done it. If they did, it meant all of my friends were innocent. Something I could throw my weight behind as far as what I wanted to believe."
                mc "There's... someone else that could have done it."
                show boar annoyed
                boar "Someone... Else?"
                show dragon pout at left with dissolve
                dragon "But...[mcname], we're all here. Who else could there possibly be?"
                show croc pout at right with dissolve
                croc "Someone else... Another butler? A maid?"
                dragon "But we haven't seen anyone else like that, have we?"
                boar "I sure as hell haven't."
                "I looked to Hoss, who seemed to have his phone out, poised to dial a number but holding off to listen in."
                mc "I... No one here did it, right? I'll believe you if you tell me, I just... want to hear you say it."
                "In turn, each of us said that we didn't do it, almost vowing to one another that we were innocent. After Orlando had gone last, finishing off the claims of innocence, I nodded."
                mc "Then... if none of us did it... It could only be... Oz."
                show boar scared
                show dragon scared
                show croc neutral
                croc "Oz. Like the... wizard?"
                dragon "Wait, no, let's backup a little bit here. There's actually another person here?"
                boar "That'd make... Nine people in the mansion, right? But... we haven't seen anyone else, right?"
                if bearroute == True:
                    "I thought back to the woods, and that white blur that I'd stupidly followed. Was that Oz? Was that who had killed Benson?"
                "It seemed unlikely that Oz would kill his own butler, especially after claiming that he was going to be more of an ally. But who else could it be?"
                hide boar with dissolve
                hide dragon with dissolve
                hide croc with dissolve
                show wolf yell with dissolve
                show bear mad at left with dissolve
                show lion mad at right with dissolve
                wolf "The fuck, [mcname]! Why'd you keep this from us?"
                mc "I-I... I don't know!"
                bear "Well who is he then?"
                mc "He's the one that owns the house, I think?"
                lion "How do you not know that! You must have spoken to them, or to Benson about this person, right?"
                mc "We spoke, sure, but-"
                show bear yell
                bear "When!? Where!?"
                mc "U-Uh... In my room! Night before last?"
                show bear scared
                if bearroute == True:
                    bear "But that'd mean... After I left..."
                else:
                    bear "Seriously? You're going to invite others to your room?"
                wolf "Shut it, bear! Pup, you better start talking!"
                scene diningroom with dissolve
                "So I recounted to the group as to what had happened. How I'd used the vault, and then spoken to via radio planted in my room to someone claiming to be Oz."
                "I told them how I was told to meet Oz in the library last night to talk in person but he never showed up."
                mc "I'm... sorry for not telling you..."
                show lion mad with dissolve
                lion "You should have told us that there was someone else here. Who knows what they could be up to?"
                mc "Sorry..."
                lion "I'm going to go call it in though."
                hide lion with dissolve
                show boar pout at left with dissolve
                boar "What... should we do? Should we go looking for this Oz person?"
                show croc sad at right with dissolve
                croc "Potentially. It... wouldn't hurt, right?"
                show boar sad
                boar "If the police are on their way, it'd be faster to split up to search everywhere in case they try and make a break for it."
                show croc pout
                croc "They may have already left."
                show boar pout
                boar "Good point."
                hide boar with dissolve
                hide croc with dissolve
                show bear pout at left with dissolve
                bear "So we're just meant to wait?"
                show wolf neutral at right with dissolve
                wolf "Yup."
                show bear mad
                bear "What do you mean, 'Yup'?"
                wolf "You can go off looking if you want, I'm staying right here until the cops arrive. No way I'm getting pegged for this by wandering around."
                hide bear with dissolve
                "Dean stormed off, leaving the same way Hoss did, presumably to go see what he was doing; I wasn't really paying attention."
                mc "What... should I do, Ty?"
                wolf "Stick with me. Have to keep you out of trouble."
                show boar annoyed at left with dissolve
                boar "[mcname] will be fine."
                wolf "And I'm gonna keep it that way."
                hide boar with dissolve
                "Roswell grumbled for a while before he wandered off too, again, same direction as Dean and Hoss."
                hide wolf with dissolve
                show croc neutral at right with dissolve
                show dragon sad at left with dissolve
                dragon "I don't... Can we maybe wait in the foyer? I don't really want to be standing around uh... Well, y'know."
                mc "Oh... Yeah, me neither."
                show croc pout
                croc "Tyson and I... can watch this room, if you want. You two stick together."
                mc "Really?"
                hide dragon with dissolve
                show wolf neutral at left with dissolve
                wolf "Go on, pup. Stick with Orlando."
                scene foyer with dissolve
                "I nodded and followed Orlando out to the foyer, looking around and feeling an odd... unease about the place that wasn't there before."
                mc "Orlando...?"
                show dragon sad with dissolve
                dragon "Yeah?"
                mc "No one... did it, right?"
                dragon "I wish I knew... Still..."
                if dragonroute == True:
                    dragon "Do you think... this Oz person you spoke to has anything to do with the vault downstairs?"
                    mc "Huh?"
                    show dragon pout
                    dragon "Just... curious. I was thinking that... if they owned the house, they might know something about it, right?"
                    mc "Maybe, but... It's not as if we can ask, right? He only speaks to me when he wants, I don't have a means of communicating with him."
                    dragon "Right, right..."
                else:
                    "Orlando trailed off there, thoughtful but he didn't continue."
                "As we sat in the foyer, Orlando fidgeted, eyes looking over to the staircase."
                dragon "Hey, [mcname]? Do you think... we could go check something out?"
                hide dragon with dissolve
                "He barely waited for me to nod before he guided me forward."
                scene basement with dissolve
                "Down into the basement."
                scene vault with dissolve
                "...and into the room with the vault door."
                show dragon sad with dissolve
                dragon "This room. This is what I wanted to check."
                mc "What... did you want to check?"
                if dragonroute == True:
                    dragon "Just... something that had been bothering me since yesterday."
                else:
                    dragon "I was down here yesterday morning with Hoss. We uh... had some things to talk about."
                    dragon "More importantly, something was bothering me since then about... Well, the room itself."
                "Orlando began to pace, checking things and frowning."
                mc "What's... What are you looking for?"
                dragon "I just... expected there to be more here, right?"
                mc "Something more than... what? A keypad? A door?"
                dragon "Maybe... uh... Okay, let me put it this way."
                dragon "This room is concrete, right? Floor, walls, and ceiling. The exception being the doors and the keypad."
                mc "Right."
                dragon "So... How does it work? If it was paneled walls, or floorboards I'd expect a trap door or some sort of... I don't know..."
                mc "For... Someone to come out of? I just thought the keypad worked like, press buttons, beep-boop, hooray you did it."
                dragon "Look, I'd like it if it was that simple but..."
                if dragonroute == True:
                    dragon "Do you really think that it'd be that simple given what we've both been through?"
                else:
                    dragon "Just... trust me. I get the impression it's a lot more than just a big door guarding treasure."
                    dragon "You said it before, how you used this thing. But... How did it give you a vision if anything? Lights? Sound? Some sort of... aerosol?"
                show dragon pout
                dragon "I just... I'm sorry, I'm probably being silly but I just needed to check it out one last time before the police arrived. I doubt I'd get another chance otherwise."
                mc "Oh... Okay. But what now? Back upstairs?"
                dragon "Yeah... I think so. Who knows how long we've got to wait until the police arrive, right?"
                scene foyer with dissolve
                "Orlando and I headed back upstairs, looking to meet back up with Tyson and Sal."
                show bear neutral with dissolve
                show lion sad at right with dissolve
                show boar pout at left with dissolve
                mc "Oh! You three! I thought you'd be outside."
                boar "We were."
                bear "We came back in before giving the place a look around for anyone else that might be here."
                show boar sad
                boar "But... Nothing. We couldn't find anyone else, not even a trace of them. Not that we really knew what we were looking for, but still."
                mc "Oh... Well okay."
                lion "What were you two doing downstairs?"
                mc "Just checking out the vault. Seeing if there was anything that might be a clue or just... anything really."
                lion "And...?"
                mc "Nothing... Sorry..."
                lion "Huh... Well... I did have a question for you, [mcname]."
                mc "What's... that?"
                lion "This Oz fellow that you spoke about... It occurred to me when we were looking around that... It could have just been one of us, right?"
                mc "...What?"
                "The realization hit me suddenly. With how Oz spoke, I'd just assumed that it was some extra person rather than some one of my friends. But that would mean that they owned this place, right?"
                "Or... was able to lie about a bunch of things that made no sense. But then there was the thing installed in my room."
                show lion annoyed
                lion "Let's say Oz is the owner of the house and Benson is... {i}was{/i}, their butler, right?"
                show bear pout
                bear "Right."
                show lion sad
                lion "Well... One option is he killed his own butler and tried to implicate us. Another option... Is that one of us did and tried to peg it on someone else."
                show boar mad
                boar "Wait... I don't think I like what you're insinuating."
                show lion mad
                lion "If this Oz person was Benson's boss... Who's to say they wouldn't want revenge on the person that did it?"
                mc "But that's if he didn't do it himself though, right?"
                show lion annoyed
                lion "I'm sorry, [mcname]. But there's no sign of this person you claim to have spoken to at all. No trace, no sign, nothing."
                lion "So let me rephrase this question. Are you Oz, [mcname]?"
                mc "Wait, me?"
                show lion sad
                lion "Well... All things considered, the only one that knew about this person was you, right? If you wanted, I'm sure you could've spun a yarn about some ninth person here as a cover."
                mc "But... Why would I kill Benson? That'd be..."
                bear "Betrayal."
                boar "Betrayal of the highest order."
                mc "But... {i}why{/i}?"
                "I looked back to Orlando who had until this point stayed quiet, having moved to massage my shoulders in an attempt to keep me under control."
                mc "I didn't..."
                lion "There's... No evidence pointing to you that did it. Not that I can tell, anyway. So I think you're in the clear."
                show bear sad
                bear "But... Why kill Benson? Was he going to kill one of us? Was he... guilty of something?"
                show boar sad
                boar "It's... hard to say. But I get the impression that... This was an act of betrayal."
                boar "He seemed so nice. And... Just..."
                "Roswell finished his thought off with a sigh."
                show bear neutral
                bear "I guess... There's nothing else we can do. The police will be here soon but... I think we're done."
                show lion scared
                lion "Done?"
                bear "Done."
                hide lion
                hide bear
                with dissolve
                show boar pout
                "Hoss and Dean wandered off, and I was about to follow them before I realized Roswell was glued to the spot, deep in thought."
                mc "Uh... Roswell?"
                "Nothing, no indication that he'd heard me, instead his brow just furrowed further."
                boar "That word..."
                mc "What... word?"
                show boar mad
                "The look Roswell gave me intensified, almost searching me for something while he thought over his answer."
                boar "Nothing. It's nothing."
                show boar sad
                boar "Just a fleeting feeling that I'd just..."
                "He shook his head."
                boar "It doesn't matter now. Come on, let's go meet back up with the others."
            "Stay Quiet":
                mc "I think... we should call the cops?"
                boar "Yeah... There isn't really much else we can do, is there?"
                show lion sad at left with dissolve
                lion "Alright, I'll go call the cops."
                boar "Sure, I guess."
                hide lion with dissolve
                mc "What... What should we do now?"
                hide boar with dissolve
                show wolf pout at left with dissolve
                wolf "You're sticking with me."
                show dragon annoyed at right with dissolve
                dragon "I... don't think I trust you enough to leave him alone with you. Dean can take care of him."
                show bear pout with dissolve
                bear "Not that I'm complaining, but..."
                mc "Hey, I can take care of myself!"
                hide wolf with dissolve
                show croc mad at left with dissolve
                croc "[mcname], I mean this in the nicest way possible, but please go wait in the foyer."
                show dragon mad
                dragon "Sal! Not you too!"
                mc "I don't... Just..."
                "I hated it. I hated what my friends were doing, of all things. The moment something bad happens, the very moment, and all of a sudden I'm just... Something to be protected."
                "I wanted to help! I wanted to be equal. Sure, I admit that there wasn't much I could do, and being anywhere near the body was freaking me out but..."
                scene foyer with fade
                "I stormed off. The police would be here soon anyway, it didn't matter. It'd just be like talking to the other officers at dad's work; I'd be polite, answer anything they needed to know, and I'd be able to go home quicker. I didn't do anything wrong, and they were just doing their jobs."
                "Slumping on the stairs, I took a seat, running my hands through my fur."
                show bear neutral with dissolve
                "Dean wandered out from the foyer, coming to sit down next to me but stayed quiet. Was he here because somehow they'd decided I needed to be chaperoned?"
                mc "Dean, I'm fine. You can go back with the others. I don't need anyone taking care of me."
                bear "You say that, but I'm still concerned. No one told me to come out here, I just wanted to see if you were okay."
                mc "How could they just... I don't need protecting from everything! I saved someone's life, Dean!"
                show bear scared
                bear "Uh..."
                mc "I'm not even the youngest one here! Why is it always just..."
                bear "I-I'm sorry! I didn't mean..."
                show bear pout
                bear "Geez, no wonder you haven't said yes to an actual date. Can't say I'm innocent of wanting to protect you either."
                "I crossed my arms and turned away from him, I was annoyed, and the stress of an incoming interrogation was not making things better."
                bear "Is there... anything I can do? Anything I can say?"
                mc "Dean, just..."
                "I trailed off, shaking my head."
                bear "Because... I know our friendship started with some... random encounter at a coffee shop. I know that at the rate we're going, we're going to be old and grey before we get a romantic night to ourselves to really see how things go."
                bear "But even if you started dating Hoss tomorrow, I'd still care about you. We all do. That's all that was in there. Maybe unwarranted and maybe we went too far, sure..."
                show bear neutral
                bear "Just thought you should know, is all."
                mc "Okay..."
        scene black with dissolve
        "Eventually... the cops came and questioned us all."
        "It was odd though, no one was taken away, and we were allowed to go home with little fuss."
        "It was only a day later that I heard from Dean that we were all in the clear and that they'd ruled Benson's death as a suicide. Not that that went down with him, Hoss, or Roswell."
        scene street with dissolve
        "A week later I was just sitting outside when I saw Roswell wandering down the street. Seemed he was on the way to visit, as even upon waving him down he made a beeline to my front gate."
        show boar sad with dissolve
        boar "Hello, [mcname]."
        mc "Hey..."
        "It'd been a tense couple of days, especially with Hoss moving back home and talks of others moving away too."
        mc "You... doing okay? Didn't expect you over otherwise I would've, uh..."
        "Roswell shook his head, sighing."
        boar "No, I just... I wanted to just swing by before I go do something is all."
        mc "Do something? Anything fun?"
        "My attempts to be chipper fell on deaf ears apparently, as he just shook his head and kept his eyes elsewhere."
        boar "Just... Benson's death. If it was a suicide there's nothing we could've done, right?"
        mc "I... guess not. You... You're not about to say you still think it was murder, do you?"
        show boar pout
        boar "Of course I am! The evidence was there!"
        mc "But... The police said..."
        show boar annoyed
        boar "I know what the police said. I know what they decided and I disagree. That's why I'm going back to the mansion to find out if I can do any investigating of my own."
        mc "But that's trespassing!"
        boar "Hey, we were allowed there for the month, besides I can just say I forgot something. It's not that big a deal."
        show boar pout
        boar "I would've accused Tyson for doing something so gruesome, but he can't even do math let alone mess with a crime scene."
        mc "Hey, you don't need to go taking pot shots at Tyson. That's not fair, Roswell."
        show boar annoyed
        boar "Enough. Enough of you coming to his defense whenever an analysis comes into question."
        boar "This trend of you overlooking every single shortcoming he has as if he's this idol you have needs to stop. It's not fair on Orlando, myself, or most importantly {i}you{/i}. Have you just forgotten everything he did to you? To us?"
        mc "B-But...! He's changed! He's a good guy now!"
        boar "No, [mcname]. I might be a year younger but you're much more naïve."
        "Roswell turned to leave and I stood, annoyed."
        mc "I'm not naïve! I know what he did!"
        "Roswell's tone was bitter, almost cold in his reply. His gaze was equally fierce, almost cruel to the point of me getting chills and I sat down again."
        boar "I was hoping that, somehow, you'd remember who the enemy was, [mcname]. You've got some kind of... Stockholm syndrome that I just... cannot help you through."
        boar "This is betrayal, pure and simple. I just hope one day you can wake up from whatever spell he's put you under."
        hide boar with dissolve
        "I was in a daze for a few moments as Roswell stormed off, and I made chase."
        mc "R-Roswell! Wait!"
        scene black with dissolve
        "A week later he turned up dead. Shot apparently, although they had no suspects. Was found apparently near the mansion, but I never found out if he made it all the way there."
        "With Hoss gone, and Tyson driving off one day with no promise to return, that just left Sal, Orlando, Dean and myself still in town."
        "Last I heard from Orlando and Sal, they were taking a road trip out to visit Sal's sister but they didn't say when they'd be back."
        "Eventually though, Dean and I had our date. It wasn't bad, but something was certainly missing. A week later we tried again and now we're just testing the waters. I've been meaning to let Orlando know but for some reason he never picks up anymore."
        "The one thing that sticks with me though, is the note I left things with Roswell on. I wish I could've said or done something to have ended things better. Instead I just have his last sentiment as what I have to remember our friendship by."
        "At least... Hopefully, things can start getting better now."
        $ renpy.pause (3.0)
        "{color=#EE2c2c}{b}BAD END: BENSON{/b}{/color}"
        return

    else:
        scene bedroom with dissolve
        if crocroute == True or bearroute == True or wolfroute == True:
            "Surprisingly, I slept well. Or at least, as well enough as I could with so many things running through my head as I lay down."
            if wolfroute == True:
                "As my eyes adjusted to the room, I remembered the weight on my chest, looking down to Tyson still cuddled up on my front. With how his face was scrunched up, and his tail flicking, it seemed like he wasn't having a very pleasant dream."
                menu:
                    "Leave him alone.":
                        "I wasn't sure if disturbing him was going to be any good. Who knows? What if I accidentally woke up and he still thought he was dreaming?"
                        "Ty shifted against my front so he was up against my chin, making it impossible to see what expression he was pulling. But given the soft growls and whines he was making, his dream mustn't have been a good one."
                        mc "Ty...? You okay?"
                        show wolf shirtless mad with dissolve
                        "I shook him gently by the shoulder and he sat up with a start, staring down at me with bulging eyes, eyes furious for a second before they dulled back down to a sleepy stupor."
                        show wolf shirtless sad
                        wolf "Fuck... It's just you... Okay, just... Just... Five more minutes."
                        hide wolf with dissolve
                        "He sighed out, laying back down and resting his head against my chest."
                    "Pet him.":
                        $ wolflove += 1
                        "My right arm was still mostly free, so I carefully wrapped it around Ty's back and rested my hand atop his head. His tail stopped flicking, but his frown lingered."
                        "Ever so slowly I began to stroke his fur, gently digging in to massage his scalp. Almost immediately his frown disappeared, and he let out a sigh with a soft moan soon following."
                        wolf "Fuck..."
                        "I hadn't been going all that long, but Ty stretched, nestling in under my chin and shifting his right hand from my shoulder to my waist as he pulled me closer. He didn't say anything else, but I figured he was awake somewhat, now."
                        "What was the harm in continuing? As I did, Ty's tail flicked happily behind him, before he reached up and grabbed my hand."
                        wolf "Okay, enough of that pup. Lemme have five more minutes."
                        mc "Oh, okay..."
                "While Ty rested I looked to Dean who was laying nearby. He looked wrecked, cuddled up to a pillow in the same ways that Tyson was to me. Seemed to be having a nightmare or was just that uncomfortable."
                "Sal meanwhile was on his stomach, half chewing on his pillow with a happy smile on his face. Maybe he was just hungry?"
            if bearroute == True:
                "As I woke up, I could see Dean's fingers drumming lazily against his chest, his other arm still wrapped around me to keep me close. I shifted only a little bit, reaching out for his hand and finding him shying away the moment my fingers grazed his."
                mc "Huh?"
                show bear underwear scared with dissolve
                bear "Oh. Sorry, did I wake you?"
                "I looked up at him and saw that he looked tired. {i}Really{/i} tired."
                mc "N-No... But... How long have you been awake?"
                bear "Oh... uh..."
                "Dean started to rub my back, keeping his eyes trained on the ceiling."
                bear "Woke up sometime in the middle of the night."
                mc "And you... didn't sleep?"
                show bear underwear pout
                "I sat up so I was sitting next to Dean, looking down at him. I placed my hands on his belly, trying to catch his eye. My voice kept down low to try and let the others keep sleeping."
                mc "Is everything alright?"
                bear "Y-Yeah. Yeah, I'm good. Ugh..."
                "Dean threw his hands to his face, rubbing his eyes. I caught a glimpse of his fur, but they seemed puffy and wet. Maybe he was having an allergic reaction?"
                show bear underwear sad
                bear "Just after yesterday. Would've taken something to help me sleep but priorities changed."
                mc "Priorities?"
                show bear underwear smile
                "Dean pulled his hands away, shooting me a tired smile."
                bear "You, of course. Had to make sure you were alright. Can't have you all worried now, can we?"
                mc "But... are you going to be alright on this little sleep?"
                "I watched as he pushed himself up onto his elbows, then propping himself up on one hand so he can pull me closer with his other. His nose brushed softly against mine before he kissed me, backing off so he could sit opposite from me."
                bear "I'll be alright. Might just take a nap later."
                mc "If you say so..."
                hide bear with dissolve
                "I looked over to the other two, who so far still seemed to be asleep. Sal was having a pleasant dream from how he was idly chewing on his pillow with a happy smile."
                "Ty on the other hand looked about as rough as Dean looked, although he still seemed asleep. Didn't help that he seemed to be growling though."
            if crocroute == True:
                "When I awoke though, I felt my whole body shifting. Rising and falling gently, and I realized where I was."
                "Sure enough I was still on Sal's front, his breathing gently shifting me up and down in a steady rhythm, almost like being rocked to sleep."
                "Looking at him, he seemed to be drooling slightly, although wore a broad smile as he slept."
                mc "Someone's having a nice dream..."
                "No sooner than I'd said it that Sal snored loudly, shifting in his sleep enough that I fell off his front, now flat on my back next to him."
                croc "Hm...?"
                show croc shirtless dazed
                "Sal rolled over onto his side, looking down at me seemingly in a daze, not registering immediately who he was looking at."
                "We held each other's gaze for a bit before he seemed to realize, eyes going wide in shock."
                show croc shirtless scared
                croc "O-Oh! Good morning."
                mc "M-Morning...? Everything alright?"
                show croc shirtless pout
                croc "Yes, just... Took me a while to remember last night."
                "We kept our voices low as to not disturb the others. Or at least that was my reason for doing so."
                show croc shirtless neutral
                croc "I hope that wasn't... You know."
                "Sal patted his chest, specifically the spot where I had spent the night."
                mc "Oh, no, it was comfortable enough."
                show croc shirtless pout
                croc "Oh. Good..."
                hide croc with dissolve
                "I looked over to Tyson to see if he was as comfortable. If anything, he seemed to be having a bad dream while he clung to a pillow, growling into it with a scrunched up frown. Even his tail was twitching in irritation."
                "As for Dean, he looked much the same way. He was cuddling into a pillow but his expression was just as pained. Almost as if he was trying to sleep still."
            show wolf shirtless sad at left with dissolve
            show croc shirtless neutral at right with dissolve
            show bear underwear pout with dissolve
            play music calm fadein 2.0
            "In our own time, we all got up. Not that it took that much longer after I'd awoken."
            mc "Morning, guys..."
            show croc shirtless pout
            croc "Did... everyone sleep alright?"
            bear "Sleep? Maybe got a couple hours at best."
            show wolf shirtless pout
            wolf "Slept, yeah, not very well."
            mc "Everything... Alright?"
            croc "Is it because of the company?"
            show bear underwear neutral
            bear "Nah. Stuff on my mind. Don't worry about it."
            wolf "You too, huh? Know that feeling."
            mc "Did... either of you want to talk about it?"
            show wolf shirtless neutral
            wolf "Nah. I'm good. Just need coffee."
            bear "Coffee sounds great. And a nap later."
            show croc shirtless neutral
            croc "Should we get sorted and meet up with the others?"
            mc "Maybe a good idea... Yeah..."
            croc "More importantly... [mcname]. Did this... help?"
            mc "Huh?"
            show wolf shirtless pout
            wolf "You, you dork. With what you were worried about."
            mc "I... guess so?"
            bear "And about doing stuff as a group?"
            mc "Well I still want that to happen, of course."
            show croc shirtless pout
            croc "Board games, right?"
            mc "Anything, really. I just... I just wanna stress how important all three of you are to me. The other three too, but..."
            show wolf shirtless neutral
            wolf "But?"
            bear "But we're going to have to get along, huh?"
            mc "Right."
            croc "That... might be difficult."
            mc "Really?"
            show wolf shirtless pout
            wolf "Cause of me, huh?"
            show croc shirtless neutral
            croc "Right, but not... you specifically."
            show bear underwear pout
            bear "Roswell, I'm guessing? He was laying into you pretty hard yesterday."
            wolf "At least he's grown a pair."
            croc "That's... one way of putting it."
            mc "It was a little odd. He's not normally that... uh..."
            wolf "That much of an asshole?"
            mc "Well, no, but..."
            show bear underwear neutral
            bear "There's not really a nicer way of putting it."
            show wolf shirtless neutral
            wolf "Look, I get it. I'm an ass. I did bad things to him. I deserve it."
            show bear underwear scared
            bear "How... long ago though? Even I heard the stories but uh... Truth be told I probably judged you faster than I should've based on them."
            show croc shirtless sad
            croc "Orlando told me stories too. For that I apologize."
            if wolfroute == True:
                croc "That... said."
                show croc shirtless mad
                croc "I do want to have a talk about something I saw and heard the other day."
                bear "What... happened?"
                "My hand went to my nose as I looked from Sal to Ty, who seemingly had his eyes locked with the crocodile."
                wolf "I fucked up again. That's all. Don't worry about it."
                show croc shirtless pout
                croc "[mcname]?"
                mc "Yes?"
                croc "You know what I saw, yes?"
                mc "I think so... But..."
                wolf "Nah. It's fine. We'll talk about it later. If you saw it, no point hiding it."
                show bear underwear pout
                bear "Do... I get to know about it?"
                mc "I'll... tell you later?"
                croc "Still. Even if that was an isolated incident. The other stories must be true, too."
            show wolf shirtless pout
            wolf "Fuck it. I get it. No point hiding that I've been an asshole to people in the past."
            mc "But he's a good person now!"
            wolf "I'm getting {i}better{/i}, pup. Trying to at least."
            mc "But...!"
            wolf "No buts, pup."
            show croc shirtless pout
            croc "For what it's worth... It's admirable. But forgive me for still being cautious."
            show bear underwear neutral
            bear "Same here. Yesterday helped though, believe it or not."
            if bearroute == True:
                bear "Remind me to pull you aside for a chat too, Tyson. Something I want to... run by you."
                show wolf shirtless neutral
                wolf "What?"
                "I looked between the two of them before noticing Dean gesturing my way. Ty then gave me a look before nodding to Dean, seemingly catching on to something."
                wolf "Alright. Sure."
                "I looked to Sal who seemed to be looking elsewhere, distracted by something; but I knew Dean and Ty well enough that even if I asked, they weren't going to tell me."
            else:
                wolf "Oh yeah?"
                show croc shirtless neutral
                croc "Much like movie night. You're just... another person."
                show wolf shirtless neutral
                wolf "Well yeah. I have my moments."
            mc "We should go downstairs now, right? Sort out breakfast and whatever?"
            show bear underwear pout
            bear "Yeah, plus getting into a fresh set of clothes, too."
            wolf "Alright. Guess I'll see you guys downstairs then."
            hide wolf with dissolve
            mc "Thanks for hosting us in your room, Sal!"
            show croc shirtless smile
            croc "Next time, clean your room better so you can host."
            show bear underwear grin
            bear "Hey, maybe I'll do the same. Y'know, then I don't have to worry about leaving afterwards and can have a sleep in?"
            if crocroute == True:
                hide bear with dissolve
                show croc shirtless neutral
                "I turned to follow Dean before feeling Sal's eyes bore into the back of my head."
                show croc shirtless pout
                croc "[mcname]."
                mc "Uh... Yeah?"
                croc "Close the door, please."
                "Once Dean was gone, I quietly shut the door and looked back to Sal, who was sitting down on the bed."
                mc "Is... everything okay?"
                show croc shirtless neutral
                croc "Yes. For the most part."
                show croc shirtless pout
                croc "What about you?"
                mc "I'm... fine?"
                "I stood awkwardly by the door, unsure if there was more he wanted to talk about."
                croc "[mcname], are you sure? I have concerns about you... worrying about death."
                "I sighed, wandering back over to the bed to sit next to Sal, rubbing my eyes."
                mc "Just... You know, this vacation was supposed to be fun, right?"
                mc "But seeing images of people dead... Not fun."
                show croc shirtless neutral
                croc "Have you considered just... not messing with the vault if that's what's happening?"
                mc "I... But what if something happens?"
                show croc shirtless pout
                croc "But it's unfair to shoulder that burden by yourself. Life... can be rough, and can have unfortunate tragedies."
                croc "You have the choice to mess with it more if you want. But you alone must face the consequences of what comes after. We can only... help where we can afterwards."
                mc "Sal... Can I ask you for some advice?"
                show croc shirtless scared
                croc "Advice? About what?"
                mc "What if..."
                mc "What if there was a reason that I had to keep checking it?"
                show croc shirtless mad
                croc "A reason?"
                mc "Well... If I saw Benson dead, there's that... chance that one of our friends killed him, right?"
                show croc shirtless pout
                croc "Do... you really think that?"
                mc "Huh?"
                croc "Do you think that one of your friends would have killed an innocent butler?"
                croc "It takes a lot to kill someone. To have to make that decision and follow through."
                croc "Do you, [mcname], really think that one of us here could do it?"
                mc "I..."
                "I felt silly again, conflicted between what Oz had told me and what Sal was suggesting. If Sal was right, then the only one left was Oz. But why would he warn me about people dying if he was the one behind it?"
                mc "I... don't know."
                show croc shirtless sad
                croc "That's... unfortunate."
                show croc shirtless pout
                croc "But... understandable. I don't know if I'd be able to, but... I suppose it's hard to say what one's capable of depending on the circumstances?"
                mc "What... do you mean?"
                croc "If someone was trying to kill you, would you kill to save your life? In self defense?"
                show croc shirtless neutral
                croc "If one of your friends tried to kill you, would you be able to fight them off?"
                mc "But who would do that though?"
                show croc shirtless mad
                croc "Hopefully no one."
                show croc shirtless pout
                croc "But if what you're seeing is the truth, then... Someone's been lying to us."
                croc "And I don't like the idea of that."
                mc "So... Where does that leave us?"
                show croc shirtless sad
                croc "Honestly, I don't know. I do not mean this to come out the wrong way but... I'm... skeptical about what you saw. Maybe it was your imagination."
                mc "But...!"
                show croc shirtless pout
                croc "I know. Even after you caught me sleepwalking. But admit that these occurrences are hard to accept at face value."
                mc "All I'm getting from this is that you don't believe me."
                show croc shirtless neutral
                croc "I believe you enough that if you're upset I'll try and make you feel better."
                show croc shirtless pout
                croc "But I do not readily accept premonitions of death as truth."
                "I didn't know what to say to that. He was right, the only way you could possibly believe it was to experience it yourself. Much like Oz, Sal had thoughts about believing my friends but claimed to be on my side."
                "Still... I was torn between how I should be feeling. On one hand I felt reassured that Sal was open about wanting to make me feel better, and that my concerns were coming across as real."
                "But on the other, he didn't believe what I was seeing. He didn't trust that what I had seen was legitimate."
                croc "[mcname]... Maybe it's best we head down for breakfast. You could do with some coffee. Wake up a bit."
                mc "Sal..."
                croc "I'm sorry, I'm probably making things worse."
                croc "Trust me when I say I care for you, [mcname]. Enough that I'd do a great deal to make sure you're okay."
                show croc shirtless neutral
                croc "It... just might take a little more for me to completely come around to what you're claiming. That's all."
                mc "Okay..."
                hide croc with dissolve
                "I nodded slowly and stood up, with Sal following suit. He had a hand on my shoulder, rubbing gently as we walked to the door. It made me feel a little better, but if anything it reinforced something that I had assumed might be needed."
                scene black with dissolve
                "Sal shut the door behind me, leaving me to my thoughts. Evidence. I needed evidence. Some sort of proof that what was happening was real."
                "Nodding to myself, I headed back to my room to get changed in preparation for breakfast."
                jump Day8Breakfast

            scene black with dissolve
            "I left behind Dean, heading towards my room."

            if wolfroute == True:
                #Ty private conversation in Dave's room
                scene bedroom with dissolve
                show wolf neutral with dissolve
                "No sooner had I entered I did a double take, wondering if I'd entered the right room."
                mc "Uh... Ty? What are you doing in my room?"
                show wolf pout
                wolf "Waiting for you."
                mc "Well yeah, but why?"
                show wolf neutral
                "Ty just shrugged, wandering over to the door and pushing it closed behind me. He left his hand lingering on it, staring down at me looking... uneasy about something."
                mc "Ty...?"
                "With his free hand he reached out and touched my face, his eyes unfocused as he did so. Not that he did anything beyond that, just touching, his thumb rubbing over my cheek."
                wolf "You sleep alright?"
                mc "Y-Yeah...?"
                mc "{i}You{/i} had a rough night though."
                show wolf pout
                wolf "Well, you're not as soft as a pillow. Pretty soft though."
                mc "That's on you. Not that you gave me much of an option there."
                wolf "Yeah, I know. Just needed... something, y'know?"
                show wolf neutral
                wolf "Like... That one time, yeah?"
                mc "I guess so..."
                mc "Ty... um..."
                hide wolf with dissolve
                "I shuffled around him to my clothes and he followed close behind. I bent over to pick up a new shirt and as I stood he snaked his arms around my sides and buried his nose into my neck, making me jump."
                mc "Ty..."
                wolf "Just... let me enjoy this. Please."
                mc "You... just wanted to cuddle? We could cuddle. I'm all about that cuddling."
                wolf "Cuddling is gay."
                mc "{i}I'm{i} gay, Ty. Remember?"
                "Tyson stepped back, letting me go and I used the opportunity to put on a fresh shirt. As I turned around, Tyson's hands were on me again, picking me up just enough to throw me onto the bed."
                show wolf grin with dissolve
                "He had this smug look on his face, almost predatory that made me quake just a little bit. I watched him join me on the bed, scooting closer."
                wolf "Yeah, but you're just a pup. Cuddling you ain't gay."
                mc "Hey, I'm not that young anymore. You don't have to call me that anymore, either."
                show wolf pout
                "Ty stopped his approach, resting his hands on my knees and looking off to the side, bored."
                wolf "What, don't like it anymore?"
                mc "Well... No, I'm not saying that."
                show wolf grin
                wolf "Could call you a lot worse if you were mine."
                mc "If I was..."
                show wolf neutral
                "I trailed off, watching Tyson's smile fade, seemingly thinking about something."
                wolf "Sal saw what happened the other day, didn't he?"
                mc "Oh... uh... I think he might have."
                mc "He didn't step in though. Like, you took me up to your room and..."
                show wolf sad
                "I gulped, realizing where that recount was going and I averted my gaze."
                mc "Well... y'know. I don't know why he stayed out of it, or how much he heard, but..."
                wolf "But what?"
                mc "Maybe with everything going on, he felt that maybe... we should talk about it? Just us? About us, I mean."
                mc "Is there anything between us, Ty?"
                show wolf neutral
                wolf "Dunno. Is there?"
                mc "I don't know! Like... On one hand whenever you're around I feel safe, but at a moment's notice I feel like I need to be on edge, ready to react to something you might say or do."
                mc "Not just to me, but the others, anyone really."
                show wolf pout
                wolf "Not your responsibility to do that."
                mc "No, but... You're important to me. I want to... do... something...?"
                "The words were out of my mouth before I'd processed them. I didn't even really know what I meant by that. Maybe it was just the tiredness catching up to me."
                wolf "Do something, huh? Like what?"
                show wolf neutral
                wolf "Ask me out on a date?"
                mc "No, that's {i}your{/i} job. I want to be the one asked. I don't even know if you're... y'know. You say you aren't, but..."
                show wolf mad
                "Ty lunged forward and slammed his hand down next to my head, sinking into the bed."
                wolf "I'm not gay."
                mc "Then..."
                show wolf annoyed
                wolf "If you want me to fuck you, then that's a different story. I'd only be doing it because... uh..."
                "I growled, sitting up and pushing Ty back by leveraging away with my head."
                mc "Because what? You're only into me?"
                show wolf yell
                "I looked at Ty as he rested back on his ankles. He made to yell, going so far as to point at me as if to threaten me with something but nothing came out."
                mc "Well, come on, then! {i}Tell me{/i}, Ty."
                show wolf mad
                wolf "So what if I am, huh?"
                show wolf annoyed
                wolf "So what? I don't care about that stuff but you're different."
                wolf "It's too fuckin' early for this, [mcname]. Just... I'll meet you downstairs."
                mc "Oh no you don't. You stay right here."
                "I grabbed him firmly around the arm to keep him there."
                mc "I'm not going to confess that I love you, Ty. But you're so damn important to me that I want you to be honest. About everything."
                mc "Why does this have to be the exception?"
                show wolf neutral
                wolf "Because I'm not good enough. Not yet."
                mc "W-What?"
                show wolf pout
                wolf "How can I tell you something I don't know, huh?"
                wolf "You said you're gay. Great. You have that figured out. I sure as hell don't."
                mc "You don't... know?"
                show wolf neutral
                wolf "Nope."
                mc "But..."
                show wolf pout
                wolf "What, you expect me to be hooking up with randoms every week?"
                mc "Well no, but..."
                wolf "All I know is that for whatever fuckin' reason, you're my weakness. It sucks but... Fuck, I wouldn't trade it for anything."
                "I blushed at that, unsure to take it as a compliment or to start picking at the specifics of what he meant."
                show wolf neutral
                wolf "Look, I'm gonna be honest when Sal asks about what happened. Keep the first aid kit on hand. Sure as hell have had enough of a time with my dream last night that if he wants to throw down I'm just gonna let him."
                mc "Wait, that's... a lot to unpack."
                wolf "Which part?"
                mc "What did you dream about last night? Is that why you looked like you were having a nightmare?"
                show wolf annoyed
                wolf "Shit. Didn't realize that it showed when I was sleeping. Don't worry about it."
                mc "Ty, come on. You're killing me. Be honest, remember?"
                show wolf scared
                "Tyson's eyes bulged as I asked my question, searching my face for something. His mouth agape, brow furrowed and he almost looked like he could cry."
                wolf "I don't..."
                show wolf sad
                wolf "I had a dream of you dying, alright? It sucked."
                mc "And that's why... cuddles?"
                show wolf neutral
                wolf "What if I never got another chance to do that again?"
                mc "Well... uh... We were cuddling while you slept."
                wolf "And it helped, but... Can only do so much in front of other people."
                mc "Oh..."
                show wolf pout
                wolf "Look, I...{w=0.5} Just throwing it out there, but... For old time's sake, did you wanna... y'know."
                mc "Uh... No? I mean, I don't get what you're talking about."
                wolf "Sleep together."
                mc "We did that last night though."
                show wolf annoyed
                wolf "Fuck. Just...{w=0.5} You. Me. Bed.{w=0.5} Alone."
                mc "Oh... Well... I guess so? Did you mean actually sleep or... did you mean..."
                show wolf pout
                wolf "I'm not suggesting anything. If you wanna mess around then I'll leave that on you, pup."
                "I thought about my goal for today. What I needed to accomplish. The curiosity of what I {i}could{/i} get up to with Ty made me shift on the bed."
                mc "Tomorrow night? Does... that work?"
                show wolf neutral
                wolf "...I guess."
                mc "Sorry, I just... Not tonight. I'll... fill you in later as to why."
                show wolf pout
                wolf "Spending it with Dean instead?"
                mc "What? No! Just... something else. Promise."
                show wolf neutral
                wolf "Well alright. Sure. Tomorrow night."
                "Ty got up from the bed and wandered over to the door, looking over his shoulder at me."
                wolf "I'm gonna head on down and get coffee. Don't be long, yeah?"
                mc "Yeah, okay."
                hide wolf with dissolve
                "Closing the door behind him, I was left on the bed, worked up. I grabbed my pillow, covering my face with it as best I could and screamed in frustration, coming out somewhere between a high pitched whine and a shriek."
                "We'd been here a week and I was questioning everything I knew about my relationship with Tyson. Thanks to Roswell's behavior yesterday, and Tyson's... were they even advances?"
                "It took me a few moments to calm down, realizing that maybe this was why I needed coffee in the morning. Not only that, but Tyson admitting that I was {i}his{/i} weakness made me think... what if he was mine?"
                "Still, as much as spending another night in the same bed excited me, I had a job to do. And if I had any hopes of Ty taking me seriously with what I was going to explain to him, I needed something to show for it. I needed proof."
                "I got up off the bed and headed downstairs for breakfast with a renewed determination that I hoped would last long after I had my morning coffee."
                jump Day8Breakfast

            if bearroute == True:
                #Dean pulls Dave into his room for makeouts
                "I didn't get very far before I felt his hand entwine with mine and he pulled me into his, instead."
                scene bedroom with dissolve
                "No sooner than we'd ended up on the other side of the door he closed it behind us, pressing his muzzle against mine firmly. I squeaked as he kissed me, holding me against the bedroom door as his tongue explored my mouth."
                "When he pulled away, my cheeks were red, but I was certainly more awake now than I had been so far. Sadly for Dean..."
                show bear underwear grin with dissolve
                "He looked just as tired, if slightly happier than he had been in Sal's room."
                bear "Morning, handsome."
                mc "Good... Good morning?"
                show bear underwear smile
                bear "What, cat got your tongue?"
                mc "No, but uh... Wow. I wasn't expecting that."
                show bear underwear grin
                bear "Hey, behind closed doors, I'm taking advantage of all the alone time we can get. At least until it's official."
                show bear underwear neutral
                bear "Unless you're not okay with that?"
                mc "Oh, no, it's fine just uh..."
                "I adjusted myself, clearing my throat and trying to find the words for how I was feeling."
                mc "I just assumed that you'd be too tired to uh..."
                show bear underwear laugh
                bear "What, kiss you? Maybe if we were going beyond that into something involving a lot less clothes maybe. Even still, if you asked I'd probably still try."
                show bear underwear grin
                bear "Why? {i}Are{/i} you asking?"
                mc "No, no!"
                show bear underwear smile
                "I gave Dean a gentle shove to give myself some breathing room, catching a whiff of how he smelled. Surprisingly... Not of honey."
                mc "Huh...?"
                show bear underwear scared
                bear "What?"
                "I smelled again, stepping forward and burying my face into his fur. A sign that he took to slip his hands into the back of my pants. The scent that lingered on his fur had remnants of that honey smell but it was otherwise just... earthy. Slightly sweaty."
                bear "Why... are you smelling me? I need a shower, sure but..."
                mc "Oh, it's... You normally smell of honey."
                show bear underwear laugh
                bear "Oh!{w=0.5} Is that all?"
                show bear underwear smile
                bear "It's in most of the stuff I use for my fur. Shampoo, conditioner, even have some moisturizer that Hoss recommended."
                mc "But why honey though?"
                show bear underwear pout
                bear "You don't like the smell of honey?"
                mc "No, it's fine! It's very... you? At least that's what I associate you with now?"
                show bear underwear smile
                bear "Well, I'm your honey bear, after all."
                mc "My... honey bear?"
                show bear underwear grin
                bear "Of course. You're my handsome little honeybee, and I'm your honey bear."
                "I chuckled as he kissed me atop my head."
                bear "You're conscious of how I smell though?"
                mc "Well... Not really. It's... a nice smell? Whenever I smell honey I think of you, at least. It's like that for a few things."
                show bear underwear smile
                bear "Oh? That's news to me. Wanna share?"
                mc "Maybe... some other time? I'm more interested in what kept you from sleeping last night."
                show bear underwear pout
                bear "Oh... That."
                "Dean wandered over to his bed and sat down on the edge, picking up a fresh set of underwear from a clothes pile nearby."
                bear "Was going to take some medication. Y'know, after what we talked about yesterday."
                mc "Yeah. And you said, priorities changed."
                bear "Right. Sometimes... it's easier to not sleep. Specially if it gets real vivid."
                mc "So you just... Lay there awake?"
                show bear underwear neutral
                bear "Having you cuddled up made things easier. Made me feel like I was doing something right."
                "I wandered over, standing opposite Dean as he continued."
                bear "It was nice, but... dunno. Would've been nicer in our, uh... {i}my{/i} bed. With a bit of privacy."
                mc "Well... I wouldn't mind trying it?"
                show bear underwear smile
                bear "Sharing a bed with me like we originally planned?"
                mc "Well... if it'd help?"
                show bear underwear grin
                bear "And what if you rile me up that I might want something else before getting some sleep?"
                mc "Well..."
                "I looked Dean over, eyes trailing down a little farther than they probably should have. If we were going to share a bed, and if yesterday morning was anything to go by..."
                mc "Didn't you say that I got to say when? Like... When I felt ready?"
                show bear underwear laugh
                bear "Well, that's true. But even if you're not ready for... {i}that{/i}, can do other things."
                mc "What... other things?"
                show bear underwear annoyed
                bear "Come on, [mcname]. You're not that naïve."
                mc "O-Oh... Well... You're right but is that... okay?"
                show bear underwear smile
                bear "What, potentially seeing each other naked? Touching? Or...?"
                mc "And mouth stuff, right?"
                show bear underwear laugh
                bear "'Mouth stuff', huh?"
                mc "Well hey, I've never sucked a dick before!"
                mc "Is there a right way to do it? Are there rules?"
                bear "Not really any rules aside from just watching the teeth, but we don't even need to go that far if you don't want to."
                show bear underwear grin
                "I must've been bright red from how hot I was feeling in the face. Not only that but the look Dean was giving me made it all the worse."
                bear "Hey now. No pressure. I'll even put on more clothes if that'd make you feel better so we could just cuddle and sleep."
                mc "But if I wanted to do more?"
                show bear underwear smile
                bear "Then all you gotta do is tell me you're ready and we go from there."
                "I nodded slowly. Watching as Dean smiled through a loud yawn."
                mc "You sure a nap is going to be enough to get you caught up on sleep?"
                show bear underwear neutral
                bear "Hope so."
                bear "Probably will use some medication tonight, so let's aim for tomorrow night. That work for you?"
                mc "Oh! Um..."
                "For the briefest moment I'd forgotten about my meeting with Oz. All things considered, it worked out well, so I nodded quickly."
                mc "Sure, tomorrow night works. I've been uh... Well... There's something I wanted to do tonight anyway."
                show bear underwear grin
                bear "Oh?"
                mc "No! Nothing like that! Just uh... Just something I need to sort out is all."
                show bear underwear neutral
                bear "Well alright. But if you need a hand, let me know. Don't know how much help I'll be, and I'll be out of it after those meds, but I'll come running if you call."
                mc "Thanks Dean."
                hide bear with dissolve
                "Dean stood up and kissed me on the forehead as he wandered past me and into the adjoining bathroom."
                scene black with dissolve
                "For me, I headed back to mine to get changed properly. The lack of coffee was starting to get to me, and I had a big day ahead of me."
                jump Day8Breakfast
        if lionroute == True or dragonroute == True or boarroute == True:
            "When I awoke, I felt oddly rested. For everything that had been running through my mind when I went to sleep, I must've slept alright."
            if lionroute == True:
                "As the room came into view, I realized that I was in a different position than when I lay down. Carefully, I looked down, seeing Hoss's arm draped over me."
                "I did fall asleep with us the other way, right?"
                "Me stirring must have started to wake him up as well, his hand rubbing a spot on my chest in small circles, slowly as he cuddled in. I kept my voice low, as to only bother Hoss if he was awake."
                mc "Hoss?"
                "I didn't realize how loud Hoss could yawn, the slight rumble in his throat sounding somewhere in the ballpark of a muted roar."
                lion "Hm?"
                mc "Oh... Just checking if you were awake."
                lion "Am now, yeah. Did you sleep well?"
                "I made a noise in affirmation, or at least I hoped Hoss interpreted it as such. Much like I did when I was cuddled up behind him, Hoss buried his face into the mass of fur on the back of my neck as he stretched."
                show lion weeb neutral with dissolve
                "Apparently he was ready to get up though, sitting up next to me and prompting me to do the same."
                lion "Feeling better after yesterday?"
                mc "A little bit? I mean... It's crazy, right?"
                show lion weeb laugh
                lion "Well, you caught a fair few of us off guard, that's for sure."
                "I looked to the other still asleep. Roswell... looked peaceful, spooning a pillow with a broad smile. Seemed as though he'd been drooling a little too."
                "Orlando was sprawled out on his back, leg twitching every now and again as he mumbled in his sleep. Seemed like everyone was getting a decent rest; at least those in this room."
                show lion weeb neutral
                lion "Time to get up?"
                mc "Is it bad that I want to just lounge around for a bit?"
                show lion weeb grin
                lion "Why? Something on your mind still?"
                mc "Maybe... Just... I dunno."
            if dragonroute == True:
                "I was toasty warm, a relaxed sigh escaping as I cuddled into the mass of dragon that I'd fallen asleep next to. I was just how I remembered falling asleep; cradled by Orlando's arms, cuddled for both comfort and warmth."
                "With my ear pressed up against his front, I could hear the low rumble in his chest, along with his heartbeat. I wasn't sure if it was just how dragons purred, or if that was the sound of his fire going on in there, but it was nice to listen to."
                "I just lay there for a bit, basking in the warmth. It wasn't often that I got to enjoy this, with Orlando rarely getting the opportunity to sleep over, but every now and again we fell asleep, ending up in something like this. Rarely {i}this{/i} close though."
                "The minutes ticked by before I nudged Orlando gently, trying to rouse him from sleep."
                dragon "H-Hey... Why are you poking me?"
                "The comment came out immediately, kept in a hushed tone."
                mc "Oh! ...You're awake already?"
                dragon "Mmhm! Been awake for a little while now. You were just so comfy I didn't wanna disturb you."
                mc "I feel like I'm sitting next to a fireplace. It's nice."
                dragon "Well... don't need to get up just yet. Did you sleep okay?"
                mc "Alright I guess? How about you?"
                show dragon pantsless neutral with dissolve
                "Orlando backed off so he could sit up and stretch, quickly throwing a pillow over his lap as he did so."
                dragon "Not... too bad all things considering."
                show dragon pantsless sad
                dragon "But... we'll see how today goes. I did make a mess of things. I guess I sorta forgot about it with what happened with you?"
                "I put a hand on Orlando's shoulder as I looked back at the others."
                "Roswell was happily spooning a pillow, fast asleep. Whatever he was dreaming of must've been pleasant."
                "By comparison, Hoss was looking equally peaceful but not as happy as Roswell. He too seemed to be asleep, resting on his side."
                mc "What's... the plan with that?"
                dragon "Probably talk to Sal some more about it, if he'll let me. It's... a start, but I'm still a bit shaken. Some more closure would be nice."
                mc "That... seems good? If there's anything I can do, let me know though."
            if boarroute == True:
                "Opposite me was Roswell, still sleeping peacefully. He seemed just as happy as I remembered, but my smile faded upon realizing everything else still on my mind."
                "I rolled onto my back, letting my hand rest on my chest as I stared at the ceiling. Would Roswell be a good person to ask for advice on this?"
                "How he seemed to tear into Tyson yesterday seemed out of character, too. Did something happen? I stole a look at his happy face again before going back to the ceiling. Mustn't be eating him if he was having that good a sleep."
                "Roswell had changed over the time I'd known him, and I was only really starting to realize it the longer we were living in such close proximity. He used to be more of a pushover, timid. But {i}now{/i}?"
                "I hadn't realized it properly but he'd become a lot more sure of himself. A lot more confident, something that I wasn't sure that I was matching him in."
                show boar shirtless smile
                "I looked to him again, just in time to see him start to wake."
                "The others seemed to still be out of it as I checked. Orlando was sprawled out on his back, fingers twitching every now and again. Hoss meanwhile was curled up on his side, looking placid enough that the only sign of him still being alive was the steady rise and fall of his chest."
                "Roswell yawned, drawing my attention as he slowly opened his eyes and looked at me."
                show boar shirtless neutral
                boar "Good morning, [mcname]."
                mc "Morning, Roswell. Did you sleep alright?"
                show boar shirtless smile
                boar "I did! I had a pretty good dream. Don't think I've had one of those for a while."
                mc "Oh yeah? What was it about?"
                show boar shirtless pout
                boar "Oh, well... This is probably going to silly but... Cake."
                mc "Cake?"
                show boar shirtless smile
                boar "Decadent chocolate cake. Whipped cream, cherries, the works."
                mc "Well... That sounds pretty good. I don't think we'd be able to get away with it for breakfast even if we asked nicely though."
            scene bedroom with dissolve
            "No sooner than the words were out of my mouth the others began to stir, all three of us taking a few more moments to properly wake up before acknowledging one another."
            show boar shirtless smile with dissolve
            show dragon pantsless neutral at left with dissolve
            show lion weeb neutral at right with dissolve
            play music calm fadein 2.0
            mc "Morning!"
            dragon "Yeah! Good morning, everyone. Did everyone sleep okay?"
            boar "Brilliantly, in fact. Ready for another day."
            lion "Didn't sleep too badly myself."
            show lion weeb
            lion "Gotta get that beauty sleep in, right?"
            show boar shirtless pout
            boar "Beauty sleep? Really?"
            show dragon pantsless annoyed
            dragon "Do you have to be so extra in the morning, Hoss?"
            show lion weeb sad
            lion "Oh, sorry."
            mc "Extra what?"
            show dragon pantsless scared
            dragon "Extra... uh, y'know."
            show lion weeb neutral
            lion "More than what you can handle before coffee, [mcname]."
            mc "Oh, yeah, hard skip on that then, please."
            show boar shirtless sad
            show dragon pantsless pout
            boar "Hoss, do you really care about your appearance that much?"
            lion "What makes you ask?"
            show boar shirtless grin
            boar "Well, your mane is a mess for starters."
            show lion weeb scared
            lion "It... It is?"
            "Hoss hurriedly tried to comb it back into place with his fingers. It was hard to tell if he was putting on an act or if his efforts were genuine."
            show dragon pantsless neutral
            dragon "It doesn't look that bad, Hoss. Don't worry about it."
            show lion weeb laugh
            lion "To be honest, not getting it sorted soon after waking can get it all tangled, which is a pain already to comb out."
            mc "Oh, yeah. I don't like getting my fur brushed when it's like that, it hurts."
            show lion weeb neutral
            lion "Let it get too bad and you just have to trim it down."
            show dragon pantsless scared
            dragon "Really? It can get that bad? I'll count myself lucky that mine never bunches up like that."
            show boar shirtless pout
            boar "It's... one of the advantages of having short fur, I suppose. But those two are just really fluffy."
            show dragon pantsless neutral
            dragon "I wonder if Dean and Tyson get the same sorta problem."
            show boar shirtless annoyed
            boar "Can we not talk about him, please?"
            mc "Why? What's wrong?"
            boar "I just really don't want to be thinking about him this early in the morning."
            show dragon pantsless sad
            dragon "Oh, uh..."
            show lion weeb sad
            lion "I guess... we can talk about something else?"
            lion "Uh... [mcname]. How are you feeling after yesterday? Better?"
            mc "Wait what?"
            show dragon pantsless neutral
            dragon "Yeah!"
            dragon "All the stuff that upset you last night with the vault showing you stuff."
            show dragon pantsless pout
            dragon "Nothing... happened, right? We're all here, the other group should be too, right?"
            show dragon pantsless scared
            dragon "Actually, we should go to breakfast, right? Meet up with the others?"
            mc "Probably a good idea. Guess I'll head back to mine to go put on some pants at the very least."
            show dragon pantsless grin
            dragon "Let's do this again though! It was nice!"
            hide dragon with dissolve
            show boar shirtless pout
            boar "Hrm... Yeah, time for breakfast. Thanks again, Hoss."
            hide dragon with dissolve
            hide boar with dissolve
            "Orlando and Roswell shuffled out of the room, leaving just Hoss and I behind."
            if lionroute == True:
                show lion weeb smile
                lion "Not going to join them, [mcname]?"
                mc "Oh, um... In a bit?"
                show lion weeb aroused
                lion "What, sticking around to watch me get changed then?"
                mc "No! No, I'll get going."
                show lion weeb neutral
                lion "Hold on there, mister."
                "I stopped, mid turn, giving Hoss a look."
                lion "You doing alright? And I mean that. Are you really doing alright after yesterday?"
                mc "I..."
                "I started speaking without any answer prepared. It was still early, early enough that I hadn't really processed much beyond my plans to seek out Oz tonight in the right location."
                show lion weeb annoyed
                lion "You...?"
                mc "Oh, um... I'm fine, I think."
                show lion weeb neutral
                lion "So this whole thing with the vault. It's legit?"
                mc "Yeah! That's what I was saying to people. Is it... that hard to believe?"
                show lion weeb sad
                lion "[mcname], listen, think about it from our perspective. It's a little hard to just... {i}believe{/i} that's what was going on, right?"
                lion "Even if Orlando claims the same thing, who knows if he's just thinking he saw something too. It's a lot to ask to just have us believe that you can see dead people."
                mc "Well... That's disappointing."
                show lion weeb neutral
                lion "Hey now, it's alright. Not saying I won't believe, you. Just might... Hrm... Take some proof?"
                mc "Proof? How am I meant to prove that?"
                lion "It'll be hard, for sure."
                lion "Maybe have someone in the room with you when you mess with it next? Maybe... If someone else could verify how it works and confirm that you seeing stuff is, for lack of a better word, normal?"
                mc "Who... Should I be asking?"
                show lion weeb laugh
                lion "Don't know! But hey, maybe make a game of it. See if you can rope someone in to your investigation?"
                mc "Are you volunteering?"
                lion "No, no."
                show lion weeb smile
                lion "But try not to let it drag you down. If you're legitimately worried about something, grab me and we can talk it through. If what you're feeling is legitimate, that's all that matters to me."
                "I sighed out as Hoss made his way over to me."
                if lionlove >= 12:
                    show lion weeb aroused
                    "Before I had a chance to react, Hoss leaned in and kissed me softly on the cheek, easing away with a sly smile."
                    lion "You'll be alright. Promise."
                    "I felt my cheeks go red, followed quickly by my laugh shining through. I was an odd combination of nervous and embarrassed but in a good way. It was different to getting kissed by a parent, that's for sure. But wasn't as intimate as you'd imagine with a boyfriend."
                    mc "T-Thanks..."
                    lion "Now go on. I want to get changed."
                    mc "Oh. Right. Um... See you at breakfast?"
                    show lion weeb laugh
                    lion "Sounds good to me!"
                else:
                    show lion weeb neutral
                    "He wrapped both his arms around me and pulled me in close. Then, while he held me there by my shoulder he stroked my head gently."
                    lion "Anything goes wrong, you can count me in your corner, alright?"
                    "I hesitated wrapping my arms around him to return the hug. He seemed to have my number though, knowing where to touch and how to bring me a sense of calm."
                    "Then, as a flourish, he wrapped his arms around me and gave me a tight squeeze. Making me squeak quietly."
                    show lion weeb laugh
                    lion "[mcname], did you just squeak?"
                    mc "I... M-Maybe?"
                    show lion weeb aroused
                    lion "Well geez, isn't that adorable?"
                    "I felt my cheeks go red, once again that hyena chuckle coming through. Flattery was something that was hard to accept, or even respond to. I wasn't anything all that special, right? I was just... {i}me{/i}."
                    show lion weeb neutral
                    lion "Now, go on. Scram. I have to get changed, and you do too."
                    mc "Alright. See you at... breakfast?"
                    show lion weeb smile
                    lion "See you at breakfast."
                scene black with dissolve
                "I left Hoss to head back to my room, changing into a fresh set of clothes before heading on downstairs for breakfast."
                jump Day8Breakfast
            mc "Oh, um... Thanks for letting us sleep in your room, Hoss."
            show lion weeb laugh
            lion "Not a problem, [mcname]. Now scram so I can get changed."
            scene black with dissolve
            "I filed out of the room to head back to my room so I could get changed."
            if dragonroute == True:
                scene bedroom with dissolve
                show dragon pantsless sad with dissolve
                "But on my way over to mine, I noticed Orlando waiting by the door into his room, half hiding behind it and watching me as I went by."
                mc "Is... everything okay?"
                dragon "Um... Mind if we chat for a little bit? Won't be long. Promise."
                mc "Oh, sure. What's up?"
                "I wandered into Orlando's room, with him closing the door behind me as soon as I was in. I was getting vibes similar to the day before when he cornered me in the kitchen."
                dragon "I just... Be honest. Everything about yesterday, last night, you were telling the truth, right?"
                "I frowned, giving Orlando a look."
                mc "Of course I was telling the truth!"
                mc "You're not thinking I lied about that, right?"
                show dragon pantsless pout
                dragon "No... Not really. Just... Well..."
                "There were a few moments of silence before Orlando continued, notably picking his words carefully."
                show dragon pantsless sad
                dragon "Maybe... I just feel like coming clean might have been the wrong thing to do."
                mc "But...!"
                dragon "No, hear me out on this."
                dragon "What if... the person behind it can also do what we can. Or... get the vault to work, right?"
                mc "But then... why would that matter? We can just undo everything we see, so..."
                show dragon pantsless pout
                dragon "Can we? We don't even know how it works."
                dragon "What if the person behind it was listening in and just... Changed how they did things to make it harder for us to stop them?"
                "I gulped, sinking into my shoulders. This was bad, or I got the impression that this was my fault all the same."
                mc "Oh... Oh no..."
                show dragon pantsless sad
                dragon "I might... Try and ask Sal and see what he thinks?"
                mc "Is that... wise?"
                show dragon pantsless scared
                dragon "Why wouldn't it be?"
                mc "Well... After yesterday. Y'know, with... what happened?"
                show dragon pantsless sad
                dragon "Oh. Right. Um... You might have a point. But... I don't want to stop hanging out with him."
                mc "I expected... you to be less okay with what happened. You and him must've had some talk, huh?"
                dragon "Well... We did, yes. There's... a few things about that though. Secrets were shared. I... sorta wish there was more to it, but no, just talking."
                show dragon pantsless pout
                dragon "Don't think I was prepared for what he told me though."
                mc "Was it... bad? What did he say?"
                show dragon pantsless sad
                dragon "Sorry, [mcname]. That's not my secret to share."
                mc "Oh..."
                mc "Well... Did you want to hug it out?"
                show dragon pantsless smile
                dragon "Yes please!"
                "We wrapped our arms around one another near the same time, embracing one another tightly."
                show dragon pantsless neutral
                dragon "Well, I don't know about you, but my plan is to put on some pants. What about you?"
                mc "Probably the same."
                "I contemplated telling Orlando about my meeting with Oz. After all, it seemed as though Orlando wasn't on his radar as far as being able to get the vault to work. But... Maybe it was best if I didn't for now."
                "It was hard enough to try and piece together what I should be doing, and saying, without throwing Orlando's worries into the mix. And if I was being honest with myself, part of me wanted to use this as a chance to rise up and prove I could be useful too."
                mc "Got some things I need to think over too, but that can wait until after coffee."
                show dragon pantsless laugh
                dragon "Well in that case, guess I'll see you down there!"
                mc "Yup! See you in a bit!"
                scene black
                "I headed back to my room, getting changed into a fresh set of clothes before heading downstairs to see the others."
                jump Day8Breakfast
            if boarroute == True:
                "As I headed back to mine, I noticed Roswell mumbling to himself, dipping into his room and shutting the door behind himself quickly."
                "Something about that seemed odd, odd enough that I doubled back to his door and knocked lightly."
                scene bedroom with dissolve
                show boar shirtless annoyed with dissolve
                mc "Uh... Roswell?"
                mc "Are you okay? You're uh..."
                boar "No, I'm not okay, [mcname]."
                show boar sad with dissolve
                "Roswell picked up one of his shirts and threw it on, sighing out."
                boar "I have a lot on my mind, okay? I'm tired, stressed, and a whole lot of other things."
                mc "Tired? But didn't you have that nice dream about cake?"
                show boar pout
                boar "It's... a different kind of tiredness."
                mc "Oh, well... Is there anything I can help with? I don't like seeing you upset, and you've been acting all weird lately."
                show boar sad
                "Roswell looked away from me, not wanting to make eye contact and he went quiet."
                mc "Did... Did I do something?"
                show boar scared
                boar "Oh, god, no. Not at all!"
                show boar sad
                boar "Well... It's complicated. Something I'm still trying to sort out."
                mc "Is this what... caused yesterday?"
                show boar mad
                boar "Don't. It's still too early for that talk."
                "I did a double take. It was unlike Roswell to be so... fired up about anything, even this early."
                mc "But... am I right?"
                show boar annoyed
                boar "...Partially."
                mc "Well hey now. That's... not fair, Roswell. Weren't we... I mean... the other day, we... and..."
                "I was gesturing loosely with my hands between us, hoping that my explanation was coming across clear enough without having to explicitly say it."
                show boar sad
                boar "Well... Maybe. It's not like I've had any experience with this sort of thing."
                mc "You think I do?"
                boar "Well..."
                mc "Roswell... is... everything alright? Like really, is this something I can help with or is this another one of those things that you just need to work through by yourself?"
                show boar pout
                boar "I don't... quite know yet. Can I get back to you on it? I think for now I just need some alone time before breakfast to think."
                mc "Oh, um... Okay..."
                "I started to back out of the room before turning to the door, hand placed on the handle."
                mc "You said... I was like an older brother, right?"
                boar "I... did, yes. Why?"
                mc "Do you see me as someone able to help too, or...? You've always been the smarter of the two of us but..."
                boar "Like I said, it's... complicated. Sorry."
                mc "Well... I guess we'll talk later then?"
                boar "Sure. I'll see you downstairs, [mcname]."
                scene black with dissolve
                "I left Roswell to his thinking and headed back to mine. It stung a little to think that he looked up to me but at the same time didn't see me as reliable enough to help. I could totally help, even if it was just listening to his problems."
                "But if it was something more than that... well, I had my job to do today. Maybe finding out some information about the vault from Oz would be a good start. Roswell was smart, but he didn't know everything."
                "Even then, maybe if I just asked Oz what the code to the door was so Roswell and I could open it together, it might put him in a better mood."
                "Once I was changed, I double checked I had everything I needed and headed downstairs for breakfast."
                jump Day8Breakfast
        return
        pass
        #Benson alive

label Day8Breakfast:
scene diningroom with dissolve
"I came downstairs, with everyone else arriving within minutes. My eyes looked at each of them in turn, checking them off in my head. The moment that all six of them were in my sights, I sighed out in relief."
show boar smile with dissolve
boar "Good morning, everyone."
show bear neutral at left with dissolve
bear "Morning."
show lion neutral at right with dissolve
lion "Hope everyone slept alright?"
hide bear with dissolve
hide lion with dissolve
show wolf pout at left with dissolve
show dragon sad at right with dissolve
wolf "Could've been better."
dragon "Wouldn't have minded if it was a longer rest. I still feel sorta stiff after yesterday."
show dragon pout
"I looked across to Orlando, catching him watching Sal briefly before looking at the ground."
boar "Good! Good... Now... with everyone here, I suppose I should ask if anyone killed Benson last night. Anyone?"
"My heart sank, stomach sinking. Was Roswell making light of what I went through yesterday now for some reason?"
if boarroute == True:
    "Is this what Roswell wanted to think about? Is he just trying to light the mood?"
show wolf mad
show dragon mad
wolf "The fuck is your problem?"
dragon "Roswell! What's gotten into you?"
show boar pout
boar "What? Too much in poor taste?"
show boar mad
boar "Well sorry for me trying to-"
stop music fadeout 2.0
"I started to drown out what the others were saying, something else catching my ear instead."
hide wolf
hide dragon
hide boar
with dissolve
"It was the distinctive clacking of shoes on tile. Each stride taken with deliberate purpose, measured in equal cadence."
"Even Roswell, Orlando and Ty had stopped talking to look towards the door to the dining room."
show otter neutral with dissolve
"Standing there, hands clasped behind his back as if nothing was wrong, was Benson."
otter "Good morning, gentlemen."
hide otter with dissolve
"All of us watched as Benson kept his pace, walking around us to the kitchen. He opened the door, looking back at me before calling out."
otter "Master [mcname], would you mind if you and I had a chat in private? Should not take long."
"I found myself pointing at myself, with the otter wandering into the kitchen without waiting for an audible reply. He spoke the same way a teacher or a parent would, where their question was rhetorical."
mc "I uh... I guess I'll be back guys?"
scene kitchen with dissolve
play music tense fadein 2.0
"I pushed open the door to the kitchen and closed it behind me, looking around to see if I could spot Benson, finding him near the coffee pot."
show otter neutral with dissolve
mc "Um..."
"Benson held a finger to his muzzle, focusing on the coffee brewing for a few more moments before he turned to me proper."
otter "I owe you a great deal of thanks, Master [mcname]."
mc "For... coming to talk?"
show otter pout
"Benson stroked the ends of his muzzle where the fur bunched up in a sort of moustache, thinking something over."
show otter neutral
otter "May I be plain?"
mc "Uh..."
show otter pout
otter "Apologies. I mean, may I speak in a more casual manner?"
mc "Oh! Of course."
otter "Now [mcname], m'boy. The master of the house informed me of the efforts you went through last night."
mc "The... master?"
show otter neutral
otter "I believe he'd given you the title 'Oz' to go by, yes?"
mc "Oh, uh... Yeah. Him. So you do work for him?"
otter "Of course. I'm his butler."
show otter pout
otter "Beyond that however. You fretting over my life is a gesture that has flattered this old otter, m'boy."
show otter neutral
otter "Truthfully, thank you."
mc "Well... Uh..."
"I wasn't sure how I should be responding here. Was he just humoring me? Was he sincere about how he was feeling about the whole thing? Where had he been while it was going down, anyway?"
"No one mentioned seeing him during the search for the gun, after all."
otter "As a sign of my gratitude, may I offer some advice?"
mc "Advice about what?"
show otter pout
"Once more Benson's hands stroked his moustache before returning to their place behind his back."
otter "Would I be right in assuming that your... plans for this evening are to converse with Oz?"
mc "That's... well yes, but if you know his name, can't you tell me?"
show otter neutral
otter "I'm under instruction to not speak as plainly as I am now until you two have spoken proper."
mc "But why?"
show otter pout
otter "Loyalty, m'boy. Loyalty."
show otter neutral
otter "There is no greater pleasure in life for a butler than to serve the house and its inhabitants. You are bred for the role, or at least grow into it. For me, there is no more fulfilling purpose."
otter "The downside however, is that your whims are beholden to another, sometimes to your detriment."
show otter pout
otter "I am getting off track."
show otter neutral
otter "He's deliberately testing your ability to find him."
mc "I just have to find the library, right?"
otter "Correct."
mc "Where is that, though?"
otter "Have you... not found it? There are multiple points of entry."
show otter pout
otter "Oh bother. Well... then perhaps a clue. I've been forbidden to disclose its location to you, but... I can nudge you in the right direction."
mc "Is that okay? You're not going to get into trouble, are you?"
show otter smile
otter "Ah, the kindness of youth."
show otter neutral
otter "Do not worry for me, m'boy. I've lived long enough that I know what I can take, and what's deserved."
otter "I can assist you in many other ways, just not the location of the library. Not yet, at least."
mc "What... other ways could you help me?"
otter "If I can manage it, advice, insight, weapons if you so desire."
mc "W-Weapons? Why would I need a weapon?"
show otter pout
otter "All things considered, [mcname], is it much of a surprise? You claim to have seen the results of what a weapon can do, and yet you baulk at an offer to keep yourself adequately armed for self defense?"
show otter neutral
otter "Truthfully, I'm astonished, though the offer is indeed genuine. There are many things around the manor that you could use. Some less... subtle than others."
mc "Um... Can I let you know... later? Oh! Actually batteries. Can I have batteries?"
show otter pout
otter "Batteries."
otter "What the devil do you need batteries for, m'boy?"
mc "Oh, um... In case the ones in my flashlight go flat."
show otter neutral
otter "Heavens, and here I was thinking you were planning something with a car battery. I shall see what I can scrounge up and leave them in your room later."
mc "Oh um... That... should be fine?"
show otter pout
otter "Again, it seems we've gotten off track."
show otter neutral
otter "Once you meet Oz, I'll be freer to talk. Until then, the key to finding the library is to talk to one of your friends."
mc "One of my friends has found the library already? Wait... Why does that sound familiar?"
otter "I can confirm that yes, one of them has. After all, they've been here before."
"Benson's admission left me stunned. Someone had been here before? When? Why?"
mc "Which... one?"
show otter pout
"It must've been a habit, with Benson playing with his moustache once more before replying."
otter "Unfortunately, that's all I can tell you. For now."
"Benson turned away from the coffee pot, satisfied with how it was coming along. Either it just took a long time to get going or this was some sort of special slow roasting process I was unfamiliar with."
"I watched as he started to prepare breakfast, pulling things out of the pantry that I hadn't noticed before. Muffins and alike, almost as if it had been restocked recently."
mc "Is it normal to be concerned?"
show otter neutral
otter "Concerned about what, m'boy?"
mc "I just... want to keep my friends safe. That's all. But I get the feeling the more that I mess with the things the harder I'm making it for myself."
show otter pout
otter "Ah. Grounded worries at that."
show otter neutral
otter "For what it's worth. The master of the house is a decent person. Someone that I'd put trust in having a vested interest in things coming out for the best."
mc "But is that outcome everyone surviving?"
otter "Would any other ending be as satisfying?"
mc "So I can trust him, then?"
show otter pout
"My question made Benson freeze, if only for a moment before he continued preparing things at his usual pace."
otter "Decency... and trust aren't mutually exclusive, m'boy. It is something you will need to decide upon meeting him."
mc "Okay, but... do you know who's behind it?"
mc "Who'd want you dead, or who's putting these images in my head?"
show otter neutral
otter "I do not. A lot of the enemies I once held are now long gone. For various reasons mind you, but nothing I know of can assist in your understanding here."
mc "But can I trust {i}you{/i}?"
show otter pout
otter "I believe the best way to answer that would be... to say that if you can trust Oz, you can trust me."
otter "My loyalty to the master of the house guides me to act in his best interest. If his objectives align with yours, then consider me an ally."
show otter neutral
otter "Bear in mind, I am still just a butler. Your decision to trust in me does not effect my duties around the house."
show otter pout
otter "Which I'm assuming after yesterday, means that there is a likelihood that you may need some laundry done."
mc "Well... Yeah. Sorry about that."
show otter smile
otter "It's quite alright."
show otter neutral
otter "Now, any other questions?"
mc "Just one."
otter "By all means, m'boy. What's on your mind?"
mc "Do you think... we're going to make it out of this okay?"
show otter pout
"Benson sighed out, going to play with his moustache but stopping short. Perhaps he was lost in thought, searching for the right thing to say before he gave me a look. I couldn't place the expression exactly, but it was somewhere in the realm of worry."
stop music fadeout 2.0
otter "I can only hope so."
hide otter with dissolve
"We stood in silence, with Benson breaking before I did to continue preparing breakfast. Meanwhile my eyes found the floor, tired again. Coffee, I needed coffee."
show lion neutral at right with dissolve
play music light fadein 2.0
lion "Everything going alright in here?"
"I jumped, not hearing Hoss enter the kitchen."
mc "Hoss! Oh, um..."
show otter neutral at left with dissolve
otter "Ah, Master Hoss, yes,  everything is fine."
show otter smile
otter "Master [mcname] and I were just having a chat. That's all. I hear you all had a busy day yesterday and he had some concerns about my wellbeing. Well, truth be told I heard much of it myself."
lion "Oh.{w=0.5} I see."
lion "Where have you been, anyway? You've been scarce lately."
show otter neutral
otter "Ah, just resting the old bones. When you get to my age, you fall under the weather from time to time."
lion "Hrm..."
show lion smile
lion "Yup. Lying."
show otter pout
otter "Pardon?"
show lion neutral
lion "You're lying."
show otter smile
otter "Lying? My, what an amusing idea."
otter "Perchance, would you be willing to lend a hand with breakfast? A man with a keen sense such as you must make for some excellent conversation."
lion "Sure. I don't mind giving a hand. What about you, [mcname]? Gonna help out too?"
lion "Wouldn't blame you if you wanted to head back out to the others though. Dean and Tyson were getting antsy as to how long you were being, but I'm not sure how much of that was their want of coffee coming through."
menu:
    "Help":
        mc "Oh, um... I can help. Sure. What do we need to prepare still?"
        show otter neutral
        otter "All things considered, with the rate at which you go through coffee, it'd be appreciated if you could brew another pot, Master [mcname]."
        "I nodded to Benson. It seemed as though speaking plainly was over in favor of taking an air of professionalism in front of extra people."
        "Hoss seemed to be pulling things out of the fridge while Benson continued basic prep work. I wasn't sure if Hoss was just dictating what we were having for breakfast and Benson was just going along with it, or if they were that in sync already."
        otter "Master Hoss, you've made me curious now."
        lion "Curious about what?"
        otter "I was, in fact, lying. How could you tell?"
        show lion laugh
        lion "Oh, just natural talent. Always been able to clue in when people weren't quite being truthful. Maybe it's all the time I spent around my siblings trying to figure out if they were fibbing or not."
        show otter smile
        otter "Ah yes. That would do it."
        otter "A skill such as that though. Would have fine applications in law enforcement, or perhaps the court room."
        show lion smile
        lion "Thanks, but no thanks. Not interested in any of that sort of stuff. Comes with the territory, y'know?"
        mc "Territory? What sort of territory?"
        show lion neutral
        lion "Just where I fit in the world. Easier to pick out what people are intending from afar, no point in confronting anyone about it if you're already in the know of where you stand."
        lion "Sometimes, it's even better to just... go along with it."
        mc "What, like acting?"
        lion "Sort of. Sometimes the best place to find information, or even hide it, is right in plain sight."
        mc "But why? How?"
        show otter neutral
        otter "Ah. I believe I follow. Who questions what's right in front of their face? People are, typically, prone to believing what they see at face value."
        show lion grin
        lion "Got it in one."
        otter "An interesting concept to be sure. I'd agree with Master Hoss on this. There have been many a time where telling someone something with no air of illusion has brought them around to believing what I've said."
        show otter pout
        otter "Even if it were a blatant lie. Or even subtle misdirection."
        mc "Isn't that... bad, though?"
        mc "Okay, so... lying already is pretty bad. Why would you need to lie?"
        show otter neutral
        show lion neutral
        otter "Morality is... a fairly grey scale, Master [mcname]. Varying greatly based on one's experiences and perspective of the world."
        lion "Not that I disagree, but what makes you say that, Benson?"
        otter "I've served the Hammond family for countless years now, caring for the masters and mistresses of the manor and their guests."
        show otter pout
        otter "But not every head of the house has been a pleasant individual."
        hide otter with dissolve
        hide lion with dissolve
        "We continued to work on breakfast, finishing up fairly quickly. Before taking it out to the dining room and laying it out on the table."
        scene diningroom with dissolve
    "Leave":
        "I looked at the door Hoss had come through thinking about the others I left back there."
        mc "Yeah, I probably should head back, if only to make sure Dean and Tyson are okay, right?"
        show otter neutral
        otter "Young men that are without food in their stomachs can be irritable for sure, Master [mcname]."
        show otter smile
        otter "Go on, the two of us can manage just fine."
        mc "Alright. Thanks for the chat, Benson!"
        otter "No, no. Thank {i}you{/i}, Master [mcname]."
        scene diningroom with dissolve
        show bear scared at left with dissolve
        show wolf sad at right with dissolve
        "No sooner than I'd walked into the dining room, I bumped into Dean who was lingering near the door."
        mc "W-Whoa! Dean!"
        bear "What... did he want to talk to you about?"
        wolf "You alright, pup?"
        mc "Uh..."
        "I looked between the two of them, before looking past them to Roswell, Orlando and Sal currently seated at the table."
        mc "I wasn't gone that long, was I?"
        show wolf neutral
        wolf "What did he say?"
        mc "Nothing important, really."
        hide wolf with dissolve
        hide bear with dissolve
        show dragon sad at left with dissolve
        dragon "[mcname]! You were gone a while for a brief chat! Did he chew you out for something, or?"
        show croc pout at right with dissolve
        croc "My guess would be that he wanted to thank you for being concerned. Am I right?"
        mc "Uh... Yeah, it was. How did you know?"
        show croc smile
        croc "We weren't exactly quiet last night when searching."
        show croc neutral
        croc "He probably heard us."
        dragon "Did he... say anything about that?"
        show boar annoyed
        boar "Like who might've wanted him dead?"
        mc "Nope. He had no idea."
        show croc pout
        croc "It was worth asking."
        show boar pout
        boar "But where does that leave us?"
        show dragon annoyed
        dragon "Waiting for breakfast."
        hide croc with dissolve
        show wolf pout at right with dissolve
        wolf "What, not going to go help out?"
        dragon "Hey, I don't have to cook if I don't want to."
        wolf "You're right. Who's on for meals today, anyway?"
        show boar sad
        boar "I suppose I could volunteer for lunch? Depends on what Benson's doing. If he's around more now we might not need to worry about it."
        hide dragon with dissolve
        show bear neutral at left with dissolve
        bear "Any idea where he went, anyway? Like, why he's not been around?"
        mc "Oh, um... Sick, apparently."
        boar "No surprise there. He is pretty old, right?"
        "Almost as soon as he'd finished talking, Roswell started coughing again, covering his mouth."
        show bear scared
        bear "Oh geez. That hasn't cleared up, huh?"
        show wolf annoyed
        wolf "You taking anything for it? I don't wanna catch whatever you have."
        show boar mad
        boar "Your concern is noted, Tyson."
        "It seemed that Roswell's behavior had possibly improved from yesterday, but he looked exhausted from almost coughing up a lung."
        show bear neutral
        bear "Just take it easy. We'll see if we can't get something to help out that cough."
        hide wolf with dissolve
        "I watched as Tyson got up and headed towards the kitchen, brought back to reality by Sal nudging me."
        show croc neutral at right with dissolve
        croc "Do we have any plans for today?"
        mc "Not that I know of. Anyone have any ideas?"
        show bear pout
        bear "Not really. Assumed that you'd want to do something again as a group. So long as it's not too draining I should be alright. Just need to get a nap in later to make up for last night and I should be alright."
        if lionroute == True or boarroute == True or dragonroute == True:
            mc "You didn't sleep well last night?"
            show bear neutral
            bear "Not really. Had a bunch of... Well, stuff on my mind. Maybe the sleeping arrangements didn't help."
            mc "Ugh... Sorry, Dean."
            show bear smile
            bear "It's alright. Nothing a nap later won't fix. I'll be fine."
        scene diningroom with dissolve
        "It wasn't long before Benson and Hoss emerged from the kitchen, laying food out on the table."
"As I grabbed food for myself and started eating, Dean poured me a cup of coffee."
"No sooner had the smell of it hit my nose I felt at peace again, sighing out despite the mouthful of banana I had."
"Occasionally I'd shoot Benson looks, unsure of what to make of my situation. He was joining us for breakfast this morning it seemed, satisfied with eating his porridge and coffee nearly as black as dad took it."
"I looked to the others at the table. Which one of them had been here before? Who knew where the library was? I had a feeling I knew but... With a whole day ahead of me, I wanted to try and figure it out myself first."
mc "I was wondering..."
show croc neutral at right with dissolve
croc "Wondering what?"
show otter neutral at left with dissolve
otter "..."
"I noticed that Benson was now listening in, curious despite keeping his attention for the most part on his porridge."
mc "What's... everyone doing today?"
show otter pout
show bear neutral with dissolve
bear "Probably just hang around until I'm ready for my nap. Maybe I'll go soak in the tub for a bit before turning in."
show croc pout
croc "Maybe... I'll do the same."
if wolfroute == True:
    croc "Tyson. You should join us."
    hide bear
    show wolf pout
    with dissolve
    wolf "Guessing I know why. Alright."
else:
    hide bear
    show wolf neutral
    with dissolve
    wolf "Hot tub, huh? Mind if I tag along?"
    show croc neutral
    croc "Not at all."
show otter pout
hide croc
hide wolf
with dissolve
show dragon neutral
show lion neutral at right
with dissolve
lion "Hrm... Might take a load off today. Just sit and watch TV. Orlando, want to join me for a bit?"
dragon "Sure!"
dragon "Watching anything in particular?"
show lion smile
lion "Nothing comes to mind. How about you pick?"
show dragon grin
dragon "Alright! I think I've got just the thing."
hide dragon with dissolve
hide lion with dissolve
mc "What about you Roswell?"
show otter neutral
show boar pout at right with dissolve
boar "No plans. Might just be lazy today, or wander around the house."
mc "Hrm... Well okay."
show boar grin
boar "What, worried about me? I can take care of myself."
show otter pout
"I shot Roswell a look, wary but said nothing more on it. I did need to talk to him about yesterday, but I had to get a start on searching for the library."
mc "Well... Good. Meet back for lunch then? Dinner?"
"There were nods all around and I got up to leave."
stop music fadeout 2.0
show boar pout
boar "Benson, something's been bothering me as of late."
show otter neutral
otter "Oh? Whatever can I do to ease your troubles, Master Roswell?"
boar "It's just..."
boar "We're the only ones here at the moment, right?"
boar "Just the eight of us here in this room now?"
show otter pout
"My eyes darted to Benson, who moved to play with his moustache once more."
show otter neutral
otter "That's correct. The only ones currently in the manor are the eight of us in this room. No one else."
show lion annoyed with dissolve
"Right as Hoss cleared his throat I looked at him. He caught my eye and stopped, about to say something but giving me a look instead. Was he about to call out a lie from Benson? Should I let him?"
"My mind tried to remember if this was going to be a problem or not. I vaguely remembered something about Oz not wanting to give himself away, so if he was a mysterious ninth person in the manor, was I meant to keep him hidden, or say something?"
"Benson must've caught Hoss's gaze directed at me, him too now looking at me expectantly for a decision to be made. No one else was saying anything, seemingly happy with Benson's original answer."
boar "Just eight... huh..."
menu:
    "Reveal Oz":
        play music calm fadein 2.0
        $ OzKnown = True
        mc "But... Isn't there nine?"
        show otter pout
        "There was silence following my question. Benson's expression was somewhere between disappointment and contained panic."
        show boar grin
        boar "So there {i}was{/i} someone else here. Interesting."
        show otter neutral
        "I could see Benson tensing up. I wasn't sure if I was meant to be ashamed that I'd opened my mouth or relieved that there were no more secrets to be shared."
        show lion annoyed
        lion "Better question is, why hide it?"
        hide boar with dissolve
        hide lion with dissolve
        show dragon scared with dissolve
        dragon "Even better question, who is it?"
        show otter pout
        otter "Ah, my apologies to all of you. The master of the house is, indeed, still here."
        show otter neutral
        otter "His proclivity for being a recluse led him to believe that his presence here was... unnecessary to divulge. After all, he never intended to interact with any of you."
        lion "Why? We're staying at his house, right? It {i}is{/i} a 'he' based on 'master', right?"
        otter "Correct."
        show dragon sad
        dragon "Well... I guess that's not so bad? If he wants his space... that's fine, right?"
        hide lion with dissolve
        show wolf pout at right with dissolve
        wolf "He leaves us alone, we leave him alone. What's the big deal?"
        hide dragon with dissolve
        show croc pout with dissolve
        croc "...Last night."
        show croc neutral
        croc "Does he know about last night?"
        show otter pout
        otter "He does. Yes. But I assure you he paid your search no mind. He's... a skeptic, shall we say."
        show croc pout
        croc "He doesn't believe you were in danger either?"
        show otter smile
        otter "As I said to Master [mcname], the thought was flattering all the same. That you would all flock to your friend's aid is a touching sentiment, too. The master and I were both pleased that the youth of today would have such solidarity for one another."
        show wolf neutral
        wolf "So what? He gonna come say hello that we know he's around or nah?"
        show otter neutral
        otter "Likely not, Master Tyson. He does like his space."
        show wolf pout
        wolf "Well, whatever then."
        mc "But..."
        show otter smile
        otter "Now, now, Master [mcname]. No need to worry about this any more."
        show otter neutral
        otter "I apologize again for misleading you. I assure you that everything is fine."
        "I got the impression Benson was trying to stop me from saying something, but I couldn't place why."
        hide wolf with dissolve
        show bear neutral at right with dissolve
        bear "Well, that's it, then?"
        show bear pout
        bear "Now we know there's just the nine of us in the house. Unless there's going to be a mysterious tenth person showing up later, shouldn't be any cause for alarm, right?"
        show otter smile
        otter "Precisely."
        show otter neutral
        otter "Now, if I may, I will take my leave now. Laundry calls."
        hide otter with dissolve
        "Benson strode out of the room, his dishes from breakfast held neatly in front of him as he disappeared into the kitchen. Chances were he'd take the exit from there out into the rest of the house to avoid coming back into the dining room."
        show croc neutral
        croc "..."
        show lion annoyed at left with dissolve
        lion "Uh... Sal? You doing alright?"
        show croc pout
        croc "I have a bad feeling about this."
        show bear scared
        bear "About... What?"
        show croc sad
        croc "I... don't know. Just something's... not seeming quite right with me."
        mc "Like... feeling sick, or?"
        show croc neutral
        croc "No, more like... an uneasiness. Something feels wrong."
        show lion neutral
        lion "Well... If you figure out what it is, and we can help, let us know."
        show croc smile
        croc "It's... probably nothing, but I shall let you know if I figure it out."
        hide croc
        hide bear
        hide lion
        with dissolve
    "Support Benson":
        mc "Y-Yup! Just eight!"
        play music light fadein 2.0
        show otter smile
        show lion scared
        "I laughed, nervous. No sooner were the words out of my mouth that classic hyena chuckle gave me away. I snuck a glance at Hoss who seemed floored by my comment, but made no mention of it beyond that. Guess he was happy letting things unfold for now."
        show boar pout
        boar "Well... Good to know, I suppose. Might've been a little odd if the person who lived here was still... well, here."
        show otter neutral
        otter "Now, Master Roswell. That's why I am here. If the master of the house were still around, you'd likely have seen him around by now."
        "I nodded slowly. At this point I wasn't sure if I was convincing myself further on what Benson claimed to be fact, implicating one of my friends as Oz, or not."
        show lion neutral
        lion "Only us eight, huh? Well hey, if Benson ever wanted in on the scavenger hunt proper, at least we'd have even teams."
        show otter smile
        otter "No, no. These old bones are much too tired to be gallivanting about the place like I did in my youth."
        otter "Though I appreciate the offer."
        show lion laugh
        lion "Well, if you change your mind, just let us know."
        otter "Why, I believe I shall."
        show otter neutral
        otter "But I believe, for now, I shall clean up from breakfast and move to doing some laundry."
        show otter smile
        otter "I shall be around if anyone needs anything. Anything at all."
        hide otter with dissolve
        "Benson picked up his breakfast dishes and wandered into the kitchen without another word."
        "I watched him go, fidgeting as to whether or not I made the right decision."

show boar neutral with dissolve
boar "Well... That clears that up."
show boar smile
boar "Well, I'm going to go wander around the mansion. See everyone at lunch."
hide boar with dissolve
"Roswell left soon after in the same way Benson did, disappearing into the kitchen."
hide lion with dissolve
show bear neutral at left
show croc neutral
with dissolve
bear "I'm going to get changed for the hot tub."
croc "I'll be coming too."
show croc pout
croc "Tyson?"
if wolfroute == True:
    show wolf sad at right with dissolve
    wolf "Yeah. I'm coming."
    "Part of me worried about was going to happen, but I just had to have faith that Ty would be alright."
else:
    show wolf neutral at right with dissolve
    wolf "What?"
    croc "You're coming, yes?"
    wolf "Oh. Yeah. Gimme five to get ready."
hide wolf
hide bear
hide croc
with dissolve
"The three of them filed on out, leaving their spots at the table as they were. Thankfully they hadn't made too much of a mess, but..."
show lion annoyed at left
show dragon sad at right
with dissolve
lion "Must've been in a hurry. Didn't clean up after themselves."
"Hoss started stacking his dishes along with Tyson's, before moving onto Sal's."
dragon "Well... I was going to offer to clean up after breakfast anyway. Least I could do given you helped make it."
mc "Well... I'm happy to help out too. Many hands and light work and all that, right?"
show lion smile
lion "Sure. Between the three of us it'll be quick."
scene kitchen with dissolve
"We gathered up what we could and brought it into the kitchen, making a few trips back to put what leftovers we had back in the fridge for later."
show lion neutral at left with dissolve
lion "That should just about do it."
show dragon pout at right with dissolve
dragon "Shouldn't we... wash the dishes too? I feel bad just leaving them for Benson."
show lion laugh
lion "It'll be fine. Right?"
mc "Will it be though?"
show lion neutral
lion "Probably."
lion "Come on, Orlando. Let's go hang for a bit."
hide lion with dissolve
hide dragon with dissolve
"I watched both of them leave, sizing up the dishes. There weren't all that many in the grand scheme of things."
mc "Maybe... {i}I{/i} should do the dishes."
"At the same time though, I could just as easily leave them for Benson to do."
menu:
    "Clean Dishes":
        $ DavePride += 1
        mc "Okay. Dishes."
        "I wandered over to the sink and started working down the list of things I needed."
        "Dish soap, check. Plug, check. Sponge? Double check. I don't know why there were two, but I guess I had a backup in case one... broke? Do sponges break?"
        "I started filling the sink with hot water, waiting until it was actually hot before putting the plug in. Dad said that only hot water made dishes clean, and I remembered Orlando saying something to that effect too."
        "Then again, the stuff Orlando used was really fancy. Or at least said that you had to clean them in particular ways to stop them from breaking or just... going bad."
        "Plug in, dish soap in, and the water began to foam."
        mc "Okay... so... What do I clean first...?"
        "I looked to what Hoss, Orlando and I had gathered. There were plates, mugs, some glassware too."
        mc "I wash... glass first, right? Or was it... plates?"
        mc "Lemme think... Water is clean. Which means the first thing I clean is..."
        menu:
            "Glass First":
                mc "Glass. I think. That way they stay really clear? I think that's what I'm supposed to do."
                "As I washed the glassware, I noticed that after I'd scrubbed them clean, they were crystal clear after the suds had been rinsed off."
                "Then came the plates. Hoss and Orlando had already started things off by scraping what scraps were leftover, so all I had to do was scrub them free of grease and alike."
                "With the plates done, the water was starting to get cloudy. With only a few mugs left, I washed them up too before sitting them aside."
            "Plates First":
                mc "Plates. You wash... the dirtiest first, right? So it doesn't get all stuck? I think?"
                "I started scrubbing in earnest, working through all the plates until all I had were mugs and glassware."
                "I grabbed the mugs, if only because I knew how gross they could get if you didn't wash them after having coffee. I pulled a face remembering the time I left a mug on the floor of my room once."
                "Not to mention the scolding I got from dad about not bringing my dishes down after I'd finished eating in my room."
                "The water was murky now, and I took a look at the glassware left. With a grimace I washed the first glass, pulling it out of the barely soapy water soon after and cringed."
                mc "Okay, yeah, that just looks worse."
                "I changed the water over, embarressed, and got the glass looking at clean as everything else. Not the most efficient use of water, but hey, at least everything was clean now."
        show otter neutral with dissolve
        "As I dried my hands on a tea towel and turned around, I came face to face with Benson."
        mc "A-Ah... Benson. Hello."
        if OzKnown == True:
            otter "..."
            show otter pout
            otter "Hello, Master [mcname]. Doing the dishes, are we?"
            mc "I just... wanted to help. I didn't expect you to... well... I didn't hear you come in. Sorry, should I have left them for you or? I think I did them properly?"
            show otter neutral
            otter "They look fine to me from here."
            otter "Have you made any... progress, with your little task?"
            mc "Not yet. Just been... here. Doing this."
            "I gestured behind me to the sink, and the dishes that were on the rack to dry."
            otter "...I see."
            mc "I'm sorry, did I... do something wrong?"
            show otter pout
            otter "It's... not my place to say, Master [mcname]."
            mc "Oh, you can just call me [mcname]. [mcname] is fine as is."
            show otter neutral
            otter "Very well, [mcname]."
            otter "I hope that your... decision at breakfast was the right one."
            mc "What... decision was that?"
            otter "Exposing Oz to your friends."
            mc "Oh... Well... they had a right to know, right? And it's bad to lie."
            otter "Agreed, [mcname]. Lying is fundamentally bad, if sometimes necessary."
            show otter pout
            otter "The things parents say to their children to protect them from the hard truths of the world in infancy."
            show otter neutral
            otter "And the lies adults say to one another to protect not only themselves, but those they hold dear."
            otter "Lies can be wielded for good, or evil. A lie to save someone's life for example: Good, or bad?"
            mc "I..."
            show otter pout
            otter "Forgive me, [mcname]. It is not my place to be interrogating you on such matters. Merely... raising a point of philosophical importance."
            otter "Oz entrusted you with information, a sign that he was willing to let you make a decision."
            otter "Whether or not your decision was the correct one, who can say?"
            mc "Oh..."
            show otter neutral
            otter "Do not misunderstand me. I harbor no ill will towards you, m'boy. There's no need to be alarmed or ashamed."
            mc "Okay..."
            mc "I... did have one question for you though. How... did you get in here so quietly?"
        else:
            otter "What are you doing, Master [mcname]?"
            mc "O-Oh... I just thought... Dishes. Helpful. Y'know."
            "I gestured over my shoulder with my thumb, hoping I'd done a good enough job to pass for something a professional butler could do."
            show otter smile
            otter "Ah. Well it is appreciated that you'd step in, but that {i}is{/i} very much why I'm around."
            mc "But... Helping is good. Right?"
            show otter neutral
            otter "Absolutely, Master [mcname]."
            mc "Oh, um... Just [mcname] is fine."
            otter "As you wish."
            otter "There is... another thing I wish to thank you for, at least now, knowing you did the dishes."
            mc "What's... that?"
            show otter pout
            otter "For... Not pointing out the master's presence."
            mc "Well... There's every chance that he's one of us, right? And there being an extra person will just... complicate things, right?"
            otter "Complications are a matter of opinion, m'boy. But you are correct. There is every chance that he's one of your friends, or someone else."
            show otter neutral
            mc "Wait, so... is he or isn't he an extra? I was starting to think there were nine of us here."
            show otter pout
            otter "Did you not come to that conclusion when you conversed last night? That there was indeed an extra beyond just your friends?"
            mc "Well... Now that I think about it... Couldn't {i}you{/i} be Oz?"
            show otter neutral
            otter "Pardon?"
            mc "Yeah! Like... You know the house well enough, and I haven't seen you and Oz at the same time, so..."
            show otter smile
            otter "Astute observation. Perhaps I {i}am{/i} Oz."
            mc "Wait, really?"
            show otter neutral
            otter "I suppose you'll just have to wait until tonight, assuming you can find the library."
            mc "Any tips for that? Beyond what you said before?"
            show otter pout
            "Benson seemed to think things over, stroking his moustache."
        show otter neutral
        otter "How much about large houses like this do you know, [mcname]?"
        mc "They cost a lot of money."
        otter "They do. What else?"
        mc "...Like a {i}lot{/i} of money."
        show otter pout
        otter "Perhaps I should rephrase my question."
        mc "Oh! And they can be spooky."
        otter "Why do you say that, m'boy?"
        mc "Cause sometimes, they have..."
        show otter neutral
        "The realization dawned on me as I worked through it. This wasn't some movie, or some work of fiction. This was an actual house, right?"
        show otter smile
        otter "Have what, m'boy? I feel like you might be onto something."
        mc "Benson, does... does this house have hidden... thingies? Passages and rooms?"
        "Benson, with a knowing smile, held a digit up to his muzzle, indicating to be quiet."
        otter "Why, what a novel idea, [mcname]."
        mc "Wait, so..."
        show otter neutral
        otter "I believe that, should you go searching, there is a chance you might find something of the sort, but who's to say?"
        show otter smile
        otter "Now, run along [mcname]. Happy hunting."
        scene black with dissolve
        "I nodded to Benson and scurried along, there was somewhere I figured I should start my search."
    "Leave":
        mc "I... I'll leave them for Benson. That's fine, right?"
        scene foyer with dissolve
        "Orlando and Hoss must have hurried along, as there was no sign of them when I entered the foyer."
        "I did a quick stock of who would be where, thinking about Benson's clue from earlier. One of my friends had been here before apparently, but how to start figuring out who?"
        "Would they just... tell me? Why wouldn't it have come up before?"
        mc "Who could it be though?"
        "Almost on cue, I looked up the stairs, hearing the footfalls of those coming down it."
        show bear swim smile at left with dissolve
        show croc shirtless neutral at right with dissolve
        show wolf neutral with dissolve
        "Based on how Dean was dressed, seemed as though they were on the way down to the pool, I stepped aside as they reached the bottom of the stairs so I was out of the way."
        if wolfroute == True:
            show wolf sad
            "Ty tussled my fur as he walked past, shooting me a look. He looked uneasy, almost scared. I threw him a quick thumbs up."
            show wolf pout
            "All that got me in kind was him rolling his eyes, making me frown."
            show wolf grin
            "Still, it seemed to take the edge off however he was feeling. I did remember that it might be good for me to have the first aid kit on hand, although I was only half sure how to use it. If it was a few cuts and bruises, then maybe I'd be alright."
            "Hopefully their chat was just that. A chat."
        if bearroute == True:
            show bear swim grin
            "As he wandered on past, Dean leaned in and gave me a quick peck on the cheek, lingering behind as to not catch the attention of the others. That said, I caught Sal looking back briefly and wondered just how much he'd seen."
            "They continued in stride though, with Dean mouthing the words 'hot tub' at me while throwing both thumbs up."
            "I returned the gesture, smiling and shaking my head. That bear and his hot tub, I almost wondered if I should start saving up for one just in case we ended up working out as a couple."
            "Not only that, but the idea of having a private one excited me just a little bit. It was like a bath, but instead of getting clean..."
            "...Well you sorta just sat in them, right?"
            show bear swim laugh
            "I must've been zoning out, cause when I looked at Dean next he was laughing, shaking his head; throwing me a wave before he passed through the door into the back yard."
        if crocroute == True:
            show croc shirtless laugh
            "Sal patted me on the shoulder as he wandered past. Seemed like he was in high spirits for some reason."
            "I looked to the other two, who seemed to wait for Sal by the back door, noticing Sal wasn't pottering along behind."
            "He gave me a thumbs up, a gesture that I returned, uncertain but near immediately before getting another pat on the head."
        hide bear with dissolve
        hide wolf with dissolve
        hide croc with dissolve
        "All three of them headed out back. Guess they were sorted for the morning."
        scene black with dissolve
        "I'd catch up with them later, for now I had somewhere I wanted to be."
scene museum with dissolve
stop music fadeout 2.0
"I headed upstairs and wandered into the museum. This was the best place to start looking, after all."
"I had a good reason for assuming this too. Oz knew I was here, and of all the rooms that I knew existed, there was no better to start researching."
if boarroute == True:
    "I'd been in here with Roswell, I remembered something in one of the books about a floorplan, if only in passing. It seemed that there was any chance of me finding the library this way, the museum held the answer."
if crocroute == True:
    "The only notable time I'd been in here recently, aside from last night, was with Sal. Not that there was any way of really looking up information from what I could tell. It was better than nothing."
else:
    "After all, where else was there likely to be a secret held? With so many books, the answer was bound to be in here somewhere, right?"
play music calm fadein 2.0
"Pulling a book at random off the shelf I started to flick through it. I frowned, seeing nothing but pages upon pages of text regarding... something. The words were long and difficult."
mc "What is this, anyway?"
"Turning the cover over in my hand, looking at the title."
mc "I really should look at the covers of books. This one's just about... wait, mycology?"
"I looked at the book again, flipping through. Sure enough there were pictures of mushrooms, listing what they were called, a bunch of other scientific terms about them."
if bearroute == True:
    "My attention stopped on a page about deathcaps, a chill running down my spine."
    mc "Ugh... Of course they'd be in a book about mushrooms."
    "I scanned the page briefly, noticing a couple of things."
    "Namely..."
    mc "Wait... Six {i}days{/i}? I thought they said six {i}hours{/i}. But that..."
    "I frowned, thinking back on it before turning back to the book. A lethal dose was only half a mushroom as well. So... maybe if Dean ate a full one, that'd make him die in three days? Maybe?"
    "I sighed out, slightly relieved that Dean dying was less and less likely to be a suicide. Maybe it was just an accident, maybe, something else, but something I'd have to talk to him about later."
    "Not only that, but it'd give me another chance to ask him what he was talking to Roswell about, too."
    show boar smile with dissolve
    boar "Mycology? Didn't think you'd be into mushrooms, [mcname]."
    mc "Whoa!"
else:
    mc "Ugh... This book is too hard... Can't I just have one with pictures?"
    "I put it back on the shelf, pulling out another one, not bothering to look at the cover in favor of checking if it had pictures first."
    mc "Wait... This is just children's stories."
    if crocroute == True:
        "I stopped on a page, looking at the title."
        mc "Hansel and Gretel..."
        "I thought back to when Sal and I were trying to navigate the maze. How he lay a trail behind us to get back to the entrance. Did he know these stories too?"
    else:
        "I read a few of the titles as I flicked through the pages. Stories that I remember my dad reading to me as a kid."
    "But now was not the time for such stories; they weren't going to help me find the library."
    show boar smile with dissolve
    boar "Doing some light reading?"
    mc "Whoa! Roswell!"
show boar grin
boar "It's only me, don't worry. Doing some wandering of your own? I half expected you to follow the others to the pool, or even hang out with Hoss and Orlando in the rec room."
mc "Well... Just thought I'd... do some research?"
show boar smile
boar "Oh? On anything in particular or?"
mc "Oh, um..."
show boar grin
boar "You don't have to try so hard, [mcname]."
if boarroute == True:
    show boar neutral
    boar "After all, we're partners, right?"
else:
    show boar smile
    boar "A lot of these books are well beyond the normal comprehension level of people our age, [mcname]."
mc "I can still try! After all, after yesterday, I don't want to be the one everyone's protecting."
show boar pout
boar "No offense, but what you were claiming was a bit... out there."
mc "Right. That's why I'm looking for proof. Something, anything to prove I'm not crazy."
boar "Well... Alright. Need some help?"
mc "I won't turn it down if you're offering, but I'm able to do it myself, I think."
show boar pout
boar "If you say so. I'll just go look over here for some completely unrelated reason, then."
hide boar with dissolve
"I shot Roswell a dirty look as he wandered away, snickering to himself. It seemed as though his attitude was still lingering."
"The next half hour we just looked through books in silence, at some point Roswell picked something out and sat down on the floor, leaning against the wall as he idly read something he'd chosen off the shelf. So much for being beyond our level of comprehension."
"Still, I kept at it, before finding a green covered book and flicking through it. The moment I saw floor plans I knew I'd hit the jackpot."
"Most of it was about the architect that built the house, but thankfully it had the original floorplans along with annotations. On some notes regarding the layout. The downside however, no library."
"In fact, a large portion of the house seemed to just not be here. The vault wasn't listed in the basement. Some of the rooms that I hadn't been to weren't on here, almost as if they'd added a whole extra wing as an afterthought."
mc "Damn, I thought that'd be it..."
show boar smile with dissolve
boar "What would be it?"
"I hesitated, wondering whether or not it'd be best to clue Roswell in to what I was looking for. Whether or not he was the one that had been here before. I shot him a look, sizing him up."
mc "I was wondering if there was like... maybe a clue as to how the mansion was built."
boar "Anything in particular?"
mc "Maybe a clue to where... more medals could be?"
show boar neutral
boar "..."
"Roswell looked at me, expression blank shy of that smile he had plastered on his face. It was hard to tell what he was feeling, but it was clear he was thinking in the silence following my question."
mc "Hidden rooms, stuff like that."
show boar smile
boar "Hidden rooms, huh? Interesting..."
mc "Interesting how?"
if OzKnown == True:
    boar "Well, if the master of the house is here, that's the only place he could be, right?"
    mc "Because we hadn't seen him yet?"
    show boar neutral
    boar "That, and it'd explain where Benson would be disappearing to."
    mc "What do you mean? How he was just... scarce?"
    boar "Well, think about it."
    boar "If he was just sick, he'd just be in one of the bedrooms, right? And there are plenty of those, and we're up at different enough times that we should have seen him leaving to get some medication or even food, right?"
    mc "I guess that makes sense..."
else:
    boar "It'd be very... on theme, don't you think?"
    mc "What, like murder mansion having secret means of moving around to get us?"
    boar "Exactly."
    show boar neutral
    boar "Wouldn't surprise me if there was something given how big the place is."
    boar "Why wouldn't you have a secret panic room? If you're rich, why not splurge on one?"
    mc "Is that... normal?"
    show boar laugh
    boar "Like I said, if you have the money, why not?"
    mc "I feel like that's sort of a waste of money, isn't it?"
    show boar neutral
    boar "Maybe. Unless you're hiding something there as well."
    mc "Hrm... Maybe..."
show boar smile
boar "In any case, secret rooms seems likely."
mc "Huh... Well, any ideas on where any could be?"
show boar neutral
boar "Honestly? They could be anywhere. Unless you went through every room with a fine toothed comb, you're unlikely to get one by accident."
mc "Hrm... You have a fair point..."
show boar grin
boar "But are medals really why you're doing this?"
show boar smile
if boarroute == True:
    boar "Cause if that's what we're doing next, more than happy to start going through the rooms with you!"
else:
    boar "Or are you just itching for an adventure?"
"I gave Roswell a quick once-over, unsure."
mc "Gotta do something, right? Especially after yesterday, maybe there's something more to what's going on?"
show boar neutral
boar "Yesterday sure was something, not gonna lie there."
mc "Yup. You were tearing into Ty something fierce too."
show boar annoyed
if boarroute == True:
    boar "You're not going to let this go, are you?"
else:
    boar "So what if I was?"
mc "Don't you think that you were going a bit overboard? I've never seen you act that way, it was... well..."
boar "It was {i}what{/i}?"
mc "You were being a bit of an asshole."
show boar mad
mc "Like... Saying that he's unable to love? That's... pretty low, Roswell."
show boar annoyed
boar "And if it's true?"
mc "But how do you {i}know{/i} it's true? Have you spoken to him recently?"
boar "Why would I go and do that? You do remember who he is, right? Tyson. {i}The{/i} Tyson. Remember?"
mc "No, I remember just fine. Remember, he's my friend?"
show boar sad
boar "You really think that?"
boar "You really think that he's..."
mc "That he's what? That he's changed?"
show boar annoyed
boar "Well, yes. Given his behavior so far, why would I expect that all of a sudden he's turned over a new leaf?"
mc "Because he hasn't?"
boar "Exactly."
mc "No, what I mean is, it wasn't sudden. He's been like this for a while."
mc "You were gone a long time, Roswell, things... change."
show boar pout
boar "You can't honestly expect me to believe that you've fallen for him?"
if wolfroute == True:
    "My immediate retort fell short, the words catching in my mouth. Denying the possibility should've been all to easy, but I couldn't."
else:
    mc "No! Not that, but just... uh..."
show boar annoyed
boar "Go on, then."
mc "He's... important to me?"
show boar mad
"Roswell shook his head, sitting his book down and standing from his spot on the floor, rubbing his temples."
boar "You have Stockholm Syndrome pretty bad, [mcname]."
mc "I... what?"
boar "Have you forgotten everything bad that he did?"
mc "What... do you mean?"
show boar annoyed
boar "You can't honestly tell me that you've forgotten everything he did to us."
boar "He shaved your fur, he stapled my ears to the school notice board, he dragged you around by the tail... Need I mention the countless times that he beat you for your lunch money?"
mc "But that's all in the past?"
boar "What, and I'm just meant to forgive him?"
boar "Oh, sorry, Tyson. Guess I should just forgive you for everything now. [mcname] said it was okay."
mc "That's not what I meant."
boar "Then what, pray tell, are you meaning?"
mc "It's... not really my place to say, is it?"
boar "Do you genuinely have a reason for him or are you just making excuses?"
"I sighed out, mimicking Roswell in rubbing my own temples."
mc "Just... When you moved away, a lot happened."
mc "Sure, Orlando was around but... Tyson was also around. Things... changed."
mc "But also I learned about... other things. Why he did some of the things he did."
boar "Oh this is going to be good. What sob story did he tell you, [mcname]?"
mc "Not... so much a sob story, but I was over at his place once and there was... a fight, with him and his dad. Kept me behind him the whole time so his dad didn't get to me too."
show boar pout
boar "What, and you just stayed there? Why didn't you run?"
mc "Because I wasn't going to abandon him, Roswell! He was hurting, because of me or something else, it didn't matter. You don't just abandon people in trouble."
boar "You can't be serious."
mc "I am. What would my dad have thought if I left him in the lurch like that? He was in trouble and I was the only one that could help."
boar "So what happened after? He then tell you his life story?"
mc "No, this all happened after I knew bits and pieces. This was more... proof? Maybe? Not that some of the things he said were stuff you'd normally lie about anyway."
mc "Like... the lunch money thing."
show boar annoyed
boar "What about the lunch money thing?"
mc "Well..."
mc "Probably doesn't show now, but... He doesn't get to eat every meal, Roswell."
boar "I find that hard to believe."
mc "Okay, so... maybe I invite him over pretty often to eat."
show boar mad
boar "So now he's just leeching off you at home!"
mc "It's not like that!"
mc "If you didn't get to eat every meal, sometimes for a week, what would you do?"
show boar pout
boar "Uh..."
mc "Roswell, he stole from us so he didn't go hungry. Whether he wanted to or not, he didn't have a choice."
show boar annoyed
mc "When his dad was blackout drunk, he showed me. The cupboards were bare, what little was in the fridge had gone off, it was real bad!"
boar "That's..."
show boar pout
boar "That's... not an excuse..."
mc "Look me in the eye and say that, Roswell, I dare you."
mc "You've been so harsh on him that you haven't given him a chance. You don't even {i}want{/i} to give him a chance."
mc "Yesterday was just not fair, so much so that you should probably apologize."
show boar mad
boar "You can't be serious. There's no way I'm apologizing to him."
mc "What, and you're going to keep picking fights with him?"
mc "You're the smartest out of everyone here Roswell, so I expected you to at least know better."
show boar scared
boar "W-What...?"
mc "You heard me. Tyson can be a jerk, but yesterday you were more of a jerk than he's been lately."
show boar sad
"I let the comment hang in the air for a bit. Roswell went to speak a few times, the words just not coming instead he resigned to pulling at the fur on his chin instead."
"It felt uncomfortable confronting Roswell like that. There was history, I knew that, but with him being gone so long it just didn't seem right that he'd be holding onto things that happened so many years back."
mc "So... Was there a reason?"
boar "..."
mc "Anything? Did he do something recently, or?"
boar "No... not that."
if boarroute == True:
    boar "It's... probably silly, and not much of an excuse, but..."
    mc "But what?"
    boar "After... The other day, I've been thinking more about dying recently. Not suicide but more...  conscious about what little time we have left."
    mc "We're still young, Roswell!"
    boar "Yes, I know, but..."
    show boar pout
    boar "What if tragedy strikes? What if something happens to either of us?"
    boar "Death can come at any time and just... what happens if it's tomorrow? What if it's in five minutes?"
    boar "Shouldn't that be enough of a drive to get you to confront the things you've wanted to? To say the things you've always needed to?"
    mc "But to take it out on Tyson? For things that happened all that time ago? How's that fair?"
    show boar annoyed
    boar "I have... a vested interest now."
    mc "In what, me?"
    show boar sad
    boar "You, dummy.{w=0.5} I've maybe been crushing on you for a while now. At least I think that's what it is."
    mc "How... bad of a crush are we talking?"
    show boar mad
    boar "Just... enough that you make it really hard to think about what I should be doing. What I should be saying."
    boar "I've prided myself in being able to see things so logically but..."
    mc "But that doesn't give you an excuse to treat him like dirt."
    show boar annoyed
    boar "What, so I have to forgive him?"
    mc "To some extent, yeah!"
    boar "But why?"
    mc "Because like it or not, he's important to me, Roswell. He's family."
    boar "{i}Family{/i}?"
    mc "Yeah. {i}Family{/i}. I'm not picking sides, but the moment you make me choose between the two of you, then I'm sorry, but..."
    boar "Am I not important?"
    mc "You're important too! But I'm not going to put up with you putting me on the spot having to choose between my friends? What sorta friend would I be to have to abandon either one of you?"
    show boar scared
    mc "And what sort of friend would {i}you{/i} be to make me have to choose?"
    boar "I..."
    show boar sad
    boar "...I..."
else:
    boar "There's... a reason."
    mc "Is it a good reason?"
    boar "Probably not, in all honesty. I've just been overly... conscious of something of late."
    mc "Something that's worth taking it out on Ty?"
    boar "I just keep thinking to myself... {w=0.5}Time."
    boar "How much do I have left? How much do {i}we{/i} have left?"
    mc "What... sort of time? Before we part ways? The vacation?"
    boar "Death."
    show boar pout
    boar "We have so little time left, [mcname]."
    mc "We're both young! How can you possibly think that?"
    show boar sad
    boar "Countless possibilities for tragedy around every corner. I feel the shadow of the grim reaper lingering over us more and more as time goes by."
    boar "I wish I could say that this was just some... shtick that I'm pulling like I would to get a rise out of Orlando but... I genuinely have this sense of dread about things."
    mc "Nothing in particular? Just... in general?"
    boar "Someone's going to die, [mcname]. I can't tell you how I know, but... I know."
    boar "I don't know who, either. You, me, or one of the others; it could be anyone."
    mc "But then why antagonize Ty? He didn't deserve what you pulled yesterday."
    show boar annoyed
    boar "It's not that. Just... If I were to die tomorrow, or even if {i}he{/i} were to die tomorrow, I'd just... want to try and balance things out?"
    mc "{i}That{/i} was about balancing things out?"
    boar "Yes?"
    mc "Cause to me it just seemed you were being a dick for no reason."
    boar "Excuse me? He had it coming."
    mc "Not to the extent you went to. You seemed to get in whenever you could with one thing or another. And I don't want to see it happen again."
    boar "You realize that he's just been leeching off you this whole time, right?"
    mc "No, he hasn't."
    show boar mad
    boar "What, and you think there's some noble reason that he's the way he is? Some excuse he's fed you?"
    mc "I don't need anything he's said as proof, I've seen it, Roswell. I just told you that."
    mc "I've seen first hand what his dad does to him for no reason. I've seen how bare his cupboards are. I've seen him be scared as you or me for the smallest things we take for granted."
    show boar pout
    boar "Like... what?"
    mc "Like having a safe place to sleep."
    mc "Or not having to worry about going hungry."
    mc "If he'd told me that when we were kids I'd have trouble believing him. But having seen it?"
    boar "So... he had a reason this whole time to treat us like dirt? And I'm just meant to forgive him?"
    mc "To some extent, yeah."
    show boar mad
    boar "And why's that?"
    mc "Because like it or not, Roswell. He's..."
    if wolfroute == True:
        "I gulped, suddenly feeling uncertain. For a long time I'd seen Ty in... a certain light? A brother maybe. Something more was equally likely. The more time he and I spent around one another though..."
        "Was there something more than that? Had I just yet to put it into words or was I seeing something that wasn't actually there, and just something I wanted to be there instead?"
        mc "...He's family."
        "It didn't feel right. It wasn't inaccurate, but it felt like I was putting things lightly too. Thankfully Roswell's mood seemed to make him not question my tone."
        show boar pout
        boar "You can't be serious. Family?"
        mc "Family. He's as important as any of the rest of you. Maybe in the same way, maybe for different reasons, I don't know."
        mc "Think of him like... an older brother? Regardless of what he is though, he's still important."
        show boar mad
        boar "So I'm to play second fiddle to him just because I was gone for a while?"
        mc "No one's playing second to anyone, and I'm not picking favorites. I'm not choosing sides, Roswell."
        boar "And if it came to it?"
        mc "Then I'd be disappointed that you'd think I'd be willing to abandon any one of you, just because of a personal gripe you can't let go of."
        mc "And trust me when I say that if you make me choose, well... You might not like what the answer would be."
        show boar pout
        boar "I... But..."
    else:
        "I nodded to myself, knowing full well where I'd place Tyson, staring down Roswell."
        mc "Family."
        show boar pout
        boar "You can't be serious."
        mc "I am. He's... important to me. Maybe like a brother if I had to pick something, maybe something different entirely, but he's still that important to me."
        mc "And if you're going to make me choose between the two of you, then... well..."
        show boar mad
        boar "Is it really going to come to an ultimatum?"
        mc "It better not, because I'm not picking sides."
        mc "Just know that if you put me in a position where I have to pick, I'm going to have to weigh up the fact that someone's making me choose to abandon someone, and if they're worth keeping around."
        show boar pout
        boar "I..."
        "Roswell looked me over, I could see him searching me for an answer, as if he wasn't completely sold that I was being genuine on that claim."
mc "Look, just... No more pot shots at Tyson. He's been good so far, right?"
show boar annoyed
boar "What about the other day?"
mc "What {i}about{/i} the other day? I'm not an idiot, Roswell. You were pressing his buttons deliberately."
show boar smile
boar "You can't prove that."
mc "You're right, I can't."
show boar scared
mc "But I know Ty, and I know you."
mc "And I know,{w=0.5} that {i}you{/i} know,{w=0.5} he wouldn't kick up a fuss about the wolf and dog thing unless provoked about it."
mc "Why would you rile him up like that, anyway? Was it to try and get him to hurt you on purpose?"
mc "Are you jealous? Are you trying to get rid of him? What?"
show boar mad
boar "Okay! Fine! I'm jealous!"
boar "{i}We{/i} were friends first! {i}He{/i} is a terrible person! And I hate that I didn't clear who you wanted to bring first."
mc "No, {i}you{/i} need to accept that he's changed, or at the very least give him a chance."
mc "I can't make you apologize, but I think you owe it to him. Or if not an apology, promise me you won't go making it hard on him on purpose. If he acts up then by all means! But don't go picking fights with him."
show boar annoyed
boar "Fine."
"Roswell started to grumble, kicking the ground."
if boarroute == True:
    show boar sad
    boar "Sorry, [mcname]."
    mc "Not to me. To Tyson."
else:
    boar "I'll try."
    mc "You mean it?"
"He sighed out, retrieving his book and dusting it off, tucking it under his arm."
show boar annoyed
boar "It's not easy to let that go. I want to see proof from him that he's gotten better."
mc "You're not willing to trust me on this?"
boar "Not really. Those scars run deep. I want an apology from him just as much."
mc "So if you apologize to each other...?"
show boar pout
boar "I'll... consider it?"
show boar sad
boar "We're here for a month, so logically speaking... you're right. It makes no sense to be at odds given proximity."
"He wandered past me towards the entrance of the museum."
mc "Where are you going?"
show boar pout
boar "To my room, to read."
mc "And the... apology?"
show boar annoyed
boar "You're not my mother, nor my therapist, [mcname]."
mc "I'm not trying to be! But you're my {i}friend{/i}, and I'm trying to help make things better."
boar "Well... Let me work through it on my own."
hide boar with dissolve
"I reached out in vain to stop him from leaving, but he strode out of the room with a purpose."
mc "Hoo boy..."
"Looking around the museum again, I wondered if there was any hope of me finding what I was looking for in here. As much as there were books, this apparently wasn't the library."
"It did leave me with two options though. I could check in with the guys at the pool, or see what Hoss and Orlando were up to."
scene foyer with dissolve
show otter neutral with dissolve
otter "Master [mcname]."
mc "Oh, hello Benson. How're things?"
show otter smile
otter "Fine. Thank you for asking."
show otter neutral
otter "How fares the search?"
mc "Not... too well. I was just in the museum, trying to figure out if there were floor plans or... maybe something as another clue."
show otter pout
otter "Have you questioned your friends yet?"
mc "Oh, no. Only spoken to Roswell but he wasn't very... helpful. Not that I asked him about it directly."
otter "Ah well, the day is still young, Master [mcname]."
show otter smile
otter "Now, if you excuse me, there's much work to be done."
if OzKnown == False:
    show otter neutral
    otter "Ah, but before I do."
    otter "Oz wanted me to deliver something to you."
    mc "Oh? How come?"
    otter "You will grow tired of me saying this, but it comes down to loyalty. Suffice to say, he entrusted me with something to pass on."
    mc "Oh! I like presents!"
    show otter smile
    otter "No, Master [mcname]. It is not a physical boon."
    mc "Oh."
    show otter neutral
    otter "Information."
    otter "Just something to keep in mind for later."
    mc "Alrighty. Lay it on me."
    otter "Bring your flashlight."
    mc "My... flashlight?"
    show otter pout
    otter "I'll provide adequate batteries for you if you need them and leave them in your room before dinner if you so wish."
    mc "Easy. I can do that."
    show otter smile
    otter "Very good. Now... Happy hunting."
else:
    mc "Alright. See you later, Benson!"
hide otter with dissolve
"I watched as he wandered down a side corridor and out of sight before weighing up what I should do next."
"There was still some time before lunch, so depending on how long I checked in with either group, I might not get a chance to check with the other."
menu:
    "Check in on..."
    "Orlando and Hoss":
        scene casino with dissolve
        show lion weeb neutral at left
        show dragon neutral at right
        with dissolve
        "I could hear them as I approached, discussing something in earnest. The moment I heard my name come up, I hid on the outside of the room, listening in."
        dragon "What about him?"
        show lion weeb annoyed
        lion "So... Did he seem odd this morning to you or what?"
        show dragon scared
        dragon "Uh... Not really, why?"
        show lion weeb pout
        lion "Do you really believe him when he said... with the thing downstairs?"
        "My breath caught in my chest, waiting for the answer from Orlando."
        show dragon sad
        dragon "Of course I do! I just worry that... What if I was wrong in what I saw? What if I was wrong in... Well..."
        show lion weeb neutral
        lion "Wrong in what?"
        show dragon pout
        dragon "What I experienced, and what he experienced being the same thing."
        show lion weeb pout
        lion "But you did see... something?"
        dragon "I'm positive. I just don't know what to make of it. It was... fuzzy, like... I was dreaming? Or that there were a few things going on at once?"
        dragon "I just worry that this is going to mess with him in some serious ways."
        "Both of them fell silent, and sneaking a peek I could see them both thinking it over. I took this as my cue to enter, doing my best to pretend I hadn't overheard anything."
        mc "Hey guys!"
        show lion weeb scared
        show dragon scared
        dragon "[mcname]!"
        lion "How long have you been there?"
        mc "I caught some of the conversation but uh... Should I pretend I didn't hear it?"
        show lion weeb neutral
        show dragon sad
        lion "No, it's alright. Just talking about yesterday."
        dragon "Just... it's weird, right?"
        dragon "The whole thing about downstairs? What is that thing? Why is it affecting you like that?"
        mc "I... wish I knew?"
        mc "But you guys have been talking about that all morning?"
        show lion weeb laugh
        lion "Oh, no. Just came up, really. We've just been swapping back and forth between shows. Just relaxing."
        mc "So another day at the anime club, then?"
        show dragon laugh
        dragon "Sort of! All we're missing is Roswell!"
        mc "Well, don't go expecting him to come join us. He's settled in to do some reading at the moment."
        show dragon neutral
        show lion weeb neutral
        dragon "Did you run into him?"
        mc "Yeah! I was just looking in the museum for something and he ran into me."
        mc "Had uh... It wasn't much of one, but I spoke to him about yesterday, too."
        show dragon scared
        show lion weeb sad
        lion "What did he say?"
        mc "You could probably guess. Essentially he's jealous, but what Ty did to him way back runs deep."
        show dragon sad
        dragon "I didn't realize that it was... well, that bad. Sure, Tyson still gives me the shakes when he's talking to me but..."
        show lion weeb neutral
        lion "He hasn't actually done anything that bad."
        show dragon scared
        dragon "You don't think so?"
        if wolfroute == True:
            "My hand went to my nose, touching it gently, thinking back on what Ty had done to it."
        lion "All things considered... He's been pretty blunt and outside that one thing with Roswell, he hasn't been that bad. Can't be that bad a guy if he's willing to help me out in the gym, right?"
        show dragon sad
        dragon "That... makes sense, I suppose. I dunno, I'm still a little skeptical."
        mc "Well..."
        if lionroute == True:
            mc "You said you were going to give him a shot, right Hoss?"
            lion "That's right."
            show dragon scared
            dragon "Wait, really?"
            show lion weeb smile
            lion "Sure. Couldn't hurt, right? Feel like he and I might have a couple things in common."
            show dragon pout
            dragon "Geez... Guess I better give it a shot, too..."
        elif dragonroute == True:
            mc "Would you be willing to give him a shot, Orlando?"
            dragon "I... don't know..."
            show lion weeb grin
            lion "Oh go on. What's the worst he could happen?"
            show dragon scared
            dragon "Well... I suppose you're right..."
        else:
            mc "I can vouch for him at least. That must mean something?"
            show dragon pout
            dragon "[mcname]... I dunno..."
            show lion weeb smile
            lion "Sure, I'm in."
            show dragon scared
            dragon "You what?"
            show lion weeb annoyed
            lion "What? I'm not scared of him, and he might just need a friend."
            show lion weeb laugh
            lion "Aside from [mcname], at least."
        mc "If it helps, maybe... I can be in the room too?"
        show dragon scared
        dragon "What do you mean?"
        mc "Like... How about you, me and Tyson do something?"
        mc "Same with you, Hoss."
        show dragon sad
        dragon "I don't know..."
        mc "It doesn't have to be anything big. Maybe we could just watch a show together."
        show lion weeb grin
        lion "Anime. Got it."
        mc "Wait no."
        show dragon smile
        dragon "Tyson likes anime too! Maybe we should make him a shirt!"
        mc "Okay, maybe we should slow down a little bit. Maybe find out if he wants to watch anime first?"
        show lion weeb laugh
        show dragon mad
        dragon "Okay! Hoss, we have to pick something good. If he hasn't watched anime before, we have to start off strong."
        lion "That's a tall order. Don't even know what sorta things he likes."
        show dragon annoyed
        dragon "Well, maybe we can tick off magical girl anime. Unless he's like Sal I don't think that'd go over very well."
        show lion weeb neutral
        lion "Sport anime? Maybe just get something with a bit of humor?"
        mc "Maybe just ask him?"
        mc "But otherwise that seems like a good idea. Include him in things and maybe he'll be... uh..."
        show dragon neutral
        dragon "Well... We'll see. There's time, right?"
        mc "Right."
        show lion weeb laugh
        lion "Come sit with us for a bit, [mcname]. Still got a bit before lunch, anyway."
        mc "Alright."
        scene black with dissolve
        "For the next while I sat with Hoss and Orlando, watching the TV as they swapped episodes with one another."
        "When it was time for lunch, we filed out and headed downstairs."
        scene foyer with dissolve
        "We reached the bottom of the stairs, with me lingering behind Hoss and Orlando. Was it worth asking them if they'd been here before? It'd be better to ask one of them now, before we all grouped up again, right?"
        menu:
            "Ask Orlando":
                mc "Hey, um... Orlando? Can I talk with you for a moment in private?"
                show dragon neutral with dissolve
                dragon "Oh, um... sure."
                "Hoss waved us off as he headed to the dining room, leaving Orlando and I on the stairs to talk."
                dragon "So what's up, [mcname]? Everything alright?"
                mc "Oh, yeah, just... had a strange question for you."
                if dragonroute == True:
                    show dragon scared
                    dragon "Oh no. Is this... an appropriate question for out in the open?"
                    mc "Wait, what?"
                    show dragon neutral
                    dragon "What, so you're not tagging me in as your 'goach' for something?"
                    mc "No! Not that. Just... something else."
                else:
                    dragon "A strange question? How strange are we talking?"
                    mc "Maybe a little strange, but not... really strange?"
                    show dragon annoyed
                    dragon "Speaking of strange, you're being a little... y'know."
                    mc "Okay, okay. Let me get right to the point."
                mc "Have you been here before?"
                show dragon scared
                dragon "Excuse me?"
                mc "Like... Be honest with me. Have you been to this house before?"
                show dragon sad
                dragon "No...? Why do you ask?"
                mc "Oh. Um..."
                show dragon pout
                dragon "Did... something happen?"
                if dragonroute == True:
                    dragon "Was it something with the vault again? Did you get another word correct?"
                else:
                    dragon "Did... it happen again? Like yesterday?"
                mc "No, no... Just..."
                mc "Apparently one of us has? At least Benson thinks so."
                show dragon scared
                dragon "Whoa. That's... news. It's not me, that's for sure. Roswell would be my guess. Given he arranged the thing and all, right?"
                mc "That'd make sense. I should go ask him after lunch maybe."
                show dragon neutral
                dragon "Sorry I can't be much help. But really, why did you want to know?"
                mc "Oh, nothing... important. Just had a question about the layout. That's all."
                show dragon smile
                dragon "Not a problem!"
                show dragon laugh
                dragon "Shall we head to lunch then?"
                mc "Alright. Sure."
                jump Day8Lunch
            "Ask Hoss":
                mc "Hey Hoss, can I borrow you for a moment?"
                show lion weeb neutral with dissolve
                lion "Me? What's up?"
                mc "Just need your opinion on something. But in private."
                show lion weeb scared
                lion "Uh... Alright. Sure."
                "Orlando wandered towards the dining room on his own while Hoss and I remained on the stairs."
                show lion weeb neutral
                lion "So need my opinion on something?"
                mc "Yeah, sorry."
                show lion weeb laugh
                lion "Don't apologize!"
                show lion weeb neutral
                if lionroute == True:
                    lion "Were you wanting some more advice for your fur? Can get you some more of that stuff you like, if you want."
                    lion "Or if you want something that had a different scent, I'm sure I could maybe figure something out."
                    mc "Oh, no. Not that. Well... Maybe that too, but maybe later?"
                    show lion weeb smile
                    lion "Well alright. What's on your mind?"
                else:
                    lion "For what it's worth, the shirt looks fine. Cute, even."
                    mc "I... What?"
                    show lion weeb smile
                    lion "The design. It's cute."
                    mc "Oh. Thanks! But that's... not what I wanted to ask about."
                    lion "Well I'm all ears."
                mc "Have you... been here before, Hoss?"
                show lion weeb neutral
                lion "..."
                mc "Uh... Hoss?"
                lion "Sorry, did I hear you correctly? {w=0.5} Were you asking if I'd been here before?"
                mc "Yeah, to the mansion. Like... Benson reckons one of us has."
                lion "Does he now...?"
                mc "Mmhm!"
                lion "How did that come up, anyway?"
                mc "Oh... um..."
                show lion weeb grin
                lion "Remember, I'll know if you're lying!"
                mc "I know... Um..."
                mc "I was looking for something, but that's the only clue Benson gave me. Well... If you could call it a clue."
                show lion weeb neutral
                lion "So far so good. What are you looking for?"
                mc "A room, actually."
                mc "The... wait..."
                "I thought back, the memory coming back to me. Something Hoss had said way back when we arrived."
                mc "Hoss, there's a library here, right?"
                lion "Yup."
                mc "Can you... show me where it is?"
                show lion weeb smile
                lion "But you already know where it is. Surely you've been there already. With the suit of armor, no?"
                mc "No, no. That's a different room. That's the museum."
                show lion weeb neutral
                lion "Well, guess I was mistaken then."
                mc "You're... lying?"
                lion "..."
                mc "Hoss, the day we got here you said... um... That the library was a big room that covered multiple floors. Right after Roswell talked about the museum."
                show lion weeb smile
                lion "..."
                mc "Uh... So..."
                mc "So you must've found it then, right? That or... you'd been here before?"
                show lion weeb neutral
                "Hoss sighed out, running his fingers through his mane, sizing me up. The corners of his mouth twitched upwards, almost as if he was trying not to laugh but he kept a straight face beyond that."
                lion "Sure, I can show you the library."
                mc "You mean it?"
                show lion weeb neutral
                lion "Yup. Cat's out of the bag. I know where it is, so I'll show you after lunch."
                mc "Sweet! Thanks!"
                show lion weeb annoyed
                lion "Although you don't strike me as the library type. Is there another reason you wanted to go there?"
                mc "Um..."
                show lion weeb laugh
                lion "Y'know what? Don't worry about it."
                show lion weeb smile
                lion "You don't want to tell me. It's written all over your face. But if you ever feel like sharing, you've got my curiosity piqued."
                mc "Alright, I'll uh... I'll keep that in mind. But... lunch?"
                show lion weeb neutral
                lion "Lunch."
                $ Library = True
                jump Day8Lunch
            "Stay Silent":
                "I shook my head. There was no way to know if either of them knew anything. Even then, maybe it was best that I didn't bring it up."
                "After all, if what Benson said was true, then maybe there was a good reason they were keeping it a secret."
                jump Day8Lunch
    "Tyson, Dean and Sal":
        scene mansionback with dissolve
        "Sal, Tyson and Dean were all hanging around by the pool, so I figured I'd see what they were up to."
        if wolfroute == True:
            "Not just that, but I was a little worried that Sal might've gone at Tyson."
        if bearroute == True:
            "Plus, I wanted to make sure that Dean hadn't fallen asleep in the hot tub. That seemed like a recipe for disaster."
        if crocroute == True:
            "With Sal there, it seemed unlikely that anything bad was going to happen given they were in a group of three, but I just wanted to make sure."
        scene pool with dissolve
        "I unlatched the gate and wandered on in, looking around."
        show croc swim smile at left with dissolve
        "Sal seemed to be enjoying himself in the water, as per the usual."
        if crocroute == True:
            "Although now that I knew why, the smile I had twisted slightly into a concerned frown. For someone that was supposedly afraid of water, you couldn't tell."
        show bear swim neutral at right with dissolve
        "Dean was in the hot tub, as I expected him to be."
        if bearroute == True:
            "But with how tired he looked, I was hoping that he didn't plan on having his nap in there. That seemed dangerous."
        show wolf shirtless laugh with dissolve
        "Ty however looked happy as can be sprawled out on a deckchair. Was he soaking up what sun he could? Was he even awake?"
        if wolfroute == True:
            "With how happy he looked, it seemed as though Sal hadn't chewed him out for the other day. That or he'd spoken to him about something else entirely if they had had a conversation at all."
        mc "Hey guys!"
        show wolf shirtless scared
        wolf "Whoa!"
        show croc swim laugh
        show bear swim smile
        "Ty sat up suddenly, looking around before his eyes settled on me."
        mc "Oh, um..."
        show wolf shirtless pout
        wolf "Oh, it's just you. Geez..."
        mc "Did I... wake you?"
        show croc swim neutral
        croc "He's been asleep for a little bit."
        mc "To be honest, I was expecting Dean to be the one asleep given how he's looking now."
        show bear swim grin
        bear "Later. Dangerous to fall asleep in the pool. Or even the hot tub for that matter."
        show croc swim sad
        wolf "Weather ain't bad. Could just soak up some sun and get a nap in."
        show bear swim laugh
        bear "I'd much rather my own bed."
        show wolf shirtless neutral
        wolf "Suit yourself."
        show croc swim pout
        croc "Sun baking is best at the beach. Or on a nice rock."
        mc "Really? But... all that sand though."
        show bear swim pout
        bear "Yeah, the beach is fine but the sand is a killer."
        wolf "Haven't been to the beach in... Well, years."
        show wolf shirtless pout
        wolf "Would've been happy to go to the beach even instead of a mansion, but you won't hear me complaining."
        mc "Not {i}yet{/i} anyway!"
        show wolf shirtless annoyed
        show bear swim laugh
        show croc swim laugh
        wolf "Oi."
        "Ty got up from his chair and made a break for me, grabbing me around the middle and picking me up."
        wolf "Should throw you in the pool for that one!"
        mc "No! Wait, please!"
        show croc swim smile
        croc "Alright, calm down."
        show croc swim neutral
        croc "It's not safe to run around the pool."
        show bear swim smile
        bear "Plus, [mcname] doesn't look like he's got anything else to be wearing if you get him soaking wet. At least right now, anyway."
        if poolnotexplored == True:
            mc "Aren't there spare towels in the lockers?"
            croc "True, but then you'd be naked beyond that."
            show bear swim aroused
            bear "Naked, huh?"
            show wolf shirtless pout
            wolf "Okay, okay. Fine. You get off easy this time, pup."
        else:
            mc "Y-Yeah, please don't throw me in, Ty?"
            show wolf shirtless smile
            wolf "You sure you don't wanna go for a swim?"
            mc "Not right now!"
            show wolf shirtless pout
            wolf "What if I jumped in with you?"
            mc "Later, Ty!"
            wolf "Fine."
        "Tyson put me down and wandered over to the hot tub with me in tow, sitting just around the outside and dipping his feet into the bubbling water, gasping at the temperature change."
        "Sal wandered over as well, but opted to just stand nearby."
        mc "So how's things been for you guys? Good day so far?"
        show bear swim neutral
        bear "Been an easy one, although I'm for sure getting a nap in after lunch. I'm bushed."
        croc "So far so good, how about you, [mcname]?"
        mc "I was just in the museum. Looking at stuff, ran into Roswell, y'know."
        show wolf shirtless neutral
        wolf "What did the oinker have to say?"
        show croc swim annoyed
        croc "Tyson."
        show wolf shirtless pout
        wolf "Sorry. Habit. What did Roswell have to say?"
        mc "Um... Well..."
        wolf "Me, huh?"
        mc "Yeah..."
        show bear swim pout
        bear "Did he say what the deal was?"
        show bear swim neutral
        bear "To be honest, it seemed out of character for him to just... go all in."
        show wolf shirtless neutral
        wolf "I'm fine with it."
        mc "I'm not."
        show wolf shirtless pout
        show croc swim pout
        croc "How bad was it?"
        mc "He said Tyson couldn't love anyone. That he couldn't have nice feelings."
        show wolf shirtless neutral
        wolf "Pretty much."
        croc "That's... pretty bad. Should I talk to him?"
        mc "No, it's alright. I got an answer out of him as to why he was being a jerk yesterday though."
        show bear swim pout
        bear "Was it a good reason, at least?"
        mc "Well..."
        if boarroute == True:
            mc "After my first run-in with the vault, he's been thinking about his own mortality a bit, really."
            show bear swim scared
            bear "What, he's afraid of dying?"
            mc "Well, I think so? I understood it more as him not wanting to have any regrets about his feelings towards Tyson."
            show croc swim pout
            croc "Is this what Orlando was telling me about?"
            mc "Uh... Depends?"
            croc "Uh... Hate... something..."
            show bear swim pout
            bear "Oh, I think I know what you're talking about. But uh... No, I think it's more like... an eye for an eye sorta thing?"
            mc "Maybe?"
            mc "I talked him into at least patching things up though."
            show wolf shirtless pout
            wolf "Well great. Looking forward to that."
        else:
            mc "I think the... overall concern was... How much time we have left?"
            show bear swim neutral
            bear "What, alive?"
            mc "Well yeah."
            show bear swim pout
            bear "I... think I can understand that a little."
            show croc swim pout
            croc "Doesn't give him an excuse however, he can be mindful and respectful at the same time."
            show wolf shirtless neutral
            wolf "So what, he's worried about dying?"
            mc "Sort of?"
            mc "It's more about uh... Getting even?"
            show wolf shirtless pout
            wolf "Well shit, does he want to get a few punches in, or what?"
        mc "To be clear, uh... It's still up in the air if he'll actually do anything. Or even what he wants from you Ty."
        show croc swim neutral
        croc "I've been curious about this for a while. What did you do to him as a kid?"
        mc "Hey, that's not-"
        wolf "I was a fuckin' jerk, Sal."
        wolf "You seen any movies with a school bully? Basically me as a kid. Shaking down nerds for lunch money, messing with them, taking it too far."
        show bear swim neutral
        bear "Got... examples?"
        mc "Hey, Dean, he doesn't-"
        show wolf shirtless pout
        wolf "Sure. Held [mcname] down and shaved him once."
        show bear swim scared
        show croc swim annoyed
        "My hand went to the patch of fur that he really dug in with the clippers, thinking back."
        bear "But... Why?"
        mc "That's... um..."
        show wolf shirtless neutral
        wolf "Why does any kid do the shit they do?"
        show wolf shirtless pout
        wolf "Don't get me wrong, I don't like that I did it to him these days."
        if wolfroute == True:
            "I caught Tyson shooting me a quick look, the faintest hint of a smile on his face before he looked away."
        else:
            "I nodded slowly, looking at Dean who seemed to be struggling with the concept."
        bear "You... really regret it?"
        show wolf shirtless neutral
        wolf "Hands down, got [mcname] to thank for a lot of good that's happened to me lately. Wouldn't be here without him, yeah?"
        show croc swim sad
        show bear swim pout
        wolf "Well... Him and his dad."
        croc "This... is a lot to take in."
        bear "What... Do we even say to that?"
        show wolf shirtless pout
        wolf "Look, all I'm saying is I get where Roswell's coming from. I'd be a hypocrite if I couldn't take what I dish out, yeah? If he wants a free shot in, then I'll let him."
        mc "That's... going overboard."
        show wolf shirtless neutral
        wolf "I got limits, but if it'll help him get his shit together, why not?"
        show bear swim neutral
        bear "That's... very big of you, Tyson."
        wolf "I got my reasons for wanting to be better. Don't think I'd be able to look him in the eye if I stayed a little shit forever, yeah?"
        mc "Look... who in the eye?"
        show wolf shirtless pout
        "Tyson kept his eyes elsewhere, not wanting to look at me."
        show bear swim neutral
        bear "Not... to be a downer, as I wouldn't mind continuing this conversation some other time, but... it's about time for lunch, isn't it?"
        show bear swim pout
        bear "At least I'm getting hungry."
        mc "Probably about that time, yeah. Should we head in?"
        show croc swim neutral
        croc "Sure."
        show bear swim neutral
        bear "Alright, lemme just go rinse off in the shower and I'll be good to go."
        if bearroute == True:
            show bear swim grin
            bear "Mind coming with, [mcname]? Wanna have a chat about something."
            mc "Oh, uh... Okay."
            scene pool with dissolve
            "I took Dean's towel from him as he went inside, and soon enough I heard the water running as he called out over the divider."
            bear "So!"
            mc "So...?"
            bear "Should I be jealous of you and Tyson?"
            mc "Wait, why?"
            bear "That a no, then?"
            bear "Cause sounds like you and him are pretty close. Closer than just friends anyway."
            mc "Ty's... uh..."
            bear "'Just Ty', huh?"
            mc "Pretty much."
            show bear swim grin
            bear "So I don't need to worry about dating you both as a complete package?"
            "I laughed as Dean reappeared and I handed him the towel so he could dry off."
            mc "No, it's not like that. Win him over maybe, but I don't think you need to {i}date{/i} him to date me."
            show bear swim laugh
            bear "Well good!"
            show bear swim smile
            "Dean held his towel, an end in each hand, and threw it over my head so it hooked behind my neck. With a gentle tug, he pulled me to him so he could give me a quick kiss on the forehead."
            show bear swim grin
            bear "Come on. Let's go get some food."
        elif wolfroute == True:
            hide bear with dissolve
            "We watched as Dean hauled himself out of the tub and wandered over to the showers."
            show croc swim pout
            croc "So..."
            show wolf shirtless neutral
            wolf "What?"
            show croc swim neutral
            croc "[mcname], how's your nose?"
            mc "My... Oh. Right."
            show wolf shirtless sad
            croc "So good enough that you forgot, it seems."
            wolf "We having that talk now?"
            show croc swim pout
            croc "Just answer me this."
            croc "Those things you said. Did you mean them?"
            "My breath caught in my chest as my gaze shifted slowly from Sal to Tyson."
            show wolf shirtless neutral
            wolf "Could've said it nicer. But yeah, I meant it."
            "I preemptively flinched, waiting for Sal to throw a punch but it never came. Instead, Sal just looked thoughtful, as if processing something."
            croc "I... won't rehash what you already know, we all have our failings."
            show croc swim neutral
            croc "But I want to reinforce that people can be good deep down."
            show wolf shirtless scared
            wolf "What, that's it?"
            croc "Yes? Was there more?"
            show wolf shirtless sad
            wolf "Well... Depends on what you heard after that."
            show croc swim pout
            croc "If you were talking about pushing [mcname] to have sex with you, well..."
            "I went still, having been thankful that for the last little bit I'd been quiet. I tried to make myself smaller without moving, somehow, waiting for something to happen."
            show wolf shirtless neutral
            wolf "He didn't consent, so nothing happened. Almost did, shouldn't have, but that's how it went."
            croc "[mcname]?"
            "I squeaked when Sal addressed me, eyeing me carefully."
            mc "That's... that's basically how it went down. I didn't even say no but Ty... knew? I guess?"
            show croc swim annoyed
            croc "Alright..."
            show croc swim mad
            croc "I feel like I'm letting you off easily but... it doesn't involve me. If it happens again though."
            wolf "You have permission to lay into me. Whatever way you want."
            croc "And of [mcname]?"
            mc "I don't think I could."
            wolf "Which is enough incentive for me to not want to hurt you on purpose, pup. Not again."
            "Sal looked over to Dean who had just gotten out of the shower, making a move to leave the pool area."
            croc "Alright. Time for lunch. That's all I wanted to say for now."
            hide croc with dissolve
            "I sighed out when Sal wandered away to retrieve his towel. I was expecting something worse, a lot worse, and part of me worried that this was just the quiet before the storm."
            mc "Ty...?"
            wolf "Yeah?"
            mc "You promise you won't hurt me like that again?"
            "Ty stood up, pulling his feet from the hot tub and wandering closer."
            show wolf shirtless smile
            wolf "Not on purpose, at least. Promise."
            show wolf shirtless pout
            wolf "Now come on. Let's get some grub."
        elif crocroute == True:
            hide bear with dissolve
            "Dean wandered over to the showers, grabbing a towel on the way. Ty got up to go find a towel to dry his feet and Sal wandered off to find a towel of his own."
            scene pool with dissolve
            "For a moment, I wondered if I should find a towel too before realizing I hadn't actually gotten into the pool."
            show croc swim smile with dissolve
            croc "Are you alright, [mcname]?"
            mc "Hm? Oh, yeah, I'm good. How goes... drying off?"
            show croc swim laugh
            croc "Fine."
            show croc swim smile
            croc "Weather isn't so bad today. Sunnier than I thought it'd be."
            mc "You thought it'd be different?"
            croc "Well... With the rain we had recently, I was expecting more of it."
            mc "Maybe the sky just... ran out of rain?"
            show croc swim grin
            croc "I don't think that's how clouds work."
            mc "No, I know that but uh... Well... It's sunny. Sun is good."
            show croc swim neutral
            croc "Yup."
            mc "But how are you Sal? Had a good morning?"
            show croc swim pout
            croc "It's been fine. Yesterday is weighing on me a bit still. At this stage I'm just looking for other things to think about while I... Hrm..."
            show croc swim neutral
            croc "I suppose it's contextualizing it. Feelings are... difficult, and keeping Orlando in mind is both painful and concerning."
            mc "In what way?"
            show croc swim sad
            croc "Maybe it's best with an example."
            croc "Let's say... You made Tyson sad."
            mc "Why Tyson?"
            croc "Why not Tyson?"
            mc "Oh, um..."
            show croc swim pout
            croc "If my read is correct, then... it's a close enough comparison, isn't it?"
            mc "Well... If I made Ty sad I'd probably feel terrible. And..."
            show croc swim neutral
            croc "And what?"
            mc "And I'd probably be worried about what I could do to make it better?"
            croc "Which is where I'm at with Orlando."
            croc "I have no doubt that it'll be fine, eventually, it just might take a few things to get there."
            "I nodded slowly, understanding enough to get where Sal's stress was coming from. Although if anything I was wondering more what I could do to help him out rather than a hypothetical scenario where I made Tyson upset."
            show croc shirtless pout with dissolve
            "Sal put on his pants over his swimwear and turned to me again."
            croc "Shall we head inside?"
            show croc neutral with dissolve
            croc "It's probably time for you to have another cup of coffee."
            mc "Probably a good idea, yeah."
        else:
            scene pool with dissolve
            "Each of them wandered off to go find towels, leaving me by the hot tub. Having not gotten into the water, I had time to kill, and wandered over to the bridge that sat over the pool."
            "Looking into the water, I could see my reflection, rippling gently on the water's surface. I almost had to do a double take, mistaking the person I saw staring back at me for someone else."
            "It was different somehow than looking at yourself in the bathroom mirror. Maybe it was that subtle ripple that made me seem older, or maybe it was just where the past couple of days had put my mind."
            "I pulled out my phone and sat down, letting my legs dangle off the edge as I sent a SMS."
            "It wasn't a long message, just one asking how his day was doing. I'd sent many of them before, and I'd stopped bothering to scroll up to count them."
            "No sooner had it been sent, I shoved my phone back in my pocket. I think a part of me, deep down, knew that I wouldn't get a reply but it made me feel better knowing I still could send the messages in the first place."
            show wolf shirtless pout at left with dissolve
            wolf "You doing alright?"
            mc "Hm? Oh, yeah. I'm good."
            show bear swim smile at right with dissolve
            bear "Ready for lunch?"
            mc "Yeah, I could eat."
            "I got up, dusting myself off."
            bear "Just thinking about things?"
            mc "What do you mean?"
            show wolf shirtless pout with dissolve
            wolf "Told you he wouldn't realize."
            show bear swim laugh
            bear "No kidding."
            bear "You've been sitting there for a bit just in a daze."
            show wolf shirtless neutral
            wolf "Better get used to it. Happens often enough."
            show bear swim grin
            bear "Gotcha. I'll keep that in mind."
        scene mansionback with dissolve
        "As a group we wandered back towards the manor, with me lingering in the back with my thoughts. All in all, it was good seeing them getting along but there was still something else I needed to potentially ask."
        menu:
            "Ask Dean":
                mc "Um..."
                "Tyson looked back at the same time Dean did, but with my attention on the bear, he wandered inside with Sal to give me some alone time."
                show bear swim neutral with dissolve
                bear "Everything alright?"
                mc "Oh, yeah, everything's fine."
                show bear swim grin
                bear "But...?"
                mc "But... I wanted to ask you a question."
                show bear swim aroused
                bear "A 'question', huh? Should I be excited?"
                mc "No, no! Nothing that exciting, really."
                show bear swim pout
                bear "Probably for the best."
                show bear swim neutral
                bear "But still, what's on your mind?"
                mc "It's a bit of... an odd question, so..."
                mc "Have you been here before, Dean? To the mansion?"
                show bear swim smile
                bear "Can't say I have. Why?"
                mc "Oh, uh... Benson said... one of us had. And I was looking for something so..."
                bear "So you thought the person that had been here might know where the thing is?"
                mc "Essentially, yeah!"
                show bear swim pout
                bear "Well, sorry. It's not me, as much as I'd love to help."
                mc "That's alright Dean, worth asking, right?"
                show bear swim smile
                bear "Of course! Feel free to ask me anything, anytime!"
                show bear swim grin
                bear "But for now, care to join me for lunch?"
                "I laughed as Dean opened and held the door open for me, the two of us heading inside to get something to eat."
                jump Day8Lunch
            "Ask Sal":
                mc "Hey..."
                "I reached out and tugged on Sal's shirt, him slowing enough to fall back behind the other two. I looked past him to see Dean and Tyson heading inside, not paying us any more."
                show croc neutral with dissolve
                croc "Yes?"
                mc "Sorry, I just uh... a question."
                show croc pout
                croc "Okay...?"
                mc "It's going to be an odd one. Just so you know."
                show croc neutral
                croc "Alright. What is it?"
                mc "Have you been here before, Sal?"
                show croc pout
                croc "..."
                mc "Sal...?"
                croc "Y'know... I was thinking that I might have. Maybe."
                mc "Really?"
                show croc neutral
                croc "Something about this place feels... familiar. I just can't place it. But if I had to guess... I wouldn't say I had. Maybe a house similar?"
                mc "Oh... Well that's alright."
                show croc pout
                croc "Sorry. Is there a reason you wanted to ask?"
                mc "Benson said one of us had been here before so... I dunno, just figured it'd be worth asking."
                show croc neutral
                croc "How did that come up?"
                mc "Oh, I'm looking for something, well... It's sorta like that anyway."
                show croc pout
                croc "Something... important?"
                mc "Important enough. At least I think so."
                show croc sad
                croc "Well... I hope you find it. If I can help, let me know, but otherwise... I'm probably not one to ask."
                mc "That's alright. It's all good."
                show croc neutral
                croc "Now... Lunch?"
                mc "Right."
                "I held the door open for Sal and the two of us wandered inside to meet with the others."
                jump Day8Lunch
            "Ask Tyson":
                show wolf shirtless neutral with dissolve
                "Instinctively I reached out for Tyson, taking hold of his hand. He froze, looking back at me before glancing at the others and pulling his hand away. The fact I wasn't smiling was enough to make Tyson understand."
                wolf "What's wrong?"
                "Sal and Dean wandered inside, either they didn't notice or figured to pay us no mind while we talked."
                mc "Nothing... really?"
                show wolf shirtless pout
                wolf "So you're just being a dork? Why'd you go grab my hand like that?"
                mc "I just... had a question. But it's probably stupid, don't worry about it."
                show wolf shirtless annoyed
                wolf "Don't make me ask you what the question was."
                mc "Okay, fine, so like... this house, yeah?"
                show wolf shirtless neutral
                wolf "What about it?"
                mc "You haven't... been here before, right?"
                wolf "..."
                mc "See? Stupid, right?"
                show wolf shirtless pout
                wolf "You thought I cased the place?"
                mc "No, not that..."
                show wolf shirtless neutral
                wolf "I know you well enough that you're bothered by something, so spill it."
                mc "Well... Benson said one of us had been here before. Said that I should ask them for help finding something."
                show wolf shirtless pout
                wolf "Well shit. News to me. Looking for anything good, pup?"
                mc "Not really, just nerd stuff."
                show wolf shirtless grin
                wolf "If you find anything worth some money, let me know."
                mc "Ty, we're not stealing anything, just... I wanna prove myself."
                show wolf shirtless neutral
                wolf "Prove yourself why though?"
                mc "That I can take care of myself and also help and stuff. Y'know, be more like, uh..."
                wolf "Like your dad?"
                mc "I guess? Maybe a little like you?"
                show wolf shirtless scared
                wolf "Why the fuck would you want to be like me?"
                mc "I dunno, you just seem to be good at this sorta stuff."
                show wolf shirtless neutral
                wolf "Then just aim to be like your dad and you'll be right. Trust me."
                mc "Okay..."
                show wolf shirtless pout
                wolf "Now come on. Get inside so we can eat."
                jump Day8Lunch
            "Stay Silent":
                "I went to say something but shook my head."
                "There was no way of knowing if any of them had been here before without asking, and if they hadn't said anything so far, they'd must of had some reason to keep it a secret."
                "Filing in behind the rest of them, we headed inside for lunch."
                jump Day8Lunch

label Day8Lunch:
scene black with dissolve
"By the time we'd all filed into the dining room for lunch, we all looked at one another, wondering where lunch was coming from. Had we not decided this beforehand?"
"Still, in my mood of wanting to do more, I wandered into the kitchen. After all, I may as well have a turn at some point, right?"
scene kitchen with dissolve
mc "Lunch... Lunch... Um..."
"I looked around the kitchen, wondering what I could make. I hadn't exactly told anyone I was going to make lunch but that should've been the expectation... Right?"
"The loaf of bread I'd picked up seemed good. Sandwiches were... lunch, right?"
mc "Sandwiches..."
"I must've zoned out. I could smell the bread in my hand and I thought back to lunch at home. To breakfast before toast had been made."
show dragon sad at left with dissolve
show croc pout at right with dissolve
dragon "Uh... [mcname]? Are you okay?"
croc "He's... got the bread."
show dragon annoyed
dragon "Sal, not now."
mc "Bread... Sandwiches, right?"
"I gestured to the loaf in my hand in vain, momentarily forgetting if bread was a necessity for sandwiches."
show croc neutral
croc "For lunch, yes?"
mc "Yeah!"
show dragon neutral
dragon "Did you need some help?"
mc "No, no. I've got it. Just uh... what do you want on them? Peanut butter?"
show croc pout
croc "I don't mind peanut butter but..."
croc "Can I have... Well... I prefer PB & J if we're doing sandwiches."
mc "Oh... I can do that."
show dragon laugh
dragon "I'll go get what you need, [mcname]. Call it out and you can be the chef today."
show croc neutral
croc "I'm gonna get the bread."
mc "But {i}I{/i} have the bread."
show dragon annoyed
dragon "You can {i}both{/i} have the bread. No way one loaf is going to be enough to feed everyone anyway."
scene kitchen with dissolve
"It was pretty basic, but after I got to cutting the bread, along with the loaf Sal brought over, I assembled it all into sandwiches and brought it into the dining room."
scene diningroom with dissolve
mc "Sandwiches!"
show bear swim smile at left with dissolve
bear "Can't beat a classic. Thanks!"
"Dean sounded tired but he took a sandwich and sat down, eating a lot slower than I'd seen him eat before."
show wolf shirtless pout at right with dissolve
"Ty wandered over and snatched up a sandwich before sitting down a few seats down from Dean, biting into his sandwich. I must've had too much peanut butter on that one, as he started eating with a lot less gusto and chewed a lot longer on a second bite."
hide bear with dissolve
hide wolf with dissolve
show lion weeb neutral at left with dissolve
"Hoss came up next, taking a sandwich and taking a bite without bothering to sit down."
show boar sad at right with dissolve
"Roswell took his sandwich much like Tyson did, without a word before sitting on the other side of Dean."
show lion weeb annoyed
lion "Well... Thanks for the sandwich."
mc "Sorry it's um... a little basic?"
hide boar with dissolve
show dragon neutral at right with dissolve
dragon "Hey, you took initiative and made something. Doesn't matter if it's something fancy or basic, you made an effort."
"I chuckled, embarrassed but held onto a sense of pride welling up in my chest hearing Orlando say that."
show croc neutral with dissolve
croc "You got that bread."
show lion weeb laugh
lion "Sal, I don't think..."
show dragon pout
dragon "Oh no, he's being literal. We walked in on [mcname] with a loaf of bread in his hands."
show croc pout
croc "Is... that not what you say? When someone goes for their goals?"
show lion weeb grin
lion "And [mcname]'s goal was just... bread?"
show croc neutral
croc "For sandwiches."
show dragon sad
dragon "Oh, honey, no."
"Orlando and Sal took a sandwich before I sat the platter that carried them, down. Taking one for myself I stayed standing, looking around as I ate."
if Library == True:
    "I looked to Hoss and I caught him looking back at me. He was going to show me the library, which... Made the next part of my day easier. All that I needed now was to scope it out and go from there."
else:
    "What was I going to do? Who was likely to know where the library was? Who was it that had been here before?"
show dragon neutral
dragon "While I remember, who's on dinner duty tonight?"
show croc pout
croc "Please, not me."
show lion weeb neutral
lion "Guess I can again."
show croc neutral
croc "Even though you were last night?"
show lion weeb annoyed
lion "Well someone's gotta do it, and [mcname] did lunch. Any other takers?"
hide croc with dissolve
hide dragon with dissolve
show bear swim neutral with dissolve
show boar neutral at right with dissolve
bear "I'll do it. Assuming I get my nap in."
bear "Might need some help though. Roswell, you able to give me a hand?"
show boar pout
boar "Oh... I... suppose so? Should we plan what we're going to have then?"
show bear swim laugh
bear "Well, let's see if we can find Benson first. If he's got dinner sorted then we won't need to do anything at all."
show lion weeb laugh
lion "If I see him, I'll let you know then!"
scene foyer with dissolve
"Once we'd all been fed, I took the platter back into the kitchen and wandered back into the foyer."
"Everyone else had wandered off for the time being, I didn't even pay attention as to where. Not that any of them had stuck around to see what I was up to, either."
show otter neutral with dissolve
mc "Well... Now what?"
mc "I guess I could... uh... Hrm..."
show otter pout
mc "Oh! ...No, wait..."
"I didn't notice Benson until he'd cleared his throat, just standing off to the side."
mc "Ah!"
show otter neutral
otter "Is everything alright?"
mc "Yeah! Everything's fine!"
if Library == True:
    mc "I even know where the library is!"
    if OzKnown == False:
        show otter smile
        otter "Very well done, Master [mcname]."
        mc "Yeah! Hoss is going to show me later."
        show otter neutral
        otter "Is he now?"
        mc "Mmhm!"
    else:
        otter "I'm glad."
        mc "Well... I still need to go there, but Hoss is showing me later."
        show otter pout
        otter "Oh really, now?"
        mc "Yeah!"
    "There were a few moments of silence before Benson spoke again, almost to the point where I was wondering if I was meant to say something else."
    show otter neutral
    otter "Shall I leave you to it then? You seem to have yourself sorted."
else:
    mc "Although..."
    show otter pout
    otter "Yes?"
    mc "Still no luck on finding where I'm meant to be going tonight."
    show otter neutral
    otter "This is... unfortunate."
    mc "No new clues for me?"
    otter "Regrettably, I'm unable. You shall have to question your friends on this one alone."
    mc "Oh... Alright."
    if OzKnown == False:
        show otter pout
        otter "Apologies, Master [mcname]."
        otter "I have faith you'll think of something."
        mc "Thanks, Benson."
    else:
        show otter smile
        otter "Don't fret. I'm sure you'll find a way."
        mc "I hope so..."
    show otter neutral
    otter "Shall I give you some space, Master [mcname]?"
mc "I... Yeah, okay. I think I know where to go from here."
show otter smile
otter "Then I am glad."
mc "Oh, but um... Benson?"
show otter neutral
otter "Yes?"
mc "Thanks."
show otter pout
otter "..."
show otter neutral
otter "Think nothing of it."
hide otter with dissolve
"I watched as Benson wandered off down the corridor back towards the kitchen, leaving me alone in the foyer."
if Library == True:
    "My next job was to go find Hoss and get him to show me the library."
    if lionroute == True:
        "I was worried though. My partner for the scavenger hunt knew this house better than... Well, anyone else here it seemed."
        "If he had been here before... what other secrets did he know? Was him knowing about the house meaning he was the one behind what's going on?"
        "I rubbed my head, frustrated. That couldn't be it, after all I'd seen him die. But what could it mean? Why would someone kill Hoss?"
        mc "Argh... This doesn't make any sense!"
    else:
        "I scrunched up my nose as I tried to think things over. Hoss knew about the library, so he'd either been here before, or had just found that room, right?"
        "But if he'd been here before... Did that mean he was behind the others dying?"
        "The thought sent a chill down my spine. The other option was that he was Oz, which meant he was trying to help, right?"
        mc "Why doesn't this... But it doesn't..."
    "Looking up from the foyer to the first story, I wondered where he was now. He said he'd show me, and there was no time like the present, right?"
    "I started to climb the stairs, figuring I should check his room to see if he was there."
    jump HossLibraryDiscovery
    #Already know about the library, skip to Hoss meeting
else:
    "I looked up the stairs to the first floor, frowning."
    scene conservatory with dissolve
    "I felt bad about confronting Roswell about his behavior yesterday when I was in the museum and wanted to go check in on him."
    mc "Roswell?"
    show boar sad with dissolve
    "He didn't look up from his book, but he looked troubled all the same, gesturing me closer."
    "I sat down next to him on the sofa, waiting for him to make the first move. With a sigh, he closed his book and looked off into the distance, looking wary."
    mc "Are you... okay?"
    boar "Yeah..."
    show boar pout
    boar "I owe you an apology. A proper one."
    mc "It's Tyson you owe an apology to."
    boar "Not that..."
    "Roswell breathed in deep, sighing it out again before looking at me proper."
    mc "Then... what for?"
    show boar sad
    boar "For assuming I could come back into your life as if nothing happened. Like I never left."
    "I gave Roswell a confused look and I found myself scratching my head."
    mc "You never left though. We couldn't hang out, but dad helped me send you letters, and occasionally send each other an email. Like... I just assumed..."
    "I scratched my head, sighing out."
    mc "I guess things changed a bit while you were gone... huh?"
    "We sat in silence for a few moments before Roswell spoke again."
    show boar neutral
    boar "Y'know... I think I'm going to miss school."
    mc "Really? Why?"
    boar "I'm good at school. I'm good at homework and academics. Being top of the class though? The attention was nice."
    mc "But uh... What about getting bullied?"
    boar "Well no, not going to miss that. If anything, that's something I'm... probably a little thankful for."
    show boar pout
    boar "That feels weird to say. Feeling grateful I was used to Tyson so I knew what to expect moving forward."
    "Roswell rubbed the bridge of his nose, grumbling."
    if boarroute == True:
        show boar sad
        boar "I'm sorry for kissing you, [mcname]. I shouldn't have done that."
    else:
        boar "I guess what I want to say is..."
    boar "The specific reason that I'm jealous? You look at Tyson with such adoration, and for Dean it's just... some awe filled expression I just can't place. When you look at Orlando you're so calm and cheery."
    mc "I don't..."
    "I shook my head, still confused. If anything it made me wonder how I looked at Roswell."
    boar "Putting my hate for Tyson aside... I don't understand why you look at him so. That's the sort of look I want to earn someday."
    mc "Well... Uh..."
    "I chuckled, nervous. The smile on my face crept there long before I was conscious of it."
    mc "I think... It's kinda like how you saw me as an older brother?"
    show boar scared
    boar "What...?"
    mc "Yeah! Like... How to put it..."
    mc "As I got older and understood more about what it means to do the right thing, I stood up for him once."
    show boar pout
    mc "Since then... I dunno, he looked out for me and it felt like I had an older brother?"
    if wolfroute == True:
        "I chuckled again, shifting uncomfortably. It was maybe a half lie. There was more than that, and it was becoming more apparent to me the longer we stayed here."
    else:
        "I smiled. Thinking back fondly."
    mc "It was nice, having someone else just around. Sure, it probably would've come across as him just taking advantage, but he did stuff too."
    show boar annoyed
    boar "You skirt around what, exactly, he's done a lot, you know."
    mc "I know..."
    "It was my turn to sigh out and my ears drooped slightly, ashamed."
    mc "Maybe... it wasn't the best of things, but his heart was in the right place? Or it was just... embarrassing stuff?"
    show boar pout
    mc "Like... He ditched school when I was sick just to keep me company. Or... he managed to get the test answers for something I was freaking out over, maybe he stole them, he never said."
    mc "But even outside of school, he'd check in and make sure I was okay. He'd take me places on the weekend and show me stuff that he thought was cool."
    mc "To be honest, he never really... asked for anything. He called the shots, but made sure I was cool with it in some way beforehand."
    boar "That doesn't sound like the bully I remember."
    mc "Because he's not anymore. Like I said before, he's like family now. I..."
    if wolfroute == True:
        "I had to stop myself from saying it. If I was going to make that sort of call, I wanted to be certain. Sure, admitting that you loved a brother was one thing but that very idea was tainted for me, and I didn't want to risk it."
    else:
        "I chuckled, nervous. I wasn't sure how best to really put it without sounding corny."
    mc "Y'know. I care."
    show boar sad
    boar "I see..."
    mc "What I think I'm getting at is that it's just time. Him being around made that happen, he's been good."
    mc "It's the same for Orlando, right? He and I have hung out so often over the years he's just been a consistent presence in my life."
    show boar pout
    boar "And Dean?"
    mc "Well... uh... Dean's handsome?"
    show boar grin
    boar "Oh, so that's how it is."
    mc "Wait, no. Uh... What I mean is I guess it's part that but I'm still trying to figure out the rules and expectations of how to date someone? I like his confidence at least, and Orlando seems to like pushing me towards him."
    if boarroute == True:
        boar "So I should ask Orlando for tips on how to romance?"
    else:
        show boar smile
        boar "I do admit, you being a lovestruck hyena never gets old, with how flustered you can get sometimes."
    "I chuckled, nervous, happy, and embarrassed all at the same time."
    boar "What about Sal? And Hoss?"
    mc "What do you mean? How I look at them, or?"
    show boar neutral
    boar "Right. Sal's... sorta the same? As Dean I mean. A look I can't quite place. And Hoss..."
    show boar pout
    boar "Well... He's hard to place too. It's a positive look, I think. Different but similar to the one you give me maybe?"
    if lionroute == True:
        mc "Well... Hoss is just hard to place. I called him out for being fake the other day, and..."
        show boar scared
        boar "Wait, literally? You {i}literally{/i} called him fake?"
        mc "I... oh... um..."
        show boar laugh
        boar "You didn't!"
        mc "He wanted me to be honest!"
    else:
        mc "Hoss gives me some odd vibes sometimes. Almost like he's... uh..."
        show boar neutral
        boar "Like...?"
        mc "Not completely honest? Not in a bad way, it's just weird."
        show boar smile
        boar "I think I understand that. He's... thrown me for a loop a few times. I like him though."
        mc "Oh, you 'like' him do you?"
        show boar laugh
        boar "Not like that! Well... I hadn't really considered it that way at least!"
    show boar neutral
    mc "I think I like Hoss, but just... I dunno. I feel like I'm missing something."
    mc "I don't think it's anything bad either, but... Hrm..."
    show boar smile
    boar "Why don't you ask him?"
    mc "Ask him what though?"
    boar "Maybe he might know about that secret room you're looking for. You never know."
    mc "That..."
    "I gave Roswell a look, frowning."
    mc "Have you... been here before, Roswell?"
    show boar neutral
    boar "What, in this room?"
    mc "No, I mean... The mansion itself."
    boar "Can't say I have. If I had, I'd have told you about it before, easily. Not just that, but I'd be able to give you more info on the mansion itself, too."
    mc "Hrm..."
    show boar smile
    boar "Like I told you. My parents organized this for me. All I said is that I wanted to go out with a bang with my friends, and asked if they had any ideas."
    mc "And they just...{w=0.5} Mansion?"
    boar "Mansion."
    show boar neutral
    boar "It wouldn't surprise me if some wealthy client owed one of my parents a favor, or there was something else in play like that."
    mc "I dunno..."
    show boar smile
    boar "Look, everyone has their secrets, [mcname]. Everyone."
    boar "For me, I like the ghosts of my past and the skeletons in my closet to stay right where they belong. Out of sight, out of mind."
    show boar neutral
    boar "They aren't important to anyone but me, anyway. But as far as your mission to find hidden rooms, I reckon Hoss might be the one to ask."
    mc "But why Hoss?"
    show boar pout
    boar "Well... It's probably a bit presumptuous but... He's always been pretty... How do I wanna say it?"
    mc "Conscious of his appearance? Over the top?"
    show boar smile
    boar "I was going to go with genre-savvy, but I suppose those aren't wrong either. If there's a hidden room, or a secret passage, Hoss would probably know where to look."
    mc "You're probably right..."
    show boar neutral
    boar "Wish I could be more helpful, but unless you're trying to commune with, or otherwise banish a ghost, I'm tapped."
    mc "It'd be worth asking. Thanks, Roswell."
    show boar smile
    boar "No, thank {i}you{/i}."
    boar "For checking in on me. I'll... try and get better, I feel like I should go talk to Tyson, maybe. I just need to figure out the best way to do it."
    mc "If I can help with that, let me know. He's uh... Well, I get it. I do."
    show boar neutral
    boar "So... See you at dinner?"
    mc "Yup! I'll let you know if I come up with anything with the search!"
    show boar smile
    boar "See ya later! Good luck."
    scene black with dissolve
    "I waved to Roswell and left him to his book. I still felt uneasy about a few things, but there wasn't anything I could do about them right now. Just had to stay focused on finding Oz."
    "That's what kept me going. Find Oz, ask questions, put myself at ease of what was happening to me."
    "Right now, my only lead was to ask Hoss. I could ask any of the others, but a suggestion of who to start with was better than picking at random."
    #don't know about library, go find Roswell

label HossLibraryDiscovery:
scene bedroom with dissolve
mc "Hoss?"
"I peeked into his room, covering my eyes just in the off-chance he was indecent."
show lion weeb laugh with dissolve
lion "What are you doing?"
mc "Are you decent?"
show lion weeb annoyed
lion "Nope, stark naked, [mcname]."
mc "Oh, uh..."
show lion weeb neutral
lion "I'm just messing with you. Come in."
"I shuffled into his room and closed the door behind me, eyeing Hoss carefully."
if Library == True:
    show lion weeb annoyed
    lion "What? Something on my face?"
    mc "No, no. Just... nervous? Curious?"
    lion "About... what?"
    mc "Well... You were going to show me the library, right?"
    show lion weeb neutral
    lion "...Ah."
    lion "Right."
    mc "You're not just pulling my leg, right? You can actually show me where it is?"
    show lion weeb laugh
    lion "Yeah, I can. Wanna go now?"
    mc "I'm free. But if you're busy..."
    lion "Not at all! Shall we?"
    #skip to library
else:
    show lion weeb grin
    lion "So! What brings you here, [mcname]?"
    mc "So... um... This is probably going to be a strange question..."
    if lionlove >= 12:
        show lion weeb aroused
        lion "Ah, was it about the kiss earlier?"
        mc "Oh... um..."
        "Hoss sauntered forward, clapping a hand on my shoulder with a laugh."
        show lion weeb laugh
        lion "You're cute. Not going to lie about that."
        "My cheeks went red again, and I found myself chuckling, half covering my face."
    else:
        show lion weeb smile
        lion "Oh? What's up?"
    mc "Um... You've been here before, right?"
    show lion weeb neutral
    lion "..."
    "I stared at Hoss, trying to read his expression. But it was hard to tell exactly what he thought of that."
    lion "To... the mansion?"
    mc "Well... yeah."
    show lion weeb smile
    lion "Now why would you be asking something like that?"
    "Benson said one of us had been here. Roswell said to ask Hoss given he was likely to know if there were hidden rooms."
    "And I realized he was avoiding the question."
    mc "Hoss, have you, or haven't you?"
    lion "Maybe."
    "My eyes narrowed on him before, by some fluke, I had an epiphany."
    mc "The library..."
    show lion weeb annoyed
    lion "What about the library?"
    mc "The library! When we first got here, you said there was a library that covered multiple floors! How did you know about that?"
    show lion weeb neutral
    lion "What, you haven't been there yet?"
    mc "Hoss, I have no idea where it is. Can you show me?"
    show lion weeb sad
    lion "Ah, well... Yeah, I guess I could. You've been there before so..."
    mc "No I haven't!"
    show lion weeb annoyed
    lion "With the suit of armor. You've been there."
    mc "Yeah, and that's not the library."
    mc "Benson said one of us had been here before. You seem to know of this room I can't find that I'm trying to. So..."
    show lion weeb pout
    lion "..."
    show lion weeb sad
    lion "Alright, you got me. Yeah, I know where it is."
    show lion weeb annoyed
    lion "You good for me to show you now?"
    mc "I'm ready but... Why would you lie about that?"
    show lion weeb neutral
    lion "When we get there, I'll fill you in. Promise."
    lion "Come on."
    #talk about library
scene conservatory with dissolve
"I followed Hoss out of his room and let him lead me to the conservatory."
mc "Um..."
"I looked around. There was no way this was the library, and Hoss seemed to be aware that I wasn't buying it."
show lion weeb neutral with dissolve
lion "So the library."
mc "The library. This isn't it."
lion "Nope. But we get there through here."
mc "What... do you mean?"
show lion weeb laugh
lion "Alright, well... Consider it this way. We're in a reading room, right?"
mc "Right... So... Books."
show lion weeb grin
lion "Exactly."
"Hoss wandered over to a bookcase against one of the walls, leaning against the wall beside it as he continued."
lion "And what better source for books than..."
mc "...A library..."
"Nodding in confirmation, Hoss pulled two books on the bookshelf forward and something clicked. I watched in awe as Hoss gently slid the bookshelf aside, revealing a corridor beyond."
if OzKnown == False:
    "I gulped, realizing why Benson had said to bring my flashlight with me. It was almost pitch black down there."
else:
    "It was dark, my eyes straining forward to make out anything further down. Despite not being complete darkness, it may as well have been."
mc "Why's it so dark down there?"
show lion weeb smile
lion "Lights don't work. But come on, I'll show you the library."
scene black with dissolve
"Hoss turned the light on his phone on, stepping into the corridor. With one last look at the conservatory, I followed."
lion "You doing alright? Stay close, don't want you tripping over anything."
"I shuffled closer and bumped directly into Hoss who had stopped suddenly. He reached back, feeling down my arm until he took hold of my hand before walking forward, holding his phone in front of him."
"The corridor must've been long, because we were walking for a bit before we stopped."
mc "Why'd we stop?"
lion "We're here. Ready?"
"I nodded in the darkness. Who knows if Hoss could actually see me or not but he proceeded forward anyway."
scene library with dissolve
"The room filled out before us, bookshelves filled to the brim in some cases and left completely bare in others. A lot of which I could only make out as Hoss scanned the room with his phone."
show lion weeb neutral
lion "Ta da. The library."
mc "Huh..."
"I stepped forward, looking around some more. We were standing on the higher of the two levels, with a rail stopping me from just falling down to the floor below."
mc "It's dark here, too. But why? There's no windows, either."
show lion weeb smile
lion "Nope. It's... uh... Well, a private library for sure."
mc "But... How is this here? How deep are we?"
lion "Still on the same level as the conservatory. Go down there and you'll be on the same level as the bedrooms."
"Hoss and I wandered forward carefully, as my eyes tried to adjust to the dark."
lion "Kinda cool, huh?"
mc "but there's no lights?"
lion "Only candles."
show lion weeb neutral
lion "See? Down there."
"Hoss pointed down to the lower floor, where a large desk sat with a few candles set up, unlit. The only way I could make them out in the dark was because they were bone white against the dark wood."
mc "Okay... So the conservatory is the only way in here?"
show lion weeb smile
lion "Far as I know."
mc "Huh... Alright..."
show lion weeb sad
lion "So... Why'd you want to come here?"
mc "Oh, I was just... looking for it."
show lion weeb annoyed
lion "But why though? Not all that much here. Only... well..."
"Hoss started to lead the way, descending a staircase and guiding me over to one of the walls. My heart sank as I realized what I was looking at."
scene vault with dissolve
play music dark fadein 2.0
mc "W-Wait..."
"Before us looked a very familiar looking door. Right down to the keypad sitting next to it."
mc "There's another one!?"
show lion weeb sad with dissolve
lion "Sure looks like it."
mc "This... This wasn't what I was expecting to find here."
show lion weeb annoyed
lion "What {i}were{/i} you looking to find here? Unless there's a book, there's nothing here, right?"
mc "I... Yeah, you're right."
show lion weeb neutral
mc "But... How did you find this room? How did you know about the books?"
show lion weeb scared
lion "I... uh..."
mc "Have you been here before?"
show lion weeb scared
lion "Okay, okay. Fine."
lion "This mansion? Yeah, I've been here before. I know it very well."
show lion weeb neutral
lion "After all. This was where I was supposed to make my first big break as an actor."
mc "Wait, really?"
lion "Yup. Didn't realize it until we pulled up, but this is the same place. Confirmed it when I tried the bookcase."
mc "Who... else knows about this? You having been here before, I mean."
lion "Honestly, it'd be hard to say. Benson would know, if only because he was around when we were setting up."
mc "What about... the owner?"
show lion weeb annoyed
lion "The owner of the mansion? Dunno. Never met him."
mc "Do you know his name at least?"
show lion weeb sad
lion "Nope. He was scarce when we were setting up the hidden microphones and cameras for stuff. Always just assumed he was off somewhere else given we had free rein to wander around."
lion "Only know it's a guy based on context clues."
mc "Damn... Okay..."
show lion weeb neutral
lion "So... Happy?"
mc "I guess so..."
stop music fadeout 5.0
"We stood in silence for a few moments before my gaze wandered over to the vault-like door on the wall."
lion "So what are you going to do? Keep this a secret?"
mc "I don't know why {i}you{/i} were keeping it a secret still. Especially after... Well..."
show lion weeb annoyed
lion "About Benson?"
if lionroute == True:
    show lion weeb sad
    lion "And...{w=0.5} about me?"
mc "Well... Yeah."
show lion weeb sad
lion "To be honest... It's a few different things. I left a lot of regrets here. Being here again both makes me pumped up as if I was getting another shot, but also sad that it never got to eventuate."
lion "So... places like this? They're private, at least for now. Places that only I, and I guess now you, can enjoy. Secrets, y'know?"
"I nodded slowly, understanding somewhat."
mc "I'm sorry, Hoss. I uh... At least I feel like I should be? I didn't know. I mean, you know I didn't know, it's just... ah..."
show lion weeb neutral
"I chuckled quietly, pulling my gaze to the floor. I leaned back on the desk, sighing out. At least I was ready for tonight it seemed."
scene library with dissolve
if lionroute == True:
    if lionlove >= 12:
        $ HossKiss = True
        show lion weeb aroused with dissolve
        "Hoss eased my chin up to look him in the eye, setting his phone down on the desk next to me."
        "That same hand slid up to cup my cheek, rubbing softly with his thumb. I gulped, my heart starting to race as he eased himself closer."
        mc "Hoss..."
        lion "Yeah?"
        mc "I... um..."
        lion "Can I... uh... share another secret with you?"
        scene hosskiss with dissolve
        "I nodded slowly as Hoss edged closer still. I could feel the heat of his breath on my nose as he got close, closing my eyes to brace for what I felt was about to happen."
        "He pressed his muzzle to mine, gently. Soft enough that despite expecting myself to flinch from the contact I just stood very still."
        "It felt... nice, and I brought one hand up to rest on his chest. He leaned in more, dipping me back and parting my mouth with his tongue."
        "Not in any crude or overly lusty way. Every motion he made was careful, delicate, almost as if he were savoring this moment. Before I could really do much else he pulled away just as slowly as he'd pressed in, sighing out softly."
        "I slowly opened my eyes again, looking at Hoss who seemed to be in daze."
        scene library
        show lion weeb sad
        with dissolve
        lion "That... uh..."
        mc "Yeah..."
        lion "So..."
        mc "Y-Yeah?"
        show lion weeb neutral
        lion "Yeah."
        "I blinked, not fully comprehending what had just happened between us. I liked it, sure, but in my addled state I wasn't too sure what it meant."
        mc "That was... some secret."
        show lion weeb sad
        "Hoss dipped in quickly, picking up his phone and tapping it against an open palm, thoughtful. Troubled about something from how his brow was furrowed."
    else:
        $ lionlove += 2
        show lion weeb sad
        "Hoss wandered over to the desk and sat on it next to me, looking around. I watched him as he did so, and witnessed him start to look at the ground with a troubled frown."
        mc "Are you okay?"
        lion "Yeah... I think so. Just..."
        "He gestured in the air dismissively around us, as if alluding to something."
        lion "Secrets, I guess."
        mc "Good ones?"
        lion "Depends. Could go either way."
        mc "Oh..."
        "We spent the next few moments in silence before he broke it again, his voice low."
        lion "It's just... hard."
    "I blinked, having missed something, looking at him with a level of concern."
    mc "I... Did you wanna talk about it? You look like you wanna talk about it. Whatever 'it' is."
    show lion weeb sad with dissolve
    lion "My parents."
    mc "Your... parents?"
    lion "Yeah. They don't know."
    "I blinked, eyes darting around quickly before settling back on Hoss."
    mc "They don't know about... uh..."
    if HossKiss == True:
        mc "Well they couldn't know about us... y'know. That just happened. No one else knows."
    else:
        "I scratched my head, not really sure what Hoss was getting at."
    lion "I told you yesterday morning, right? That I'm bi?"
    mc "Well... Yeah. I'm gay. Is... that a problem?"
    lion "Liking guys... Isn't exactly something that's considered a good role model for younger siblings."
    lion "At least I think so. Don't know what my parents would think either given how much mom wants grandkids and dad asks if I've found a girlfriend yet every time we talk."
    mc "O-Oh..."
    "Again, more silence as I let the sentiment sink in."
    lion "So... Secrets. The ones I can keep others from finding out about, or that might make them think less of me, or even the ones that just feel special to {i}me{/i}?"
    lion "I'd rather them stay secret."
    if HossKiss == True:
        "That put me in an awkward position given what had just transpired. He wanted to share a secret with me and then just... Well, kissed me. Was it the kiss that was the secret? The reason he kissed me the secret?"
        mc "So what... did you want me to do regarding... Well..."
    else:
        "I nodded slowly. I had a few secrets of my own, but nothing nearly as big as this. At least it felt bigger coming from Hoss than thinking about what secrets I held close to my chest."
        mc "Is there... Anything I can do?"
    show lion weeb cry
    "Hoss hiccupped, desperately wiping his face when I went to look at him next. I placed a hand on him, trying to reassure him in some way that things would be alright. The downside of which was all I had was a hope it'd turn out that way."
    show lion weeb sad
    lion "I'll be okay, just uh... Gimme a minute."
    "I watched him carefully as he just closed his eyes for a few seconds, breathing in deep before groaning into his hands. After that, he seemed recomposed, or enough to keep talking."
    lion "Ugh... Sorry."
    mc "It's... okay? I mean I don't really get it, but..."
    lion "Which part?"
    mc "Well... if you're bi, then... I don't understand the problem. You could still get a girlfriend. Or if you didn't, you could adopt."
    show lion weeb laugh
    "I didn't expect Hoss to chuckle at that, but it seemed it was enough to lift his spirits."
    show lion weeb neutral
    lion "I know. It's dumb. It's a little more complicated than that but..."
    "Hoss sighed out, gesturing dismissively again."
    mc "Oh! I know something that might help!"
    show lion weeb laugh
    lion "Alright. Lay it on me."
    mc "So um... Apparently it's common in hyenas? Or common enough that dad was ready to have... 'that talk'."
    show lion weeb annoyed
    lion "Uh..."
    mc "Y'know... that gay couples can adopt, and that they can still be good parents."
    show lion weeb scared
    lion "Oh!"
    show lion weeb laugh
    lion "I see."
    mc "So... um... I guess what I'm trying to say is that... It shouldn't matter?"
    show lion weeb smile
    lion "You're right. But it's uh... more complicated than that. I appreciate it though."
    "Hoss clapped me on the shoulder before bringing me in for a quick hug."
    show lion weeb neutral
    lion "Thanks, [mcname]."
    lion "But between you and me... Keep this uh... This whole thing a secret for me?"
else:
    show lion weeb smile with dissolve
    lion "Happy?"
    mc "I... think so..."
    show lion weeb neutral
    lion "Good!"
    show lion weeb sad
    lion "...{w=0.5} Good."
    mc "Hoss? Are you... okay?"
    "There were a few moments of silence before he sighed out, scratching himself through his mane."
    lion "Just... secrets. This whole thing... Can I share another one with you?"
    mc "Oh, um... Okay."
    lion "It's uh... part of the reason why I moved out here."
    lion "Admittedly... I'm bisexual, right?"
    mc "O-Oh! You like girls too? I just like guys."
    show lion weeb annoyed
    lion "Focus, [mcname]."
    mc "Oh, sorry. Go on."
    lion "Anyway..."
    show lion weeb sad
    lion "It's the liking guys part that's the problem. Parents are constantly asking me if I have a girlfriend, mom wants kids. But guys are just a little easier to get along with."
    mc "Well... I don't know what it's like for lions but... hyena girls are scary."
    mc "And I just prefer... Well..."
    "I pointed down, hoping Hoss would get the picture."
    lion "It's not about that, [mcname]. It's just... family stuff. Expectations."
    mc "What, to... have a family? Dad said that adopting was always an option. A family is a family no matter what."
    lion "Oh, [mcname]. If only."
    lion "There's... certain views about what a family should be that makes it hard. Me liking guys isn't setting a good example for my siblings for instance."
    "I shook a little, confused."
    mc "But that... doesn't make any sense. Why does that matter?"
    mc "Love is... love, isn't it?"
    show lion weeb laugh
    lion "It'd be nice if that was the case but... I don't know."
    show lion weeb sad
    "Hoss sighed out and came to stand next to me, leaning on the desk."
    lion "Just... The library, what I just told you... Can you keep it a secret for me? Just for a little while."
lion "Please?"
mc "Okay..."
lion "Only for a little while. We'll show the others soon, I just... Y'know."
mc "If you don't, I will. Especially because..."
"I pointed to the door he showed me, looking to Hoss to see him nod."
show lion weeb neutral
lion "And that's fair."
lion "If... Another thing happens like last night, then we'll show everyone right away, yeah?"
mc "I think that'd be best. Otherwise... What, a couple days? Tomorrow?"
show lion weeb sad
lion "Couple days."
lion "But uh... Give me a chance to get the courage together."
mc "Okay..."
show lion weeb neutral
lion "For now... Wanna get out of here? It's dark, probably dustier than it needs to be. Unless there's something else you need from here?"
mc "No, no. I think I'm good."
hide lion with dissolve
"Hoss moved to lead the way, making sure the light on his phone was on before making his way towards the stairs."
"I rushed to catch up to him, hesitating on my approach."
"I felt like I understood Hoss a little better, maybe understanding why he'd keep this under wraps."
if lionroute == True:
    "In the dark, my eyes glanced down to his spare hand, hanging by his side."
    menu:
        "Hold his hand":
            $ lionlove += 2
            "My hesitation caused Hoss to look back at me briefly with a curious smile, waiting for me to do whatever it was that I was waiting for."
            "Carefully, I reached out to his hand, brushing it and making him flinch away. Only briefly before his hand closed gently around mine."
            scene black with dissolve
            "Hoss squeezed my hand back, leading me out of the library."
        "Follow quietly":
            "I looked Hoss in the eye for all of a second before chuckling, nervous. A reaction he mimicked before he led me out of the library."
else:
    "Nodding to myself, I took the last few steps confidently, shooting Hoss a friendly smile."
    mc "Alright. Let's go!"
    scene black with dissolve
"Up the stairs and back through the dark corridor, Hoss guiding the way until we were back in the conservatory."
scene conservatory with dissolve
play music calm fadein 2.0
"I winced as my eyes adjusted to the light."
show lion weeb neutral with dissolve
lion "One last thing."
mc "Hm?"
"Hoss pulled the bookcase back into position, it locking into place with an accompanying click. He then pointed to the two books, tapping their spines."
lion "Pull these two to open it."
mc "And to close it I just move it back?"
show lion weeb smile
lion "That's it!"
show lion weeb scared
lion "Oh! But here's the important thing. If you're on the other side, and someone's closed it, you're stuck. No way to open it from the other side."
mc "So what happens if I get stuck?"
lion "Well..."
show lion weeb sad
lion "I guess if you go missing I'll come check here first? Otherwise maybe just have your phone on you to call for help."
mc "Does... this get used all that often?"
show lion weeb neutral
lion "Y'know, I'm not sure. I'd assume Benson would know about this too; whether he uses it or not... who knows?"
mc "Easy, I'll have my phone on me when I go to visit it."
show lion weeb smile
lion "There you go."
if lionroute == True:
    mc "So, uh... What happens now?"
    show lion weeb neutral
    lion "What do you mean?"
    mc "Did you... uh... Wanna do anything? Still got a while before dinner at least."
    show lion weeb laugh
    lion "Have any ideas in mind? Anime?"
    mc "Y'know... I'd be happy with anime, or if you wanted to go hang by the pool. I'm easy."
    lion "Well, how about we go find something to watch. I'll even let you pick."
    mc "Really?"
    show lion weeb neutral
    lion "Doesn't even need to be anime. But if you're not sure I could always...?"
    mc "No, no! I got it! Let's go!"
    scene black with dissolve
    "Hoss and I spent the rest of the afternoon watching anime. Something about alien clothing? I enjoyed how flashy it was and Hoss seemed to have a smile plastered on his face. Even to the point where I caught him stealing glances at me throughout the episodes."
    jump Day8Dinner
    #Do some Hoss things
else:
    show lion weeb neutral
    lion "Now, was there anything else you needed today, [mcname]?"
    mc "Uh..."
    show lion weeb annoyed
    lion "What, so now that I've showed you my secrets, you're done?"
    mc "No! Well yes, but... um..."
    show lion weeb neutral
    lion "But what?"
    mc "I kinda... Did you need a hug? I kinda wanna give you a hug."
    show lion weeb scared
    lion "What?"
    mc "Because of... before. I feel like I shouldn't have pried."
    mc "And not only that but you uh... With your family?"
    show lion weeb sad
    "Without a word, Hoss stepped forward and hugged me tight, pinning my arms to my sides."
    mc "O-Oh..."
    "As best as I could I hugged him back, catching a whiff of something strong and tropical smelling in Hoss's fur. It reminded me of the beach."
    mc "Is there... anything else I can do to help?"
    show lion weeb neutral
    lion "Nah, it's alright. I'll just go chill out for a bit. Maybe take a cat nap."
    "Hoss let me go and wandered over to the door leading out."
    lion "See you at dinner?"
    mc "Oh, okay..."
    hide lion with dissolve
    "He was gone before I could even wave. Looking out the window I saw that there were still some hours of sunlight left. Hours that I had to fill waiting until it was time to meet Oz."
scene foyer with dissolve
"I made my way back to the staircase, sitting at the top of the stairs and looking down at the foyer."
mc "What a day..."
if bearroute == True:
    "I ran my hand through my fur, feeling tired. Tired enough that I considered taking a nap. Which in turn made me remember that Dean was likely taking one now."
    "Dean had walked in on me sleeping and joined me, plus if I was going to be up late tonight it'd make sense I had a nap so I wasn't falling asleep, right?"
    scene bedroom with dissolve
    "Convincing myself on the way to Dean's room, I opened the door slowly, peeking in to find him sprawled out on the bed asleep in just his underwear."
    "He'd walked into my room already undressed, and there was no way I was going to get into bed with him fully clothed. Not with how damp I'd likely end up in case I drifted off and he drooled all over me."
    "Off came my shirt and I stretched, wandering closer to the bed. Dean's clothes were dumped in the middle of the floor, seemingly strewn about. I didn't realize he had so many of the same plaid shirt."
    "As I tried to take my pants off..."
    show bear underwear scared
    bear "What? Who?"
    "I turned to look at Dean and he had woken up, still in a daze trying to make out who I was. His curtains were drawn so the room was darker than normal, but he sighed out."
    show bear underwear pout
    bear "Oh, it's just you [mcname]. Almost gave me a heart attack. Everything alright?"
    mc "Oh, yeah, I just thought um..."
    show bear underwear smile
    bear "That you'd join me?"
    mc "Y-Yeah... Is that alright?"
    show bear underwear laugh
    bear "Of course! Although I don't know how much sleeping we'll be doing."
    show bear underwear aroused
    bear "Y'know, given you're undressing."
    mc "Hey, you've seen what I wear to bed! You've even felt it!"
    show bear underwear laugh
    "I placed a hand on his face and pushed him back onto the bed, chuckling."
    mc "Do you want a cuddle partner and a nap or should I put my clothes back on?"
    show bear underwear smile
    bear "Nah, you're perfect. Come join me and we can get a couple hours in before I have to get dinner sorted."
    "Dean shuffled aside, making sure I had enough space to lay down. He stayed on his side, head propped up an elbow as I mirrored him."
    bear "So... Good day so far?"
    mc "It's been good. How's your nap been?"
    show bear underwear laugh
    bear "Fine until you woke me."
    mc "Ugh... Sorry about that..."
    bear "It's fine!"
    show bear underwear grin
    bear "But how are you going to make it up to me?"
    "Dean placed a hand under my chin, scratching gently before moving that hand over to my neck and letting it rest there just above my shoulder."
    mc "I dunno... Maybe... Well..."
    "I placed my hands on his chest, rubbing and scratching gently. They dipped lower still, down his belly towards the waistband of his underwear."
    show bear underwear aroused
    bear "Yeah...?"
    "I leaned forward and snapped the waistband of his underwear back, holding his gaze. I threw caution to the wind after a moment of hesitation and felt him up through the fabric."
    "Dean breathed in suddenly, rumbling in his chest right up until I pulled my hand away."
    mc "I think that's enough for now."
    show bear underwear scared
    bear "Wait, what? But..."
    mc "{i}That's{/i} payback for yesterday."
    show bear underwear pout
    mc "But I guess I could let you cuddle me and get a kiss."
    bear "Awww..."
    show bear underwear neutral
    bear "I guess I had that one coming."
    "I planted a quick kiss on his nose before settling in."
    mc "Tomorrow night though, maybe... uh..."
    show bear underwear aroused
    bear "Oh?"
    mc "Maybe. I dunno. Maybe start with being naked and... I dunno?"
    show bear underwear neutral
    bear "Works for me. You set the pace and we'll go from there, alright?"
    mc "Okay..."
    show bear underwear laugh
    bear "Come on, get comfy and let's get a nap in before dinner."
    scene black with dissolve
    "It didn't take long for Dean to get to sleep, and after listening to him for a while I drifted off too."
    "The next thing I know, Dean's phone was going off, some alarm that he'd set so he didn't sleep too far into the afternoon. We both got up and got dressed to head downstairs for dinner."
    jump Day8Dinner
if dragonroute == True:
    "My eyes were drawn to the corridor leading off to the side. Down there was the staircase leading into the basement."
    "I wasn't thinking about working out, but the vault. Why was there another door like it in the library? Did the two connect as a secret passage like the bookcase?"
    scene basement with dissolve
    "My curiosity was drawing me down into the basement before I was conscious I'd made the decision."
    "The lights were on though, so I knew I wasn't alone."
    scene vault with dissolve
    show dragon neutral with dissolve
    dragon "Hey, [mcname]."
    mc "Orlando? What are you doing down here?"
    show dragon sad
    dragon "Just thinking. I figured no one else would be down here, so good place to think things over?"
    mc "Kinda creepy place to think things over, don't you think? After everything that's happened?"
    dragon "I know..."
    mc "Orlando, are you alright? Really?"
    show dragon pout
    dragon "Mostly. I've been thinking about yesterday a bit, it was... a big day."
    mc "No kidding..."
    show dragon sad
    dragon "If you could have a do-over... Would you take it? I'm... uh..."
    "Orlando gestured over his shoulder to the door behind him, my eyes followed."
    dragon "Been wondering if there was a way this thing could do it. Maybe it's a time machine?"
    mc "I don't know... It could be, but..."
    "I wandered around Orlando and poised to put something into the keypad, thinking."
    mc "We can't... change the past, can we?"
    dragon "Afraid not, [mcname]."
    mc "Then why ask for a do-over?"
    show dragon pout
    dragon "Because... I wouldn't mind if I could do yesterday over. Make different decisions, maybe say different things."
    mc "Is that... how that works? Wouldn't there be two of you?"
    show dragon scared
    dragon "If I went back in time? Wouldn't it be just... the day resets and I'm the only one that remembers?"
    mc "That feels like it'd be cheating though. Why do you get to remember and no one else does?"
    show dragon annoyed
    dragon "Well gee, thanks [mcname]."
    mc "It just... I dunno, feels like that sorta thing could be used for evil if it was a thing that existed."
    show dragon sad
    dragon "You're right... Maybe... I could just get lucky that it'd go down differently?"
    mc "Can always hope I guess?"
    "I looked back to the vault door, thinking back to the library with a frown."
    mc "Orlando?"
    show dragon scared
    dragon "What?"
    mc "This door... Do you think there's anything behind it?"
    show dragon neutral
    dragon "There's gotta be, right? It's a vault."
    mc "I mean... What about it just being a corridor somewhere?"
    show dragon annoyed
    dragon "Chances are it'd just be a room, right? Why else would you call it... Well, y'know."
    mc "I guess, but... I dunno..."
    mc "What if it was like... a bomb shelter, or... something like that?"
    dragon "That'd still just be a room though."
    mc "Uh... Fair point."
    show dragon neutral
    dragon "I guess I just have to uh... take it in my stride, right?"
    show dragon sad
    dragon "Listen... Do you wanna go hang out until dinner?"
    show wolf neutral at left with dissolve
    wolf "The fuck are you two doing in here?"
    show dragon scared
    mc "Oh! Hello, Ty."
    show wolf pout
    wolf "Yeah, hey. You two being dorks in here or what?"
    dragon "Uh... Something like that."
    show wolf neutral
    wolf "I'm gonna work out. Was just wondering who else was down here."
    show wolf pout
    wolf "Orlando. You look like you need a stiff drink, or a nap. Sort your shit out, man."
    mc "Hey, Ty, be nice."
    show wolf neutral
    wolf "I'm just saying it like it is, pup. Take care of him, yeah?"
    hide wolf with dissolve
    mc "Hrm..."
    show dragon sad
    dragon "Uh... What just happened?"
    mc "Tyson is going to go work out?"
    show dragon annoyed
    dragon "Not that, just... Y'know what, never mind. Let's go veg until dinner."
    show dragon smile
    dragon "Wanna go lay on the grass and watch the clouds?"
    mc "Sure! Weather is nice enough for it!"
    scene black with dissolve
    "With as big as the backyard was, it wasn't hard to find a nice grassy spot to just lay down and watch the clouds rolling on by. At some point I must've fallen asleep, as Orlando was gently waking me for dinner."
    jump Day8Dinner
"I thought about what to do for the rest of the afternoon. I was tired but not tired enough to go take a nap, so maybe I just needed some sun."
scene mansionback with dissolve
"Wandering outside, I figured I'd splash around in the water for a little bit. Not a full swim, but just enough to keep me going until dinner."
scene pool with dissolve
show wolf pout at right with dissolve
show croc swim pout at left with dissolve
"I entered the pool and looked around, seeing Sal and Tyson talking to one another about something."
wolf "Okay, fine, I get it."
croc "Are you sure you do? I can run through it again if you need it."
show wolf annoyed
wolf "I said I get it! You can lay off it already!"
show croc swim annoyed
croc "Okay! I heard you!"
show croc swim sad
croc "Still..."
mc "Uh... should I... leave you two alone or?"
show croc swim scared
show wolf scared
wolf "Shit, pup. How long have you been here?"
mc "Not long! But uh... You were talking about something?"
show croc swim pout
croc "...Nothing important."
show wolf neutral
wolf "Yeah. Just... having a chat."
if wolfroute == True:
    wolf "I'm about to leave though. You going for a swim?"
    mc "Oh, I was just wandering around. Maybe splash around my feet or something..."
    show croc swim neutral
    croc "..."
    show wolf pout
    wolf "..."
    "I looked between Sal and Ty, wondering what was going on. It was almost as if Sal was waiting for something to happen, and Tyson wasn't doing it."
    mc "Um... Or maybe something else...?"
    croc "You can stay if you want. I wouldn't mind talking if Tyson doesn't need you."
    show wolf sad
    wolf "Well..."
    show wolf neutral
    wolf "Come walk with me instead."
    mc "Oh, uh... I guess I could do that."
    show wolf pout
    wolf "Well, come on, then."
    scene woods2 with dissolve
    "Tyson led the way, heading away from the back door to the mansion in favor of heading off to the side of the house, towards the treeline of the forest and stopping short of a tree, turning to face me."
    show wolf neutral with dissolve
    mc "Ty?"
    wolf "What?"
    mc "Uh... What were you talking to Sal about? Was it... y'know."
    show wolf sad
    wolf "Yeah. It was."
    show wolf annoyed
    wolf "Bastard tore into me something fierce."
    mc "But... Was it the truth though?"
    show wolf yell
    wolf "Of course it fuckin' was! It sucked!"
    mc "I'm sorry, Ty."
    wolf "You know the worst of it though, pup?"
    mc "Uh... No? But-"
    wolf "He offered to hang out more!"
    "I let the comment hang in the air, confused at what Tyson had just said."
    mc "But that's... good, right?"
    show wolf sad
    wolf "Yeah, I guess... Just... Fuck."
    "Ty began to pace and I just watched, at a loss of what to say or do. I almost jumped when he slammed his fist against the tree nearby, recoiling and shaking his fist soon after."
    show wolf annoyed
    wolf "And then that stuff he said about you and just..."
    mc "What... did he say about me?"
    show wolf scared
    wolf "Oh, uh..."
    show wolf neutral
    wolf "Nothing. Don't worry about it."
    "I closed the distance between us and threw myself at him, wrapping my arms around his chest."
    show wolf scared
    mc "Come on, Ty. Tell me?"
    show wolf pout
    wolf "Fine. Fine!"
    "He didn't hug me back, but he didn't push me away either."
    wolf "Asked if what happened with him and Orlando helped you and me any. Wondered if either of us had confessed soon after."
    mc "Confessed, like..."
    wolf "Love, [mcname]. Come on, keep up."
    mc "Sorry, uh... That doesn't seem so bad."
    show wolf annoyed
    wolf "It pissed me off a little. Maybe Roswell yesterday made him ask about it, I don't know."
    show wolf sad
    wolf "Just wish they'd leave you out of it."
    mc "Ty?"
    wolf "What?"
    mc "I've got your back."
    show wolf aroused
    wolf "Fuck off."
    mc "I really do!"
    wolf "Yeah, I know pup."
    show wolf grin
    wolf "And I fuckin' have yours."
    "It was then that he hugged me back. Giving me a slight squeeze. I stole a look around us, frowning. It was always when we were alone, always when others couldn't see."
    show wolf neutral
    wolf "What's wrong?"
    mc "Just... Moments like this. We do this often, right?"
    show wolf pout
    wolf "Often enough I guess?"
    mc "No one else is ever around."
    wolf "And?"
    mc "Well... if the others knew and could see, then maybe..."
    show wolf sad
    wolf "Yeah, I dunno about that, pup. Like the idea of having you to myself, at least until you find yourself a decent guy."
    "I blushed, chuckling softly to myself."
    show wolf pout
    wolf "But you think it'd help?"
    mc "I do! And for what it's worth you're a decent guy."
    show wolf grin
    wolf "Yeah well imagine how Dean's gonna react seeing you get all comfy with me instead of him."
    "I laughed openly and the pair of us separated. Tyson seemingly in a happier mood after a good hug."
    show wolf smile
    wolf "So what now? You doing anything?"
    mc "Not really. I was just going to wait around until dinner. What about you?"
    show wolf pout
    wolf "Was going to go do some weights after that conversation. But uh..."
    mc "But what?"
    wolf "Wanna just go chill and listen to music instead? Don't feel tired and uh... Not much else to do with just the two of us."
    mc "If you wanna go work out I can come keep you company. Doesn't bother me any."
    show wolf smile
    wolf "Alright. I'll go blow off some steam and then we can go chill."
    scene black with dissolve
    "After Ty lay into the punching bag for a bit, we went back to his room so he could have a shower. I ended up falling asleep on his bed, with him waking me up when it was time for dinner."
    jump Day8Dinner
if crocroute == True:
    show wolf pout
    wolf "I'm gonna head out. You two have fun, yeah?"
    mc "Oh... Alright."
    hide wolf with dissolve
    "I waved as Tyson left, turning back to Sal who was standing by the pool. Compared to Tyson he was still damp, so he must've been the only one swimming as if his speedo wasn't enough of a give away."
    mc "So... What were you and Tyson talking about?"
    show croc swim neutral
    croc "Nothing important. Just guy stuff."
    mc "You? Talking about guy stuff?"
    show croc swim pout
    croc "After yesterday. I needed to get stuff off my chest."
    mc "O-Oh... Right. Did you get what you needed to from Tyson? As far as someone listening."
    croc "He's... got an interesting take on things. Mind if I talk to you about it for a bit?"
    mc "Oh, uh... Sure. Should I sit, or...?"
    show croc swim smile
    croc "Sure, I'll jump back in the pool though. I won't get you wet."
    "I pulled my shoes off and dipped my feet into the water. Good thing I was wearing shorts today."
    mc "So... Stuff with Orlando I'm guessing?"
    show croc swim neutral
    croc "That's right."
    "Sal got into the pool and idly floated in place."
    mc "Anything in particular... you want to start with?"
    show croc swim pout
    croc "Well... Let's see..."
    croc "As far as what Tyson was helpful for... That part is covered."
    mc "And that was...?"
    show croc swim neutral
    croc "Not important."
    show croc swim pout
    croc "What's your take on... Orlando's state of mind? How do you think he's feeling?"
    mc "Oh... uh... Orlando's very... emotional? I think I'd say emotional?"
    mc "He's very passionate, that's for sure."
    show croc swim sad
    croc "That's what I thought too."
    croc "Do you think... he hates me?"
    mc "What? No! Of course not."
    show croc swim pout
    croc "You're sure?"
    mc "Absolutely. There's no way Orlando would hate you over something like that. Uh... sure, he's probably still hurting but he bounces back pretty quick."
    croc "I wasn't sure if he was just being nice, or putting on a brave face."
    mc "Well... I don't know what you two talked about. But uh..."
    show croc swim sad
    croc "Well..."
    croc "Love, really."
    croc "And... just..."
    show croc swim cry
    croc "And I..."
    mc "Sal? Are you okay? You're shaking!"
    "Sal scrambled to the side of the pool, hanging off the side to rest on his elbows, hands clutching his head. I scrambled over on all fours, placing a hand on his arm."
    mc "Sal...?"
    show croc swim scared
    croc "[mcname]...?"
    "I watched as Sal looked back at the ripples on the surface of the pool, silent."
    croc "I need to get out of the pool."
    "He scrambled out, no sense of grace in how he hauled his frame out to just lay on the ground beside the pool."
    mc "H-Hey... What happened? Are you okay?"
    croc "I..."
    show croc swim sad
    croc "I'm okay. Promise. I'll be alright."
    mc "Does that happen often? The... Whatever that was?"
    croc "This is why... I might need some help teaching Orlando to swim."
    mc "Oh! Hydrophobia, right?"
    croc "Right, but... It doesn't happen often. I feel with Orlando it... just might."
    croc "...Tomorrow."
    mc "You're going to teach him tomorrow?"
    croc "No, no. I'll tell you tomorrow. Everything. I need your help."
    mc "Alright... Sure, whatever you need."
    if croclove >= 8:
        "I caught Sal's gaze for the briefest of moments before he looked away, mumbling something."
    else:
        croc "Thanks..."
    croc "We should... We should head inside."
    show croc swim neutral
    croc "I'll be alright. I just need a decent shower and I'll be in a better headspace. Then dinner, then... a good night's rest."
    mc "Did... You need some company? Like last night, I mean."
    show croc swim pout
    croc "I'll be fine, but... thanks for the offer."
    "Sal retrieved a towel draped over one of the deck chairs and dried himself, keeping his gaze elsewhere. I tried my best to shake my legs dry and picked up my shoes, figuring that I'd dry out properly before putting them back on."
    mc "Did... You wanna hang out for a bit before dinner or did you want your space?"
    show croc swim neutral
    croc "I need some space, so... No, thank you."
    hide croc with dissolve
    "Sal wandered off, shoulders slumped and head hung low. I felt bad, but at least I'd know the answer tomorrow."
    scene black with dissolve
    "I shook my feet dry a little more before hurrying after him, figuring I may as well hang around in my room until it was time for dinner."
    scene black with dissolve
    "Despite Sal being hunched over, he moved quickly, disappearing inside long before I'd reached the back door."
    "I wanted to help but if he needed space then I'd give it to him. I'd never seen him freak out like that though, someone so large suddenly seeming so small... was scary."
    "I spent the rest of my afternoon on my phone in my room; thinking of ways I could help."
    jump Day8Dinner
else:
    "I looked between the two of them with a frown."
    mc "Just... a chat. huh."
    show wolf pout
    wolf "Yeah. A chat."
    show croc swim pout
    croc "It really wasn't anything important. The conversation was over."
    show wolf neutral
    wolf "I'm gonna bail and do some weights. Wanna come with, pup?"
    mc "No, I'm good I think."
    show wolf pout
    wolf "Oh. Well... Alright, I guess. Catch you at dinner."
    hide wolf with dissolve
    "I looked to Sal, who seemed to be watching Tyson leave with a slight frown. When Ty was out of sight, he looked back to me carefully."
    croc "So..."
    mc "Yes...?"
    show croc swim neutral
    croc "You and Tyson."
    mc "Uh..."
    mc "What about me and Ty?"
    show croc swim pout
    "Sal scratched his cheek briefly before shaking his head."
    croc "Don't worry about it. I'm imagining things."
    mc "Imagining... What?"
    show croc swim neutral
    croc "If I didn't know better, you two were close. Very close."
    mc "Well we are, but-"
    show croc swim annoyed
    croc "{i}Really{/i} close."
    mc "He's just... Ty. Right?"
    show croc swim neutral
    croc "If you say so."
    hide croc with dissolve
    "With a shrug, Sal slipped back into the water and begun to swim around, leaving me to my devices."
    "I came out for some sun and figured that I may as well sit back on one of the pool chairs and maybe have a nap."
    scene black with dissolve
    "I closed my eyes and let my mind wander."
    "Tonight. Tonight was going to make everything make sense again. I just had to talk to Oz."
    "It was almost becoming like a mantra, a grounding statement to keep me on task. That said, with how tired I was, and the warmth of the sun above, I was quickly succumbing to sleep."
    "I'd been tired a lot lately. More tired than maybe I should be even with coffee. Was I not drinking enough? Was I drinking too much?"
    "The next thing I know, Sal's gently shaking me to bring me inside for dinner. He'd apparently already showered and changed back into his clothes, and was walked inside together."
    jump Day8Dinner

label Day8Dinner:
    scene diningroom with dissolve
    "I entered the dining room for dinner in a daze. My mind was going a mile a minute."
    if bearroute == True:
        "I remember Dean wandered over at some point and sat a plate of pasta in front of me, kissing me on the cheek, but I didn't respond. Maybe he was just worried."
    else:
        "Roswell wandered over and put a plate of pasta in front of me, much like he was with the others."
    "I thought I was hungry, but as it got closer to the meeting with Oz, I found I had less and less of an appetite. I ate half and spent the rest of dinner playing with what was left with my fork."
    show bear scared at left with dissolve
    show boar sad at right with dissolve
    bear "[mcname]? You alright?"
    mc "Huh?"
    boar "You've been spacey all dinner. This isn't..."
    show boar pout
    boar "Well okay, maybe it's a little on-brand for you, but not this much."
    mc "I'm fine. Maybe just tired."
    "I scrunched my nose up, wiping my face."
    show bear mad
    bear "I feel like it's more than just tiredness."
    if bearroute == True:
        bear "After all, I was there when you had a nap."
    else:
        bear "You're not bottling something up again, are you?"
    mc "No, no. Just... I guess yesterday is still weighing on my mind. I'll be alright."
    "I looked to Roswell and flashed him a smile, doing the same to Dean. They looked at one another before shooting me a concerned look."
    boar "Well, if you're sure... If you need to talk though."
    show bear smile
    bear "Feel free to grab either of us. Alright?"
    hide bear with dissolve
    hide boar with dissolve
    "I nodded to them and they backed off, saying something to one another only once they were close enough to the kitchen that I couldn't hear them."
    stop music fadeout 2.0
    scene black with dissolve
    "When all was said and done, I headed back to my room."
    "I showered, changed into a fresh set of clothes, almost as if I was dressing to impress. I was nervous. Was this what going on a date was like?"
    "My phone was in my hand constantly, checking if it was time to head on out."
    "In the back of my mind, I wondered if this was a mistake after all. Was I just about to go marching to my death? Should I back out?"
    "As I lay on my bed, waiting, all I could think of was if I'd survive the night and see my friends again in the morning. Not just my friends but also... well..."
    "I sighed out a shuddered breath, wiping the corners of my eyes. I had to steel myself. I could do this."
    jump Day8Oz
label Day8Oz:
"And then it was time."
$ renpy.pause (1.0)
play music vault fadein 2.0
"Carefully, I left my room, checking if the coast was clear."
if OzKnown == False:
    "I had my flashlight in my hand, primed with new batteries thanks to Benson. Not only that, but seeing the state of the library myself told me that I was going to need it."
else:
    "I figured I should bring my flashlight. I wasn't sure if... Well, the batteries were still good. I should've asked Benson for some new ones."
    "With how dark the library was, especially at night, I was going to need more than just my phone's torch mode."
scene conservatory with dissolve
"Slipping into the conservatory, I took another look around. No one else was here, no one was wandering around, I was free to continue on undisturbed."
"Looking at the bookcase I remembered Hoss's warning from before, patting my pocket to make sure I had my phone. There was no telling what could happen, so I wanted to be prepared."
mc "Okay, [mcname]. You can do this. Time to meet Oz."
"The two books I needed to pull to open the passage looked a lot more obvious now that I knew which ones they were. Once I'd pulled them, I heard the click and gently pushed the bookcase aside."
"It was heavy, and moved aside slowly, but I pushed it just enough to clear the gap and enter the dark corridor."
scene black with dissolve
stop music fadeout 2.0
"I stood there in the dark for a couple moments, bracing myself. It was a heavy darkness, different from the one I was used to, but it felt similar all the same."
"Turning on my flashlight I wandered forward, keeping it trained low in case there was anything on the ground I could potentially trip on."
scene library with dissolve
play music dark fadein 2.0
"As I entered the library, I looked down to the lower floor. The candles on the desk were lit, signaling that someone else had been here recently, if they weren't still here."
"Down the stairs, I wandered over to the desk, keeping my eyes peeled for anyone lingering just out of sight. If I was going to get jumped, I realized that I was thoroughly unprepared to fend off an attack."
mc "H-Hello?"
"I flicked the beam of my flashlight around, trying to catch a glimpse of literally anyone else."
"As the light landed on the vault-like door, I froze, watching as it opened with a low metallic creak. My throat was suddenly dry, making me gulp."
"There was a pit in my stomach growing now, a lingering dread or a worry that something was about to go wrong. Roswell's joke from days ago echoing through my mind again."
mc "Oz? Is that you?"
"A darkness lingered on the other side of the door, to the point where I wondered if my flashlight was broken. I edged forward, legs shaking, reaching towards the threshold of the door before a shadow moved, making me squeak and drop my flashlight."
scene black
mc "Oh no, oh no oh no... Please don't kill me!"
$ oz = Character ("???", what_color="#2bb8e1", who_color="#aa1f13")
oz "[mcname]."
"I almost shrieked, keeping my eyes closed and arms up to protect my head and face. I heard something shuffling around near me before I felt the butt of my flashlight nudge me."
oz "Take your flashlight, boy."
scene library with dissolve
"I carefully opened my eyes, taking the flashlight back and lifting it to illuminate who was speaking to me."
show oz neutral with dissolve
oz "..."
mc "Um..."
show oz pout
oz "Have a seat. I'm sure you have some questions."
mc "Are you... um..."
show oz neutral
oz "Very well."
oz "Allow me to introduce myself."
oz "My name, is Oswin Hammond. Youngest of the three Hammond siblings, but you may know me as Oz."
$ oz = Character ("Oswin", what_color="#2bb8e1", who_color="#aa1f13")
"I searched the older boar's face, curious, questions running through my head. Oswin wandered over to the side of the desk closest to the candles, sitting down."
mc "Oh, um... Nice to meet you. I'm-"
show oz smile
oz "I know, [mcname]. Sit down."
"I sat in the chair opposite him, eyes flicking across to the handles before looking him in the eye."
show oz neutral
oz "I'm sure you have many questions. Most of which I'll answer for you soon. I'll get the obvious ones out of the way first."
mc "Um... Okay."
oz "After that, you can ask me whatever you like freely. But I'll tell you now that I'm not going to waste my time answering inane questions that are irrelevant to what's going on. Understood?"
mc "Yes, sir."
show oz pout
oz "Furthermore, it behooves me to tell you the truth where I can, but understand that I too have my secrets. Seem fair?"
show oz neutral
mc "But what if you're the bad guy?"
oz "What do you mean?"
mc "Well... If you don't tell me everything, then who's to say you aren't just... y'know. Making me trust you just so you can kill me later."
"The question hung in the air for a moment, Oswin's gaze focused on me."
show oz annoyed
oz "Boy, if I wanted you dead, you'd have been disposed of a long time ago. There's less sense in warning you of dangers and alike if I, myself, am the one behind the death of your friends."
mc "I... guess that makes sense..."
show oz pout
oz "Now... Where to begin..."
mc "Sorry, but can I ask something real quick?"
show oz neutral
oz "What is it?"
mc "Why... are you wearing a lab coat? Are you a doctor?"
oz "I was, once upon a time. Not any more."
mc "What happened?"
oz "That in of itself is a long story. As much as I love stories, that one isn't like one of the child-friendly ones I'm so fond of."
mc "Oh..."
show oz pout
oz "My area of expertise and specialty was pharmaceuticals and drug development. Testing. In other words I developed vaccines."
mc "That sounds... good? Why'd you give it up?"
oz "My license was revoked when a test went bad. Of one hundred subjects, ninety-nine died."
"I tensed up, not wanting to ask what I was thinking. Sadly, Oswin seemed to know exactly where my head was and I paled when he told me."
oz "It's ridiculously small for a proper clinical trial, but for what we were testing, it was hardly legal."
show oz neutral
oz "Because of my arrogance, I am responsible for all ninety-nine of those deaths. All children, too."
mc "U-Um..."
oz "Don't worry about it, [mcname]."
mc "What... was the medicine you were testing?"
show oz pout
oz "A cure-all vaccine. A miracle elixir for everything and anything. Cancer, organ failure, HIV, you name it. Probably some of my best work."
mc "But..."
"Oswin's gaze narrowed on me slightly, making me go quiet before I could continue."
oz "But it didn't work."
oz "I botched my calculations along the way and created something quite fatal instead."
mc "So... If you were a doctor... What do you do now?"
show oz neutral
oz "Nothing. Shy of enjoying children's stories and reading up on mycology, I live comfortably doing whatever I feel like, which admittedly is very little."
mc "But... why do you still wear the coat then? Do you still do experiments and stuff?"
"That seemed to hit a nerve, with Oswin's gaze narrowing slightly."
oz "Funnily enough, yes. I do. My lab is still in the house, hidden away given what's in there. Chemicals and poisons that are kept securely away from easy access. Not to mention some samples of diseases and bacteria for development purposes."
"I shifted uneasily in my chair. The boar opposite me had poisons and chemicals just around?"
if bearroute == True:
    "The vision I had of Dean flashed to the front of my head. Poisoned. Was what killed him something  that came from Oswin's lab?"
else:
    "The prospect of having poisons around was scary. Or even having diseases on hand just ready to go. If he was telling the truth, he could infect us with something really nasty if he really wanted to."
show oz pout
oz "We're getting off track."
mc "I... Okay. Sorry."
oz "Let's discuss the vault itself."
show oz neutral
oz "The three of us made it. My older brother, may he rest in peace, myself, and my older sister."
mc "But what... is it?"
show oz pout
oz "It is what it's name suggests. A storing place. Although truthfully it's closer to... a containment unit."
mc "So there's something inside? What's in there? Benson apparently is giving us the code to open it if we found all the medals."
show oz laugh
oz "Ah yes. Father's old collection of medals."
show oz pout
oz "I'm not at liberty to say what's in there, and I have no intention of telling you anyway. All I can promise is that while not dangerous, it would be best if that door were never opened."
"I frowned, confused as to what he meant. As I pondered it over, I noticed him watching me think it through with a slight smirk. I pouted, mumbling to myself."
mc "Couldn't be that bad..."
show oz neutral
oz "Perhaps. Or it could be something that could end the world as we know it."
mc "Okay, but... it just holds a thing, right?"
oz "Correct."
mc "But then why when I use it..."
show oz smile
oz "Ah. That. I was getting to that."
show oz pout
oz "It was never intended to just be a quarantined room, but more... an attempt at something more. A collective effort to make the world better."
oz "My older siblings were more keen on designing and theorizing about it. Speculating was something more they dabbled in, when I'd much rather have something more quantifiable."
mc "But... How was it going to change the world for the better?"
show oz laugh
oz "Morphic resonance."
"The blank stare I gave him in return must have disappointed him, stopping him from getting revved up about the tangent he was about to go on."
show oz neutral
oz "Put another way, making a better use of the inherent survival instinct instilled in every living being on the planet."
mc "But... I haven't seen myself die, just..."
oz "Just what?"
if bearroute == True:
    mc "I saw Dean dead. Looked like... a poisoning?"
    oz "A poisoning. Where?"
    "Oswin's tone was just an echo, almost in disbelief."
    mc "Right. Um... In the greenhouse."
    show oz pout
    oz "What did you put into the keypad?"
    mc "Uh... 'Deathcap'."
if lionroute == True:
    mc "I saw Hoss... stabbed. In the shower, I think?"
    oz "..."
    "I scratched my head, trying to remember more to be helpful, but finding the recollection somewhat painful."
    if HossKiss == True:
        "Especially with him kissing me this afternoon, how I was feeling was quickly becoming more and more muddled between being more invested than I should be, when I was trying to be helpful."
    else:
        mc "Um..."
    mc "In the... gym. Yeah."
    show oz pout
    oz "What let you see that?"
    mc "I put the word 'Heroism' into the keypad."
if crocroute == True:
    mc "Sal was... in the freezer. Frozen but..."
    oz "But what?"
    mc "He was sleepwalking, so... Someone told him to go there."
    show oz pout
    oz "'Someone'?"
    mc "Orlando and I... uh... Well..."
    oz "Speak, [mcname]. We're getting nowhere if you stay quiet."
    mc "Apparently someone's been talking to him, using the name 'Hypnos', um..."
    oz "Well... as one that chose to use a false name I can understand that I'd come under suspicion."
    mc "Right..."
    show oz pout
    oz "And what code did you put into the keypad?"
    mc "Um... 'Dreamer'."
if dragonroute == True:
    mc "Orlando... Um..."
    oz "He what?"
    mc "It looked like he was sleeping, just outside the door of the vault."
    oz "Dead, or alive?"
    mc "I'd... assume dead, but he was just sleeping. No marks, no blood, no nothing. It was... strange."
    "Oswin's brow furrowed for a moment while he thought."
    show oz pout
    oz "Bizarre. That could've been any number of things. What was the keyword?"
    mc "It was... 'Sentence'? Yeah."
if wolfroute == True:
    mc "Tyson, he... uh... Was pretty beat up."
    oz "Explain, please."
    mc "Like... y'know. Cut up all... over..."
    "As I tried to mime what sorta marks I remembered I felt my voice crack, finding it hard to remember."
    show oz pout
    oz "Where?"
    mc "Um... outside? On the grass."
    show oz neutral
    oz "You seem distraught."
    mc "Of course I'm distraught! I don't like thinking about any of my friends potentially dead."
    show oz pout
    oz "Then take a deep breath, calm down, and tell me what word you used."
    mc "...'Solidarity'."
if boarroute == True:
    mc "Roswell was in... the li- museum."
    oz "..."
    mc "Uh... Attacked from behind, next to a book."
    oz "Anything else distinguishable about the scene?"
    mc "Not that I can think of aside from the book he was next to. Just a big one left open."
    oz "Anything of note with it?"
    mc "Looked like the word 'Discovery' was underlined in blood."
    show oz pout
    oz "By chance, did that happen to be the password?"
    mc "Yeah."
elif DISCOVERY == True:
    mc "Oh, and there was another one with Roswell."
    show oz neutral
    oz "What do you mean?"
    mc "It was uh... him attacked from behind I think? Next to a book with a word underlined in blood."
    oz "..."
    mc "..."
    oz "What was the word?"
    mc "Oh, 'Discovery'."
    show oz pout
    oz "And the code you used?"
    mc "Oh, it was the same."
mc "And then for Benson..."
show oz neutral
"Oswin tensed up rolling his shoulders briefly as I trailed off."
oz "Go on."
mc "Shot. But... It didn't seem right."
mc "I used the word 'Betrayal' for that one."
mc "But if this was meant to be a thing for my survival instinct, why haven't I seen myself?"
oz "Perhaps I wasn't clear."
oz "The theory was that it'd rely on morphic resonance, but... Well, you've seen how that works."
mc "Have I... been in danger?"
oz "Indirectly. The concept revolves around trauma, survivors using traumatic experiences to have different behaviors in similar situations moving forward. "
extend "So while you've not been in danger as such, you've suffered through these events."
mc "But... they never happened."
show oz smile
oz "As Reginald would say, 'Not this time around'."
mc "I... Hrm... I don't get it."
show oz annoyed
oz "Nor do I expect you to. It's a load of rubbish to me, to be frank. Bah, timelines, alternate realities. Rubbish."
mc "I don't... understand. I'm sorry."
"With a sigh, Oswin took a moment to collect his thoughts before he explained."
show oz pout
oz "The reason the vault showed you those things, and again consider this is all just theory and hypothesis, is because you've lived through these experiences before. In another lifetime perhaps."
oz "Those words must have some... significance to how you lived through those experiences. How those events shaped your life after they happened."
oz "Those words, along with a sound played at the right frequency, is supposed to trigger the reaction. But therein lies the problem."
mc "There... seems to be a lot of problems, I think."
show oz neutral
oz "Agreed, but I'll state the specific one."
oz "As the only person present that knows how the systems behind the vault operates, I'm the only one that can program those passwords in."
oz "And I assure you, I've only programmed two. Neither of which I'll tell you, as they're the codes for the door itself to open, plus... something else."
mc "But that's..."
oz "But what?"
if dragonroute == True or lionroute == True:
    mc "Hoss had a list of words, right? That..."
    "Oswin's brow furrowed, thoughtful or maybe slightly irritated."
    oz "That {i}what{/i}?"
    mc "Well, we don't know where it came from but..."
    if DISCOVERY == True:
        mc "One of the words on there was 'Discovery'. It can't just be a coincidence, right?"
        oz "Perhaps, but I supplied no one with a note of words. Like I said, I've only programmed in two words."
    else:
        mc "It seemed fishy, right? That there'd be a list of words and just... I don't know."
        oz "Do you know where the list came from?"
        "I shook my head quickly, making Oswin grumble and rub his nose briefly."
    mc "But if you've only programmed in two passwords then... why did the words I used, work?"
else:
    "I started at him, dumbfounded."
    mc "But that's impossible. How else would the words get in there?"
"The question hung in the air without an answer for a while before Oswin replied, his tone quiet and uncertain."
show oz annoyed
oz "...I don't know."
mc "Oh..."
scene ozmeet with dissolve
oz "Now... I think it's your turn, [mcname]."
"Oswin's voice was lowered, taking on an air of seriousness. While he was very no nonsense before, I felt the tone of the conversation get heavy from how he poised himself."
oz "I've said what I need to say. If you have any questions, I'm all ears."
"I gulped, looking Oswin in the eye. He stared right back through his glasses, watching me carefully."
"This was it. In the off chance I never had a chance to talk to him again, I had to make sure I asked anything that might be important."
mc "Okay..."
"He was only going to tell me things that were relevant, all I had to do was ask. But what was considered relevant?"
jump inputQuestions

label AfterOz8:
    scene library
    show oz neutral
    with dissolve
    "Oswin got up from his side of the desk, supporting his weight on it as he did so."
    oz "I hope tonight was... informative."
    if OzKnown == True:
        "There was a sense of emptiness that accompanied his comment, eyes lingering on me while I got up."

    else:
        "Oswin stretched before yawning, not bothering to cover his mouth or hold it back. I got up, shaky before following suit."
    mc "It... was. Yeah."
    show oz pout
    oz "Then good."
    "He made to walk away, and I called out."
    mc "Wait!"
    show oz neutral
    oz "What is it?"
    mc "What... happens now?"
    show oz pout
    oz "You go to bed."
    mc "And you?"
    oz "I have some calculations I need to run. Something I need to... test."
    show oz neutral
    oz "But hopefully you'll sleep soundly enough despite what we talked about tonight."
    mc "I... should, sure. But what about us? Will we meet again? Will we... talk again?"
    oz "If you believe that it's needed, then we can arrange something for a few days from now. Let me think..."
    show oz pout
    oz "Three days. Give me three days and we'll reconvene here, same time, same place."
    mc "To... talk again?"
    oz "No. By then I should be able to show you something. Something in my lab, assuming you were interested."
    mc "But... would that help? Help us figure out what's going on?"
    show oz neutral
    oz "Not necessarily, but you can never go wrong with more information. So in three days, meet me here, and I'll show you the lab."
    mc "Alright."
    hide oz with dissolve
    "Oswin wandered over to the door, stepping through it before turning around to look at me once more. With a nod, he closed the heavy door and it clicked shut, almost with the sound of a mechanism ensuring it'd stay that way."
    scene black with dissolve
    "For me, I wandered back upstairs to the corridor, the meeting playing over in my mind."
    "Had I said everything I needed to? Was everything put away at least for the time being? I hoped that, if anything, there was going to be some breathing room to try and enjoy my time with my friends."
    if crocroute == False:
        "I stopped in the darkness, smelling something. My nose scrunched up, trying to remember where I'd placed that smell."
        "It wasn't one I associated with danger, so there was that. But definitely not one that I was expecting to be smelling here, and now of all times."
        scene conservatory
        show croc dazed
        with dissolve
        "I froze, emerging from the corridor right into Sal, standing in the middle of the conservatory."
        mc "Uh..."
        "Something didn't seem right about this. Something felt... off."
        mc "Sal? Are you okay?"
        "I looked behind me quickly, closing the bookcase while keeping an eye on Sal. It was odd; he wasn't responding to anything, instead just standing there, just staring at me."
        mc "Sal? What are you doing? I can explain about the bookcase, it..."
        "I gestured over to the now concealed passage, expecting him to have said something about it by now."
        mc "Um... Maybe you should go to bed."
        croc "Go... to bed. Right... Bed..."
        hide croc with dissolve
        "I watched as Sal wandered off, leaving the room and bumping into the door frame on the way. He looked out of it, and I wondered why he wasn't asleep."
        "Still... Of all the odd things that had been happening of late, at least he wasn't brandishing a weapon around."
    else:
        "I shook my head, finding that even thinking {i}that{/i} was maybe being a little too hopeful. I was on edge, and I was going to need to go all out to unwind."
    stop music fadeout 2.0
    scene bedroom with dissolve
    "I made it back into my room and nearly collapsed on my bed, kicking off my shorts, peeling off my shirt and laying on my back."
    "Any other night I probably would've indulged in relieving myself of some of this pent up stress but instead I lay there with my thoughts."
    "With phone still in hand, I lifted it up to my face so I could scroll through my messages. Each one of these a record of a time where I didn't have to worry about the person on the receiving end dying."
    "My finger paused over one message chain, hesitating before clicking on it."
    "There were so many messages, all sent by me still waiting for a reply. I scrolled up, not bothering to read them for a bit before a backed out."
    "I knew what all of them said, almost like a journal of the points of my life where I just needed to let someone know something was up."
    "It couldn't be Tyson, or really anyone. These were... private things."
    "I dialed my voicemail, the options memorized from having done it so many times before. Holding the phone up to my ear, I closed my eyes, breath catching in my chest."
    $ renpy.pause(1.0)
    "There was always that brief delay before the message started, to the point I could count the seconds from when the person on the other side realized the beep had sounded."
    dad "Oh!"
    "There was a brief smirk on my face as the familiar voice came through."
    dad "Guess I missed you, huh sport?"
    "There was his laugh. My laugh.{w=0.5} {i}Our{/i} laugh.{w=1.0} That nervous hyena chuckle when we'd been caught off guard by something."
    dad "Ah well. Figured I'd just check in on how things are going. You going alright, champ? Oh. Right, this is just a message, isn't it?"
    "He laughed again, and despite the tears welling up I laughed along with him much like I'd done every time in the past when listening to this message."
    dad "Well, best I get back to work. Rest up and I'll see you when you wake up, alright?"
    dad "I love you, son!"
    "My reply was halfway out of my mouth before the message ended, the rest of the reply trailing off into silence to be replaced with my quiet sobs."
    "My arm went limp and I let the phone fall away from my head."
    "I'll see him when I wake up."
    "My eyelids drooped a little, and I breathed out, wiping the corner of my eyes and yawning."
    mc "When I... wake up..."
    scene black with dissolve
    "I fell asleep soon after, exhausted. I should've at least gotten under the covers or something, but by the time I realized, it was already morning."
    jump day9morning
    $ renpy.pause(3.0)
    "{color=f00}{b}TO BE CONTINUED: END OF DEMO{/b}{/color}"
    return
#Stuff for after the interrogation













#
