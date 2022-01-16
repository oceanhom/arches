label Day11CMorning:
    scene day11 with fade #NOTE replace with altered version to indicate alternate timeline
    $ renpy.pause (3.0)
    scene black with dissolve
    "It felt like I was floating, my mind still replaying the events over in my mind while I slept."
    scene davelivingroom with dissolve
    play music dark fadein 2.0
    "When I woke up, I was sitting on the sofa in the living room. "
    if bearroute == True:
        show bear smile with dissolve
        extend "Sitting next to me was Dean. He seemed... nervous? It was hard to say but he was rocking back and forth."
        mc "Dean...?"
        "He turned to me quickly, almost too quickly and remained silent, keeping that smile on his face. When I tried to move, it was almost as if I was glued to the spot."
        mc "Didn't you...? Aren't you...?"
        hide bear with dissolve
    elif boarroute == True:
        show boar neutral with dissolve
        extend "Roswell was there too, eyeing me curiously."
        mc "Roswell...?"
        show boar smile
        "All he did was smile though, staying on his spot at the opposite side of the sofa. When I went to reach out for him, I realized I couldn't move, and he was just out of reach."
        mc "But aren't you...?"
        hide boar with dissolve
    else:
        show boar neutral at left
        show bear neutral at right
        with dissolve
        extend "Dean and Roswell were standing nearby, looking at me expectantly. Upon seeing them, I felt my stomach lurch."
        mc "Guys..."
        show bear sad
        "It seemed like Dean went to say something. "
        show boar pout
        extend "But when he didn't, Roswell tried. {w=0.3}Neither of them were saying anything, instead just looking at me. Waiting."
        mc "I thought... I thought you both..."
        hide boar
        hide bear
        with dissolve
    "When I blinked, I was alone again."
    scene davekitchen with dissolve
    "My body felt heavy as if chained down, but my feet took me to the kitchen. Be it because of instinct, or that it was just the next closest room, I don't know."
    mc "Dad...?"
    "He wasn't there. I knew he wouldn't as he, like Dean and Roswell now, wasn't around anymore."
    "But that didn't make the pain in my chest go away.{w=0.3} It didn't shake the sick feeling welling up from my stomach."
    scene black
    "In a flash it was all gone."
    scene bedroom with dissolve
    "The sound of loud banging is what roused me from my sleep, and I looked to the others in the room also waking up."
    "It lasted for all of a second before that confused stupor wore off and we looked at the door with dread. The banging turned into the door rattling, trying to open."
    "What came next was the distressed voice of the person trying to enter, sounding almost frantic."
    croc "Everyone! Where are you!?"
    "I looked to Ty and he quickly shook his head. Hoss was eyeing the door wary and Orlando had his hands covering his mouth, also watching the door."
    if BensonAround == True:
        "My mind then went to Oswin and Benson, wondering if they were aware of what was going on. Chances are they hadn't made themselves known given how Sal was reacting."
    "Soon enough he left, his voice fading away quickly."
    show lion shirtless sad at left
    show dragon pantsless cry at right
    show wolf shirtless mad
    with dissolve
    wolf "Shit. He's awake."
    lion "Shows that the soundproofing exists though. Could hear him right outside the door, but chances are he's been searching for a while."
    show dragon pantsless sad
    dragon "What makes you say that? The tone of his voice?"
    mc "He did sound panicked, maybe scared, I don't know..."
    wolf "Or he's trying to do us in."
    show lion shirtless pout
    lion "Well, we can't stay here forever. We're going to have to leave eventually."
    show wolf shirtless sad
    wolf "I know that. Fuck, just... alright. When we're all ready let's head on out."
    scene black with dissolve
    "All of us mentally prepared ourselves before Tyson and Orlando moved the barricade from the door. There was a moment of hesitation from Orlando when he reached out to open the door, but when he did, we kept close together."
    scene foyer with dissolve
    stop music fadeout 2.0
    "As we reached the stairs and looked down, Sal was huddled on the floor. He was cowering, talking quietly to himself. Quiet enough I couldn't make out what he was saying."
    "The trail of blood from where Dean and Roswell had been dragged off into the adjoining room was unmissable. A stain of red on the tiled floor we were heading towards."
    show croc scared with dissolve
    "Sal must've heard us descend the stairs, standing and turning suddenly to face us."
    play music tense fadein 2.0
    croc "Everyone! There's been..."
    "Ty stuck an arm out to stop me advancing, shepherding me behind him almost."
    croc "Dean and Roswell, they..."
    "He took a step forward, and three of us took a step back while Ty remained firm."
    show croc scared at left with ease
    show wolf shirtless mad at right with moveinright
    croc "Why did you..."
    "I could hear Ty start to snarl."
    wolf "You fucker! You did this!"
    "From behind Tyson I could see Sal's arms go limp in shock."
    croc "What...? No! Dean and Roswell, they're... I tried to and... but..."
    "He took a step forward and Tyson took another forward as well, his voice raising."
    show wolf shirtless yell
    wolf "You tried to what!?"
    show croc sad
    croc "I found them this morning but... It was too late. CPR wouldn't be enough, so..."
    "He scrambled for his phone in his pocket, pointing to it."
    croc "I tried calling for help, calling any of you, but no signal. "
    show croc cry
    extend "Honestly, seeing you all alive is a relief."
    "It's then I realized he didn't know. He didn't remember what had happened and what role he'd played. "
    extend "The words caught in my throat, but it was Tyson who picked up the slack."
    show wolf shirtless mad
    wolf "Yeah? You're relieved we're alive, huh? You planning on doing us in too?"
    show croc scared
    croc "What...?"
    show lion shirtless sad with moveinright
    lion "Hey, something about this doesn't feel right, Tyson. Maybe back off a little."
    show wolf shirtless yell
    wolf "Fuck that! I'm not letting him kill anyone else!"
    "Sal took a step back upon hearing what Ty had said. In fact, his words echoed in the foyer with none of us saying anything."
    croc "What... did you say? I didn't... I couldn't..."
    "He took another step back, his head slowly turning to the stain on the floor he was inches away from."
    lion "Sal? Do you... not remember what happened last night?"
    "Looking at Hoss he shook his head slowly. He almost seemed stunned by the question."
    lion "Damn... This is going to be uh..."
    wolf "Who do you think killed those two, huh?"
    show lion shirtless scared
    show wolf shirtless mad
    lion "Tyson!"
    "Hoss grabbed Tyson quickly, but just as quickly pulled away when Tyson went to punch him. When he was riled up like this, suddenly grabbing him wasn't a good move."
    croc "Please... What happened...?"
    mc "Last night, um..."
    show lion shirtless sad
    lion "[mcname], wait..."
    hide lion with moveoutright
    "With his attention on me, Tyson took the chance to move away from Hoss and approached Sal. His tone was spiteful, and he punctuated his sentence by snarling even more."
    wolf "You wanna know what happened last night, you piece of shit? You stand there all scared and confused but I don't fucking buy it. You took an axe to the oinker, fucked up Dean with the same axe and went for a casual walk after."
    "Sal took a step back further, his foot landing in the smear on the floor. He was followed, Tyson increasing his snarl."
    wolf "So those two bodies in there? Yeah, that's all your fucking handiwork."
    hide wolf with moveoutright
    croc "No... "
    extend "No, it can't... "
    extend "I couldn't have..."
    hide croc with moveoutleft
    "With a few more steps back, Sal turned tail and ran. Out the front door and out of sight."
    show dragon pantsless sad with moveinright
    dragon "Sal! Wait!"
    show lion shirtless sad at right with moveinright
    lion "Orlando, buddy, you can't be serious."
    dragon "But..."
    show lion shirtless mad
    lion "Remember, he killed two of our friends. He's unstable. It's dangerous. "
    show lion shirtless sad
    extend "I'm sorry, but..."
    "Hoss gestured in the air, unable to finish his thought with words."
    mc "What... do we do now? We have to be able to do {i}something{/i}, right?"
    show wolf shirtless neutral at left with moveinleft
    wolf "Go put on clothes before you get cold. "
    show wolf shirtless pout
    extend "Then... We go from there."
    lion "So we're splitting up?"
    show wolf shirtless annoyed
    wolf "Fuck no. We go together. It's only pants and shirts, right?"
    scene black with dissolve
    "Together we went upstairs. It was odd, three of us outside while the last one went in to retrieve a piece of clothing. I kept peering over the railing, watching the front door as if expecting Sal to come back."
    "I didn't even get to go into my own room, as clothes were brought out to me while I was in a daze watching the foyer."
    "Once we were all dressed, we headed down for breakfast."
    scene diningroom with dissolve
    "We filed in, keeping watch just in case we were going to get jumped the moment we entered a room."
    scene kitchen with dissolve
    "Once we were in the kitchen, we stopped to look at one another."
    mc "I... I don't think I'm all that hungry..."
    show dragon sad at left
    show lion sad at right
    show wolf pout
    with dissolve
    dragon "But... we can't just {i}not{/i} eat, right?"
    show lion pout
    lion "Normally I'd agree, but if we don't try and keep something down..."
    "Ty wandered over to the coffee machine and flicked it on before grabbing some bread from the pantry."
    show wolf neutral
    wolf "Here."
    "He held out a slice of bread to me and I gingerly took it, staring at it while I held onto it with both hands."
    show wolf pout
    wolf "You gotta eat something. I'll get coffee going."
    mc "But... why?"
    show wolf annoyed
    if wolfroute == True:
        wolf "We're family. Someone's gotta look out for you and I'll be damned if it's not going to be me."
        show lion scared
        lion "Isn't that going a bit far?"
        show dragon pout
        dragon "No, I suppose it makes sense. Honestly, just having someone that's keeping it together is helping. "
        show dragon sad
        extend "And, if someone's at least looking out for someone else among us, that's something to relax a bit about, right?"
    else:
        wolf "[mcname], take the damn bread and eat it."
        show lion scared
        lion "Pushy, much? He's just in shock, so ease off."
        show dragon pout
        dragon "I don't think that's it, is it?"
        show wolf pout
        wolf "What?"
        show dragon sad
        dragon "You... Do you love him? Is that why?"
        show wolf annoyed
        wolf "The fuck?"
    "I zoned out as they continued to talk. The bread in my hands was soft, and while it was only a single slice my body was torn between eating it for sustenance versus throwing up from the pit in my stomach."
    "Trembling I devoured it, figuring that forcing it down fast was better than thinking about it too much. Still, I felt slightly worse once it was gone."
    show wolf neutral
    "Looking to Ty, he gave me a nod and wandered over to the coffee machine."
    hide wolf with dissolve
    lion "Well... I think this is as good a time as any to talk about a plan, right?"
    dragon "Maybe... What is there to even do?"
    lion "The first thing is securing a way out, right?"
    show wolf pout with dissolve
    wolf "Landslide is going to get in the way of that."
    mc "So checking out that is one thing we need to do today, huh?"
    dragon "What about Sal? Shouldn't we ask him about what happened?"
    show wolf mad
    wolf "You can for all I care. [mcname], you ain't going near him."
    mc "But why not? It's... uh..."
    wolf "You're not going near him."
    show dragon annoyed
    dragon "He can do what he wants! "
    show dragon sad
    extend "But I kinda get why you'd say that. It's dangerous, right?"
    lion "We don't have enough to go off. Who knows what could happen if we went and talked to him. No telling where he even went, right?"
    mc "I guess that's true. He went out the front door and I haven't seen him since."
    show wolf annoyed
    wolf "If he's planning on coming back, then chances are he'll get hungry at some point. We can lock him in the freezer or something until the cops arrive if we have to."
    show dragon scared
    dragon "The... freezer?"
    show wolf neutral
    wolf "Yeah?"
    show dragon pout
    dragon "I think that might do a bit more than just detaining him. We'd be better off... I don't know... isolating him somewhere else?"
    show wolf pout
    wolf "Don't care. So long as he's out of the way is fine by me."
    mc "Okay... Landslide... Sal... but what about... um..."
    show wolf sad
    show dragon sad
    show lion sad
    "I gestured behind me, hoping the others would clue in."
    if BensonAround == True:
        lion "I'd been thinking about that too. Chances are we can't just leave them there without it getting uh... y'know."
        show wolf annoyed
        wolf "Well what do you expect us to do about it? Bury them in the back yard?"
        mc "No! We need to bring them with us!"
        show dragon scared
        dragon "That's... uh..."
        show lion pout
        lion "Hopefully we can get in contact with an ambulance or something to come retrieve them, but... yeah. We can't just leave them there."
        mc "Would... Asking Benson, or Oswin what to do help here?"
        show wolf neutral
        wolf "What, you think one of them might just magically know what to do with a body?"
        mc "Well I sure don't!"
    else:
        wolf "Shit, yeah... Can't just leave them like that, huh?"
        lion "Glad to know I wasn't the only one considering that. Not being able to get in contact with the police, or an ambulance makes dealing with it harder."
        dragon "Burial is out too, I'm guessing..."
        mc "Of course! I'm not just going to leave them here!"
        show wolf annoyed
        wolf "No one's leaving anyone behind, [mcname]. "
        show wolf pout
        extend "But... we gotta do something about them, right?"
    show dragon pout
    dragon "Well..."
    "We all looked to Orlando, who seemed to be considering something."
    dragon "If... If there are no other options, we might be able to keep them in the freezer, right?"
    show wolf mad
    show lion scared
    wolf "Are you fuckin' serious?"
    lion "I guess it makes sense, but... is that safe? Is that... I don't know, proper?"
    dragon "All things considered, I think that's the best option we have, right?"
    show wolf annoyed
    wolf "What, you're planning on bagging them up and keeping them there to stay fresh?"
    show dragon sad
    dragon "Kinda, yeah. It works for meat, and if I'm being honest, it's not the first time this has come up."
    mc "Uh..."
    show wolf mad
    wolf "The fuck do you mean this isn't the first time?"
    show dragon annoyed
    dragon "You see a lot in my family's line of work, Tyson. You learn to... or you witness... uh... "
    show dragon sad
    extend "Hoss? Help?"
    lion "I could make a guess if that's what you're looking for."
    if dragonroute == True:
        mc "Oh... I know why..."
        dragon "Ah... Right. But uh... Well I guess there's no avoiding it now."
    else:
        "Orlando breathed in deep, running his hand through his mane."
        dragon "It's better I do it I think. Just to make sure no one's assuming anything wrongly."
    show dragon pout
    dragon "My family, the Noble family, are an organized crime syndicate with me being the heir. "
    show dragon sad
    extend "So when it comes to dealing with bodies... While not me, or my parents, or grandparents... someone had to deal with them. And you learn."
    if dragonroute == False:
        "I gulped, staring at Orlando. All this time he'd been involved in crime, whereas I had just assumed his parents were bankers and that he was fairly wealthy. But this explained some things."
        mc "So... When I wasn't allowed to come over anymore... or... or when I forgot your birthday..."
        "I paled, overcome with a sense of dread."
        dragon "Oh, [mcname], no. It's not like that. Sure, dad found out that your dad was a cop and that's why you weren't allowed over but I wouldn't say you specifically are in any danger."
        show wolf yell
        wolf "He better not be!"
        show dragon mad
        dragon "He isn't! I will set my dad on fire before I let him touch [mcname]."
        "I felt a strange mix of flattered and terrified and took a step back."
    else:
        mc "I'm sorry, Orlando..."
        show dragon pout
        dragon "It's alright. If anything that's just... one small upside to what's happening right now?"
    show wolf annoyed
    "Ty sighed out, rubbing his face."
    wolf "Fine. So there's that. We have a plan for those two. "
    show wolf neutral
    wolf "But I ain't moving them if I don't have to. I'm checking out the landslide first to see if there's a way out first."
    if wolfroute == True:
        wolf "So [mcname], get your ass ready and we'll head on over."
        mc "Wait, what?"
        show wolf annoyed
        wolf "I'm not letting you out of my sight. If I'm going, you're coming too."
        mc "But what if I don't wanna go?"
        show wolf mad
        wolf "We're not arguing about this. You're coming even if I have to drag you myself."
    else:
        wolf "So when we're done here, let's head on down."
        show dragon sad
        dragon "We have to walk down there, again?"
        show wolf pout
        wolf "Well I'm not going down there alone. "
        show wolf mad
        extend "Fuck if I'm gonna leave [mcname] alone with any of you either."
        show lion annoyed
        lion "Excuse me?"
        show wolf annoyed
        wolf "What? You really expect me to spell it out for you after what we saw last night? Far as I know either one of you could be looking to do [mcname] in next."
        show dragon mad
        dragon "He's our friend too! Why would we want to kill him!?"
        show wolf mad
        wolf "Yeah? Reckon you could've said the same about Sal?"
    mc "Okay! It's fine! Let's... all just go down together. That'd be fine, right?"
    show dragon sad
    dragon "I suppose sticking together would be the safest option..."
    show lion sad
    lion "Right."
    if BensonAround == True:
        mc "What about Benson? And Oswin?"
        show wolf annoyed
        wolf "Fuck 'em. Don't care what happens to them, they've gone and fucked off somewhere and left us to fend for ourselves."
        mc "I guess that's fair..."
        show lion pout
        lion "Should we try and contact them? Tell them where we're going?"
        wolf "What part of fuck 'em did you not get?"
        dragon "But shouldn't we...?"
        show wolf mad
        wolf "No!"
        mc "I'm sure they'll be fine, right? They'll uh... be around later? Hopefully?"
        show dragon pout
        dragon "Right..."
        show lion sad
        lion "I guess there's no avoiding it, huh?"
    else:
        "I looked between the others, feeling tense. Tyson was being protective, which was nice in that it put me at ease but at the same time he was starting to frighten me a little."
        mc "Well... I guess we better go, huh?"

    scene woods2 with dissolve
    "Ty didn't give us much time to get ready, instead leading us along towards the main road. The way forward was familiar from having trekked it during the night, but something about it being the middle of the day made it feel safer."
    show wolf mad with dissolve
    wolf "Come on, keep walking."
    "He'd occasionally grab me by the hand and give me a tug to hurry me along. He was stressed, maybe worried, and his scowl was just putting on a brave face."
    hide wolf
    show lion sad
    with dissolve
    lion "Not much farther. At least I think so."
    "We'd been walking for a while, and I remembered about how long the drive it was from the main road and the front of the house. We passed the spot I'd stopped to rest on my own walk ages ago, but the path seemed to continue on."
    hide lion
    show dragon sad
    with dissolve
    dragon "So what's the plan when we get to the main road?"
    mc "I guess call for help? See what's happening?"
    show lion sad at right with moveinright
    lion "Right. I've been checking my phone occasionally until I see we have reception again. So far, nothing."
    mc "Is that normal? I mean... We're on a mountain, right?"
    show wolf annoyed at left with dissolve
    "Tyson slowed down, huffing and grumbling out an answer."
    wolf "Something like that. Bus drove up the mountain to get here, but fuck if I know which one or where."
    show lion pout
    lion "Don't worry, I've got that sorted. Doesn't mean much if I can't contact anyone though."
    mc "Is that... likely?"
    show lion sad
    lion "Well, it's strange that I'm getting no reception whatsoever. Sometimes it can be a bit spotty the further away from civilization you get but we shouldn't be that far out from the city for it to matter that much."
    show dragon scared
    dragon "Do you think someone's messing with it somehow?"
    show lion scared
    lion "What do you mean?"
    show wolf pout
    wolf "You can't mess with that kinda shit can you?"
    show lion annoyed
    lion "You can, but... question would be why."
    if lionroute == True:
        "I gave Hoss a look, frowning. He returned it briefly, knowing where my mind was at but all he did was shake his head."
    else:
        mc "Why would you even know about that, Hoss?"
    lion "Speaking from experience, it's more difficult unless you really go all in. There's no reason to do that here, right?"
    dragon "Oh no... Not unless..."
    mc "Not unless... what?"
    show dragon sad
    dragon "What if it was to assassinate me?"
    show wolf mad
    wolf "What did you do?"
    show dragon sad
    dragon "Nothing! Honest!"
    show lion sad
    lion "Is this because of your family?"
    dragon "I mean, it'd make sense, right? This is the perfect spot for getting rid of me given we're helpless and alone."
    "Tyson roughly grabbed Orlando and shook him."
    wolf "Let me make two things real clear. "
    show dragon scared
    extend "First is if this all because of you, I'm ditching you the first chance I get and taking everyone else with me. Die alone and leave us out of it."
    mc "Tyson!"
    show wolf yell
    wolf "You shut the fuck up now, [mcname]! I'm not talking to you right now!"
    "He turned back to Orlando, spittle flying from his mouth."
    wolf "Second, and listen real closely; if you think Dean and Roswell died in some fucked up attempt to kill you, get over yourself."
    hide wolf with moveoutleft
    "Roughly, he threw Orlando back into Hoss and turned to march off. He didn't even bother to drag me along with him."
    show dragon cry
    "Orlando was a mess, trembling and bawling as he tried to stay standing on his own two feet. Hoss glared daggers into Tyson's back for a few moments before consoling Orlando with something barely whispered to him."
    "Whatever it was, it seemed to do the trick. Looking to Ty though, he looked tense, marching forward with his arms almost completely rigid with his fists clenched tight."
    menu:
        "Check on Orlando.":
            "Ty would likely be fine on his own, right? He was tough, and if I was being honest he looked ready to punch someone."
            mc "Orlando? Are you okay?"
            show lion annoyed
            lion "Come on, [mcname]. Does he {i}look{/i} okay to you?"
            dragon "I... I just... I only wanted..."
            "I shrank into my shoulders, looking between Orlando and Hoss. I knew what it was like to be on the receiving end of Tyson's jabs."
            mc "Sorry..."
            show lion sad
            lion "Just... be more mindful. "
            show lion mad
            extend "But hell does that guy have problems."
            show dragon sad
            "Orlando wiped his face with the back of his arm, looking further down the road. I looked as well, noticing that Tyson had moved on ahead and out of sight."
            mc "Should we go after him?"
            lion "He can fuck off and do his own thing."
            show dragon scared
            "Hearing Hoss swear made my ears sting. It was a rarity, but the way he delivered it had a tinge of malice that rarely made its way known."
            lion "Harsh as it may be, if he wants to wander off when we should be sticking together then that's on him. "
            show lion annoyed
            extend "And to be frank? If he's going to make a show of not letting you out of his sight and bail, [mcname]? Where does that leave us?"
            mc "As in, you and Orlando?"
            show lion mad
            lion "No, I mean all of us. He's unhinged, maybe as much as..."
            "He looked to Orlando quickly before turning back to me, sighing out."
            show lion sad
            lion "Well, you know who I'm talking about."
            "I nodded slowly, not exactly knowing for sure at first but the pieces fell into place pretty quick upon seeing him gesture at Orlando with his head."
            show dragon sad
            mc "Okay... What do we do now? Do we head back, do we stay here?"
            show lion annoyed
            lion "It's a tough call."
            dragon "W-Well... If we headed back now, we'd be safer, right?"
            show lion sad
            lion "You sure about that?"
            if BensonAround == True:
                dragon "Well, Benson and that Oswin guy are back there, right? So more people means safer?"
                mc "Is that really how that works? We don't... I mean I don't..."
                "As I struggled to put it into words, Hoss seemed to finish off my sentiment."
                lion "There's no telling if they're much safer. "
                show lion annoyed
                extend "Where did he even come from?"
                mc "Well it's his house, so..."
                dragon "Maybe he just arrived back home?"
                show lion sad
                lion "You really think so? Why come back to your house when other people are staying there? I think he never left."
                mc "But..."
                show lion pout
                lion "He could've done it easily too with Benson running him food or whatever. That said, no idea {i}where{/i} he could've been in the house. We were pretty thorough when we were looking for that gun."
            else:
                dragon "If I'm being honest, not entirely? But if Sal left then he'd probably be looking for somewhere to either hide or someone to help."
                show dragon pout
                dragon "Which if the way out is the main road, and Tyson also headed that way..."
                "I felt my breath catch in my chest, quickly looking down the road in the direction that Tyson went."
                mc "But that could mean Tyson's in danger!"
                show lion annoyed
                lion "While I feel like he's not helping behaving the way he is over what's happened, I don't want to see him turn up dead either. "
                show lion sad
                lion "So at the very least, I think we should hold off going back for now."
            mc "If I got to vote, I'd be wanting to follow Tyson."
            show lion annoyed
            lion "No surprise there."
            show dragon sad
            dragon "Well... We should stick together regardless, and I get the feeling that you're not going to just abandon him."
            mc "Sorry, but... if Sal ended up going this way, then... Plus the road and..."
            show dragon cry
            dragon "I know, I know!"
            show lion sad
            lion "Well... Let's get going. We can figure it out as we go. Chances are he's stormed off ahead without stopping, so we should probably catch up."
            scene black with dissolve
            "Together we set off down the driveway towards the main road, following in the direction Tyson went."
            "Eventually, the trees started to clear and we were at the main road."
        "Chase after Tyson.":
            "Orlando seemed like he'd be okay, but Ty on the other hand..."
            mc "Ty! Come back!"
            hide dragon
            hide lion
            with dissolve
            "I left the other two behind, chasing after Ty who didn't slow down even after I called to him."
            show wolf mad with dissolve
            "His pace was faster than before, and he kept his eyes trained straight forward."
            mc "Ty?"
            wolf "Shut up."
            "I blinked, faltering in my steps to stay next to him and quickly recovered."
            mc "Did I do something wrong, Ty?"
            wolf "What did I {i}just{/i} say?"
            "I kept quiet, the pair of us just walking for a few minutes longer. The other two hadn't caught up yet, and I was starting to worry."
            show wolf neutral
            "Tyson seemed to be calming down a little, and as I went to check he spoke he beat me to it."
            wolf "Sorry."
            mc "It's okay."
            "He grunted, and we walked for a couple minutes more in silence."
            show wolf pout
            wolf "It's really not. You didn't do anything wrong."
            mc "Right..."
            "We stopped for a bit, with Tyson scratching his head."
            wolf "This whole thing, right? It's fucked. I'm stressed, worried, angry, and just..."
            mc "Just... what?"
            show wolf sad
            wolf "Well I need to keep you safe. I gotta."
            mc "But you don't think... that it was one of them, do you?"
            show wolf mad
            wolf "I don't fuckin' know. "
            show wolf annoyed
            extend "But if it was?"
            mc "But... Sal, and..."
            show wolf neutral
            "Tyson looked me over. He seemed tense, serious, but I couldn't tell if he was more worried or angry when he spoke next."
            wolf "Sal... Yeah, no brainer there. And if he's not the only one, what then?"
            mc "But Ty!"
            "I kept my voiced hushed, throwing a glance over my shoulder to see if the other two were catching up."
            mc "They're my {i}friends{/i}."
            "His response was cold, holding eye contact with me."
            wolf "Sal was your friend."
            mc "He..."
            "I didn't have a thought to finish. Was Sal my friend? Or at least would he still be after killing both Dean and Roswell?"
            mc "...Right. I guess... I guess you're right..."
            "Ty nodded and took my hand, leading me forward."
            wolf "Now me? I'm someone you can lean on, pup."
            "His hand tightened slightly, and while he didn't smile, he did give me a quick look before turning forward again."
            wolf "Promise. You know why, right?"
            mc "No...?"
            show wolf pout
            "He sighed, shaking his head."
            wolf "Then I'll tell you later."
            "I stopped, holding tight to Ty's hand to force him to stop as well."
            mc "Tell me now."
            show wolf annoyed
            wolf "If I do, will you keep moving?"
            mc "Sure."
            show wolf neutral
            wolf "Last time I saw your dad, he made me promise I would."
            "While my grip on Tyson's hand loosened in shock, my heart sinking, his tightened and he tugged me forward slightly."
            wolf "Look, it sucks, but I promised him I would. Not sure if he was being serious, {nw}"
            show wolf pout
            extend "and chances are he was just messing with me, but that's all I've got right now."
            show wolf neutral
            wolf "So come on. We have a thing to check out if we wanna bail from here."
            scene black with dissolve
            "I sighed out, nodding a little but not budging. I regretted pushing now, as bringing dad to the forefront of my mind and adding that into the mix made my stomach churn. If I'd actually seen him in my dream last night, I might've broken down then and there."
            "It took a little more coaxing but before long we continued on and eventually hit the main road."
    scene road with dissolve
    stop music fadeout 2.0
    play audio outside fadein 2.0
    "As we stepped out from the driveway it opened up, the surrounding mountains rising and falling around us. We were high up, with the far edge of the road ending in a sheer cliff."
    mc "Whoa..."
    "I wandered around a little, seeing it all for the first time. It was a shame I'd missed this on the drive to get here, but still..."
    "Tyson was off looking at a large pile of rubble obstructing the road. Hoss went to join him, leaving me with Orlando."
    show dragon sad with dissolve
    dragon "It looks bad, huh?"
    "Nodding, I looked past Orlando to the rubble. It was in huge chunks, having not only blocked the path but also taking huge chunks out of the road too."
    dragon "Do you think help will be able to arrive?"
    mc "Maybe... I guess we'll just have to see what Hoss and Tyson find, huh?"
    show lion sad at right
    show wolf neutral at left
    with dissolve
    "They were already making their way over, Hoss in particular looking grim."
    lion "This can't be right... [mcname], you have your phone on you, right? Can you see if you're getting any signal?"
    "I fished my phone out of my pocket and checked it. Low battery, but it was clear that I didn't have any signal either."
    show lion scared
    lion "But why...?"
    wolf "Well that sucks. "
    show wolf sad
    extend "The road is fucked too. That landslide has busted the road up so climbing over looks like it'd be a sure way to fall to your death."
    mc "But... That would mean..."
    dragon "We're trapped? Really? Is there no other way off the mountain?"
    show wolf pout
    "Ty seemed to think on it, but his expression quickly turned grim."
    show wolf sad
    wolf "Unless there's a way through the forest, we're stuck."
    show dragon scared
    dragon "Really? But where? How would we know which way to go?"
    show wolf annoyed
    show lion sad
    wolf "Does it look like I know? "
    extend "But...{w=0.3} We can probably safely guess that Sal didn't come this way either."
    mc "Right... He'd get stuck here too, huh? But does that mean he ran into the forest?"
    show dragon sad
    dragon "Sal..."
    show lion neutral
    lion "Okay... So things might be looking bad, but at least we have some things going right. We have shelter, food, so necessities are set."
    mc "Sure, but... That doesn't..."
    show wolf pout
    "I trailed off, and Ty threw an arm over my shoulder."
    wolf "We can make do. "
    show wolf mad
    extend "I'll keep you safe, [mcname]."
    "That made me feel better, but I caught Orlando looking anxious, also looking for the same sort of reassurance. When it became clear that Tyson wasn't going to offer the same towards him, he looked to Hoss."
    dragon "We'll be fine, right?"
    show lion scared
    lion "Huh? "
    show lion sad
    extend "Oh, right. Yeah. If we stick together we'll be alright."
    scene woods2 with dissolve
    "We started to head back to the house with Tyson leading the way. He wasn't pulling me forward by the hand anymore, but I stuck close anyway."
    "Orlando and Hoss pulled up the rear, with Orlando lagging further behind. Every time I looked back to check on him he seemed dejected, tired from everything that was happening."
    scene mansionfront with dissolve
    if BensonAround == True:
        "As we arrived back at the mansion though..."
        show otter neutral with dissolve
        otter "Gentlemen. Good morning."
        show wolf annoyed at left
        show lion pout at right
        with dissolve
        wolf "Yeah, fuckin' {i}great{/i} morning."
        show otter pout
        otter "Come now, I would hope to think you would see that more as pleasantries rather than a running commentary on the situation at hand."
        show wolf sad
        "Tyson huffed, grumbling but saying nothing more on it."
        lion "So we have some bad news. "
        show lion sad
        extend "The road is out, and still no signal even there. It's so strange; there should be no reason why that'd be happening, right?"
        show otter neutral
        otter "Not as far as I can tell. But the landslide does create some... complications."
        show otter pout
        otter "Supplies for the most part, but we should be able to make do given the stockpiles I've amassed. More than enough for a couple of days, but plenty for longer if need be."
        show otter smile
        otter "Heaven forbid that becomes the case, however."
        "I shuffled uneasily on the spot. I didn't like the idea of being here longer than we had to, and while knowing we'd be alright for a longer stay, I was more focused on hoping help would arrive soon."
        otter "Shall I see you inside? The master is up and about as well should you wish to... discuss anything with him, I'm sure."
        show wolf neutral
        wolf "Oi, butler. You seen Sal around anywhere? He wasn't down at the main road."
        show otter neutral
        otter "Why yes, I've seen Master Sal. He's sequestered himself at the pool and hasn't made a move to the mansion since he arrived."
        mc "Really? He hasn't gone looking for anything or gone to find you or Oswin?"
        show otter pout
        otter "I'm afraid not. He may be unaware that we're up and about, but he arrived there shortly after you all departed for the main road."
        mc "And he's said... nothing? He's done... nothing?"
        show otter neutral
        "Benson shook his head, leaving it there. That seemed odd, or at least didn't line up with someone who had murdered two people in cold blood. If I hadn't seen it first hand, I wouldn't have believed him."
        otter "If you'll excuse me gentlemen, I best get back to my tasks for the day."
        show lion mad
        lion "Benson."
        "The otter looked to Hoss, quirking a brow."
        otter "Is everything alright?"
        lion "I think you and I should talk later. I have a bone to pick with you."
        show otter smile
        otter "Ah. Very well. I shall look forward to it."
        hide otter with dissolve
        "He turned on heel and disappeared inside after addressing Hoss, leaving the four of us outside."
        show dragon sad with dissolve
        "Orlando stepped up, fidgeting and looking around at everything excluding us."
    else:
        "The house was quiet. When we arrived here for the first time we looked upon the house with awe, excited to be here, but now..."
        show wolf neutral at left
        show lion sad at right
        show dragon sad
        with dissolve
        lion "Well... we're back."
        mc "Do you think Sal is around here somewhere?"
        show wolf annoyed
        wolf "Fucker probably has holed up somewhere if he isn't still in the woods. Doesn't matter all that much."
    dragon "Does... that mean the only thing left to do is go inside?"
    mc "I... guess so, huh?"
    show lion mad
    lion "Well... I want to go find Sal. Probably better that someone keeps tabs on if he moves, right?"
    show wolf neutral
    wolf "Reckon you'll be alright by yourself?"
    show lion neutral
    lion "Should be fine. "
    show lion sad
    extend "Not that I have much of an option. But knowing where he is at least gives us an informed position in case anything goes wrong."
    mc "What about you Tyson?"
    show wolf pout
    wolf "I don't fuckin' know. I need to get my head straight about everything. Might go find a weapon or something."
    show lion mad
    lion "Isn't that a little extreme?"
    show wolf neutral
    wolf "Not going to be caught without one in case something else comes up."
    "I felt him look my way and I quickly looked to the ground. I was flattered, but hearing him so resolved that it was a potential thing that could happen again started to get to me."
    show lion sad
    lion "Fine. Good luck finding one I guess."
    hide wolf with dissolve
    "Ty headed inside after grunting once in reply."
    lion "Alright. I guess I'll head around the house and meet up with you guys later, right? You two going to be okay for a bit?"
    mc "I think so..."
    "I was eyeing the door, already knowing what I was keen on doing."
    show dragon pout
    dragon "We'll... be fine. I think."
    "With a nod, Hoss turned to leave, watching Orlando carefully. Then, he disappeared around the side of the house and out of sight."
    hide lion with dissolve
    "That left Orlando and I standing just before the front door, stealing glances at one another."
    dragon "You want to see them, huh?"
    mc "Is it that obvious?"
    show dragon sad
    dragon "Of course it is. You had...{w=0.3} {i}have{/i} a lot of love for them so... it's only natural."
    mc "But... You don't think I should?"
    dragon "It's not that. "
    show dragon pout
    extend "I'm just concerned that you'll... be stuck there and I won't be able to move you."
    mc "I just... I want the closure, I think. I want a chance to say goodbye."
    "While the words that came out of my mouth felt hollow, what I felt in my chest was moreso. I lied to his face about how I was feeling and he knew it too."
    "Still, he didn't say anything. He just nodded before the two of us went inside."
    stop audio fadeout 2.0
label Day11CBodyCheck:
    scene foyer with dissolve
    "Orlando and I crossed the threshold into the foyer and I sighed out. The smell of blood still lingered in the air; nowhere near as strong but it was a reminder of what had happened the night before."
    "Not that we needed it given the red smear still on the tiles. It was dry as far as I could tell, but cleaning it still wasn't something I was keen on doing."
    if BensonAround == True:
        play music fatherhood fadein 2.0
        "But then I heard something coming from the room next to us, where Roswell and Dean were."
        scene sittingroom with dissolve
        "It was the first time I'd bothered coming into this room, and part of me wondered how I'd missed it. Not that it had anything special going on, just a small room to just sit and relax in."
        "That said, as we entered I noticed immediately what the sound was. The sound of a soft singing coming from the older boar in the room."
        show oz neutral with dissolve
        "Oswin was sitting beside Roswell, looking up at us as we entered the room. As soon as he'd noticed us, he'd stopped, falling silent. For a moment we just stared at each other, then he stood slowly, dusting off his lab coat."
        stop music fadeout 2.0
        show oz pout
        oz "...Hello."
        mc "Hi..."
        "Again, more silence as I quickly looked to Orlando and then back to Oswin."
        show oz pout at left with ease
        show dragon sad at right with moveinright
        mc "What were you doing?"
        show oz neutral
        oz "Nothing. "
        show oz annoyed
        extend "Nothing at all."
        play music relaxed fadein 2.0
        mc "But I heard..."
        show oz pout
        "He sighed out, shaking his head and looking back down to Roswell."
        oz "I suppose I've been caught, haven't I? "
        show oz neutral
        extend "If you must know, I was visiting the deceased much in the same way I assume you two are here for."
        show dragon scared
        dragon "But they're our friends. Why are you here?"
        show oz pout
        oz "Just... resolving something in myself, shall we say."
        show dragon sad
        dragon "This is probably a bit presumptuous but... were you two related? You're both boars after all."
        oz "...No. "
        show oz neutral
        extend "At least not in any meaningful way."
        dragon "But... Only Roswell?"
        show oz annoyed
        oz "I don't feel I need to answer to you regarding this. "
        show oz neutral
        extend "But I will."
        show oz pout
        oz "Truth be told, why you're here is for the most part because of Roswell. Or more accurately his family."
        show dragon pout
        dragon "Okay...? But then why...?"
        show oz neutral
        oz "Because as someone who does not have any children of his own, seeing one so young die... "
        show oz annoyed
        extend "I'm not so callous to be upset of their passing too. "
        show oz pout
        extend "It just so happens that Roswell in particular I was at least aware of prior to this."
        mc "Did he know you too?"
        show oz neutral
        oz "Potentially. My dealings were primarily with his parents all things considered."
        show dragon sad
        dragon "Oh, well..."
        "Oswin shook his head, sighing out."
        show oz pout
        oz "Sorry, I should give you your time with your friends. "
        show oz neutral
        extend "If you'll need me, I'll be upstairs in the conservatory."
        hide oz with dissolve
        stop music fadeout 2.0
        "He left quickly, hands buried in his pockets and keeping his gaze forward."
        show dragon sad at center with ease
        "I looked to Orlando, unsure of what to say. He seemed shaken, but said nothing."
        "Turning to look at the doorway that Oswin left through, I wondered if my impression of him was right. Was he suffering like we were? Was his reaction to things happening coming from stress the same way it was happening for Tyson?"
    else:
        "Together we paused as we got closer, my eyes following it into the adjoining room. "
        extend "Taking Orlando's hand in mine, we entered the sitting room."
        scene sittingroom with dissolve
        show dragon sad with dissolve
        "The scent of blood was thick in the air, strong enough to blot out anything else."
    play music calm2 fadein 2.0
    "Carefully I stepped forward. I knew where I was heading mostly on smell alone even if I couldn't see both of them placed on their back on the floor, or even by the trail of blood that had been left in their wake as they'd been dragged to their resting places."
    "Orlando followed behind, and the two of us stopped next to Roswell first. "
    if BensonAround == True:
        extend "Maybe it was because Oswin was just here, or because he was closer, I don't really know."
    else:
        extend "Between the two of them, he was the one placed closer to the door, but making that walk felt like I'd walked a mile to reach him from where I'd entered the room."
    mc "Roswell..."
    "I looked down to his face, and if it wasn't for the large wound in his neck and shoulder, he'd look like he was sleeping. Maybe sick, maybe a little cold, but definitely in need of a bath."
    dragon "[mcname]? Are you okay...?"
    "Sitting down next to Roswell I crossed my legs, croaking out a reply."
    mc "I'm fine..."
    "The smell of his blood was sickening, making my stomach churn. I was surprising myself by how well I was coping from not losing my breakfast then and there seeing the combination of wound and the smell."
    "Orlando sat down next to me and kept to himself for a bit longer while I tried to decide if I wanted to check Roswell's pulse. I knew I wouldn't get anything, but there was some part of me that hoped in some way he would still be alive."
    dragon "You know my favorite memory of Roswell?"
    show dragon pout
    dragon "I remember... I remember one time he called Hoss out for not liking something I had made. Cookies I think. "
    show dragon sad
    extend "But he made it a huge lecture on snack foods until Hoss had to bribe him with candy to make him stop talking."
    mc "That's your favorite memory of Roswell?"
    dragon "I think so... "
    extend "It was just... very {i}him{/i}, right? That he'd use his intelligence to both defend something important to me, but also to trick someone else into giving him something he wanted."
    show dragon neutral
    dragon "But...{w=0.3} I don't think it ever came from a bad place, right? He'd always toe that line before taking it too far, but he always meant well."
    "I nodded slowly, thinking it over."
    mc "I think my favorite memory of Roswell was the first day we met. It happened so long ago, and we were both so young but... if that never happened we would've never become friends."
    show dragon pout
    dragon "I don't think that, [mcname]. I'm sure you would've crossed paths at some point, right? You were neighbors."
    mc "Maybe... But that day is still special to me."
    "Stealing another look at Roswell, I cracked a smile if a weak one."
    mc "Thank you for that day, Roswell."
    "Getting up I wandered over to Dean and sat down the same way. I noticed Orlando hesitated for a moment but he came and joined me in the same way he did before."
    mc "I knew Dean pretty well, I think."
    dragon "Better than I did. That's for sure."
    "I nodded slowly, reaching out and touching his arm. Maybe it was just that he was larger in stature than Roswell, but his injury didn't seem nearly as bad."
    mc "He was a good friend. Confusing sometimes, but a good friend."
    show dragon sad
    dragon "Confusing... how?"
    mc "I don't know... I think it was like..."
    "I sighed out, running a hand through my fur."
    mc "Tyson and I went out every now and again for like a road trip or something to get me out of the house, right?{w=0.3} But Dean probably did that more."
    show dragon scared
    dragon "Really? But then... about you two dating?"
    "Flashing him a smile, I looked back to Dean."
    mc "Dean always kept saying it wasn't a date because of one thing or another. Either something went wrong, or that it didn't go exactly how he'd pictured it, or someone else came along too."
    mc "But if I'm being honest, part of me thinks they were. Maybe not all of them, but enough to make me wonder if we'd been dating and I'd just been too dumb to realize it."
    show dragon sad
    dragon "Really? I would've thought that if it came to something like that, he'd be more... I dunno, forward?"
    mc "Yeah... Maybe..."
    "I clenched my fists as they rested in my lap. I felt stupid, and now I'd never know the answer because of what happened."
    mc "Hey... Orlando? I'm sorry to ask this but... uh..."
    "The words were hard, and I found myself choking them out on the verge of tears from where I'd worked myself up to."
    show dragon scared
    dragon "What... is it?"
    mc "Can... Can I have a couple moments alone with them just for a second? It won't be long, I just... uh..."
    show dragon sad
    "He stood, hands twitching in uncertainty."
    dragon "Okay... I'll just wait outside. If anything happens, uh... I'll um..."
    "The sentiment trailed off there, replaced instead by an affirming nod as he wandered towards the door."
    dragon "Take as long as you need, okay?"
    hide dragon with dissolve
    "Orlando closed the door to the room and no sooner had it closed I heard him sobbing, collapsing against the wall just outside the door."
    if bearroute == True:
        "I looked back to Dean, trying to will the tears to come to me. Trying desperately to open the floodgates that I'd been holding back for so long."
        mc "Dean... I'm sorry that this happened, that I... that we... uh..."
        "Wiping my face I tried again, starting with a deep breath and sighing it out to try and calm down. It didn't work."
        mc "I should've been better... This is my fault this happened and now you... you and Roswell are both..."
        "Maybe getting sadder was the trick to crying. Crying was meant to be normal but something just wasn't clicking, something just wasn't giving me that relief I needed."
        mc "I want this to all be a bad dream and that when I wake up, you'll be next to me in bed. We can have coffee and just cuddle. I could just... We could have a picnic by the river!"
        mc "But... But I think most importantly I just... I'm sorry that I wasn't a good boyfriend if that's what you saw me as."
        mc "I'm so, so sorry, Dean..."
        stop music fadeout 2.0
    elif boarroute == True:
        "I stood up and wandered back over to Roswell, kneeling next to him. My hands trembled as I reached out to touch the fur atop his head."
        mc "Roswell... I'm so sorry you... That I..."
        "The words caught in my throat, and I wondered if I was going to cry. The dam was threatening to break, but for whatever reason it never did."
        mc "I... I tried and... I'm sorry I couldn't... And now you and Dean..."
        "Sniffling I wiped my eyes, clenching my jaw as I stared at Roswell's face."
        mc "Some older brother I turned out to be, huh? I couldn't keep you safe, and I wasn't a great detective either."
        mc "I'm sorry, Roswell... I'm so, so sorry..."
        "I slumped next to him, whining softly."
        stop music fadeout 2.0
    else:
        pass
    "But then something in me snapped. Something that clicked into place suddenly that made all of my sadness ease off all at once."
    play music dark fadein 2.0
    "This wasn't my fault. None of this was my fault."
    "There was a spot on the floor that I'd started to focus on as my mind started to wander."
    mc "It... It wasn't my fault..."
    "My hands flexed, tensing and relaxing as a new feeling started to replace the sadness as I remained in that room."
    mc "Sal's fault... It was Sal..."
    "My fists clenched, soon after my jaw followed. Then the growling, the frown next. Sal took them away. Sal killed them."
    scene foyer
    show dragon cry
    with dissolve
    "Stepping out of the room I closed the door behind me. Maybe it was the smell of blood, but I was in a daze, focusing in on the sole thing that seemed to be the problem."
    dragon "Sorry [mcname], I'm just... I'll be okay, ugh..."
    "He'd resorted to wiping his face with the bottom of his shirt and he stood to face me."
    show dragon sad
    dragon "[mcname]...? What's wrong? You're growling..."
    if BensonAround == True:
        "He was ignored, my eyes trained on the door leading to the backyard. If Sal was out there, then I knew where I needed to go."
    else:
        "I looked through him towards the rest of the house, wondering if I could pick up Sal's scent somewhere to see if he'd moved to given he wasn't at the main road."
        "No telling if he was even here, but if he was, I'd find him."
    "Orlando grabbed me roughly and shook me by the shoulders."
    show dragon scared
    dragon "[mcname]! Snap out of it! What happened?"
    mc "Sal..."
    dragon "Sal? "
    stop music fadeout 2.0
    show dragon sad
    extend "What about Sal?"
    "I thought it over in my head. There was a solution, a permanent one, and at the moment I was blinded to all other possibilities and all sense of reason."
    play music tense fadein 2.0
    mc "I'm going to kill him."
    show dragon scared
    dragon "You can't!"
    "His grip on me tightened, as if trying to stop me from trying."
    show dragon mad
    dragon "I'm not going to let you make that mistake. I'm not going to let you put yourself in that sort of danger."
    mc "He killed two of our friends, Orlando! He killed them!"
    dragon "I know! "
    show dragon yell
    extend "But think about what you're saying! I'm just as upset as you, maybe you're more upset than me maybe but still!"
    show dragon sad
    dragon "I'm not about to resort to killing someone over this. Trust me, {i}please{/i}."
    if dragonroute == True:
        "He pulled me in quickly in a hug, rubbing my back."
        dragon "I'm so sorry, [mcname]. But this isn't going to make you feel better. This isn't what you want!"
    else:
        "He flashed me a quick smile before easing off enough to keep just one hand on my shoulder."
        dragon "You don't want this."
    "Amidst the growling I spat my reply in a cold tone. One that I'd only ever seen a couple of times from other people, none of which good."
    mc "You don't know what I fucking {i}want{/i}."
    show dragon scared
    "I shoved him away, my heart racing and breathing in deep."
    dragon "[mcname]... Please..."
    mc "Once he's dead... Once it's done then..."
    show dragon sad
    dragon "Then... what?"
    "The question made me pause."
    dragon "If you kill Sal... or try to anyway... What happens if you get killed instead?"
    "I looked to Orlando, waiting to see if he had any follow up."
    dragon "And if you died... I'd be sad, but imagine what Tyson would do. He'd try killing Sal, and either go to jail or die to Sal as well..."
    "My heart sank, resolve crippled but not dead."
    show dragon pout
    dragon "Killing just creates more killing. It creates more sadness, [mcname]. I've seen so much of it in my family and it always ends up this way."
    show dragon sad
    dragon "I want a life free of that. I want to be a baker, or someone so far removed from bloodshed that I never have to consider running into it."
    mc "Then what, Orlando? What do you expect me to do!?"
    "He gulped, unsure of where to put his hands once they'd been removed from me entirely. His reply came as a timid whisper, eyes darting to the floor."
    show dragon pout
    dragon "I don't know... "
    extend "But please... maybe just... try talking with him?"
    mc "You want me to {i}talk{/i} with him!?"
    show dragon mad
    dragon "Yes! I do! "
    extend "I get that you're hurting! We're all hurting! But if you have any respect for me, or even for the friendship you had with Sal, you'd at least talk with him first before deciding to execute him yourself."
    mc "He's not my friend after what he did!"
    show dragon yell
    dragon "Do you {i}really{/i} think that, [mcname]? Do you {i}really{/i} think the Sal you know would've just done that without a reason?"
    "I gritted my teeth, fighting desperately to stay mad. "
    extend "But I broke, sighing out and the madness faded away to a dull throb."
    mc "Fine. I'll talk to him first."
    show dragon sad
    dragon "Thank you..."
    mc "But if he admits to having done it on purpose, I don't know what I'll do."
    dragon "Hopefully it won't come to that."
    if BensonAround == True:
        mc "Well... I know he's at the pool, so that's where I'm going. Where are you headed?"
        dragon "I... I don't know. Maybe go find Hoss, maybe figure out something to do to keep my mind busy. I don't think I'm ready to confront Sal."
        mc "Okay."
        show dragon pout
        dragon "Maybe... Maybe I'll just wait here, stay out of trouble and somewhere people can find me in case something happens, right?"
        "Orlando reached out and took my hand, cradling it gently."
    else:
        mc "I'm going to start by searching the pool. I think Hoss would've checked there first given that's where he spent a lot of time. If he's not there, I'll come back inside after checking the greenhouse."
        show dragon pout
        dragon "Okay... Just be careful, okay? "
        extend "I'll... stay here, I think. Maybe hope Hoss stops by so I can stick close to someone. No offense but I don't feel like confronting Sal right now."
        "I looked away from him, towards the back door. He took the chance to take my hand, giving it a gentle squeeze."
    show dragon sad
    dragon "Be careful."
    mc "I will."
    scene mansionback with dissolve
    play audio outside fadein 2.0
    stop music fadeout 2.0
    "I stepped outside and immediately stopped in my tracks."
    if BensonAround == True:
        show lion mad at left
        show otter annoyed at right
        with dissolve
        lion "This wasn't part of the deal."
        "I noticed Benson's eyes flicking to me before going back to Hoss, his tone level."
        otter "Your understanding of the {i}deal{/i} was clearly mistaken then. "
        show otter neutral
        extend "Regardless, we have company. "
        show lion scared
        show otter smile
        extend "I believe you've had your questions answered for now, no?"
        show lion mad
        "Hoss looked to me quickly, then back to Benson."
        lion "Fine."
        hide lion with dissolve
        show otter neutral at center with ease
        "Hoss stomped around me and went inside, closing the door loudly behind him."
        mc "What was that about?"
        otter "A disagreement."
        mc "About...?"
        show otter pout
        "With a sigh, Benson looked out into the yard."
        otter "Truthfully it doesn't matter. But if you're that curious, he wished for information and I gave him exactly what he wanted. "
        show otter neutral
        extend "He just was unhappy with the resolution."
        "I looked beyond him towards the pool."
        mc "Is Sal still at the pool?"
        otter "Indeed."
        mc "Good."
        show otter pout
        otter "What are you intending to do, [mcname]?"
        mc "I don't know yet."
        show otter neutral
        otter "Then out of obligation I will advise you to exercise caution. Just in case."
        "I grunted, walking past Benson towards the pool."
    else:
        show lion sad with dissolve
        mc "Hoss?"
        lion "Hey. "
        show lion scared
        extend "Wait, where's Orlando?"
        mc "Inside. What are you doing here?"
        show lion sad
        lion "I found Sal. He's at the pool sorta just... moping. Hasn't moved from that spot in a while."
        mc "Good."
        "As I made to walk past him, Hoss grabbed me by the arm."
        lion "Where are you going?"
        mc "To {i}talk{/i}."
        show lion mad
        lion "You sure that's a good idea?"
        mc "I need to do it."
        show lion sad
        lion "Well... Alright. Just be careful, alright? Don't get too close?"
        "I grunted at him, pulling my arm free and continuing towards the pool."

label SalDay11CPool:
    $ croclove = 0 #Sal's affection points don't matter outside his route, use this as a counter for his death check. If 1, you've had the post-death scene. If 0, it hasn't happened yet.
    scene pool with dissolve
    "As I approached the fence to the pool I could see Sal sitting there, sitting on the bridge and staring into the water."
    "The feelings I had before started to well up, but I kept Orlando in mind as I passed through the gate. "
    extend "He didn't budge, or even acknowledge that I'd arrived."
    "I walked over to where he sat and stood beside him, my hands hurting from how tightly I had them balled up into fists."
    mc "Sal."
    show croc sad with dissolve
    "He didn't respond, his eyes still watching the water instead of looking at me directly."
    mc "I've come to... talk."
    "I looked him over and he seemed larger than I remembered. Maybe it was my mind telling me not to pick a fight here but the crocodile before me sighed, nodding slowly. His voice cracked when he spoke, slowly turning to face me."
    croc "...Okay."
    "He said nothing else, and I found myself folding my arms expecting him to at least apologize or something."
    mc "Do you have anything to say for yourself?"
    show croc cry
    croc "I... I'm sorry, [mcname]."
    mc "Well sorry is not going to cut it."
    croc "I know... "
    show croc sad
    extend "It should have been me."
    play music sad fadein 5.0
    "His whole form shuddered and slumped further over."
    show croc cry
    croc "Why...? Why wasn't it me?{w=0.3} Why did I...?{w=0.3} How did I...?{w=0.3} Why can't I remember?"
    mc "Is that true? You really don't remember?"
    croc "Please... Tell me what happened. I need to know. "
    show croc sad
    extend "Tyson wasn't lying. You could hear it in his voice. I killed them both, somehow, but how can I not remember that?"
    "He sighed again, hands clasped together in his lap. Looking to me again, only briefly before his gaze was peeled away elsewhere."
    "Mimicking him I sighed out, throwing my hands into my pockets and turning to stare into the water like he did. This was closer to the Sal I remembered, completely different to the Sal I witnessed murdering my friends."
    mc "Alright... I'll tell you."
    "I sat down far enough away that I was out of arm's reach and began to relay the events to him."
    scene black with dissolve
    "He didn't move while I explained how it all started, with the scream and all of us rushing down to see him with Roswell."
    "I watched his reflection in the water pale as I told him what he did to Dean when he tried to get in the way. "
    extend "Then what he did to Roswell soon after."
    "I explained what we did next, and I felt myself getting angry. Retelling the events was making me scared, and in turn enraged given he was nearby."
    "When I finished by explaining what had happened right before we met him that morning, he reacted."
    scene pool
    show croc scared
    with dissolve
    "It started with his eyes bulging in fear as he stared into the water. It continued by his shoulders heaving and shaking. And it ended with his voice cracking as he turned to me to speak."
    croc "I killed... Dean... and Roswell..."
    "He repeated the sentiment over and over, his voice cracking more as if he were sobbing between each intake of air. His breathing quickened, and he clutched his chest desperately."
    croc "My best friend... and your best friend... and I..."
    if BensonAround == True:
        croc "Benson, yesterday with the warning and..."
    else:
        croc "After Roswell's warning yesterday... it... did it... was that...?"
    croc "[mcname]... I know you said it's not going to cut it but..."
    mc "Sal? The only reason we're talking right now is because Orlando begged me to. "
    extend "You killed two people close to me, and the only way out of this I could see was to do to you what you did to them, so..."
    stop music fadeout 2.0
    "He nodded slowly, letting his hands hang in the space between his legs."
    stop audio fadeout 3.0
    show croc sad
    croc "Would that help? Would... that be enough? "
    show croc cry
    extend "Because if it is, then...{w=0.3} You can do it. "
    play music dark fadein 2.0
    extend "No amount of apology can make up for what I did."
    "I looked to him, angry enough that I wasn't sure that I could hold back from following through if I was given the opportunity."
    show croc sad
    croc "I... can only apologize over and over until my throat is sore. But if this happened once... It could happen again."
    show croc cry
    croc "That's why... to keep everyone else safe... "
    extend "I accept I might need to die."
    "I stood up, breathing in deep. Within the last hour I'd gone from grieving over the death of my friends, to being in a blind rage, to being talked down and back around to wanting to get back at the person who made it all happen."
    "But was this really the same person? At the same time, could we risk it?"
    "All things considered we were trapped, potentially for a while with someone that wants us dead."
    mc "Sal, I..."
    menu:
        "Kill Sal.":
            "I hesitated, a sudden flash of my dad crossing my mind. Was this the right thing to do? Was this what he would've done if it meant keeping me safe?"
            show croc sad
            "Sal looked at me, waiting. He wasn't putting up a fight, and if I wanted to, it'd be done."
            menu:
                "Kill Sal.":
                    $ SalDead = True
                    $ renpy.block_rollback()
                    mc "We're no longer friends. "
                    show croc scared
                    extend "We stopped being friends the moment you killed Dean, and made it worse by killing Roswell too."
                    "I glared at him as hard as I could and wished I'd brought something with me after all. Or met up with Tyson to see if he'd found a weapon of some kind."
                    mc "I {i}hate{/i} you."
                    "The growling had returned, my teeth were clenched and my fists soon to follow. I couldn't bring myself to yell, but instead the voice that came out of my mouth was barely recognizable as my own."
                    mc "You'd be better off dead."
                    show croc cry
                    croc "...I understand."
                    "I stood there for a moment, wondering what happened next. With no weapon, killing him was going to be difficult."
                    show croc sad
                    croc "[mcname]... All things considered... I don't think you'll be able to kill me."
                    "I shot him a look, but I let him continue."
                    show croc cry
                    croc "But don't worry. I'll... I'll handle it."
                    mc "Why should I trust you?"
                    croc "As it stands... I'd probably go to jail. If you killed me, then you'd be going to jail instead. "
                    show croc sad
                    extend "So...{w=0.3} Don't worry about it.{w=0.3} I'll handle it myself."
                    "It didn't sink in at first, but it dawned on me causing me to take a step back. "
                    extend "But all I could do was nod, turning away. Was this really alright?"
                    scene black with dissolve
                    "It didn't matter. What had been said, had been said."
                    "When I left the pool I looked towards the mansion. No one outside as far as I could see, and I hesitated heading back inside."
                    "But no matter how I looked at it, I couldn't avoid it forever."
                    jump Day11CAfterSal
                "Back down.":
                    stop music fadeout 2.0
                    pass
        "Forgive Sal.":
            stop music fadeout 2.0
            $ DavePride += 1
            pass
    "As he looked at me, awaiting an answer I couldn't bring myself to do it. Killing someone was wrong, wishing someone dead was just as bad."
    mc "I don't want you dead..."
    show croc scared
    croc "But... What if..."
    play music calm2 fadein 2.0
    "I sat back down, slightly closer only half sure that I was safe."
    mc "Killing you isn't going to bring them back, Sal. "
    extend "It hurts, and part of me still hates you for what you did but... was that really you?{w=0.3} The more I think on it the less sure I get."
    show croc scared
    croc "What... do you mean?"
    mc "Maybe something made you go insane? Maybe you had a reason after all? If you're not lying about not remembering then... I don't know where that leaves us."
    show croc sad
    croc "I... see."
    show croc pout
    "We looked at each other, and Sal sighed out, rubbing his arm."
    croc "How's Orlando?"
    mc "Terrified. "
    extend "Like everyone else."
    croc "I wouldn't be surprised if he doesn't come to talk to me after this. "
    show croc sad
    extend "But I don't think he'd run if I could build up the courage to face him."
    mc "What about the others?"
    show croc cry
    croc "I imagine that there's every chance that Tyson may want his pound of flesh, maybe Hoss. I'll have to deal with it when it happens."
    mc "But what if they... Y'know..."
    show croc sad
    croc "Then I'll give them the same option. It's only fair."
    "I shifted uncomfortably on the spot, thinking immediately of Tyson. Dad wouldn't want him going to jail, and I didn't either."
    "Hoss seemed open to considering things before taking any action so in that sense I'd probably need to talk with him too."
    show croc cry
    croc "Don't worry about it, [mcname]. What's done is done. I'm just going to sit here until I figure out what I can do. Or until the police arrive."
    mc "That might take a while. Hoss and I couldn't get reception even on the main road."
    croc "Well... Then I suppose I'll just wait here. Maybe if I'm lucky I can find something to use as a blanket for when it gets cold tonight."
    mc "You're planning on staying out here all night?"
    show croc pout
    croc "Do you feel safe with us being under the same roof?"
    "I couldn't rightly tell him yes, and my expression gave me away."
    show croc sad
    croc "Don't worry about it. I've been in worse living situations before, so I'll manage."
    mc "I'll... I'll check on you later I guess."
    show croc cry
    "He just nodded and went quiet. I waited, wondering if he was going to say anything else but it never came."
    scene black with dissolve
    stop music fadeout 2.0
    "Eventually I got up and left him alone. My mind was racing as to what had just happened and I was left as confused as ever."
    "I trudged towards the mansion, wondering if what I'd decided was the right thing after all. I couldn't bring myself to kill Sal, but the anger lingered and I had nowhere to direct it."
    "With a sigh, I headed back inside."

label Day11CAfterSal:
    scene foyer with dissolve
    play music calm fadein 2.0
    "As I walked back inside, I was shaking. Once I'd said it, there was no going back. It was too late to change what had happened now."
    if SalDead == False:
        "Dean and Roswell were dead, and what chance I had to channel how I was feeling was now gone. But oddly I didn't have any regrets. Not yet at least."
    show dragon sad with dissolve
    dragon "[mcname]...? You... Did talking to Sal go alright?"
    mc "Yeah..."
    "My voice was barely a squeak and I couldn't look him in the eye."
    dragon "And Sal? He's... he's still there?"
    "I kept my eyes trained on the ground and didn't respond. But maybe that was the problem, as the next moment Orlando grabbed me by the shoulders, shaking me gently."
    show dragon scared
    dragon "Sal's... still there, right?"
    "I looked him in the eye briefly before looking away. The moment I went to answer him he stepped back, terrified."
    dragon "...What did you do?"
    mc "Nothing!"
    "Throwing my hands up, I walked around him so I wasn't backed up against the backdoor."
    mc "We talked and that's all!"
    if SalDead == True:
        show dragon mad
        dragon "Liar. You did something to him, didn't you?"
        mc "I did {i}nothing{/i}."
        "I flashed him my hands, accompanied by an annoyed if sarcastic smile."
        mc "See? Hands are clean. He's fine, Orlando. He's fine, I'm fine, we're all just damn fine!"
        show dragon annoyed
        dragon "You're making it really hard to cope, [mcname]. I thought I could depend on you through this but now you're just acting like a jerk."
    else:
        show dragon sad
        dragon "Really? That's all?"
        mc "Yeah...{w=0.3} Now I don't know what to think."
        "Orlando took my hand and pulled me closer, watching carefully."
        show dragon pout
        dragon "You had me worried a little bit. I thought you might've done something that you might've regretted."
    mc "Sorry..."
    "I looked around the foyer, wondering why Orlando was still alone. He did say he'd stay here to not go missing, but even that seemed odd."
    mc "Where's Hoss?"
    show dragon sad
    dragon "Oh... He was here for a bit and then wandered off to go find Tyson."
    mc "And have you seen Tyson?"
    dragon "Not since we got back."
    "The idea that Tyson was missing made me worry. At least with Hoss he was somewhat accounted for. Thankfully, it didn't last as a problem for long."
    show wolf neutral at left
    show lion sad at right
    with dissolve
    mc "Ty!"
    "The sudden pang of relief made me rush over to him and hug him around the middle. But something was wrong, he didn't budge or even flinch."
    "He pushed me away firmly before folding his arms over his chest, looking between Hoss and Orlando."
    wolf "Where's the lizard?"
    dragon "Um... Outside? At the pool?"
    wolf "Alright. "
    show wolf annoyed
    extend "We're gonna have a meeting. Figure out what the fuck we're going to do."
    mc "Where have you been though, Ty?"
    wolf "Come on, I need some water or something. We're doing this in the kitchen."
    hide wolf with dissolve
    mc "Ty...?"
    "He was ignoring me, and I reached out in vain as he continued into the dining room without breaking stride."
    lion "How are you two holding up?"
    dragon "Fine, I suppose..."
    mc "Yeah... I'm fine, too..."
    "I was still staring at the doorway Ty had disappeared through. Had I done something wrong? Had something happened?"
    lion "Well, as far as we know, nothing has gotten any worse so that's a plus. "
    extend "Not that it's gotten any better, either."
    dragon "So we're having a meeting then? Is Tyson just deciding things now?"
    show lion neutral
    lion "Maybe, but someone should be taking charge here. Either way, the idea is a good one."
    mc "Maybe... "
    scene diningroom with dissolve
    if BensonAround == True:
        "We followed Tyson, spotting Benson already in the dining room."
        show otter neutral with dissolve
        otter "Gathering together, are we?"
        mc "Yeah. Looks like it. Tyson wanted to have a meeting."
        show otter pout
        otter "Very well. I'll go inform Master Oswin. "
        show otter neutral
        extend "I'll assume he'll kick up a fuss if he's not included, and given this affects us all it would be best if we were all in attendance, no?"
        mc "Sure, okay. I'll uh... tell Tyson?"
        show otter smile
        otter "I shall not take long to retrieve him."
        hide otter with dissolve
        "Benson wandered out of the dining room and out of sight. Meanwhile I looked to Hoss and Orlando."
        show lion sad at left
        show dragon scared at right
        with dissolve
        lion "Pushy, isn't he?"
        dragon "I guess what he said makes sense though. "
        show dragon sad
        extend "Hopefully Tyson doesn't mind? I think I need a break from people being all..."
        "He gestured with his hands to fill in the rest of his sentiment."
        mc "It'll be fine, right?"
        show lion neutral
        lion "Only one way to find out."
    else:
        "We filed into the dining room behind Tyson. Although it seemed he'd moved on ahead to the kitchen without us."
        show lion sad at left
        show dragon sad at right
        with dissolve
        lion "He's not wasting any time, is he?"
        mc "Seems that way, huh?"
        dragon "Does he seem off to anyone else? More than the usual Tyson sorta way?"
        show lion annoyed
        lion "I've picked up on it too. I don't know what his problem is, but maybe this is just how he copes. "
        show lion sad
        extend "But ignoring [mcname] like that was... odd."
        "I felt relieved that I wasn't the only one that noticed it, but there still wasn't a reason why."
        mc "Do you think I did something wrong?"
        show lion annoyed
        lion "Did you?"
        if SalDead == True:
            "I thought back to what happened at the pool, shooting Hoss a firm look."
            mc "No."
            show lion pout
        else:
            mc "Not... that I know of?"
            show lion sad
        lion "Okay then..."
        show dragon scared
        dragon "Maybe he'll tell us during this meeting? Or at the very least tell [mcname] in private. He might not be aware that he's doing it at all."

label Day11CKitchenMeeting:
    scene kitchen with dissolve
    stop music fadeout 2.0
    if OswinDead == True:
        "As we stepped into the kitchen, Tyson was pacing. He took a couple more steps before noticing we were there, shoving something quickly into his pocket."
    else:
        "As we stepped into the kitchen, Tyson was leaning against the kitchen bench deep in thought. When he noticed us, he straightened suddenly."
    show wolf neutral with dissolve
    wolf "Alright, let's get this over with."
    show lion sad at left
    show dragon sad at right
    with dissolve
    play music tense fadein 2.0
    if BensonAround == True:
        dragon "Wait, Benson is grabbing Oswin now."
        show wolf annoyed
        wolf "Why the fuck is he doing that?"
        mc "Oh, when I said we were having a meeting he kinda invited himself."
        show wolf pout
        wolf "Well I'm not waiting. Fuck 'em."
    else:
        lion "Sure we're good to just start? We don't need to prepare anything or?"
        show wolf annoyed
        wolf "Nothing to prepare. I just want to get this over with."
        dragon "Well... Alright..."
    "Tyson leaned back on the kitchen bench, looking at each of us in turn."
    show wolf mad
    wolf "Alright. So I have a couple things I wanna go over."
    "I shrank back against the fridge, letting him speak. Meanwhile Hoss and Orlando took up places around the kitchen."
    show wolf annoyed
    wolf "First up, what's happening with Sal?"
    lion "He's at the pool, or was when I was outside last."
    if SalDead == True:
        "I kept quiet, not wanting to say what had happened at the pool. If everything went as Sal said it would, then he wasn't a problem anymore."
    else:
        mc "Far as I know he's planning on spending the night out there."
    show wolf pout
    wolf "Well great, so long as we know where he is I guess that's fine. I don't think he'll go making any moves during the day at least."
    show wolf neutral
    wolf "Which is what I wanted to bring up next. I'm fuckin' tired with how much sleep I got last night, so what's the plan for tonight?"
    dragon "I'm guessing because we can't get in contact with anyone? Otherwise the police would've arrived. Which means our only option is to all be in the same room again tonight, right?"
    wolf "Right."
    lion "Bunking up together again? Not that I'm against it but is that our only option?"
    show wolf pout
    wolf "Not unless we wanted to do rotating shifts as lookout."
    mc "I don't really mind but... does this mean we can maybe prepare a bit better so we're comfortable?"
    "The others looked to Tyson and he was now not hiding the fact he was ignoring me, looking elsewhere."
    show lion annoyed
    lion "Hey, knock that off. He asked you a question."
    show wolf neutral
    wolf "I heard him."
    show dragon annoyed
    dragon "And...? [mcname] has feelings too y'know."
    show wolf pout
    wolf "{i}Fine.{/i}{w=0.3} We can get some blankets or something or move some mattresses into the same room. Happy?"
    "I whined, but nodded slowly."
    if BensonAround == True:
        hide lion
        hide dragon
        with dissolve
        "No sooner had I done so that the door to the kitchen swung open with Benson leading Oswin through."
        show wolf annoyed
        show oz neutral at left
        show otter neutral at right
        with dissolve
        oz "Having a meeting on what to do, are we? Well, far be it from me to be excluded from such a thing."
        "Tyson just grunted, shooting Oswin a sour look."
        show oz pout
        oz "Now...{w=0.3} What have you lot discussed without us?"
        mc "Sal came up, and sleeping arrangements really. Nothing else yet."
        show otter pout
        otter "Ah, then might I suggest we discuss about what to do with the deceased? All things considering they should be returned to their families so burial is out of the question."
        show oz neutral
        show otter neutral
        otter "However, storing them within the freezer will keep them... 'preserved' in a sense. It shouldn't harm any of the food stores we have in there, at least this hasn't been an issue in any other instance this... arrangement has needed to be made."
        show oz pout
        oz "To be clear, he isn't referring to this specific freezer."
        show otter pout
        otter "Oh heavens, no. "
        show otter smile
        extend "But this is not the first time I've had to personally handle the storage of a body. "
        show otter neutral
        extend "From a life lived long ago to be sure, but nonetheless relevant experience for the situation at hand."
        mc "Were you a doctor as well?"
        show otter pout
        otter "No."
        show oz smile
        oz "Quite the opposite. "
        show oz pout
        extend "But that's a story for another time. For now, I can confirm that the degradation of a body would be sufficient in a freezer such as this one."
    else:
        show lion sad
        lion "I hate to bring this up as our next topic, but... What do we do about Dean and Roswell?"
        mc "As in..."
        show dragon sad
        dragon "Oh... Right. Well... We still have the plan from this morning with a freezer?"
        show wolf annoyed
        wolf "There's no better plan for that?"
        mc "Best we can do is to just hope that the food doesn't go bad, right?"
        show dragon pout
        dragon "It should be fine. Hopefully. We don't have any other real alternatives unless we want to put up with the smell."
        "He trailed off, leaving the comment there."
    hide lion
    hide wolf
    hide otter
    hide dragon
    hide oz
    with dissolve
    "Every one of us was quiet, wondering what was next. The immediate problems we had a solution to, but the bigger ones we were still drawing up blank."
    "Was there a way to contact someone? I thought about maybe a signal flare before I remembered that if we could just solve the reception problem we could get someone to help out with the road problem."
    "A few times a couple of us went to say something before going back to contemplating things, silent."
    "For me though, I had something on my mind, something that I needed an answer to. I just didn't know how best to broach the subject."
    if BensonAround == True:
        show lion sad at left
        show otter neutral at right
        with dissolve
        if lionroute == True:
            mc "So that thing you told me about yesterday, Hoss."
            show lion scared
            "His eyes darted from me to Benson quickly."
            show otter pout
            lion "That's... uh..."
            otter "Ah, I wonder if you'd told him about... {i}that{/i} already, hm?"
            show lion sad
            lion "He wanted to know."
            show otter neutral
            otter "I suppose that saves some time then."
            mc "But what I don't get is why."
            show oz pout with dissolve
            oz "Why anything, [mcname]? "
            extend "If this is what I think it's about, then you're just now discovering one of the many things available to myself to keep my privacy intact."
            show lion annoyed
            lion "Even if it's illegal?"
            show oz smile
            oz "Oh, I have no issues with that. With enough financing, the people that care can be made to look the other way."
            show otter pout
            otter "However, there are bigger issues at hand given that the one you have likely hasn't been repaired. "
            show otter neutral
            extend "Am I correct?"
            show lion sad
            lion "Right. I don't know how to repair one of these."
            mc "So this one isn't the reason why we have no phone signal?"
            show oz annoyed
            oz "Of course not. But that isn't stopping someone else from using one. "
            show oz pout
            extend "Or potentially using a remote detonation device to cause a landslide in the absence of one."
        else:
            mc "Hoss? Benson?"
            otter "What is it?"
            mc "There's something that's been bothering me since yesterday. I didn't really know what to think of it, and part of me kinda forgot with everything that had been happening."
            show otter pout
            otter "Oh?"
            show lion scared
            lion "What's wrong? Did something else happen?"
            mc "Not... that I know of. But I wanted to ask you about that thing you had yesterday. The thingy that Benson got you to do."
            show otter annoyed
            otter "Excuse me?"
            lion "Uh... Right. That thing."
            "I looked to Orlando and Ty, both looking curious as to what I was talking about, but stayed quiet. As for Oswin, he was seemingly making himself a cup of tea."
            mc "So... What did Benson ask you to do? What was the thing?"
            otter "Yes, Hoss. I'd be {i}very{/i} interested to know what it was that I asked you to do for me."
            show lion annoyed
            "Hoss bared his teeth at me, grumbling."
            lion "It was... nothing. Don't worry about it."
            otter "I think we're long past this charade, m'boy. "
            show otter neutral
            extend "It is true, I asked him to perform a task for me. To repair an old device of mine. "
            show otter smile
            extend "Although I don't think he knew exactly what he was getting into when I asked him."
            mc "Okay but... What was it? What does it do?"
            "I posed the question to Benson, before turning to Hoss when it was clear he wasn't going to be the one to answer me. Hoss however realized he was put on the spot and continued to grumble, jaw clenched."
            lion "...It's an ECM jammer."
            mc "A... what?"
            show otter neutral
            otter "It stands for 'Electronic Countermeasure'. In essence it's a jamming device."
            mc "So then the lack of cellphone reception...!"
            show otter pout
            "Benson shook his head."
            otter "I can see why you'd think that, but no. This isn't my doing, nor is it this device's doing."
            show lion mad
            lion "And why not? You had one, why not others? Why ask me to try and repair it?"
            show otter neutral
            show oz neutral with dissolve
            oz "I can field that one. "
            show oz pout
            extend "Keeping such things is very illegal. But it just so happens that with enough financial lubrication anything can be overlooked. "
            show oz neutral
            extend "But there are reasons beyond that."
            mc "Such as... what?"
            otter "To stop prying eyes, for one. But stopping telecommunications is one of their known uses."
            oz "Indeed. But more than that, it acts as a deterrent for anyone to wish to say, use a remote detonator to cause a landslide."
        mc "But that happened anyway!"
    else:
        show lion sad with dissolve
        if lionroute == True:
            mc "Hoss?"
            lion "What's up?"
            mc "Is... Is the reason we don't have phone reception because of, uh... Y'know."
            "He shook his head."
            lion "I couldn't end up repairing it, remember?"
        else:
            mc "I... want to know something, Hoss."
            lion "Sure. What did you want to know?"
            mc "That thing you had yesterday morning. What was it?"
            show lion scared
            lion "What...? "
            show lion sad
            extend "Right. That, uh... Well that's..."
        show wolf pout at left
        show dragon sad at right
        with dissolve
        wolf "Can we cut the crap and just say what it is already?"
        show lion mad
        lion "It's a radio jammer. Stops phone signals and stuff."
        show dragon scared
        dragon "Wait, so would that be the reason why we can't contact the police? That our phones aren't working?"
        show wolf mad
        wolf "Better fuckin' not be. Cause if it is..."
        "Tyson's eyes bulged as he looked at Hoss."
        show lion yell
        lion "Well it's a damn good thing that I couldn't repair it, huh?"
        show dragon sad
        dragon "But if you couldn't repair it, then why doesn't the phone work?"
        show lion sad
        lion "Maybe someone else has one? That said, if they had one that'd cause a whole bunch of other problems."
        show wolf pout
        wolf "Like what?"
        lion "Well... These things block signals, right? Anything from phones, sometimes radio signals, and... well..."
        dragon "...bombs?"
        show wolf scared
        wolf "Fuck off. Is that why the bomb went off?"
        mc "But wouldn't one of these jammers like... stop it from going off?"
    show lion sad
    lion "Look, it doesn't matter. Sure, I shouldn't have hid this from everyone, but as far as we know someone either is probably using one of these jammers to keep us here or we're just very unlucky."
    mc "I don't think it's just being unlucky..."
    show lion mad
    lion "Neither do I."
    if BensonAround == True:
        hide oz
        hide otter
        with dissolve
        show wolf pout
        show dragon sad at right
        with dissolve
    else:
        pass
    "Tyson sighed, shaking his head."
    show wolf neutral
    wolf "Well if we're fucked in that regard, best we can do is wait it out. "
    show wolf annoyed
    extend "That or we go find a way through the forest."
    show dragon sad
    dragon "If we had the choice I'd rather... not. Just in case we get lost, right? If Dean were still... uh..."
    show wolf sad
    show lion sad
    "The room went quiet, all of us looking to the floor."
    mc "Okay, well... at least we have food, and shelter. "
    extend "But if it's alright with everyone... I think I'm done for the day. I'm going to go sleep."
    show wolf annoyed
    show lion scared
    lion "But... [mcname]!"
    mc "No, I just... I need a nap. Something."
    "I sighed out, shaking my head and keeping my eyes trained on the floor."
    mc "I'm almost at the point that if I don't care if I'm in danger. I'm tired, I'm confused, I'm sad and just..."
    "Slumping my shoulders I breathed out, turning on my heel and headed out of the kitchen."
    scene foyer with dissolve
    "As I trudged forward I reached the base of the stairs before stopping, thinking things over. "
    if BensonAround == True:
        extend "But that's when I heard the footsteps behind me. I riled myself up assuming it was Orlando or Tyson chasing after me."
        mc "Leave me alone! I'm fine."
        show oz pout with dissolve
        oz "Yes, I'm sure you're completely fine with how you're lashing out at me, [mcname]."
        mc "Oh... It's you."
        show oz neutral
        oz "We should have a chat. Your friends are concerned about you and don't know how to help."
        mc "Well I don't {i}want{/i} to talk."
        show oz annoyed
        oz "Then far be it from me to force you to do anything, but you're causing undue panic."
        mc "Sure, and Tyson's ignoring me, two of my friends are dead, another is isolating himself at the pool for being the one behind it. I'm {i}so sorry{/i} if I'm not being the most mindful right now."
        show oz neutral
        "I was growling at him, choosing to focus my attention his way for lack of any other option."
        mc "So just... fuck off. I don't care."
        "He just watched me, quirking a brow before stepping forward calmly. His hands were held in his pockets right up until he lashed out and grabbed me roughly by the ear."
        show oz mad
        oz "Now you listen here, boy. You listen {i}well{/i}."
        "I whined, his grip rough and tight. He pulled me closer, voice brought down to a whisper, the rage in his voice clear."
        oz "Are you {i}wanting{/i} to make things difficult? Do you {i}want{/i} to stress those you care about out that much, that they make poor decisions?"
        mc "N-No...?"
        oz "Then pull yourself together, [mcname]. Pull yourself together damn quick."
        "He let go of my ear and pulled me in close, hugging me tight. Something broke in me and I whined loud and unrestrained."
        show oz neutral
        oz "Times are tough, boy. But don't fight this fight alone. Take it from someone that made the same mistake."
        "He let me go and took a step back, watching me carefully. I was trembling under his gaze, and eventually he turned and left back in the direction of the kitchen."
        hide oz with dissolve
        "What had just happened? Why had Oswin done that? I braced myself on the railing of the stairs."
        if bearroute == True:
            "I looked towards the sitting room, breathing hastening. I wanted Dean. I needed Dean."
            "But Dean was gone."
        elif boarroute == True:
            "What would Roswell do? What would he say? He was smart and would've known what to do here. My chest started to hurt and I found it hard to breathe."
            "He wasn't around for me to ask anymore."
        elif wolfroute == True:
            "My heart ached in a way I hadn't felt in a long time. I wasn't sure how much of it was because of what was happening or because of some deeper yearning I was feeling."
            "I wanted my older brother. I wanted Tyson."
        elif lionroute == True:
            "For the briefest of moments I thought back to Hoss. Thinking of him was compounding on my stress, the confusion he brought making things worse."
            "But deep down I wanted him nearby. I put faith in him being able to find some positive spin on this that would take my mind off things."
        elif dragonroute == True:
            "Orlando would know what to say. Or even if he didn't, a good cuddle would be his go-to. But the thought of that, right after being hugged by Oswin didn't sit right with me."
            "Despite that, I wanted him next to me, telling me everything would be alright."
        else:
            "DEBUG. REPORT TO GRIZZ."
        scene black with dissolve
        "Choking on my thoughts, I stumbled up the stairs in a daze until I made my way to bed."

    else:
        extend "I felt numb to what was happening. Was I that selfish that I felt like someone should be taking care of me?"
        "Or was I just that far gone that I needed help, that I wanted someone to tell me it was going to be alright?"
        "Each step up towards my bedroom was a struggle, my ears trained on trying to hear anything other than my heart pounding in my chest."
        scene black with dissolve
        "I collapsed on the bed and promptly passed out."

label Day11Cafternoon:
    "I don't know how long I slept for. Minutes, hours, it could've even been days."
    "All that greeted me when I closed my eyes was an endless, heavy black."
    "At some point I heard movement in my room, or at least somewhere nearby. It wasn't enough to wake me, or maybe I was too tired to care. Part of me wondered if I had resigned myself to my fate if it was something more dangerous."
    scene bedroom with dissolve
    "But eventually, I opened my eyes."
    show wolf neutral with dissolve
    mc "Huh...? Oh... It's you."
    "I rolled over onto my side, facing away from him. I didn't know why he was here, and part of me was still hurt that he was ignoring me before."
    show wolf pout
    wolf "You doing okay?"
    mc "Go away."
    wolf "Okay... So... I was an asshole."
    "He wandered over and sat on the bed, dropping his weight down on it enough to make me look back at him."
    mc "It hurt. I don't know why you were ignoring me during the meeting but... What did I do wrong?"
    show wolf sad
    wolf "Nothing, just... I needed to focus more on the others. Something's... not sitting right with me."
    "I stayed quiet, opting instead to just listen."
    show wolf annoyed
    wolf "I'm gonna ask you something, and you have to be honest with me. No bullshit, alright?"
    mc "Okay...?"
    if OswinDead == True:
        wolf "What's your name?"
        mc "[mcname]...? Why?"
        wolf "What's your dad's name?"
        mc "Um... His name was David, why?"
        wolf "And your driver's license has your name on it, right? First and last name?"
        mc "Yeah...?"
        wolf "Then we have a fuckin' problem."
        mc "What's... the problem?"
        "I rolled over to look at him and he seemed troubled, hand shoved into his pocket seemingly thinking it over."
        wolf "Probably better if I show you."
        "He pulled something out of his pocket, it seemed like a card of some sort and pushed it into my hand."
        wolf "Don't freak out."
        "As he eased his hand away I sat up, looking at the card he handed to me. My eyes widened as I realized what it was, a chill running down my spine."
        "In my hand was a driver's license, a familiar face in the picture accompanying it. Parts of it seemed nicked and chewed on, but otherwise everything down to the name was legible."
        mc "But... It can't be."
        show wolf mad
        wolf "You didn't bring this with you, yeah?"
        mc "No..."
        wolf "Then how the fuck did it get here, [mcname]?"
        "I ran my fingers over the embossed name, each letter of the name making it clearer that I wasn't imagining it."
        mc "I don't know..."
        show wolf annoyed
        wolf "Well... Unless there's another family using your last name, that are also hyenas then something fucked is going on."
        mc "I don't... I mean... But... What do we do?"
        show wolf mad
        wolf "The fuck if I know, but I know I'm not trusting any of those other fucks with you."
        mc "Why not? They're my friends, and..."
        "Ty took both of my hands, looking me in the eye."
        wolf "You're the only family I have left now. I'm not about to let you get off'd just because someone decides to take advantage. Double check that license again and if you're absolutely sure it's real, I'll tell you what we're gonna do."
        "I flicked the card over once Ty had eased off, running over the details again."
        "David Halloway, Male, 5'10... It even had our address along with his full birthday. "
        extend "Without a doubt, this was my dad's license."
        mc "Ty... It's real. But I don't know why it's here."
        show wolf annoyed
        wolf "That's what I thought. "
        show wolf mad
        extend "Saw something scurrying around with it before and it ran off after dropping it. But that means he was here, right?"
        mc "Was? Do you think... Do you think he could still be... alive?"
        show wolf sad
        wolf "I don't think so."
        mc "But... How else would it have gotten here? We should at least search, right?"
        "Tyson grumbled, shaking his head."
        wolf "If you want to search, I'll give you a day. One day. "
        show wolf mad
        extend "But after that we're getting out of here. Just you and me. Fuck everyone else."
        mc "But Ty..."
        show wolf pout
        wolf "No buts. I'm keeping you safe. You may hate me for it, but I'm not risking you dying over it."
        mc "Even if I don't want to go?"
        show wolf neutral
        wolf "You think you could stop me?"
        "I shrank into myself, knowing that I couldn't even on a good day."
        if wolfroute == True:
            "I'd stopped him going out into the forest, but that was different. I didn't so much stop him as knew what buttons to push."
            "But this? This was different."
        "My words came out meek and feeble, and I nodded while I kept my gaze averted."
        mc "Okay..."
        show wolf pout
        wolf "Still want some space for now? Hungry? It's way past dinner."
        "Admittedly I wasn't all that hungry, especially now after seeing Dad's face on his license. I was just as scared though, wondering what was going to happen in the next couple of days."
        wolf "Well, if you want something to eat, I'll be around. Let me know and I'll take you down to the kitchen and fix something up for you."
        mc "There isn't leftovers?"
        wolf "You think I'm gonna let you eat what the others made? Fuck that."
        "I whined, thinking back to Orlando's cooking. Tyson's cooking was functional if a little bland outside a couple things, paling in comparison to Orlando's skill."
        wolf "Rest up, we'll talk later."
        hide wolf with dissolve
        "He left the room without waiting for a reply from me, the door clicking behind him gently."
        "I looked at the license Ty had found, wondering how it had gotten here. There was one person alone who would've known anything about this, and he was now dead."
        "Not that I'd told anyone about that, but I knew one place that might hold some answers."
    else:
        wolf "Did you know about Orlando's family?"
        mc "No... I just always assumed they were bankers. Why would I think anything else if that's what he told me?"
        show wolf pout
        "He sighed out, shaking his head."
        wolf "Look... I'm gonna say something, and it's either going to hurt or just straight up suck."
        mc "Okay...?"
        "I readied myself, wondering what it could be."
        show wolf neutral
        wolf "I love you."
        if wolfroute == True:
            "He was right. It did suck, maybe even hurt a little. Not like this. I didn't wanna be told that like this, not under these circumstances."
        else:
            "I blinked at him, my heartbeat hastening in my chest before becoming a dull throb. Being told under these circumstances paled in what I hoped would have been a more romantic way."
            "Hell, I assumed Ty would be the last person telling me this, but... he did."
        mc "Oh..."
        show wolf pout
        wolf "Don't go rushing to say it back or anything."
        mc "I..."
        "My voice trailed off, unsure of what I should say, or if I was allowed to say anything back to that."
        wolf "Point is... "
        show wolf neutral
        extend "Now more than ever I've got your back. "
        extend "But I don't trust the others. Not after what happened."
        mc "What are you trying to say, Ty? That one of them is going to try killing?"
        show wolf mad
        wolf "Yeah. And I don't want those fuckers thinking you're an easy target."
        mc "But they wouldn't!"
        wolf "And we saw what happened with Sal. I don't know if he suddenly went nuts or was drugged with something and was tripping... "
        show wolf neutral
        extend "Point is, no reason the others couldn't."
        mc "Including you?"
        show wolf annoyed
        wolf "Yeah, including me. But that's why I wanna take you and bail. Head back home just the two of us."
        mc "But I can't... Not without the others."
        wolf "And I'm letting you know right now, one way or another, I'm going to be dragging your ass home. "
        extend "I ain't breaking the promise I made to your dad."
        "I whined, shaking my head."
        mc "Can... Can I have a day to think about it?"
        show wolf neutral
        wolf "A day, huh?"
        mc "Just one. Just to... think about it?"
        show wolf annoyed
        wolf "I'm not giving you a choice if you're coming or not."
        "He got up off the bed and sighed out."
        show wolf pout
        wolf "Look, it's late. If you want to eat anything find me. I'll take you down to the kitchen and make you something."
        mc "You guys didn't already have dinner?"
        show wolf neutral
        wolf "I ate. Made my own food cause I wasn't gonna let the other two mess with it. Just like how I'm not letting you eat anything you didn't see getting made."
        mc "Oh... But I like Orlando's cooking."
        show wolf annoyed
        wolf "And we both like you alive, [mcname]."
        hide wolf with dissolve
        "He left before I could retort, closing the door behind him."
        "I didn't like what position he left me in, and I wondered what options I had. Thinking back to earlier, to Oswin, I wondered what he'd say."
        "We were meant to have a meeting tonight anyway, but all things considered perhaps he'd be willing to show me sooner?"


label Day11COzLab:
        scene conservatory with dissolve
        stop music fadeout 2.0
        "I made my way to the conservatory, figuring I'd just trace my steps back."
        if OswinDead == True:
            "The place was empty, and I let out a breath I had apparently been holding. This was my secret for now, at least until I had answers."
            "Maybe dad was alive, maybe he wasn't, but there was a chance, right? If this was Oswin's house, and dad had been here, there had to be something in the way of a clue, right?"
            scene black with dissolve
            play music dark fadein 2.0
            "I clutched dad's license tight in my pocket as I stepped into the dark."
            mc "I'm coming, dad."
            "I breathed in and raced forward, entering the library and throwing caution to the wind. Everything was how I'd left it, and I made my way down to the door and stepped through it to the corridor beyond."
            "But I almost retched the moment I did, the smell of something bad hitting my nose."
            "It could only be one thing, and it was suffocating the air of any other scent, it branding my nose even after I covered it with my arm."
            scene labrat1 with dissolve
            "The smell got worse the moment I stepped in, my eyes darting to the corner where Oswin lay. The knife still in his chest, blood dried and his body already paled and rigid."
            "Light from his computer was still casting a sickly glow about the place, long shadows cast along the floor."
            mc "There has to be something here..."
            rat "THERE'S NOTHING FOR YOU HERE."
            "I froze, eyes darting around looking for the voice. Familiar, robotic, and something I associated with Oswin when he spoke to me through the intercom."
            rat "LEAVE."
            mc "W-Who's there?"
            "Very quickly the shadows in the room moved, the sound of scurrying starting and coming to a sudden stop."
            rat "YOU SHOULD NOT HAVE COME HERE. NOT AFTER WHAT YOU DID TO MY MASTER."
            mc "Your..."
            scene labrat2 with dissolve
            "That's when I spotted the beady eyes watching me from the desk next to Oswin's body. The ragged body of something hunched over, a large metal collar bound to its neck with a speaker attached to it."
            "I gulped, looking at the rat as it stared at me, tail whipping about behind it."
            rat "ARE YOU LISTENING?"
            "The tone of the voice changed suddenly, although it kept most of its anger."
            rat "GET OUT."
            mc "You're... a rat! And you're talking!"
            rat "I HOPE YOU'RE HAPPY, DAVID HALLOWAY JUNIOR."
            mc "W-What...? Happy? No! I..."
            rat "I HOPE YOU'RE HAPPY THAT YOU KILLED MY MASTER. BECAUSE NOW?"
            "A rattled laughter came out of the speaker attached to his collar. The rat's whole form shifting and shuddering as it convulsed in glee."
            rat "BECAUSE NOW... I'M GOING TO TAKE {i}EVERYTHING{/i} FROM YOU."
            "I took a step back, a chill running down my spine and the scent of Oswin's body hitting me again."
            "As much as I wanted to run I was frozen in place, staring at the rat now laughing once more through the speaker."
            rat "YOUR LIFELINE IS CUT, YOUR WAY OUT LIMITED. "
            extend "YOU'RE GOING TO DIE IN THIS PLACE WITHOUT EVEN KNOWING WHY."
            mc "How do you know my name!? Who are you!?"
            scene labrat1 with dissolve
            "I cried out in vain as the rat backed away into the shadows, disappearing entirely. He was gone before I could lunge at him and stop him from escaping."
            "My heartbeat sped up and I looked around, backing up towards the door to the lab. Just as my hand reached the door the lights flickered briefly before cutting out entirely."
            scene black
            stop music fadeout 2.0
            "It was dark, a deep and heavy darkness that I was left in. Dark enough that I couldn't see the hands in front of my face and it was making it hard to breathe."
            "I began to run, tripping over my feet as I got back to the library."
            scene library with dissolve
            play music dark fadein 2.0
            "Collapsing to the floor I scrambled towards the table, turning back to look at the door, thrown open. I wondered if something was going to follow me."
            "But nothing came, the only sound echoing in the room was the sound of my heart beating frantically in my chest. Loud enough to drown out my breathing as I panicked."
            "Had I just hallucinated that rat talking? Had what it said just been an empty threat because I was stressed?"
            "That's all it must've been, right? Stress? I laughed, and I laughed hard. Hard enough to double over and clutch my stomach when it hurt to breathe, but I couldn't keep it going. I devolved down into empty sobs soon enough."
            scene black with dissolve
            "I shut my eyes trying to block it all out, block everything out. Maybe I could fix this somehow, maybe I could go to the vault and try and open it?"
            "Shaking I pulled myself up and continued back towards the conservatory."
            scene conservatory with dissolve
            "Empty and quiet. Light filtering in from outside even if it wasn't all that much. My eyes had adjusted somewhat but I felt around in the darkness in case I ran into something."
            scene foyer with dissolve
            "Then I got to the base of the stairs and looked around. It was still quiet, I half expected Tyson to be around or Hoss, or Orlando. Anyone."
            "My attention went to the door leading into the sitting room. Where Dean and Roswell were the last time I saw them. Had they been moved to the freezer? Were they still there?"
            "I hugged myself as I hung my head, heading towards the basement."
            scene vault with dissolve
            "When I reached the vault, I already knew something was wrong."
            "I shivered, cold. There was a ringing in my ears from just how quiet it was."
            "But that paled in comparison to what I'd come to realize. "
            extend "The vault was offline. Pressing the buttons did nothing, the display held nothing on it either."
            "My lifeline had been cut."
            scene black with dissolve
            "The rat had followed through on its threat. Somehow, and I didn't understand."
            "Sure, my friends called me [mcname], but that was just easier than having to always question if they were talking to me or my dad."
            "It wasn't exactly something that came up when introducing myself, and this was the first time I'd met this rat."
            "I didn't know what was going on, or even why. Before I realized I was moving I was on auto-pilot back to my room."
            jump Day11CNight
        else:
            "As I stepped in though... "
            play music calm fadein 2.0
            show oz neutral with dissolve
            extend "Oswin was there, just looking out the window."
            mc "Um..."
            "He looked at me curious, gesturing me to come closer."
            oz "You slept the day away. Are you feeling better?"
            mc "A little."
            show oz pout
            oz "Everyone's on edge, moreso after your departure. Your Orlando and Tyson have simultaneously been at each other's throats and trying to conspire to make you feel better."
            mc "Yeah... Tyson just came and woke me up. But I wanted to talk to you about that."
            show oz neutral
            oz "Go on."
            mc "He wants to leave, just the two of us, but..."
            show oz pout
            "He sighed out, shaking his head."
            oz "Well, you're both welcome to try, but from what I've heard of the road from Benson, that way is out. "
            show oz neutral
            extend "Your only option would be to go through the forest, and perhaps find a way down the mountain that way."
            mc "I think that's what he was planning. Or at least where he'd likely try and go."
            show oz annoyed
            oz "Then a word of caution. Those woods are dangerous, but finding a way off the mountain is indeed possible."
            mc "Dangerous how?"
            show oz pout
            oz "Do you know how to navigate the wilderness? Or fend off wild animals? "
            show oz neutral
            extend "When are you leaving? During the night is going to be additionally problematic given the dark."
            mc "I have a flashlight!"
            show oz pout
            oz "But does Tyson? Where does that leave your friends?"
            "I frowned, looking downwards."
            mc "Tyson's... not giving me a choice."
            show oz neutral
            oz "Does he need to be sedated? I can retrieve something from the lab to knock him out if he's proving to be an issue. "
            show oz pout
            extend "Now that I think about it, it might do him some good..."
            mc "No, that's fine, just... I figured I'd come see how you were doing instead really. If you still wanted to show me that thing in your lab."
            show oz neutral
            oz "There's nothing left to show. Not after what happened."
            mc "What do you mean? Did someone get in or...?"
            oz "More like... The reason I wanted to show you is now meaningless given what happened before. It's there, but it's best if we leave it undisturbed for now."
            "He stepped forward and placed a hand on my shoulder."
            oz "Ultimately, it was self-serving to my own curiosity. Don't worry about it."
            mc "Oh... Okay..."
            show oz pout
            oz "Besides, the lab itself has been sealed for now. You'd need me to unlock the door for you and I'm in no rush to enter that space again."
            "I grumbled, thinking about where that left me."
            show oz neutral
            oz "Were you looking for me to convince you to stay? "
            show oz pout
            extend "I said before I'm looking forward to all of you leaving this place one way or another so long as that's {i}alive{/i}, mind you."
            "He pulled away, taking a few strides towards the door before turning back."
            show oz neutral
            oz "If you feel up to having a chat, come join me in the back yard. I feel like enjoying the night air for a bit."
            hide oz with dissolve
            "I watched as he left before turning to the bookcase leading to the library. If he'd already sealed off the laboratory, there was nothing for me down that way aside from darkness and a lot of books."
            "I wasn't even hungry, it was still just exhaustion from dealing with everything else."
            if SalDead == True:
                "Looking out the window at the back yard I wondered what had happened with Sal while I was asleep, if anyone had spoken to him after I did. The thought made my stomach flip and I backed off, now wondering if I had let my anger get to me."
                jump Day11CNight
            else:
                "It was getting dark, my mind turning to Sal still by the pool. He was still out there, or at least chances were he was."
                "Had the others talked to him? What did they say? A shiver went down my spine and it was enough of a reminder for me to get him a blanket or a pillow if he was set on staying out there all night."

label Day11CSalNight:
    scene mansionback with dissolve
    "I'd stopped by Sal's room and retrieved a pillow and a blanket for him. Already I could feel the chill of the night air and I could smell a storm coming."
    show oz pout with dissolve
    "As he'd said, Oswin was standing outside, looking out into the yard and shooting me a curious look as I came to join him."
    show oz neutral
    oz "You brought a pillow and blanket for your friend?"
    mc "When I spoke to him before, he was thinking of isolating himself in the pool."
    oz "He's scared there'll be a repeat of what happened if he stays in the same house."
    mc "Right. But he's going to catch a cold if he stays outside all night by the pool."
    show oz smile
    oz "And if that were to happen, I could deal with it. "
    show oz neutral
    oz "But yes, giving him the resources to prevent it from happening would be ideal. Are you heading over now?"
    mc "Yeah. I was thinking I just wanna check in and get back inside before... well..."
    oz "Before you second guess if what you're doing is safe."
    "I whined, shrinking into my shoulders."
    show oz pout
    oz "For what it's worth, I believe this is the noble route you're taking. "
    extend "Far be it from me to tell you to do otherwise, or judge you for deciding either way."
    mc "Then why do I feel like you're doing just that?"
    show oz smile
    oz "You're an adult so you're well within your rights to make your own decisions. "
    show oz pout
    extend "But... I still do worry. You're young, effectively still a child so consider it a lingering desire to take care of you all."
    "I gave him a look, unsure how I felt about that. "
    show oz neutral
    extend "He seemed to pick up on my unease, too."
    oz "You don't trust me still?"
    mc "I don't know who I trust right now."
    show oz smile
    oz "Then I'm glad, because that means you're still being rational. "
    show oz neutral
    extend "Still, I'd recommend seeing your friend and getting back inside before it gets too late. I'd rather only one of you getting sick if it came to it."
    scene pool with dissolve
    "I left Oswin standing by the back door as I wandered over to the pool. Although I noticed that my pace slowed the closer I got, second guessing myself."
    show croc sad with dissolve
    "Sal was where I left him, almost as if he hadn't moved at all. As I opened the gate and stepped in, he looked up slowly, watching me as I got closer."
    show croc scared
    croc "[mcname]... You came back...?"
    mc "If you're that certain you want to stay out here then... well..."
    show croc cry
    "I sat the blanket and pillow down next to him, and he cradled them in his arms for a moment before getting up and wandering off to the side."
    show croc sad
    "Following him I just watched as he lay out the blanket and pillow in the corner, far away from the pool but it felt colder here."
    croc "Thank you... for coming to check on me again."
    "He looked me over when I didn't respond immediately, and he continued after a sigh."
    show croc pout
    croc "Hoss... and Tyson stopped by after you did."
    mc "Did... they say anything?"
    show croc sad
    "Sal nodded slowly, eyes glazing over as he looked towards the pool."
    croc "Hoss... asked me a few questions, nothing important really. Just wanting to know if I remembered certain things."
    show croc cry
    "Sal sighed out, slumping against the wall as he rubbed his face."
    croc "Tyson though..."
    mc "What... did he say?"
    show croc sad
    croc "I expected him to yell, or to throw a punch or something. But I've never heard someone so angry while being so quiet. "
    extend "He... {w=0.3} He told me that I'd be better off dead."
    "I gulped, feeling guilty that the thought had crossed my mind earlier. The only difference was that Tyson followed through."
    show croc cry
    croc "It should have been me."
    mc "What...? Sal, you can't possibly think that..."
    croc "I do. Dean was kind and I killed him. Roswell was clever and also kind and I killed him too."
    "I took a step back as he trembled. Somewhere between a mix of scared and worried."
    mc "But you... Do you remember doing it? Do you remember what happened?"
    croc "I don't know... The more I think about it the more I wonder if I'm just blocking it out or if I really don't remember. What parts I do remember I'm now not sure if it's my imagination."
    show croc sad
    "He looked up at me, worried and his voice kept low."
    croc "[mcname]... I don't know what I would've done if you had also... well..."
    "We looked at one another for a bit before he looked away again."
    croc "I'm sorry... Thank you for the blanket. And the pillow."
    mc "Sal... are you going to be okay?"
    show croc pout
    croc "Are {i}you{/i}?"
    "I didn't know how to answer that question, and I fidgeted on the spot. I hoped I was going to be, but my world was falling apart around me and I was struggling to keep my head on straight."
    show croc sad
    croc "For what it's worth... I hope so. Can I see you tomorrow morning?"
    mc "How come?"
    show croc cry
    croc "It... I just wouldn't mind some company, maybe a little. I don't think the others will be stopping by any time soon."
    "He deflated again, grabbing the pillow and wrapping himself in the blanket. He didn't look all that comfortable but was probably moreso than if he didn't have the blanket or the pillow."
    mc "Okay... I'll see you in the morning..."
    scene black with dissolve
    "He cracked a smile for a fraction of a second before settling back against the wall with his eyes closed."
    "I waited a little longer just in case he had anything else to say before I let him be, making my way back towards the house."
    if OswinDead == False:
        "Oswin must've headed back inside, as he wasn't by the door when I reached the house, not that it really mattered. Soon enough I headed inside as well."
    else:
        "As I reached the back door I looked up at the sky, clouds rolling in fast. The chill in the air made me shiver, and without wasting any more time I headed inside."



label Day11CNight:
    scene bedroom with dissolve
    "By the time I got back to my bedroom I was hungry, but I didn't care. I was pacing, worried. I was on edge, hyper focused on any sound or movement that happened nearby that wasn't my own."
    "The slow knocking on my bedroom door made me freeze, head snapping to stare at it until the person knocking entered the room."
    show wolf neutral with dissolve
    "He said nothing as he closed to door behind him and flicked off the light, leaving us in the dark."
    wolf "Where did you go?"
    mc "Nowhere."
    "He stared at me, and I stared right back. It was none of his business."
    show wolf annoyed
    wolf "Fine. Whatever."
    show wolf shirtless annoyed with dissolve
    "He pulled off his shirt, dumping it by the floor before wandering closer. As he stood in front of me, he sized me up before grabbing me roughly by the back of the head, pulling me in for an awkward hug."
    show wolf shirtless neutral
    wolf "Let's get some sleep."
    mc "I'm not tired."
    "His grip eased off, but he didn't pull away."
    if wolfroute == True:
        "But I wrapped my arms around his middle, hugging him close."
        mc "Ty... I'm scared."
        wolf "I know."
        mc "I didn't want any of this to happen..."
        wolf "I know."
        mc "And... Ty?"
        wolf "What?"
        "He eased me back to look at me, a hand cradling my cheek carefully."
        mc "I can trust you, right? We're going to be okay, right?"
        show wolf shirtless cry
        "He pulled me to him, tight. The hug almost painful, desperate, but I returned it in kind. He shuddered and as he nuzzled the side of my face I could tell he was crying."
        "We stood like that for a few moments, with his shoulders shaking and tears flowing freely despite the little sound he made."
        "When he finally spoke again, he sighed out before doing so. His voice was soft and uncertain."
        show wolf shirtless sad
        wolf "You can trust me, and we'll be okay."
        "I took him by the hand and led him over to the bed, and he followed me without resisting. But he was the one that lay me down first, and crawled in bed soon after holding me close."
        wolf "We'll be okay. We'll get everything ready tomorrow and just... We'll run away. We'll go somewhere. Get you out of this fuckin' mansion."
        mc "Okay..."
        if SalDead == False:
            "I wondered if Sal would be alright... Hopefully things would turn out for him, but right now I was worried more about myself."
        "We lay there as thunder started to roll in."
        wolf "Hey... I've got you, right [mcname]?"
        mc "Got me?"
        wolf "Yeah..."
        "He didn't clarify beyond that, the two of us just laying there in silence while I figured out what to say back."
        mc "Have I got {i}you{/i}?"
        "He pulled back enough to look me in the eye. "
        show wolf shirtless neutral
        extend "The gears were turning in his head, and his voice was brought down to barely a whisper when he answered me."
        wolf "Always have."
        "I squeaked, my heartbeat slowing down somewhat as a newfound calm settled in. As if to reinforce what he said, Tyson leaned in, resting his head atop mine."
        wolf "{i}Always.{/i}"
        scene black with dissolve
        "We lay like that, listening as the rain rolled in. Ty occasionally playing with my ears carefully as they twitched upon any new sound coming from inside the house."
        "I'd momentarily forgotten about all else, Hoss and Orlando included. "
        if OswinDead == False:
            extend "I'd even put all thoughts of Oswin and Benson aside in favor of cuddling up to Tyson where I felt safe."
        else:
            extend "But the rat and Oswin's body in the laboratory lingered a little. Was it worth bringing up given no one else knew?"
        "All that mattered for now is that I felt safer than I had in the last 24 hours being next to Ty.{w=0.3} Hopefully it lasted until morning."
    elif dragonroute == True or lionroute == True:
        show wolf shirtless annoyed
        wolf "I don't care."
        mc "Well you should! Orlando would! Hoss would! I thought you cared about me too but..."
        show wolf shirtless mad
        "He grabbed me roughly by the shoulders pulling me back."
        wolf "Oh yeah? And where were those fucks all afternoon? Have they waited by your door making sure no fucker is going to get to you?"
        "I winced as he yelled point blank at me face. His breath stank and I whined the closer he got."
        wolf "Neither of them came by once. Didn't even try to check if you were okay. "
        show wolf shirtless sad
        extend "But {i}I{/i} did."
        show wolf shirtless annoyed
        "I whined more and he shoved me roughly back onto the bed, approaching and pinning me down."
        "The distant sound of thunder rolling in hinted at a coming storm, but it was being drowned out by the sound of Tyson's breathing and my heart pounding in my chest."
        show wolf shirtless neutral
        wolf "Stop fighting me."
        "He stared me down, intense but not angry. Or if he was, it'd eased back to the point I couldn't see it any more."
        "Had the others had enough of me? Stopped caring? That must be it, right? Otherwise what Tyson said wouldn't be true."
        "I breathed in slowly, falling limp under Tyson."
        mc "Okay..."
        "That's when he eased up, holding me on the bed but now with enough force to keep himself propped up. I was quiet, words coming out hoarse and uncertain."
        mc "I'll stop fighting..."
        show wolf shirtless sad
        wolf "Good... "
        show wolf shirtless neutral
        extend "We'll spend tomorrow getting ready and you can say goodbye or whatever, then I'm taking you home."
        scene black with dissolve
        "He arranged us both in bed and held me against him. Most times he'd done this I'd felt safe, it was familiar."
        "But something about this felt very wrong. I was scared even huddled up against him. Scared of everything going on, or scared of Tyson I wasn't too sure."
        if SalDead == False:
            "I had been scared of Sal but now I was wondering if I was more scared of other things having spoken to him earlier."
        if OswinDead == False:
            "Would Oswin know better here? Would Benson?"
        "Tyson said nothing, just laying there and holding me to him as the rain started to roll in. I just hoped that things would be better in the morning."
    elif bearroute == True or boarroute == True:
        show wolf shirtless pout
        wolf "Yeah, yeah. Get into bed."
        mc "But I'm not..."
        show wolf shirtless mad
        "A heavy hand landed on my shoulder and he gripped tight. Hard enough that it made me yelp from how he dug into the muscle."
        wolf "It's time for sleep."
        mc "Ty, you're scaring me... It hurts..."
        "His grip didn't let up, and he took a step forward causing me to take one back. He took another, and we repeated until I was backed up against the bed."
        wolf "This hurts, huh? This hurt you more or less than Dean and Roswell getting fucking killed, [mcname]?"
        "I whined as he pushed me down to sit on the bed, finally moving his hand."
        show wolf shirtless annoyed
        wolf "I'm so fuckin' scared for you, you know that? You're such a dumbass and I'm worried that you're going to be next."
        show wolf shirtless sad
        wolf "So scared that if I lost you, then what? What happens to me?"
        "I frowned up at him, holding onto the bedsheets tightly to root me in place."
        mc "So this is all about you now? I lost both of them right in front of me, Tyson! Do you know how that makes me feel? What it's like to go through it again?"
        show wolf shirtless yell
        wolf "I was there too, you selfish fuck! "
        show wolf shirtless mad
        extend "I couldn't give two shits about Dean or Roswell when the only person here I'm worried about is {i}you{/i}."
        show wolf shirtless annoyed
        wolf "First your dad, now maybe you too."
        mc "{i}Tyson{/i}, I... !"
        show wolf shirtless sad
        "My fists started to hurt from how hard I was gripping the sheets, but I gasped when he lunged forward, dropping to his knees and hugging me around the middle."
        show wolf shirtless cry
        wolf "Please... Let me just take you home."
        "Stunned, I put my hand on his head and gently pet him.{w=0.3} What if I'd died? Had I been selfish?"
        "What would Dean or Roswell say right now? What would they want me to do? As I looked down to Tyson I became conflicted as to if I should be scared for him, for me, for all of us or feeling something else completely."
        show wolf shirtless sad
        mc "Okay... But... the others?"
        wolf "Can we talk about it in the morning?"
        mc "I still get the day to sort things out?"
        wolf "Yeah... I promised you that much."
        "Thunder started to roll in, the both of us looking towards the window on instinct."
        if SalDead == False:
            "I wondered if Sal was going to be alright out by the pool but ultimately it'd just be something I'd know for certain come morning."
        mc "Ty... I don't know how I should be feeling right now... But are you okay?"
        wolf "Not by a long shot."
        show wolf shirtless neutral
        wolf "But that's why I came here, to you. "
        if OswinDead == False:
            extend "You're safe, and I told you how it is earlier so... Some surprise that I'd be here now, right?"
        else:
            extend "I feel safe around you in a fucked up kinda way. I should be the one keeping you safe but... here we are."
        "He started to stand and pushed me into the bed, sliding in behind me and holding me close. Almost like a security blanket or a plush toy."
        scene black with dissolve
        "We lay there in silence, listening as the rain drew closer."
        "I was scared to say anything, even moreso when Tyson started nuzzling the back of my head."
        "He was worrying me, and for the briefest of moments I was more worried about what was happening to him rather than our lives. Hopefully come morning things would be alright."



    $ renpy.pause(3.0)
    "{color=f00}{b}TO BE CONTINUED: END OF DEMO{/b}{/color}"
    return


# Notes for Day12C:
# If SalDead == False and OswinDead == True: Orlando took him blankets because you forgot.
# If SalDead == True and OswinDead == False: Oswin finds Sal dead in the morning.
# If SalDead == False and OswinDead == False: Dave takes Sal blanket and Oswin treating Sal in the morning.
# If SalDead == True and OswinDead == True: Sal is dead come morning, Dave discovers the body.
