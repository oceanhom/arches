label day9morning:
$ currentDay = 9
scene day9 with fade
$ renpy.pause (3.0)

scene bedroom with dissolve
"I opened my eyes slowly, waking right where I fell asleep."
"My phone, now dead, was still in my hand and I flexed my grip around it before setting it on the bedside table."
"Quietly I looked around the room, searching it, wondering if by some miracle that I was somewhere else."
scene black with dissolve
"It wasn't always this bad. Some days were easier than others for sure. This was for sure a day where I just wanted to crawl back into bed and get some sleep."
"I almost scrambled under the covers and lay my head down, eyes still closed."
"Sleep found me quick again, but it only felt like minutes before I woke to someone coming into my room."
play audio relaxed fadein 2.0
if wolfroute == True:
    "The footsteps were quiet but purposeful, making a beeline for the bed. I could tell who it was right away."
    mc "I'm sleeping, Ty."
    wolf "Bullshit."
    "I grumbled as Tyson sat down on the bed next to me. I pulled the covers up higher over my head as he continued."
    wolf "So... You doing alright?"
    mc "I'm fine."
    wolf "Yeah, bullshit. Look at me."
    scene bedroom
    show wolf neutral
    with dissolve
    "I didn't need to do much, as he pulled the covers back exposing me to the light. Opening my eyes carefully, I looked at him, and the cup of coffee he was setting on the bedside table next to my phone."
    wolf "Hm?"
    mc "What?"
    "Ty picked up my phone, trying to do something to it before setting it back down."
    show wolf sad
    wolf "You alright? Don't lie to me, [mcname]. I have a good guess as to what kept you in bed this late."
    "I made a sound somewhere between a grumble and a whine, looking away from him."
    "With a sigh, Ty picked up my phone again, and I watched him rub his thumb across the blank screen."
    wolf "Voicemail again?"
    mc "Yeah..."
    show wolf neutral
    wolf "...Alright."
    mc "Please don't go."
    "Ty was almost about to get up before he settled back where he sat down."
    mc "I'm... I'm not fine."
    mc "I'm really not fine, Ty."
    show wolf scared
    wolf "H-Hey now, it's alright. What's going on?"
    mc "I just... Everything that's been going on... What I would give to ask dad what to do."
    show wolf neutral
    wolf "I know that feeling. I miss him too, pup."
    show wolf sad
    wolf "But... You know how it is."
    show wolf neutral
    wolf "Nothing we can do about it, either. Just... you've got me, right? And Dean. Plus the others, I guess. I dunno."
    show wolf pout
    wolf "Did you need a hug, or just coffee?"
    "I sat up, hugging my knees."
    if wolflove >= 16:
        mc "I want my dad, Ty."
        "I sniffled, my breath stuttering as I covered my eyes."
        mc "I don't know what I should be doing, or what I should be feeling and it's just... He'd know, right?"
        show wolf sad
        wolf "Probably."
        show wolf neutral
        wolf "He was pretty good with that sorta stuff. Better than I am at least."
        wolf "I know it's not the same, but uh... Here."
        "Ty shuffled closer and turned so he was on the bed proper before putting an arm around my shoulders and pulling me into a hug."
        "Almost immediately I threw myself at him, and no sooner had my arms around him he put his other around me in kind."
        show wolf scared
        wolf "Hey, [mcname]...?"
        "I looked up at him, sniffling and wiping my eyes."
        mc "...What?"
        show wolf sad
        "The look he gave me was soft and uncertain, his mouth barely open as if he was about to say something."
        wolf "You're uh... Your coffee is going to get cold."
        mc "My... what?"
        show wolf pout
        wolf "Here, I brought you coffee."
        mc "Wait, that's not... your coffee?"
        show wolf neutral
        wolf "Nah, you missed breakfast so... y'know. Coffee."
        mc "Oh. Right. Um..."
        show wolf pout
        wolf "What? You were expecting a full breakfast and a kiss?"
        mc "Maybe not breakfast but..."
        "I gulped, backing away from Tyson a little. With a sigh I looked at him, before pulling my gaze down to my hands."
        mc "I feel so... confused."
        wolf "You and me both."
        mc "No, Ty, listen, it's like... What you said yesterday. About not being gay but liking me and being a weakness and just..."
        wolf "Well... Tell me this then, pup."
        show wolf neutral
        wolf "Do you love me?"
        mc "I don't know! Maybe?"
        "I had raised my voice, fists and jaw clenched."
        mc "I've never felt this way before! It's frustrating, it hurts, and I can't act on it."
        mc "You... and dad... and..."
        show wolf scared
        "I growled, baring my teeth at Tyson. I wasn't sad so much anymore, but I wasn't angry either."
        mc "What if you up and leave one day and never come back? What then?"
        mc "Are you just going to leave me like dad did? Cause if you are then I don't wanna be around you anymore!"
        show wolf neutral
        "He didn't say anything in reply, instead just reaching over to the bedside table and grabbing the coffee, carefully holding it out for me to take."
        wolf "Anything else you want to say?"
        "My eyes flicked between him and the coffee. I wanted to stay this revved up, this annoyed but I was quickly losing the drive."
        mc "{i}Yes.{/i}"
        "I snatched the coffee from Tyson, the scent grabbing me before it made it to my mouth and I drank deep, closing my eyes."
        "As I swallowed, my frown faded and I just felt silly lashing out at Tyson. Instead of admitting it, I just kept drinking."
        show wolf smile
        "When the cup was empty I opened my eyes to see Tyson smiling at me."
        wolf "Feeling better now?"
        mc "I'm sorry."
        show wolf pout
        wolf "Don't be. If anything I'm glad you got it off your chest."
        mc "But..."
        show wolf neutral
        wolf "What?"
        mc "I don't even know anymore."
        "I sighed out, shaking my head."
        mc "I should get up and get something to eat. Then... I dunno, maybe go for a walk. I've got stuff I need to think about."
        wolf "Alright."
        "Tyson took the mug from me and suddenly grabbed me by the back of my head, bringing my forehead to rest against his chest."
        wolf "Come grab me if you need anything, alright?"
        "It wasn't a kiss, but he placed his nose against the top of my head and held it there briefly."
        show wolf smile
        wolf "I meant it when I said you're my weakness, alright? You need something, you tell me and I'll make it happen if I can. I'm fine being the strong one for you if you need it."
        mc "But what if I wanted to be the strong one for you?"
        wolf "One day you might be, maybe. Until then that's my job."
        "As he pulled away, I held tight, stopping him from leaving."
        mc "Five more minutes? Please?"
    elif wolflove >= 10:
        mc "Hug, please..."
        show wolf neutral
        wolf "Alright. Easy."
        "Ty shuffled closer and put an arm over me as I lowered my legs so he could get close enough that it wouldn't be awkward."
        wolf "So... Guessing it was a rough night for you?"
        mc "How'd you know?"
        show wolf pout
        wolf "You only listen to that when things are pretty bad."
        wolf "What happened?"
        mc "Nothing... Nothing important at least..."
        "I avoided his gaze, not wanting to let him in on the meeting just yet."
        wolf "You didn't come get me though?"
        mc "Well... No..."
        show wolf neutral
        wolf "So nothing important happened, but you're not alright, and you didn't come get me to help."
        show wolf pout
        wolf "Yeah, like that's normal."
        mc "I didn't... I didn't wanna be a bother Ty. Honest."
        mc "Why can't I be the strong one for once? You've always known what to do, or just... figure it out as you go."
        show wolf neutral
        wolf "Yeah, and?"
        mc "I wanna get good at that too, so that when you need it, I can... y'know."
        show wolf laugh
        wolf "You don't need to do that, pup. I'm fine."
        mc "No, but..."
        "I gave Tyson a look, unsure of how to feel."
        mc "You said I was a weakness for you, right? Wouldn't it be better if I wasn't one?"
        show wolf annoyed
        wolf "Geez, alright..."
        "Ty's grip on me tightened a little before it went slack completely, releasing me from the hug."
        wolf "I said I was fine with it, alright?"
        wolf "Hell, maybe I just like it."
        mc "Isn't it hard, being the strong one all the time?"
        show wolf sad
        wolf "I try not to think about it. I get what I need from it."
        mc "What {i}do{/i} you get though?"
        show wolf neutral
        wolf "You smiling is a start."
        "I blushed, chuckling a little bit. If only for a moment my worries disappeared as my mind wandered closer to seeing Ty in a more than just friendly light."
        show wolf pout
        wolf "Look, don't go being gay about it."
        show wolf sad
        wolf "Just... you know how it is."
        mc "No homo?"
        show wolf mad
        wolf "Fuck off. I meant about what you mean to me. You're important."
        show wolf annoyed
        wolf "Don't know why I've had to say that so often over the past couple days."
        mc "Well... You're important to me too, Ty."
        show wolf smile
        "He pulled me in close for another hug, pressing his nose into the top of my head."
        show wolf pout
        wolf "Your coffee is going to go cold at this rate."
        "Ty pulled away just enough to reach back and retrieve the mug, handing it carefully over to me. No sooner than I took hold of it and began to drink, he resumed the hug."
        wolf "Drink up, you need it."
        mc "Yeah... Then I should get up and get dressed, maybe go for a walk to clear my head."
        show wolf neutral
        wolf "I'll be around if you need anything. Just grab me, alright?"
        mc "Okay..."
    else:
        mc "Coffee, please..."
        show wolf neutral
        "Ty reached over and grabbed the mug of coffee he brought in, passing it over."
        "I started to drink and it was still hot, the first swig hurt as it ran down my throat."
        wolf "Careful, pup."
        mc "Ow..."
        show wolf pout
        "Ty shook his head before rolling over to sit beside me on the bed, stretching out his arms and rolling his wrists."
        wolf "So how bad are we talking?"
        mc "Hm? Oh... Well..."
        mc "To be honest, the whole thing with the vault is just... getting to me. I don't know what's happening, or {i}why{/i} it's happening."
        show wolf neutral
        wolf "So you're stressing out over nothing?"
        mc "No! It's for sure {i}something{/i}...{w=0.5} I don't know..."
        show wolf pout
        wolf "Well... Can I help? Somehow?"
        mc "It's not something you're good at, Ty. It's fine."
        show wolf annoyed
        wolf "Bullshit. You're upset and I wanna help. Now I'm not asking, so just tell me."
        mc "I'm scared, unsure, but I can't go home."
        show wolf neutral
        wolf "Why'd you wanna go home?"
        mc "I don't like the idea of anyone dying, even if nothing's happened, I just... I dunno."
        show wolf pout
        wolf "Then fuck it, let's head home."
        mc "What, together?"
        show wolf neutral
        wolf "Sure, why not? So long as I can crash at yours, we can have our own vacation."
        mc "And you'd be fine just up and leaving like that after like a week?"
        wolf "Well, it'd suck, sure."
        show wolf pout
        wolf "But you're more important to me than some stupid mansion."
        show wolf sad
        wolf "Sure would suck to miss out on that food though... Ah well, fuck it. There'll be other meals, right?"
        show wolf scared
        wolf "What?"
        "I was staring at Ty in awe, flattered all the same."
        mc "But... Mansion!"
        show wolf pout
        wolf "Yeah, well, it's just a stupid house."
        "I almost headbutted him in a hug, making sure not to spill any of the coffee while I did so."
        show wolf smile
        "And he hugged me back, pressing his nose into the top of my head."
        wolf "So what's the plan? We bailing?"
        mc "Not yet. I think... I'll take a walk to clear my head first; then go from there."
        wolf "Sure. Let me know if you need something. I'll be around."
    scene black with dissolve
    "Tyson and I cuddled for a bit longer before he got up and let me change in peace."
    "My hoodie was still being washed apparently, not that I could see it anywhere. I settled for other clothes; not that it had that same level of comfort but I'd make do."
if bearroute == True:
    "The door closed just as quick, and despite how quiet he was being, the scent gave him away without me needing to open my eyes."
    "He wandered over and placed something on the side table before placing a hand on my head, stroking gently."
    bear "Hey, rise and shine, handsome."
    scene bedroom
    show bear neutral
    with dissolve
    "I slowly opened my eyes upon smelling the coffee he had sat down, looking up at the bear standing beside my bed."
    show bear smile
    bear "Good morning."
    mc "Oh... Hey. Good morning."
    show bear neutral
    bear "You must've been tired, slept through breakfast and everything."
    mc "I had a rough night. Well... something like that at least."
    show bear pout
    bear "Oh, uh... Well... I brought you coffee at least."
    "Dean passed me the coffee and sat down on the bed, eyeing me carefully."
    mc "How'd... {i}you{/i} sleep?"
    show bear neutral
    bear "I had medication, so I was fine. Was out like a light eventually."
    mc "Oh... Okay..."
    "I gingerly sipped my coffee, looking about the room. Maybe I should clean, or... do something today to just gather my thoughts."
    bear "That's familiar."
    mc "What is?"
    bear "That look you're wearing."
    "Sighing out, I took another swig from the mug in my hands before setting it off to the side."
    mc "Just... have to work through some stuff. You know how it is."
    show bear pout
    bear "Boy, do I ever."
    mc "How's... that stuff on your end, anyway?"
    if bearlove >= 20:
        bear "Huh?"
        show bear neutral
        bear "Oh."
        "Dean kneaded his knees, pulling his gaze away from me while he seemingly thought over something."
        mc "Sorry, I shouldn't have asked so uh..."
        show bear sad
        bear "No, it's... probably better I clue you in on something sooner rather than later."
        bear "It's just hard to know... how much to tell you? This is some heavy stuff."
        mc "If it's that personal, I didn't mean to pry."
        bear "No, it's for the best. At least letting you know some of it."
        bear "So... The medication helps me sleep. I told you that, right?"
        show bear neutral
        "Dean's tone shifted so it was more measured, if slightly sickened. Or maybe not sick, at least guilty."
        bear "A long while back I uh... did something terrible to someone. I relive that moment some nights, and it's just... Ugh..."
        "He groaned, his whole body shuddering as he closed his eyes, almost shaking off a lingering thought."
        mc "Who... was it?"
        show bear sad
        bear "Maybe I'll tell you about him someday but... uh... The important thing was that he was a high school friend."
        mc "Was he..."
        show bear annoyed
        "Dean shot me a look that I rarely saw him point at me, commanding and making it clear that I shouldn't finish my question."
        "He breathed in through his nose before sighing the breath out, rubbing his forehead."
        show bear pout
        bear "So this... friend."
        bear "Should be obvious that I like you, right? No sense beating around the bush there, wouldn't still be trying to get you to myself if I didn't."
        mc "Right. Although... The aggressive flirting makes me wonder sometimes."
        show bear neutral
        bear "Trust me when I say that I love sex, and can't wait to get you to myself in that way if it ever happens."
        show bear pout
        bear "But I do want more. I {i}need{/i} more than that. Well, more accurately I think I need both?"
        mc "So...?"
        show bear neutral
        bear "So I come on strong sometimes unintentionally. Sometimes it's genuine, other times it's panic."
        mc "Why would you panic though? Like..."
        "I gestured between us, not really sure what I was getting at, but Dean seemed to derive meaning from it all the same."
        bear "I know. We're testing things out, but you can't be too careful, [mcname]. I'm older, I've been around the block before, so I'm trying to be the responsible one here."
        mc "Responsible, but horny?"
        show bear laugh
        "Dean chuckled lightly, shaking his head."
        show bear smile
        bear "I'm serious. I want us to get to a point where it's official, and I want it to work."
        show bear pout
        bear "You like me too, right?"
        mc "I mean, I wouldn't have agreed to a date or really... anything else that's happened so far if I didn't, right?"
        bear "Well... that helps at least."
        show bear neutral
        bear "But that's the gist of it. Something I did a while back keeps me up at night thinking that I'm going to screw it up in the same way."
    elif bearlove >= 10:
        "Dean shifted next to me, visibly uncomfortable."
        bear "It's... fine."
        mc "Oh... Okay. Well that's good, right?"
        show bear neutral
        bear "I'm used to it. Not that I should be, but it happens often enough."
        mc "How... bad is it?"
        show bear pout
        bear "Truth be told, it's been bad of late. I've been putting it down to spending more time together."
        mc "Did I... do something wrong?"
        show bear scared
        bear "Oh, god, no. It's not your fault."
        show bear pout
        bear "Well... Not your fault, but you are part of the reason."
        "I whined softly, watching as Dean looked about the room troubled."
        bear "So... if we're going to date, and I really want us to... You're gonna have to know a thing."
        show bear neutral
        bear "I did something bad to someone I once knew. Something really bad, and that keeps me up sometimes."
        mc "How often is... 'sometimes'?"
        show bear sad
        bear "It comes and goes. Been more... severe past couple of nights, but I've also slept better too. Ups are higher, downs are lower."
        bear "Either way, I want you to know that I do want something serious to come of this. Of us."
        show bear pout
        bear "I know I come on strong sometimes, and I don't mean to, although I am genuine about wanting to have a sexual relationship with you."
        mc "But only when I'm ready?"
        show bear neutral
        bear "Of course. Wouldn't be right, otherwise."
        bear "I'll... fill you in more at some point, promise, but I just needed to let you know that."
    else:
        bear "Fine, I suppose..."
        "Dean looked me over, before turning away with a sigh."
        bear "I should apologize about something while I remember, too."
        mc "Apologize for what? What happened?"
        show bear neutral
        bear "I know I come on strong. But I want you to know that I don't mean that's all I'm after."
        show bear sad
        bear "Chalk it up to worry on my part that I'm not making my intentions clear enough sometimes."
        mc "I'd say it was pretty clear."
        "I tried to flash him a wry smile but his expression didn't budge, instead he looked elsewhere."
        show bear pout
        bear "Still..."
        "He sighed out, rubbing his forehead."
        bear "I'm sorry. I'll try and dial it back."
    "I placed my hand on Dean's, holding it while I took another sip of coffee."
    show bear smile
    "As he looked to me, he smiled softly with his smile becoming more genuine as he took my hand in his proper."
    mc "As much as you talk about sex Dean, um... it's not as if I don't wanna get there too. It's just... a big step, right?"
    show bear laugh
    bear "I suppose it is, yeah. I mean it though, I'm happy to let you set the pace."
    mc "Right..."
    show bear neutral
    bear "But... While that's what's bothering me, what's bothering you?"
    mc "Oh, um..."
    "I looked across to my phone, eyes lingering on it before I looked back to Dean."
    mc "That's... uh..."
    mc "So... Orlando told you about my dad, right?"
    show bear scared
    bear "Oh..."
    mc "Sometimes I just miss him a whole lot. Last night was one of those nights where... y'know..."
    "I trailed off, looking down into my mug of coffee with a sigh."
    mc "I'll go for a walk later and try and clear my head, I think. It's been a rough couple of days."
    show bear neutral
    "Dean shifted closer and lifted my chin gently so I was looking at him."
    bear "Promise you'll come get me if it gets too much, alright?"
    mc "Okay. I promise."
    show bear smile
    bear "Well... I'll let you get changed."
    mc "Oh, alright. To be honest, I'm surprised you didn't make a bigger deal about wanting to see me change."
    show bear laugh
    bear "Hey! I was being serious about what I said before. My curiosity aside, I do sometimes know when to be a gentleman."
    show bear grin
    bear "Besides, I might get my chance tonight."
    scene black with dissolve
    "As I began to laugh, Dean wandered off, blowing me a kiss before he left the room."
if dragonroute == True:
    "The footsteps were slow and careful, building confidence as they got closer."
    dragon "Hey... Wakey-wakey..."
    scene bedroom
    show dragon neutral
    with dissolve
    "I groaned, cuddling into the sheets before smelling the familiar scent of coffee."
    dragon "Come on, you've slept in long enough. I even brought you coffee."
    mc "Okay, fine, I'm awake..."
    "With a sigh I sat up, taking the coffee from Orlando as he beamed at me with pride."
    show dragon smile
    dragon "You must've been tired!"
    mc "Yeah..."
    dragon "..."
    show dragon sad
    dragon "...Or something's wrong?"
    "Orlando edged closer, trying to find my gaze and I looked around, avoiding his."
    dragon "Something {i}is{/i} wrong, but..."
    "His eyes looked to my phone on my side table, then back to me, then to my phone."
    dragon "Did something... happen?"
    mc "No, nothing happened. Just a restless night."
    if dragonlove >= 10:
        "Orlando reached out and cupped my cheek, rubbing a thumb just under my eyes as if preemptively wiping away a tear."
        dragon "You're {i}sure{/i}?"
        mc "I..."
        "I felt my bottom lip quiver. My next intake of air was a rattled breath on the border of being enough to show that I was about to break down and start crying, but I kept it in."
        dragon "Did someone hurt you? Did someone say something?"
        show dragon mad
        dragon "If Tyson did something I'll go... do..."
        show dragon annoyed
        dragon "...{i}something.{/i}"
        mc "No, Ty didn't do anything..."
        show dragon sad
        dragon "Oh. Well... Dean, maybe? He didn't..."
        show dragon scared
        dragon "Unless...?"
        mc "No!"
        mc "No, just..."
        show dragon pout
        dragon "Just... what?"
        mc "Stress, I guess. Everything that's been going on has been getting to me."
        show dragon scared
        mc "I feel like I'm going crazy at times. Part of me thinks I'm being led around by someone else. Part of me thinks that I'm going to screw up and this whole... thing with the vault, just..."
        show dragon annoyed
        dragon "No, that's not all."
        dragon "You're suppressing it again. For some reason."
        "I looked down into the mug I held in both hands, letting the scent of the brew waft into my nose."
        show dragon sad
        dragon "I don't want to sound dramatic, but I'm worried about you, [mcname]. Bottling this sort of thing up... it'll kill you."
        "Flinching for only a moment, I brought my gaze up again."
        mc "I... I don't..."
        "Gingerly, Orlando took the coffee from me and sat it on the bedside table. Once it was safely out of the way, he got up onto the bed to join me."
        show dragon neutral
        dragon "You can lean on me, [mcname]. No dying on me, okay?"
        "The next thing he did was bring me in close, resting my head against his chest. Both his warmth and steady heartbeat was calming, accented by that lingering cinnamon scent he carried."
        show dragon smile
        dragon "I'll keep you safe. You can depend on me. Just... let it out."
        "I shook, teetering on the edge of crying but it just wouldn't come. Orlando knew most of what had gone on, so there was no point hiding it, but just stepping over that threshold was just something I couldn't bring myself to do."
    elif dragonlove >= 5:
        "He hesitated, but Orlando placed a hand on my shoulder, prompting me to look at him."
        dragon "[mcname]..."
        mc "It was just... a hard night, you know why, right?"
        show dragon scared
        dragon "Oh..."
        "Nodding carefully I took a sip of the coffee he had brought. It was warm, but lacking. Not from the taste but from the experience as a whole."
        show dragon sad
        "Orlando sat down on the bed, twiddling his thumbs while he thought of something to say."
        dragon "Did... you want me to get you anything? Is there anything I could do to help?"
        "I shook my head."
        dragon "Can I get anyone else? What about Dean? Or Hoss?"
        "Again I motioned in the negative."
        show dragon mad
        dragon "Well before you go saying that you're fine, just..."
        dragon "Just..."
        show dragon sad
        "Orlando shook his head, sighing out."
        dragon "I worry about you, near constantly these days."
        dragon "Everything with the vault, it just... I don't want it compounding on everything else you're bottling up."
        mc "I'm not..."
        show dragon annoyed
        dragon "Don't you start with that."
        dragon "We've known each other for years, [mcname]. I know when you're upset at the very least."
        show dragon sad
        dragon "And ever since... you know...{w=1.0} It seems like you're always just... coping."
        mc "But I {i}am{/i} coping."
        show dragon pout
        dragon "I don't mean that in the good way! "
        "Orlando rolled ungracefully towards me, scooping me up and holding me to his chest."
        show dragon sad
        dragon "You're not alone. You know that, right?"
    else:
        show dragon annoyed
        dragon "Really?"
        "I stole a glance at Orlando who seemed none too convinced about what I'd said, rubbing his forehead while he thought something over."
        show dragon sad
        dragon "Alright, Well... If you say so... I don't believe you though."
        mc "I'm fine, really. It was just a rough night is all."
        show dragon pout
        dragon "With everything that's been going on lately, it's no surprise."
        show dragon sad
        dragon "With the vault, with dealing with Roswell and Tyson, plus trying to woo Dean, you're probably stretched pretty thin."
        mc "Probably..."
        "I trailed off, thankful that Orlando wasn't being insistent on what I was sure he knew was the actual case. Between him and I there were few secrets, but he knew my boundaries. Most of the time anyway."
        "Taking a sip of the coffee, I felt a little better, but was thrown a little when Orlando leaned in and pulled me into a hug carefully."
    "He stroked the back of my head slowly and I sighed out a breath. This was nice, for sure something I could get used to."
    "Maybe I already was to a certain extent. Especially with how physically close we found ourselves at least behind closed doors."
    "My eyes widened as I realized the implication, wondering if there was something more to Orlando's hugs and alike given he seemed to always be the one initiating. I'd always just assumed he was overly friendly."
    "Who was I to turn away a living heater, but much to my shame I feel like I must've missed a cue somewhere along the way."
    show dragon smile
    dragon "Okay, well... I'll let you get dressed. You probably want your space for a bit now, anyway."
    mc "Wait, what?"
    show dragon laugh
    dragon "I confidently claim that best friend title, [mcname]. I figure you're going to want to sit in your room for a bit, or maybe take a walk and let things sort of mellow."
    show dragon neutral
    dragon "But if it gets too much, come find me and we can do something. Talk things out if you think that'd help."
    "Orlando moved away edging towards the door. With one final smile, he left my room closing the door behind him gently."
if lionroute == True:
    "I barely heard it too, thinking I'd just imagined it through closed eyes until I could smell him. That, and the beverage he was carrying."
    "Grumbling I cuddled into my pillow tighter, curling up in defiance for what he'd brought me."
    lion "Oh good. You're awake."
    show bedroom
    show lion smile
    with dissolve
    "I opened my eyes to look at him in a half scowl, awake but barely."
    show lion neutral
    lion "I brought you some tea."
    "My eyes dipped to the cup in his hand, then back up to his face."
    mc "But... {i}coffee{/i}."
    show lion pout
    lion "'But coffee', nothing. With the dependency you have on it, this'll do you some good."
    mc "But I {i}want{/i} my coffee, not leaf juice."
    lion "I'm going to chalk your reaction to withdrawals given you probably also had a rough night."
    "Now that caught my attention, and I looked him over wondering if he knew more than he let on."
    show lion laugh
    lion "You have no idea how late it is, do you?"
    mc "How... late is it?"
    show lion smile
    lion "Late enough. Closer to lunch time than breakfast, that's for sure."
    mc "Really? Why didn't anyone wake me?"
    show lion sad
    lion "We considered it, but... Well, all things considered we assumed you might just want the sleep in."
    mc "Oh..."
    show lion neutral
    "Hoss held out the cup of tea towards me and I frowned, taking it from him carefully and pouting towards the contents of the cup."
    "I could drink tea, but first thing in the morning?"
    lion "Oh come on, it's not that bad. Water is better for you first thing when you wake up anyway. This is closer to that."
    mc "But {i}coffee{/i} has water."
    show lion pout
    lion "And also a bunch of other things that'd make it not as good of an option. Still..."
    show lion sad
    lion "Everything alright?"
    "I went to reply, opting to just sigh out instead. I was almost certain Hoss didn't know about what had happened, or at least the specifics."
    "I would've just filled him now if I felt up for it, especially after yesterday."
    mc "I had a rough night."
    show lion pout
    lion "Hrm..."
    if lionlove >= 12:
        show lion sad
        lion "Okay, well..."
        "Hoss scratched his head through his mane, looking genuinely uncertain as to what to say next."
        mc "What's wrong?"
        lion "I'm not sure if you want me to offer an ear to let you vent, or if you want to talk about it at all. But I do want to do {i}something{/i} to help."
        if HossKiss == True:
            "He gulped, taking his eyes away from me for a second before returning them."
            lion "Look, maybe I'm more invested now or something, I don't know."
            "He sat on the bed, keeping his eyes trained on the ground for a bit, sneaking a sideward glance at me."
        else:
            "Hoss shook his head, sighing out."
            lion "I can leave if you want, too. That's an option."
        "I took another sip of the tea, grimacing before putting it down."
        mc "If I'm being honest... I don't think there's really anything to fix this problem."
        show lion scared
        lion "But... What's the problem? Assuming you want to talk about it."
        "I shook my head, looking at him with a weak smile."
        mc "I'm just missing someone very important. That's all."
        show lion sad
        lion "Oh... Well..."
        "Hoss pulled out his phone, seemingly out of reflex before freezing. His eyes flicked down to his phone, then to me, before sliding it back into his pocket."
        lion "I'm sorry."
        mc "Don't be. It's just... something that happens sometimes."
        show lion neutral
        lion "Well... if you're sure, but..."
        if HossKiss == True:
            "Hoss looked over to the door before messing with his hands, shooting me a coy smile."
            lion "So... yesterday, when we... y'know."
            "I gulped, my cheeks feeling hot as I recalled."
            mc "Yeah?"
            lion "I hope I didn't... I hope you, uh..."
            "He shook his head quickly, letting out a sigh."
            show lion sad
            lion "What I mean to say is that I enjoyed that a lot, and I hope you did too."
            mc "Oh."
            "I chuckled, nervous, looking away."
            mc "To be honest... I just don't know what to make of us now. It's a little confusing really."
            show lion scared
            lion "Confusing? I..."
            show lion sad
            lion "I suppose that makes sense."
            mc "But... for my first kiss, yeah, I liked it."
            show lion aroused
            "I chuckled again as Hoss played with his mane, seemingly feeling somewhat similar."
            lion "Your first, huh?"
            "He sidled in closer, joining me on the bed and laying me back."
        else:
            show lion sad
            lion "Would a hug help? Is there anything I can do if just talking about it doesn't work?"
            mc "A hug... Yeah, that'd be nice."
            show lion smile
            lion "Alright. One hug coming up."
            "He got onto the bed, getting up close and easing me back onto my back."
        "With his arms hooked under my mine he pulled me close so we were chest to chest."
        scene black with dissolve
        "I closed my eyes as I hugged him around the neck. His mane was soft and smelled nice. Despite laying on my front, he was supporting his weight on his arms and knees. With the covers between us too, there was enough covering that I was quite comfortable."
        "There was something to this, being held the way Hoss was hugging me. It was intimate without being raunchy; a big leap from what I was used to from Dean."
        "But even after spending a lot of time cuddled up to Orlando, and to a lesser extent Tyson, there was something different here."
        scene bedroom
        show lion neutral
        with dissolve
        "I must have dozed off, as next thing I knew the weight atop me had shifted enough to rouse me back to reality."
        lion "Feeling better?"
        mc "I... uh..."
        show lion laugh
        lion "You dozed off there for a bit."
        mc "Wait, I really did fall asleep? How long was I out for?"
        lion "Only a couple of minutes."
        show lion smile
        lion "But I'm glad."
        lion "You seem more perky. Want me to stick around any longer?"
    else:
        show lion neutral
        lion "Well, you're not lying. So there's that."
        "I shot him an unimpressed look before taking a sip of the tea. It wasn't nearly as good as coffee, but it was warm, and it did have something sweet mixed in too."
        lion "Did you want to talk about it?"
        mc "Not really. There's nothing really to talk about, anyway."
        show lion sad
        lion "Is coffee really that important to you? I can go get you a cup if it's that big of a deal."
        mc "No! {w=1.0} No...{w=1.0} It's alright."
        "I sighed out, rubbing my face and setting the cup of tea on the bedside table."
        mc "Coffee... is special to me. Sure, I don't mind the taste, and it gets me going, but it's more than that."
        show lion pout
        "I felt Hoss's gaze on me again, searching for another lie as if I was under interrogation. Was this how Oswin felt last night?"
        show lion sad
        "He ran a hand through his mane, giving me an uncertain look."
        lion "Did you want to talk about it?"
    "I shook my head."
    mc "No thanks. I think what I need to do now is to get dressed and go for a walk."
    show lion neutral
    lion "A walk, huh? Well... whenever you get back from your walk, or want a ear to listen to your troubles, just let me know, alright?"
    mc "Okay... Thanks."
    scene black with dissolve
    "Hoss got up from the bed and left the room without looking back."
    "In combination with what happened yesterday and everything about him being less fake, I was just confused."
    if lionlove >= 12:
        "Was Hoss... {i}Did{/i} Hoss...?"
        "More importantly, did I?"
        "I shook my head, getting up and getting ready for my day. There was no point dwelling it on it right now, anyway."
    else:
        "With a sigh I got up. Hoss was just going to have to be a mystery for now."
if boarroute == True:
    "The steps were uncertain, unmeasured and-"
    boar "W-Whoa! No, don't..."
    scene bedroom
    show boar sad
    with dissolve
    "I opened my eyes just enough to see Roswell halfway to my bed, desperately clutching a mug of coffee that was threatening to spill over from how full it was."
    "With a sigh Roswell got himself back under control and edged closer to the bed. In fear of him spilling the whole cup, I chose not to move until he sat it down on the bedside."
    mc "Morning."
    show boar smile
    boar "Good morning!"
    "He sounded chipper, or at least in good spirits. If only I could steal some of that."
    boar "How did you..."
    show boar pout
    "I flashed him a weak smile, but he saw through me."
    boar "What's wrong? What happened?"
    mc "I had... a rough night?"
    boar "Did anyone do anything? Rough nights are usually caused by something after all."
    show boar sad
    boar "If it's because of me, I'm sorry. Really!"
    mc "No, it's not you Roswell, promise."
    show boar pout
    boar "Then what?"
    "I looked away, ballooning my cheeks with air and wondering how much I should tell him."
    if boarlove >= 10:
        "When I looked back at him, he seemed genuinely worried."
        boar "If you don't want to talk about it, I understand. These last few days have been rough."
        show boar sad
        boar "The best I can do is promise that... I'll help where I can? So long as you let me know I guess."
        "I nodded slowly, looking him over."
        mc "Well..."
        "The moment I started speaking, his eyes shot up to me expectantly."
        mc "I guess a lot of it is the vault stuff, but... My head is all over the place."
        show boar neutral
        boar "Did you wanna talk about it?"
        "Roswell sat down next to me, assuming the answer was yes regardless."
        "Not that he was wrong. I did want to talk about it a little."
        mc "Maybe for a little bit?"
        "I messed with my hands, shooting him a look."
        mc "So... I guess it's about family? Um..."
        show boar pout
        "Watching Roswell's expression shift told me that he was listening if confused."
        mc "Combined with what you said yesterday, about death and all... that... y'know."
        show boar sad
        boar "O-Oh... You mean...?"
        "I nodded meekly, and Roswell shuffled closer again."
        mc "So {i}that{/i}, combined with finding out you saw me as an older brother, plus sorting out you and Tyson it's just... I'm exhausted."
        "Roswell reached over and took one of my hands, squeezing gently."
        boar "Well... is there anything I can {i}do{/i}, then?"
        show boar pout
        boar "Friends look out for one another right, and if I have any hope in more than that..."
        show boar scared
        boar "That is to say, if we, uh... I mean..."
        "I couldn't help but chuckle a little bit at how flustered he was getting. It was hard to tell if he was completely genuine about it or not, but it was enough to make me feel better, if only a little."
        show boar smile
        boar "Now that's better."
        show boar sad
        boar "But... Still. I'm sorry. You've gotten like this before. You get sad, distant, and normally you just sit in the corner on your phone."
        "He wasn't wrong, thinking back to the other times thinking about dad had put me in a slump. I managed to make my way to anime club all the same, but despite their best efforts, they just didn't know how to make me feel better."
        "Not that they didn't try or ask. I didn't know how to make myself better either half the time."
    elif boarlove >= 5:
        "Looking at him he looked away soon after, not that I blamed him."
        show boar sad
        boar "I don't... I mean I want to, but..."
        "He fidgeted, unsure of what to say or do. Not that I blamed him. He was quirky and intelligent, but his people skills were lacking. Not that mine were much better some days."
        mc "If... I think of something you can do, I'll let you know?"
        "His attention turned to me briefly before he looked elsewhere again."
        boar "Promise?"
        mc "I promise."
        "I reached over and took one of his hands, giving it a gentle squeeze. He squeezed back, a notable red tinge in his cheeks beneath his fur showing through for a moment."
        mc "But even if I don't know... Thanks for checking up on me."
        show boar smile
        boar "You're welcome."
    else:
        mc "It's really nothing. Just... a lot on my mind. The past few days have been rough is all."
        show boar scared
        boar "Oh. Right. That makes sense."
        show boar sad
        boar "Even so... Sorry you're feeling that way. it sucks seeing you like this but I get the impression there's not really anything I can do to help."
        show boar pout
        boar "Is there?"
        "I shook my head slowly. This was my problem unfortunately. Although if I knew how others could have helped, I'd have gladly taken the assistance."
    show boar sad
    #Had the talk yesterday regarding Tyson
    if Library == False:
        "Roswell looked to the floor before catching my eye. His voice held the slightest tinge of shame."
        boar "I was thinking about what we talked about yesterday."
        show boar pout
        boar "Spent most of the night laying in bed thinking about it really. Probably would have even if you didn't fill me in on how Tyson had changed."
        mc "Oh...?"
        "I wasn't sure where this was going, but I tried my best to ensure Roswell knew he had my attention."
        "He nodded, looking me in the eye."
        boar "It's... a couple of things, really."
        boar "The first being... Well, I should've been the better person about it, and revenge is really unfulfilling."
        boar "Sure, I don't think I forgive him for what he did, but I can't hold that against him forever, right?"
        "I just nodded, keeping quiet so he had the floor to continue at his own pace."
        boar "And after talking to you, I don't think there's anything left to do but to just talk to him about it either."
        mc "You're sure? I mean it'd be great if you guys got on, but..."
        "Roswell nodded, thoughtful."
    else: #didn't have the conversation, Roswell apologises
        "Roswell sighed out."
        boar "I owe you an apology."
        "I blinked, confused as to what he was apologizing for. He continued when I didn't immediately reply."
        "His voice was held low, quiet as if he was ashamed of what he was saying, but his pace implied he'd rehearsed."
        boar "I... understand that a whole bunch of things have changed in the time I was gone."
        boar "You and Tyson for instance. I get on well enough with Orlando, and Hoss is fine too I guess."
        "With a sigh he scratched his head."
        boar "The assumption was that... I guess I could just move back and pick up like nothing was different? Which the more I think on it just seems childish."
        "I shook my head."
        mc "I mean... We kept in contact, right? Sure, it was letters and email, but you never really {i}left{/i}."
        "Roswell sighed out, looking me over."
        show boar pout
        boar "The real world is going to be difficult, isn't it? What I wouldn't give to just stay in school."
        mc "Why school though?"
        show boar smile
        boar "I was good at school. Homework, academics. Plus being at the top of the class was nice with the attention and praise."
        mc "And the bullying?"
        show boar pout
        boar "Okay, that not so much. I'd rather avoid that if I got a do-over."
        boar "But as much as I'd want to avoid it... I think I'm a little bit thankful for it."
        "I blinked, not expecting Roswell to come out with such a thing."
        boar "Uh... I mean I suppose in the sense that being bullied by Tyson meant I was ready for what to expect moving forward?"
        "He grumbled, fidgeting again."
        show boar sad
        boar "And I'm sorry that... Well, we kissed, really."
        show boar pout
        boar "I think I jumped the gun on that one."
        "It takes two to kiss, so I was just as much at fault as Roswell, although before I could say this, he continued."
        boar "It's jealousy, I think. Seeing you look at Tyson with adoration, and with such awe..."
        boar "Orlando you're calm and happy, but..."
        "He trailed off, leaving me to tilt my head in confusion as to where he was going with this."
        boar "I just don't get it. Why Tyson? Why not me?"
        "I smiled softly, dipping my gaze down as I thought over my reply."
        mc "It's kind of like how you see me as an older brother, right? Or did see me like that anyway."
        mc "When I first stood up for him, it was because I'd learned what the right thing to do was."
        show boar sad
        mc "And then I guess since then, he's kinda looked out for me because I gave him a chance?"
        "Roswell's eyes were darting back and forth on the floor as he tried to come to terms with what I'd just said."
        boar "He... looked out for you?"
        "Nodding, I continued."
        mc "When I was sick, he ditched school just so I wasn't lonely. Or when I was stressing about a test, he got me the answers, not that he told me if he stole them or not."
        mc "He'd just make sure I was okay from time to time, and take me places on the weekend just at stuff he thought was cool."
        mc "Sure, he sorta decided stuff by taking charge, but he wasn't ever really... demanding, if that makes sense?"
        mc "Never asked for anything either, he just always made sure I was cool with what was going on and took me along for the ride."
        show boar pout
        boar "That... doesn't sound like the bully I once knew. I'd almost think you were talking about someone else entirely."
        mc "He's changed. Or maybe it wasn't that he's changed but... he had someone looking out for him for a change?"
        mc "He's... basically like a big brother, I guess."
        "Roswell nodded slowly, processing what I'd just said."
    boar "I guess today's apology day."
    show boar sad
    boar "Be it... I don't know... something long and drawn out or just a quick one, he's a hard one to read."
    mc "Oh..."
    "It was nice to hear that he was going to be apologizing for his behavior, but a worry in the back of my mind made me fearful for how Tyson would take it."
    mc "Did... you want me to be around for that? I'm happy to be if it'll make things easier."
    show boar mad
    boar "No. This fight I wanna handle myself."
    show boar pout
    boar "No offense, but if I can't do this by myself, then it's not going to mean as much, right?"
    mc "I guess so... But if you want help..."
    show boar smile
    boar "I'll be fine, I think. Once I figure out how I wanna phrase things, I should be good to go."
    show boar grin
    boar "Speaking of, I should let you get up and get your day started, huh?"
    mc "Oh! Yeah, I guess I've slept long enough, huh?"
    show boar smile
    boar "Yup! Well, I'll see you later, [mcname]."
    scene black with dissolve
    "Roswell shuffled off, giving me a wave as he closed the door behind him on his way out."
    "I downed the coffee he brought me before taking on the monumental effort of getting out of bed."
if crocroute == True:
    "There was only one person who had such heavy footfalls, it was hard to tell if he was actively making an effort to stay quiet."
    "He said nothing, instead wandering close to the bed, stopping as if he was trying to figure out if I was awake first."
    scene bedroom
    show croc neutral
    with dissolve
    "The smell of coffee was enough to make me open my eyes, Sal standing there with the mug held in both hands."
    croc "Morning."
    "There was a slight rumble in his throat as he spoke, the corners of his mouth twitching upwards slightly."
    show croc smile
    croc "Did you sleep well? I brought you some coffee."
    "I didn't have the heart to tell him no outright, especially as he gingerly passed the mug over."
    if croclove >= 15:
        show croc annoyed
        croc "Hrm... [mcname]."
        mc "Yes?"
        croc "What's troubling you?"
        mc "Is it that obvious?"
        show croc pout
        croc "Somewhat."
        croc "You weren't up at the normal time this morning. Some of us were worried."
        mc "Was that really all?"
        show croc neutral
        croc "No.{w=0.5} I assumed something was wrong when you looked at me."
        show croc sad
        croc "It was a familiar expression. That's all."
        mc "Oh..."
        "I sipped my coffee, pulling my gaze away."
        croc "I was wondering something. It's been bugging me for a while, but it's personal. Do you mind?"
        mc "Not... really? But I guess that depends. What's up?"
        show croc pout
        croc "Have you... lost anyone dear to you?"
        "I seized up upon him asking, but nodded slowly."
        mc "Yeah... My dad."
        show croc scared
        croc "Your... dad?"
        show croc sad
        croc "I'm so sorry."
        mc "Did... Orlando never tell you?"
        show croc pout
        croc "Even if he did, that's... something better left to hear from you directly. At least in my opinion."
        croc "He mentioned it in passing, but talking of the dead doesn't... normally come up."
        "Again I nodded, slowly, tailing my eyes up from his feet to his hands held anxiously together as he stood there."
        mc "Sit, Sal. You don't need to stand."
        show croc neutral
        croc "I'm fine. Just concerned."
        mc "About me?"
        croc "About a few things, but mostly you."
    if croclove >= 8:
        show croc pout
        "With a sigh, Sal rubbed his head."
        croc "Sorry."
        mc "Huh? What for?"
        show croc neutral
        croc "I feel as though I'm overstepping a line by saying this, but I believe you're troubled by something."
        mc "What... makes you say that?"
        "I began to chuckle quietly, putting up a façade in hopes he wouldn't ask further."
        show croc pout
        croc "You weren't up at the normal time. We were worried."
        mc "Oh..."
        croc "Some of us wanted to check in, the rest wanted to let you sleep."
        show croc neutral
        croc "It's why I'm here now. I wanted to check."
        show croc pout
        croc "I won't pry if you don't want to talk about it, but I'm almost certain you're troubled by something."
        "I took a swig of the coffee I held, sighing out after I'd swallowed. Drumming my fingers against the mug I wondered how I should answer him, but he continued on regardless."
        croc "I... recognize that look you're wearing. I recognize it from looking in the mirror."
        mc "Did... you want to sit down?"
        show croc neutral
        croc "No. I'm fine, just concerned."
        mc "About me?"
        croc "Mostly."
    else:
        show croc neutral
        "I felt Sal's eyes on me as I drank from the mug he brought."
        mc "What's wrong?"
        croc "Nothing."
        show croc pout
        croc "What's wrong with you?"
        mc "Nothing's wrong...?"
        croc "You weren't up at the usual time, and you're putting on a brave face."
        "Before I could retort he continued."
        croc "I was worried, so I brought you coffee."
        mc "Oh..."
        show croc neutral
        croc "And..."
        "Sal looked me over, brow furrowed slightly."
        croc "Orlando has told me things, in the past. Things that are the cause of your troubles now."
        croc "I'm not going to pry. I'm not going to ask."
        show croc sad
        croc "But I just want you to know I'm concerned."
        mc "About... me?"
        croc "Among other things."
    mc "I'm not worth worrying about Sal, at least not about... Well, what's got me down."
    show croc annoyed
    croc "How dare you?"
    mc "Huh?"
    show croc pout
    croc "That's not your call to make."
    croc "Your friends care about you. It makes sense that those that care about you would be worried when something's upsetting you."
    mc "I know... I just don't like talking about it."
    show croc neutral
    croc "Maybe you should."
    mc "But why? It sucks."
    show croc smile
    croc "It wouldn't be upsetting if it didn't suck."
    show croc neutral
    croc "But saying your troubles out loud helps, even if no one's around to listen."
    show croc pout
    croc "...Or if people keep interrupting you."
    croc "And it should go without saying that if you want to talk... Well, I'm available to listen."
    mc "Thanks Sal, I'll... keep it in mind."
    show croc neutral
    croc "Good."
    "I continued to drink the coffee, occasionally glancing at Sal who was watching me with an air of curiosity."
    mc "What about you?"
    show croc scared
    croc "What about me?"
    mc "Everything... Going alright on your end?"
    show croc neutral
    croc "I don't know yet. It's been a busy past few days."
    croc "Or at least...{w=0.5} Busy in the sense of thinking things through."
    mc "It wouldn't be fair if I didn't offer the same to you Sal. I mean... if you wanted to talk."
    show croc smile
    croc "Thanks, but..."
    show croc pout
    croc "I'm not sure if I have the words yet. If I think of them, I'll be sure to let you know."
    mc "Oh..."
    croc "I should let you get ready, anyway."
    mc "Off to do something?"
    croc "Don't know yet. I'll see what the others want to do and decide."
    show croc neutral
    croc "Speaking of, what about you?"
    mc "Probably take a walk. Use the time to find the words to talk about my problems for later, right?"
    show croc smile
    croc "Well alright. But if you want some company..."
    mc "Not this time, Sal. But thanks."
    show croc neutral
    croc "You're welcome."
    scene black with dissolve
    "He backed up slowly before turning around, leaving me to get ready."
    "I swirled the remainder of my coffee in the mug for a moment before finishing it off, setting it off to the side and stretching on my way out of bed."
#if Oz was told about, have Benson go on vacation
#otherwise have him run into Dave and have a brief talk
#actually have that talk either way, but cut it short with Benson leaving
stop audio fadeout 2.0
scene foyer with dissolve
"Dressed and as ready as I could be, I made my way downstairs."
play music calm fadein 2.0
if OzKnown == True:
    show otter neutral with dissolve
    mc "Oh, good morning, Benson."
    otter "Good morning."
    "There was something extra stiff with how Benson was standing this morning, and he was eyeing me carefully."
    mc "Is... everything okay?"
    otter "I believe so. How did last night fare?"
    mc "Oh, with..."
    "I looked around, checking to see if there was anyone else nearby listening in. Seemed like only Benson and I were in the foyer."
    mc "Oz?"
    otter "Indeed."
    mc "Oh. It went... Alright I guess."
    otter "Good."
    show otter pout
    otter "Well... At least I hope so."
    mc "What do you mean?"
    show otter neutral
    otter "As it turns out, I've been given leave for a vacation of my own. Effective immediately."
    mc "That's great!"
    show otter annoyed
    "Benson's stern expression immediately told me that perhaps it wasn't so great as I thought."
    otter "It wasn't so much a request as an order, Master [mcname]."
    mc "Oh..."
    show otter neutral
    otter "I'm on my way to pack a suitcase right now, actually. Within the hour I'll be well on my way."
    mc "How long's your vacation then?"
    show otter annoyed
    otter "Until I'm asked to return."
    show otter pout
    "With a sigh, Benson teased the end of his moustache, looking away thoughtful."
    otter "I suppose this might be a little odd for you, but know that the master of the house rarely makes such requests."
    show otter neutral
    otter "I can only fathom a guess as to why he's made it, too. He refused to elaborate when I was told this morning."
    mc "Oh..."
    show otter pout
    "The two of us stood looking at one another before Benson looked away again, shaking his head."
    otter "No matter."
    show otter neutral
    otter "I suppose that whatever is to happen, is to happen."
    show otter smile
    otter "I wish you the best of luck, Master [mcname]."
    mc "Wait! Is there anything you can do before you leave? Any last advice?"
    show otter neutral
    "Benson looked me over, stoic before looking me in the eye and speaking with a measured, serious tone."
    otter "Survive. As best you can."
    hide otter with dissolve
    "There was something chilling about how he said that, so much so that as he stepped around me and out of sight I was frozen on the spot."
    "Survive? I was meant to just... survive?"
    $ BensonAround = False
else:
    "At first glance, it seemed as though there wasn't anyone else around. It felt... lonely, but I knew that I needed the space to think things over."
    "Where were the others though? Were they all separated, or were they together? I grumbled, digging my fingers into my head and lightly tugging on my fur."
    show otter pout with dissolve
    "It was only when Benson cleared his throat that I took notice of him, standing off to the side, watching me curiously."
    otter "Are you quite alright?"
    mc "Oh. Sorry, I didn't see you there."
    show otter neutral
    otter "I haven't been here long. But you seem distraught."
    mc "Maybe. Actually no, yes. I am. Just..."
    "I threw my hands up, before letting the entirety of my body slump just shy of being enough to make me fall to the floor as I groaned."
    mc "Last night took a lot out of me."
    show otter smile
    otter "Did you make the most of it, though?"
    mc "I guess? It... I don't know if it's really gotten me anywhere though."
    show otter neutral
    otter "Indeed. Master Oswin mentioned as such when I brought him his breakfast."
    mc "Was he saying it about him, or me?"
    show otter smile
    otter "He's undecided about himself. All I know is that he was eager to get to his lab this morning to do... Something. I may have been around a while, but when the master goes on about..."
    show otter pout
    "Benson paused, toying with his moustache while he pondered something."
    otter "The more {i}technical{/i} aspects of both his hobbies and qualifications, I find myself at a loss."
    mc "Oh, well... Okay. Maybe I'll find out in a few days then."
    show otter neutral
    otter "What makes you say that?"
    mc "Oh. He said in a few days he'll show me something so... I dunno, maybe it's something involving that?"
    show otter pout
    otter "Hrm... I wonder..."
    show otter smile
    otter "Ah, yes. Before I forget, your laundry is almost ready."
    mc "Oh! Great!"
    otter "I would advise against being so... messy in future. Pumpkin stains are easy enough to get rid of. Other things, not so much."
    mc "Promise!"
    otter "I'll bring your clothes to your room sometime today."
    mc "Oh, okay. Sorry for the mess, I uh..."
    "I shifted on the spot, uncomfortable."
    show otter pout
    otter "Now, now, m'boy. If I've had to clean up after Master Oswin, I'm sure your room will be fine by comparison."
    mc "Is he... really messy?"
    show otter smile
    otter "Oh, you have no idea."
    show otter neutral
    otter "Now, I best be off. Good day, Master [mcname]."
    mc "Oh. See you later, Benson."
    hide otter with dissolve
    "I watched Benson move towards the stairs and about halfway up before continuing on."

#Breakfast
scene diningroom with dissolve
"I found myself looking around an empty room again, and I scratched my head as I took a whiff of the air. I could still smell the lingering scent of toast, along with coffee."
"I wandered to the other side of the room, following the scent. By the time I was near the door leading into the kitchen I found myself looking down, skirting around a particular spot on the floor that looked somewhat familiar."
scene kitchen with dissolve
"Once again I was alone, and this time sighed out without restraint. As bad as it was, I was half expecting Orlando to be in here. They just had to be elsewhere in the house, right?"
"The smell of toast was stronger in here, but I didn't want toast."
"Whenever I thought of my dad, I thought back to the breakfasts that we had, that he made for the two of us when mom was at work or otherwise just not around. That was usually... hardboiled eggs, fruit, sometimes waffles if burnt ones."
"Of the options available, I just grabbed a banana. Part of me wondered what Dean would've said if he saw me eating this."
mc "Probably... probably like...'Oh, I know something else you could put in your mouth that's the same shape.'"
"I shook my head, a slightly smile forming. The consistency was nice, if anything."
"Pacing the kitchen with my banana I ate bite after bite thinking things over."
"Was this what it was like to be a cop? Figure things out, accept that you were potentially in risk of dying in the line of duty?"

#go for a walk
scene mansionfront with dissolve
stop music fadeout 2.0
"I left the kitchen and found myself outside. Stretching I felt my spine pop and joints loosen. The plan was to go for a walk, but I didn't really know where I was going."
"The front yard was expansive, the driveway leading further down out of sight beyond the trees. Maybe following it towards the main road would be an idea, in case we needed to escape?"
"Burying my hands in my pockets I started the slow stroll towards the trees and down the driveway."
scene woods2 with dissolve
play audio forest fadein 2.0
"It was quiet, even the sounds of insects and birds were muted, almost as if there was this... silence that was draped over the place."
"Light filtered down from the canopy above, lighting my way down the winding driveway. Everything looked the same, and around each turn seemed to just be more driveway."
"If I had my phone on me, I would've been able to check how long I'd been walking, but it felt like a solid hour with no headway."
"With a sigh I looked back, the way I'd been looking just the same as what lay in front of me."
"Taking a load off on the side of the driveway, I let my mind wander."
scene black with dissolve
"It'd been about a year since it happened."
"Some days were better than others, but even after this long I refuse to believe that it happened at all."
"Orlando kept reminding me to accept it and try and move on, and I know that because of it I've withdrawn. But really, what does he know?"
"None of them, at least as far as I could tell knew what it was like. Which is probably why this whole ordeal with Oswin was putting me at odds."
if OzKnown == True:
    "I'd told the others that he was still around, but they didn't have the burden of supposedly being some chosen one that managed to see death before it could happen."
else:
    "I wondered if it was worth bringing it up with the others. If seeking help from the others was worth blowing Oswin's cover."
"At least until I could figure things out, I was in this by myself."
scene woods2 with dissolve
"Grumbling I stood back up, shooting a look down the driveway."
"I could leave now, put all of this behind me and just run."
"Looking back at the way I'd come, I grimaced. Running would maybe keep me safe, but what about the others? If I wasn't around to stop them from dying, would it just keep happening?"
"The stress was making me tug at my fur, a habit that I'd picked up from Tyson when he was upset."
mc "...Why me?"
"Groaning, I started to head back to the mansion, shoulders slumped and dragging my feet."
"As I trudged back the way I came, I wondered what Roswell's take on this would be. He always had an interesting way of seeing the world, and maybe being a boar would make it easier to have a read on Oswin."
"I smirked, the in-joke flashing to the forefront of my mind. With how often we said 'racist' to one another, I was starting to wonder where the actual line was drawn."
scene mansionfront with dissolve
"By the time I reached the front of the house I was tired again. Be it the rough night or the walk, I wasn't sure which. Either way, I was ready for something to eat or at the very least another chance to sit down."
"My hand went to my pocket to check my phone, patting it down before realizing I'd left it up in my room to charge. Was it lunch time? I wanted it to be."
stop audio fadeout 1.0
scene diningroom with dissolve
"I wandered back inside and heard people nearby. After having missed them for breakfast, I was eager to see what they were up to."
#lunch time?
#Tyson/Hoss/Dean
play music happy fadein 2.0
show wolf pout at left
show lion mad
show bear scared at right
with dissolve
"As I entered the room, I saw a... heated discussion led by Hoss between the two others he was nearby. None of them seemed to pay me any mind as I entered."
hide wolf
hide lion
hide bear
with dissolve
"By comparison though..."
#Sal/Orlando/Roswell
show croc smile at left
show boar laugh
show dragon pout at right
with dissolve
"The others were in a pause in their conversation, with Orlando looking anywhere but the other two he was sitting near."
show dragon smile
dragon "Oh! [mcname]! Perfect timing!"
mc "Perfect timing... for what?"
"I eased closer carefully, wondering what I was about to get wrapped up into."
show dragon mad
dragon "To tell these two off! They're being mean!"
mc "Oh."
mc "Guys, being mean is bad."
show boar grin
boar "We're not being mean, we're just having a little fun is all."
mc "Oh, well I like fun. Fun is good."
show dragon mad
dragon "Don't fall for it!"
show croc pout
croc "I don't understand, what's wrong with what we were saying?"
show croc neutral
croc "If you have stuff in your beard, someone should tell you."
show dragon sad
"Orlando grumbled to himself, shaking his head before resigning the point."
mc "Oh, by the way... What's the time? My phone's dead."
show boar pout
boar "It's dead? You didn't charge it while you were sleeping?"
mc "Oh, uh..."
show croc pout
croc "He forgot."
mc "No! I didn't {i}forget{/i}, I just... uh..."
show croc neutral
croc "..."
show boar grin
boar "..."
mc "So... Lunch? It's lunch time, right?"
if BensonAround == True:
    dragon "That's right. Benson made us lunch before moving off to go do something else. Not sure what though, he seemed to be in a hurry."
else:
    dragon "Yeah. I made some sandwiches earlier, just to get it out of the way."
mc "Hold on, have you all eaten?"
show dragon neutral
dragon "For the most part. We looked around for you but figured you couldn't have gone far."
show dragon scared
show croc scared
show boar scared
mc "But what if I had been killed!?"
"I snapped out suddenly, causing the three of them to look quickly at one another before facing me."
"Feeling foolish, I fell into the nearest chair and buried my face in my hands."
dragon "So... I'm going to go bring you your lunch."
boar "And I'll... help. Yeah. You could probably use some coffee."
hide dragon
hide boar
with dissolve
"Roswell and Orlando scurried off quickly, leaving me with Sal. He eyed me carefully before settling back down enough to say something, voice brought down to a hushed tone."
show croc pout
croc "Are you okay?"
"I groaned, rubbing my face."
mc "I'm fine, just still..."
"I gestured, hands in the air trying to wave off my own worries and by extension Sal's. It seemed to work enough that Sal settled back into his chair without a fuss."
hide croc with dissolve
show wolf neutral at left
show lion neutral
show bear neutral at right
with dissolve
"My outburst had  brought the other three over, seemingly done with their conversation for the time being."
lion "Did I hear you correctly, [mcname]?"
"I kept my eyes averted, looking towards the door to the kitchen feigning to just be eager to get my lunch."
show wolf pout
wolf "You did."
show bear pout
bear "Can you blame him though?"
show bear neutral
bear "How are you feeling outside of that?"
show lion smile
lion "And where did you disappear to? Have an adventure?"
mc "I just decided to wander around for a bit. After I got up, had a bite to eat and figured I'd walk down the driveway and see what I missed when we arrived."
show wolf neutral
wolf "Anything good?"
mc "Not really."
show lion laugh
lion "There really wasn't much between here and the main road from memory, but that was some long driveway."
mc "You're telling me. I didn't even make it to the main road."
show lion neutral
lion "No surprise. But explains why you were missing. Maybe just let us know where exactly you're going next time?"
mc "Okay, sorry."
show wolf pout
wolf "Couple of us were worried."
show bear pout
bear "Good thing you stuck to a path though. But as Tyson said, try to let someone know where you're going next time."
"I rolled my eyes. I understood why I might've been coddled like this but no one really kicked up a fuss about Roswell heading into the forest by himself."
mc "Okay, I promise the next time I go wandering I'll let someone know which direction I go in."
mc "But what were you guys talking about when I arrived? Seemed... intense."
show bear neutral
show lion mad
"Dean looked between Tyson and Hoss, taking a step back."
wolf "Don't worry about it. It wasn't important."
lion "Not important!? I'll have you know that it's very important."
mc "{i}What{/i} is important?"
show wolf neutral
wolf "Some show Hoss wants me to watch."
wolf "Apparently some guys pose at each other and all have the same name."
show lion yell
lion "They do {i}not{/i} all have the same name! You haven't even seen an episode, you might still like it."
show wolf pout
wolf "And what makes you think stopping time and dropping road rollers on people makes for a good show?"
wolf "Like, whatever. It sounds dumb."
mc "Oh, if this is the show I'm thinking about, it has a bunch of punching too."
show wolf neutral
wolf "Punching, huh?"
show bear pout
show lion pout
lion "Really? That's what sells it for you?"
bear "Well, it makes sense that he'd be more sold on that."
show wolf annoyed
wolf "Hey, I've not watched any of your cartoons before, cut me some slack."
lion "{i}Anime.{/i}"
show wolf pout
wolf "Whatever. Same thing."
"Hoss's eyes bulged for a second before Dean chimed in, trying to curb the conversation."
show bear scared
bear "So [mcname]! What were you planning on doing today?"
"I looked between Hoss and Tyson before addressing Dean."
if wolfroute == True or lionroute == True:
    "Or at least I would have if I wasn't cut off immediately after being asked."
    wolf "He's coming with us."
    mc "Wait, I am?"
    show lion smile
    lion "Yup. If only for a little while."
    bear "But why?"
    show wolf pout
    wolf "If I'm gonna get put through a cartoon, I'm putting [mcname] through it too."
    show lion grin
    lion "And I'm going to need the assist in convincing you it's a good show."
    mc "Well I'm not doing anything until I've had coffee and a sandwich. Or just something to eat for lunch."
    show wolf smile
    show bear laugh
    bear "Seems fair, and if there's room for one more maybe I'll check out what this cartoon is about too."
else:
    mc "I... think I'm just going to keep my options open for now."
    if bearroute == True:
        bear "Well... it's a shame we just had lunch, otherwise I'd suggest a picnic."
        wolf "A picnic? Really?"
        show bear annoyed
        bear "Yes a {i}picnic{/i}, what's wrong with that?"
        show lion smile
        lion "Don't see anything wrong with that really, but maybe Tyson's just jealous."
        "My attention turned to Tyson immediately, who seemed to have his jaw and fists clenched but he didn't seem to be acting out."
        mc "Uh... Hoss? That... might not have..."
        show wolf neutral
        wolf "Don't worry about it, pup."
        wolf "He's the one that's jealous."
        show lion scared
        lion "What? I don't... I... uh..."
        show wolf grin
        wolf "Can't take what you dish out?"
        show lion sad
        show bear sad
        bear "Well... In any case, you've gone for a walk but perhaps did you want to sit inside today?"
        wolf "Want to watch this cartoon with us?"
        bear "I can't say it's normally what I'd go for, but potentially. What do you think, [mcname]?"
    else:
        show bear neutral
        bear "Fair enough. If you want some company though, feel free to come bother me. Otherwise I'll probably just tag along with these two and check out this cartoon."
        show lion scared
        lion "Ignoring the fact that it's not a {i}cartoon{/i}, I wouldn't have picked you to be interested, Dean."
        show bear pout
        bear "What? I'm allowed to try new things, right?"
        show wolf smile
        wolf "At least I won't be suffering alone with this."
hide wolf
hide bear
hide lion
with dissolve
"I looked back over to the door leading into the kitchen just as Roswell and Orlando were emerging from it."
show boar smile at right
show dragon neutral at left
with dissolve
"Roswell had a mug, and Orlando had a plate stacked with a couple sandwiches."
"I wandered away from the other three towards them, seemingly joined by Sal on my way over."
boar "One coffee."
dragon "And two sandwiches."
show croc neutral
"I felt a hand on my shoulder, looking to Sal who joined the conversation with a comment of his own."
croc "And three of us."
show boar pout
"Roswell counted us off with his spare hand, staring down at his count of four, confused."
mc "So what are you guys doing with the rest of the day? Looks like the others are off to go watch some anime."
if bearroute == True or lionroute == True or wolfroute == True:
    mc "I've been roped in too apparently."
    show dragon smile
    dragon "Oh yeah? What are they watching?"
    mc "I'll give you one guess."
    "Orlando looked around me to Hoss, who was mid-pose while Tyson was rolling his eyes. Dean as confused as you'd expect."
    show dragon neutral
    dragon "Bold move."
    dragon "Although showing Tyson anything is a hard guess... I guess an anime about fighting is... well at least action happens in it."
    show croc pout
    croc "What... kind of show is it?"
    show boar smile
    boar "Oh, so... imagine that they're like ghosts that help you fight."
    show dragon scared
    dragon "They're {i}not{/i} ghosts!"
    show boar grin
    boar "They may as well be."
    show croc neutral
    croc "Well alright. I hope you enjoy your ghost fighting cartoon."
    show dragon annoyed
    dragon "They're not ghosts, Sal! More... embodiments of the soul."
    show dragon smile
    dragon "Of the fighting spirit!"
    show croc sad
    croc "Can't they all just get along nicely?"
    "Roswell shook his head and handed the coffee to me, letting me drink in deep. Not long after did Orlando sat down the sandwiches in front of me."
else:
    show dragon smile
    dragon "Oh yeah? What are they watching? Maybe we should all go."
    show croc pout
    croc "Given Dean's reaction, I don't think it's something we're all going to enjoy."
    mc "Hoss picked out something to... I dunno actually. But if I said road roller..."
    show dragon scared
    dragon "Oh. Bold move on his part."
    show boar sad
    boar "Somehow I think that's either going to go very well, or very poorly depending."
    show croc neutral
    croc "Is it that bad?"
    dragon "Well, if I remember correctly, the first scene of the first episode... well..."
    show croc scared
    croc "What?"
    show boar scared
    boar "Probably better you don't know, Sal."
    show boar sad
    boar "Just... Well, at least we know that's off the table as a joined activity."
    show boar neutral
    mc "Yeah... But hey, while they're doing that, you guys must have something in mind, right?"
show croc pout
croc "I was considering a swim, but now I'm not too sure."
show dragon sad
dragon "I'd... still like that lesson, if that's alright?"
show croc smile
croc "I'm happy to give you that lesson still."
show croc sad
croc "Assuming that's still comfortable for you. Just... not today."
show dragon scared
dragon "Oh... Alright."
show croc pout
croc "I just... need to clear my head of a few things."
show boar smile
show dragon pout
boar "Well, why don't we play a board game or something to pass the time? No point the others doing something when we could also do something."
show croc smile
croc "Sure, I'm down for a board game."
show boar neutral
if bearroute == True or lionroute == True or wolfroute == True:
    boar "If you get tired of watching anime, you're welcome to join us if we're still playing, [mcname]."
    show boar laugh
    boar "But if you're keen on watching anime, you'd probably want to eat lunch before they start without you, right?"
else:
    boar "Wanna join us? You're welcome to if you're not doing anything."
    mc "Sure, I'm down to play for a bit. I don't think I want to be wandering around any more after my walk anyway."
    show dragon smile
    dragon "How do we feel about Monopoly?"
    show croc pout
    croc "Uh..."
    show boar grin
    boar "Or Clue?"
    show croc scared
    croc "Um..."
    show croc pout
    croc "...Scrabble?"
hide croc
hide boar
hide dragon
with dissolve
"I turned my attention to my sandwiches, seemingly two different kinds. The first looked to be something with chicken, lettuce, and mayonnaise looked like it had cheese on it too."
"The second was the one I was more keen on. Egg salad. I just hoped it tasted good, but I had faith that if Orlando made it he wouldn't do me wrong."
"There was nothing like having a good meal, something I was reminded of while I was halfway through my first sandwich."
"Less cranky, less stressed, who knew that having a decent feed would make you feel better both physically and mentally?"
"By the time I'd downed the second one, it looked like everyone was ready to start heading off to go do their thing."
stop music fadeout 2.0
scene black with dissolve
"I took my mug and plate into the kitchen, putting it in the sink to be washed."
"It seemed like the other dishes were still here, so I felt less bad just adding to the pile."
"Still..."
if BensonAround == True:
    "I shook my head. Benson would probably get to it later, right?"
    if DavePride >= 1:
        "Even then, I felt like I really should clean up. If only to help out."
        "I opted for the middle ground, organizing the dishes so at least the plates were stacked, mugs all gathered together, so that whoever did clean up had an easier time of it."
    else:
        "This was fine, right? At least I could stack the dishwasher maybe? But with how everyone else had left them here maybe they had arranged someone to do the dishes later already."
else:
    "If Benson was heading off, it seemed unlikely that he'd do the dishes before leaving. Especially if he was going on vacation."
    "The others must have already decided who was going to do the dishes in that case, unless... They didn't know?"
scene diningroom
show boar sad at left
show wolf neutral at right
with dissolve
play music tense fadein 2.0
"I wandered back into the dining room to see Roswell and Tyson facing one another. Quickly I looked to the others, who seemed to be swapping looks just as confused as I was."
wolf "What do you want?"
#Roswell apology
show boar mad
"Roswell seemed to be readying to say something, his brow furrowed as he thought things through."
if boarroute == True:
    "It then clicked, I knew what he was about to say."
else:
    "Part of me hoped that he wasn't about to pick a fight, as unlikely as that seemed."
boar "While everyone is here..."
stop music fadeout 1.0
boar "I want to apologize."
play music calm fadein 2.0
show wolf pout
wolf "For what?"
show boar annoyed
boar "You know what for."
show wolf neutral
"Tyson looked Roswell over, eyes narrowing only slightly before he nodded to the boar."
wolf "Alright."
show boar sad
"Everyone seemed to be giving Roswell the floor to speak, and just as well."
boar "I'm not going to lie, you were the last person I wanted to come onto this trip with us."
show boar pout
boar "You were an asshole to us when we were younger. I hated you for that."
show wolf pout
wolf "This is a great apology so far."
show boar mad
boar "I'm getting there!"
boar "It's that very attitude that frustrates me. How can [mcname] move on from that? What does he even see in you?"
show boar pout
boar "But that doesn't matter. It really doesn't."
boar "Me not being able to move on shouldn't, {w=0.5} and doesn't, invalidate any improvements you've made to yourself in the time I wasn't around."
show boar mad
boar "So by extension, me taking it out on you, taking pot shots when I had no right to, put me in the wrong. No matter the reason."
show boar pout
boar "So... I'm sorry."
show wolf pout
"Tyson sighed, scratching his neck."
wolf "Look, I get it. I do."
wolf "Didn't think you had the balls to be honest, but I'm glad you got to vent... whatever it was."
show boar mad
show wolf neutral
wolf "But sure. Apology accepted."
wolf "While I'm at it, I'm sorry too."
show wolf sad
wolf "Not that it makes up for it. But that's how it goes."
boar "Really?"
show wolf neutral
wolf "Look, getting invited to this thing was great of [mcname] to do. If, y'know, a dick move on his part."
"Everyone in the room looked to me, and I stared back at Tyson, uncertain of what he meant."
mc "What... did I do?"
hide wolf
hide boar
with dissolve
show dragon pout at left
show bear neutral at right
with dissolve
dragon "Well... I wasn't going to say this but..."
dragon "It seemed... like a jerk move to invite Tyson along without checking with us."
bear "Right. Seems like something you'd want to run by everyone first."
dragon "Sorry, [mcname]. But if I knew you were going to invite Tyson, I'd uh... yeah..."
hide bear
hide dragon
with dissolve
show croc pout at right
show lion neutral at left
with dissolve
croc "I'm sorry too."
lion "Why are you sorry, Sal? You do something wrong too?"
show croc pout
croc "Not that I know of, but it seems to be what everyone is doing."
show lion sad
lion "Well hey, no need to apologize if you've done nothing wrong."
show croc neutral
croc "True. But [mcname], why didn't you check with everyone?"
show lion neutral
lion "Yeah, [mcname]. I think that's a fair enough question to be asking. You think everyone would've said no?"
mc "Well kinda, yeah!"
show croc sad
croc "Then... Why?"
mc "I... uh..."
"I looked to Tyson, who had his attention on me too."
mc "He's my friend."
hide croc
hide lion
show wolf neutral
with dissolve
mc "And..."
wolf "That's enough, pup."
wolf "It's not all on him. I knew what the go was. I accepted anyway, so there's that."
mc "Okay, well... I'm sorry. But..."
show wolf annoyed
wolf "No buts. You own up to it like a man."
"I whined, hanging my head. It was my fault. I should've checked."
menu:
    "Apologize again.":
        $ DavePride += 1
        hide wolf
        show boar pout at left
        show dragon sad at right
        with dissolve
        mc "Roswell? Orlando? I...{w=0.5} I'm sorry."
        mc "Especially to you two, I should've... y'know, checked."
        boar "This vacation {i}was{/i} meant to be for all of us. So it would have been nice to know who you'd decided to invite."
        show boar neutral
        boar "But I can't hold it against you. It's not like I bothered to check."
        dragon "Would you feel the need to check, Roswell?"
        show boar sad
        boar "No, probably not."
        show dragon smile
        dragon "The upside though... At least from my end, is that I've noticed a change. I didn't really want to make a big deal about it, but I've also been keeping my distance."
        dragon "But if you're sorry about not checking with us first, [mcname]? I forgive you. What sort of friend would I be if I held that against you, and let it sour the vacation?"
        show boar smile
        boar "Right! Ditto."
        show boar neutral
        boar "All is forgiven."
        show boar pout
        boar "Well, not everything, but we're well on our way. At least as far as you and me, [mcname]? We're good."
        mc "And of Tyson?"
        show boar neutral
        show dragon neutral
        boar "I'm... willing to keep a more open mind. Not necessarily about a clean slate, but only one way forward."
        dragon "Same here. But uh... Are we allowed to call each other out on behavior and decisions? Y'know, to avoid incidents like a couple days ago?"
        boar "I think that's fair, right?"
        mc "That... extends to everyone, right?"
        show dragon laugh
        dragon "Of course!"
        "There were rumbles of agreement from everyone."
    "Stay quiet.":
        show wolf neutral
        wolf "Well... No point dwelling on it. You'll be alright, pup."
        "I nodded meekly as everyone else seemed to be readying to head off."
        "Tyson placed a hand on my head, making me jump before flashing me a quick smile."
        show wolf smile
        wolf "Buck up."
stop music fadeout 2.0
scene black with dissolve
"With apologies out of the way now, we split up."
play music light fadein 2.0
#Tyson/Hoss/Dean - Watch Anime for a bit
if bearroute == True or lionroute == True or wolfroute == True:
    scene casino
    show lion neutral
    with dissolve
    lion "Alright! Class is now in session!"
    show lion smile
    "Hoss jogged over to the entertainment system and started messing with it, humming to himself."
    show wolf pout at left
    show bear pout at right
    with dissolve
    wolf "So... Am I going to regret agreeing to this?"
    bear "With how much Hoss was talking this up, it can't hurt, right?"
    wolf "Yeah, I guess you're right."
    show lion laugh
    lion "Alright! Moment of truth, Tyson. You a dubs guy or a subs guy?"
    show wolf annoyed
    wolf "The fuck did you just ask me?"
    show lion grin
    lion "Not that hard of a question. Dubs or subs?"
    show bear smile
    bear "If it's a choice between the two, I'd have to say dub. Right?"
    mc "What... makes you say that, Dean?"
    show bear laugh
    bear "Rub-a-dub-dub! Right?"
    wolf "Fuck off. That's not what that means."
    show bear smile
    bear "Does it really matter?"
    show lion mad
    lion "It's very important. If you pick wrong I mean... you're entitled to your opinion but I {i}will{/i} judge you for it."
    show wolf pout
    wolf "Ugh."
    wolf "Pup, help me out here."
    mc "Oh. Right. So... 'Subs' is short for subtitles. And 'dubs' is... uh..."
    bear "'Dubtitles'. Obviously. Easy!"
    show lion pout
    lion "Not even close."
    wolf "Do I have to read if I pick the dubtitle one?"
    show lion annoyed
    lion "It's not dubtitles!"
    show bear grin
    bear "But {i}can{/i} it be?"
    show wolf smile
    "I caught Ty smirking. He was doing this on purpose, and it seemed as though Dean had picked up on a chance to razz Hoss too."
    mc "Maybe we should stick to 'dubtitles', Hoss."
    show lion sad
    lion "Not you too, [mcname]. I'll have you know there's a fine art of dubbing something over. It's not as easy as you think."
    show bear neutral
    bear "But what is it?"
    show lion neutral
    lion "Imagine taking a video and then talking over it. But you need to also make sure that the amount of time a character is talking for matches how long it takes to say the line."
    show wolf pout
    wolf "Doesn't sound too hard. Just put the volume down and just talk over it, right?"
    show lion smile
    lion "Not quite. Then you have to worry about the music and the sound effects too."
    show bear scared
    bear "Bit too complicated for me, sorry. Is it really that hard?"
    show lion neutral
    lion "It takes some work, but I've done an episode or two of fan dubbing. We could watch those instead if you want?"
    mc "No!"
    show lion scared
    show wolf laugh
    show bear pout
    mc "Uh... No, not right now. Next time, maybe."
    show lion pout
    lion "Well fine. We'll watch the first episode dubbed and go from there; although I warn you that subs typically is the way to go."
    hide bear
    hide wolf
    hide lion
    with dissolve
    "Dean and Tyson went and grabbed beanbags while Hoss finished setting things up."
    "I thought back to the movie night and wondered."
    if bearroute == True:
        "Would Dean mind if I decided to go and sit in his lap? After all, we'd be saving a beanbag.{w=0.5} Not that there was any shortage of them, really."
    if wolfroute == True:
        "Tyson wanted some more cuddle time, although I don't know how he'd feel about sharing a beanbag in the company of others. But maybe that'd be something he'd want?"
    if lionroute == True:
        "Thinking back to the other night, I remembered how comfortable Hoss was to lay next to. If we were going to be settling in for multiple episodes of anime, sharing a beanbag might not be a bad idea."
    "Then again, I {i}could{/i} always just get my own beanbag, but where was the fun in that?"
    $ DeanAsked = False
    $ TysonAsked = False
    $ HossAsked = False
    menu:
        "Sit next to...?"
        "Hoss.":
            $ lionlove += 1
            $ HossAsked = True
            "I was sure it wasn't going to please Dean, but Ty wouldn't mind, right?"
            show bear laugh at left
            show wolf neutral at right
            with dissolve
            bear "Beanbags!"
            show bear grin
            bear "But if you want to share one with me, I don't mind."
            show wolf pout
            wolf "If you were planning that, at least you had the decency to bring him his own if he shut you down."
            show bear pout
            bear "Of course, don't want to force any decisions on him."
            show wolf neutral
            wolf "Good. Cause he's sitting with me, anyway."
            show bear scared
            mc "Wait, what?"
            bear "Yeah, what he said. Since when? And if he is, why did you bring a spare too?"
            show wolf pout
            wolf "I wasn't being serious."
            show wolf neutral
            wolf "Offer is there if you want it, pup."
            show bear mad
            bear "Same here!"
            mc "Thanks, really, but I was actually planning on sitting with Hoss."
            show wolf scared
            show bear scared
            wolf "What...? Seriously?"
            mc "Yeah? Why not?"
            show wolf pout
            wolf "Nothing."
            show bear pout
            bear "Well... I suppose it makes sense. We're watching one of those cartoons he knows about, right?"
            show wolf neutral
            wolf "Could've spoken up sooner so we didn't have to lug a spare over though."
            show bear neutral
            bear "No, a spare might be needed. No telling if Hoss is going to let you share, anyway."
            show lion neutral with dissolve
            lion "What's this spare for? What am I sharing?"
            mc "Oh! Uh... They were offering for me to sit with them on their beanbag."
            show lion pout
            lion "Oh really now?"
            show wolf pout
            wolf "What's with the tone?"
            show lion neutral
            lion "I expected this from Dean with them being pretty buddy-buddy, but what's your stake in it?"
            show wolf annoyed
            wolf "We're close enough. Fuck off."
            show lion smile
            lion "Oh, well in that case, you can absolutely sit with me, [mcname]."
            show wolf scared
            mc "Whoa, really?"
            if lionroute == True:
                show lion laugh
                lion "Sure!"
                lion "I have ground to make up it seems."
                show bear pout
                bear "Ground... to make up?"
                show wolf neutral
                wolf "Stop getting the wrong idea."
                show wolf pout
                wolf "And you. Stop antagonizing the bear."
                "Tyson jabbed Hoss in the chest with a finger, causing him to throw his hands up a lot more dramatically than he should've if he was genuine."
            else:
                show lion neutral
                lion "Sure. Why not?"
                lion "With these two fawning over you, maybe they can do with a reality check that you're not some prize to be won."
                show wolf annoyed
                show bear mad
                bear "Of course he's not a prize!"
                wolf "What sort of reality check are you thinking, anyway?"
                show lion laugh
                lion "If you're that desperate for a cuddle buddy, why not partner up?"
                show wolf mad
                wolf "Excuse me?"
                show bear scared
                "Tyson stepped forward and jabbed Hoss in the chest, holding his finger there as Hoss lazily put his hands up in surrender."
            "Squeezing into the space between them I pried Tyson away."
            show wolf scared
            mc "Ty, be nice. Please?"
            show wolf pout
            wolf "Fine."
            show bear pout
            "He then dropped into the closest beanbag with Dean sitting down carefully into one of his own."
            "Hoss wandered over to the lights, flicking them off before sitting down in a third beanbag and taking up most of the space."
            show lion smile
            lion "Come on, then. Lemme rub your shoulders while the other two get an education."
            "I felt myself go red beneath my fur, hidden only because of the dark of the room."
            "Still, I eased myself down and once I was comfortable Hoss started to knead my shoulders, neck and head."
        "Dean.":
            $ bearlove += 1
            $ DeanAsked = True
            show bear smile with dissolve
            "I kept my eyes on Dean, the corners of my mouth twitching upward upon noticing him giving me a smile in kind."
            bear "Everything alright?"
            mc "Yup!"
            show wolf pout at left with dissolve
            wolf "You're lucky I got you a beanbag, you dork."
            mc "Oh, um..."
            show bear grin
            bear "Who said he needed one, Tyson? Figured he may as well sit on my lap."
            wolf "Fuck off. Give him the choice at least."
            mc "I don't really mind. Honest!"
            show bear laugh
            bear "So I'll take that as a yes to sitting in my lap?"
            "I noticed that the both of them had carried over two beanbags each so there were four in total."
            if bearroute == True:
                show bear grin
                "Dean eased himself back into a beanbag, shuffling back and patting his leg as if to signal for me to sit."
                bear "Come on, handsome. Room for one more."
                wolf "Ugh."
                "By comparison, Ty just dropped into the one right next to Dean, grumbling."
                "I shot Ty a quick glance before spinning around and dropping myself into Dean's lap."
                show bear scared
                bear "Whoa! Careful!"
                mc "Oh, did I...?"
                show bear pout
                bear "No, but it could've been close."
                show bear neutral
                bear "Ah well, no harm done."
                "He shifted me slightly, and I had another reminder as to just how big he was compared to me. Sure, he stood taller, but he was broader too just through virtue of being a bear."
                show wolf neutral
                "I noticed Tyson watching us, but he said nothing. Seemed as though Dean noticed though."
                show bear grin
                bear "What's the matter, Tyson?"
                show wolf annoyed
                wolf "Nothing."
                show bear laugh
                bear "Aww... Come on, with a face like that? You want to cuddle up with [mcname] instead?"
                show wolf sad
                wolf "Fuck off. He can cuddle with who he wants."
                show bear neutral
                bear "True, but if you're uncomfortable I can back off."
                show wolf scared
                wolf "Really?"
                bear "Why not?"
                "I shuffled in Dean's lap, finding him placing a hand on my hip to keep me steady. Despite what he'd just said, it didn't seem as though he was making an effort to push me off."
                bear "Not going to rub your face in it if you're bothered. But at the same time unless you tell me something's wrong, I'm not going to stop doing what I {i}want{/i} to do just because you're sulking."
                show wolf annoyed
                wolf "I'm not sulking."
                show bear smile
                bear "Well buck up, then. No reason to be upset, Tyson. We're just having a good time as friends, right?"
                show wolf sad
                wolf "I...{w=0.5} Right."
            else:
                mc "Wait, if Ty got me a beanbag..."
                show bear smile
                bear "Had to get one for Hoss, too. Can't have him sitting on the floor, can we?"
                mc "I guess not..."
                show bear laugh
                show wolf scared
                "Suddenly, Dean grabbed me around the waist and fell back into a beanbag."
                mc "Whoa!"
                show bear grin
                bear "But I'm basically a beanbag too, so if you're comfy, I'm comfy."
                show wolf pout
                wolf "[mcname], you alright?"
                mc "I... think so."
                wolf "Oi, bear, be more careful."
                show bear annoyed
                bear "Hey, I'm only playing. He's in no real danger."
                show wolf annoyed
                wolf "Yeah, well, what'd you do if he got hurt?"
                mc "It's alright, Ty. I'm good."
                show wolf neutral
                wolf "I know you are."
                show wolf annoyed
                if wolfroute == True:
                    wolf "I just don't like how he's handling you."
                else:
                    wolf "He can just afford to be a little more careful."
                show bear pout
                bear "Hey, I didn't mean to upset anyone."
                show bear neutral
                bear "But I guess when you're my size, doesn't hurt to be more careful."
                mc "You're alright Dean. Really."
                bear "But is that the only thing bothering you, Tyson?"
                show wolf scared
                wolf "What?"
                bear "Yeah, you look down in the dumps. You're not jealous, are you?"
                show wolf mad
                wolf "No!"
                show bear laugh
                bear "Then come on, cheer up. Remember, this is just a bit of fun."
                show wolf pout
                "Ty grumbled, getting comfortable into this beanbag, shifting his attention elsewhere."
            show lion grin at right with dissolve
            lion "Someone looks comfy."
            show wolf pout
            wolf "Ugh, are we good to start yet?"
            show lion neutral
            lion "Pretty much. At least on my end."
            show bear smile
            bear "I'm good to start, too."
            "Dean made a point of rubbing my side as he spoke, prompting me to nod along too."
            mc "All good here, too."
            lion "Excellent. Before I go hitting the lights, had a question for you, Tyson."
            show wolf neutral
            wolf "What?"
            show lion grin
            lion "Wanna get buddy-buddy like Dean and [mcname] are?"
            show wolf pout
            wolf "Fuck off."
            lion "Would it help if I claimed 'no homo'?"
            wolf "Just go hit the lights."
            show lion laugh
            lion "Alright, alright. Just a sec."
            "Hoss wandered off to hit the lights, returning a moment later to sit in one of the available beanbags."
        "Tyson.":
            $ wolflove += 1
            $ TysonAsked = True
            show wolf neutral with dissolve
            "I watched as Ty wandered back over, dragging two beanbags behind him and shooting me a confused look."
            wolf "What?"
            mc "Nothing!"
            show wolf pout
            wolf "You weirdo. I got you a beanbag."
            show bear grin at left with dissolve
            bear "Hey, I did too. Or for Hoss, we needed four all up anyway, right?"
            mc "Right, but..."
            "Ty dropped both of the beanbags down and dropped himself into the closest one."
            if wolfroute == True:
                show bear laugh
                bear "Y'know, [mcname]. Don't necessarily need to sit in a beanbag if you don't want."
                show wolf annoyed
                mc "What do you mean?"
                show bear grin
                bear "Wanna sit in my lap?"
                show wolf pout
                wolf "Now hold on, he has his own fuckin' beanbag."
                show bear laugh
                bear "Hey, figured I'd at least ask. I reckon I might be just as comfy."
                show wolf annoyed
                wolf "He's not sitting in your lap, Dean."
                mc "Right."
                show bear neutral
                bear "Well, alright then."
                show wolf pout
                "Ty rolled his eyes, looking over to Hoss. This was when I made my move."
                show wolf scared
                wolf "What..."
                "I half dove on Ty, half on the beanbag he'd sat next to him, presumably for me."
                wolf "Watch it, yeah?"
                "A hand found my shoulder, but he made no effort to push me away."
                "In fact, it didn't even leave my shoulder as I propped myself up and cuddled into the spot under his arm, using it as a pillow."
                show wolf neutral
                wolf "Comfy?"
                mc "Well... Maybe a little?"
                bear "Hey now, what happened to him having his own beanbag?"
                show wolf pout
                wolf "He can do whatever the fuck he wants."
                show bear pout
                bear "Of course, but..."
                "I felt Ty's hand on my shoulder tense a little."
                mc "If this is bothering you Ty, I can go sit in my own beanbag, I don't really mind. I just thought..."
                show wolf annoyed
                wolf "Nope, you're not going anywhere."
                "As if to emphasize his point, his other hand reached over to swing my legs over his lap."
                wolf "This is fine."
                show bear neutral
                bear "Well hold on."
                bear "I wouldn't mind something cleared up."
                show wolf pout
                wolf "What?"
                show lion neutral at right with dissolve
                lion "Everyone comfy and ready to start?"
                show lion pout
                lion "...is what I'd want to ask if I wasn't just over there and could hear everything you guys were talking about."
                lion "What's happening exactly?"
                show bear pout
                bear "You and [mcname].{w=0.5} You're not... dating, right?"
                show wolf scared
                wolf "Uh..."
                show lion laugh
                lion "Really? That's what the problem is? I assumed with how buddy-buddy they've been lately that they must be."
                show wolf mad
                "Tyson roughly shoved me away, getting to his feet to prod aggressively at Hoss's chest."
                wolf "I'm.{w=0.5} Not.{w=0.5} Gay."
                show lion neutral
                "Hoss didn't even flinch, glancing down at the finger still held against his chest before gently brushing it aside."
                lion "And?"
                show wolf yell
                wolf "What do you mean, {i}and{/i}?"
                show lion laugh
                lion "So you like to cuddle dudes?"
                show bear neutral
                bear "Seems pretty gay to me."
                show wolf mad
                wolf "I'm not!"
                lion "Then that's simple."
                show lion grin
                lion "Just say 'no homo'."
                show wolf annoyed
                wolf "The fuck? What do you mean?"
                show lion neutral
                lion "If it makes you feel better, just... say 'no homo'. Might make you feel better and make it clearer for [mcname]."
                show wolf sad
                wolf "No... homo..."
                "Ty seemed shaken, repeating the words over to himself as if confused, quiet and eyes drawn to the floor."
                "He fell back into his own beanbag awkwardly, keeping his eyes away from me."
                show bear smile
                bear "Glad we got that cleared up. Should tell me what kind of women you like sometime, Tyson. Might know someone to introduce you to."
                "He made a non-committal grunt while Hoss hit the lights."
            else:
                "When I didn't sit down immediately, Ty grabbed me by the wrist and pulled me down into him, shuffling across so we were side by side with his arm around my shoulders."
                wolf "Comfy?"
                mc "Mmhm."
                show wolf smile
                wolf "Good."
                show bear scared
                bear "Hey now, that's not fair."
                mc "What's not fair?"
                bear "Why'd we get four beanbags if [mcname] was just going to sit with you? He could've just sat with me."
                show wolf pout
                wolf "What? Jealous?"
                show bear annoyed
                bear "Maybe not jealous, but it begs the question why you're so chummy."
                mc "Oh, that's easy."
                show wolf neutral
                mc "Ty and I have a special relationship."
                show wolf pout
                wolf "Oi. Don't go painting me out to be a homo."
                show bear mad
                bear "What's wrong with being a homo?"
                mc "Nothing! Right Ty?"
                wolf "I guess? I'm not one though."
                show lion grin at right with dissolve
                lion "What's this about homosexuals?"
                show wolf annoyed
                wolf "Nothing!"
                show bear annoyed
                bear "I just wanted to know why [mcname] and Tyson were getting all cuddly on the beanbags together."
                show lion neutral
                lion "What, jealous?"
                mc "I think he's a little jealous."
                show bear mad
                bear "I'm not jealous!"
                show bear pout
                bear "But I would like to know what... {i}this{/i} is, though."
                lion "Oh, thus why Tyson being gay came up?"
                show wolf yell
                "Tyson got up suddenly, poking Hoss roughly in the chest."
                wolf "I'm not gay!"
                show lion pout
                lion "Yeah, yeah. Just claim 'no homo' and move on, then."
                show wolf scared
                "Hoss gently removed Tyson's finger from his chest and looked him over."
                wolf "No... homo?"
                show lion grin
                lion "There you go! Easy."
                show bear neutral
                bear "Well... I'll admit, for a moment there I was worried that I had competition."
                show wolf pout
                wolf "Of course you did."
                "Tyson fell into the beanbag next to me, giving me the one he was originally on but sticking close all the same."
                show bear smile
                bear "You should tell me what you like in a woman sometime, Tyson. Maybe I could introduce you to someone if I know anyone that fits."
                show wolf sad
                "Tyson grunted, shooting me a pitiful look only briefly before looking at the ground. Hoss meanwhile wandered away to hit the lights."
    #Everyone talked to, watch anime
    "I'd watched this show before, or... parts of it. Hoss seemed to be in a constant state of deciding where the best place to start this show was."
    "There was another one like it, something about the Holy Grail that you could watch in any order, except you couldn't without spoiling parts of it?"
    "It was all a little too serious for me, but if it made him happy, then I was happy to just watch whatever."
    if HossAsked == True:
        "Well, not that much watching was really happening on my side of things. Hoss's hands were like magic and every now and again I sighed out happy."
        "Still... If we were going to watch anime, I would've picked something different."
    "I preferred the ones that had a mix of exciting events and lighthearted fun."
    scene black with dissolve
    "After the first episode I looked to see how Tyson was faring, and he seemed to be interested enough to keep watching."
    if DeanAsked == True:
        "Dean on the other hand seemed less than interested, although I couldn't tell how much of that was because I was sitting in his lap."
    else:
        "Dean seemed distracted, but he hadn't made a move to leave the room just yet. Maybe he was willing to sit through it as much as it seemed he wasn't enjoying it."
    "Hoss on the other hand, as expected, had a smile plastered on his face and jumped up to start the next episode the moment the end credits had finished."
    "By the second episode though..."
    scene casino
    show bear pout
    show wolf smile at left
    show lion grin at right
    with dissolve
    lion "Everyone enjoying so far?"
    wolf "Yeah, it's not bad. I'm down to keep going."
    bear "Uh..."
    mc "What's wrong, Dean?"
    show bear neutral
    bear "Nothing, don't worry about it."
    show lion sad
    lion "Not your thing, big guy?"
    show bear sad
    bear "Not... exactly."
    mc "What about if we switch? We could find something that we can all like, right?"
    show bear neutral
    bear "No, no. That's alright. I'll go make myself busy elsewhere."
    if DeanAsked == True:
        "Dean patted my back, gesturing me to get up so he could stand."
        show bear smile
        bear "Thanks, handsome."
    else:
        "Dean got up, stretching out his arms."
    show bear laugh
    bear "Still, was good to try something a bit different."
    show bear smile
    bear "Might go check into on the crops. Then... might go for a stroll of my own."
    #Diverge to Dean's route stuff here
    if bearroute == True:
        mc "Crops? Like the greenhouse?"
        bear "That's right. Wanna come?"
        "I thought about it. Part of me didn't like the idea of Dean being alone."
        "The other part just wanted to spend more time with him, and some privacy might be good, as dangerous as it could be."
        mc "Sure."
        if TysonAsked == True:
            "Ty patted me on the head before I got up, making no effort to move from his seat outside stretching out more."
        if HossAsked == True:
            "Hoss ran his fingers through the back of my skull once more before letting me get up, lounging back into his beanbag."
        else:
            "I mimicked Dean's stretch before flashing him a toothy smile."
        mc "Lead the way!"
        jump Day9Dean
    mc "Did... you want some company?"
    "Part of me worried about Dean being by himself, fearing something could happen."
    if DeanAsked == True:
        bear "Nah, I'll be alright. You seem to be enjoying yourself anyway."
        show bear grin
    else:
        show bear grin
        bear "I couldn't ask that of you given how comfy you look."
    bear "Besides, some quality 'me time' never hurts."
    show lion neutral
    lion "Well, if you're sure. Welcome to try and find something else if you did want to stay though."
    show wolf neutral
    wolf "Yeah. What he said."
    show bear laugh
    bear "How about we just watch something I pick next time?"
    show wolf smile
    show lion smile
    lion "Done deal."
    show bear smile
    bear "Alright, well you have fun and I'll see you lot later."
    hide bear with dissolve
    if DeanAsked == True:
        "I watched as Dean left before settling back into the beanbag, still warm from where he'd been sitting."
    show wolf neutral
    wolf "So what now?"
    show lion neutral
    lion "I can put on the next episode if you want."
    show wolf smile
    wolf "Sure."
    mc "You know, I didn't think you liked anime, Ty."
    show wolf pout
    wolf "I've seen two episodes, give me a break."
    show lion smile
    lion "Two of many to come, buddy."
    show wolf scared
    wolf "Buddy?"
    show lion neutral
    lion "Sure? Why not?"
    wolf "I don't..."
    "Ty looked to me, then back to Hoss."
    lion "What, you gonna say that I'm just a nuisance instead?"
    show wolf sad
    "I could see the cogs turning in his head, unsure of what to say."
    mc "Ty?"
    wolf "I don't know."
    show wolf neutral
    wolf "Not used to it."
    show lion pout
    lion "Really?"
    wolf "Outside [mcname], don't really do the friends thing."
    show lion neutral
    lion "Why's that?"
    show wolf pout
    wolf "People suck. Except [mcname]."
    if TysonAsked == True:
        "I felt his hand grip my shoulder slightly harder when he said my name."
    show lion smile
    lion "Well, we're going to have to change that. Can't have you being a lone wolf your whole life."
    lion "And anime is great at bringing people together."
    wolf "Except Dean."
    show lion sad
    lion "Well okay, maybe it's not a perfect record, but still."
    mc "Oh no."
    show wolf neutral
    wolf "What?"
    mc "Hoss, you're not going to claim that you have the power of anime on your side, are you?"
    show lion sad
    lion "Well... No, but I {i}do{/i}."
    show wolf pout
    wolf "I'm not going to regret sitting through more of this am I?"
    mc "Hey, you were hardly just sitting through it. You were liking it, right?"
    show lion grin
    lion "He totally was."
    show wolf annoyed
    wolf "Just shut up and put the next episode on."
    scene black with dissolve
    "Despite Ty's attitude, he had a good enough time I think. After the next episode he started to get more chatty and asked Hoss stuff about the show."
    if TysonAsked == True:
        "Not that I was really paying attention, I was comfy cuddled up to Ty and he was lightly scratching the top of my head while he talked to Hoss."
    if HossAsked == True:
        "Not that I was really paying attention, Hoss kept massaging my scalp as he talked to Ty and it felt good."
    else:
        "I didn't really get the show, so I let them talk. It was rare to see Ty ask so many questions, but rarer still to see Hoss answer each without raving about the content."
    "After each episode, there'd be a few minutes to talk about stuff, but I mostly just kept quiet to let the other two have at it."
    scene casino
    show wolf smile at left
    show lion neutral at right
    with dissolve
    lion "Well... That's it."
    show wolf scared
    wolf "What?"
    show lion smile
    lion "That's it.{w=0.5} For part one, at least."
    show wolf sad
    wolf "Oh, so... there are more parts?"
    show lion grin
    lion "Of course!"
    show wolf neutral
    wolf "Oh, good."
    lion "What, you thought that'd be the end of the story?"
    show wolf pout
    wolf "No...?"
    mc "Ty just wants more is all."
    show wolf scared
    wolf "I... uh..."
    show lion laugh
    lion "So you're a fan of anime too now, Tyson?"
    show wolf pout
    wolf "Ugh..."
    mc "What's wrong, Ty?"
    show wolf sad
    wolf "Nothing. Just didn't realize this was what you liked to watch. Probably would've let you pick more if that was the case."
    show lion grin
    lion "Oh, no. If you got [mcname] to pick you'd be in a very different position. His tastes are... well..."
    mc "Hey, what I like is fine! Sure, it might not be the same as that, but..."
    "Hoss waved me off, rolling his eyes before addressing Tyson with a tone of curiosity."
    lion "Overall, what'd you think?"
    show wolf neutral
    wolf "I'd watch more."
    show lion smile
    lion "Thought you might like it. It gets better as far as the punching goes, but always good to start at the beginning."
    wolf "Yeah, I like the drive of that guy who became a vampire. That was hardcore."
    show lion pout
    lion "Of course you'd like him. He's not even the protagonist."
    show wolf pout
    wolf "He should be. He's cool."
    show lion laugh
    lion "And here you thought road rollers were lame."
    show wolf scared
    wolf "What? Don't tell me..."
    lion "Yup! But I guess you'll just have to see how that plays out."
    show wolf pout
    wolf "Fine. Whatever."
    show wolf neutral
    wolf "So when are we watching the next part?"
    mc "Eager much?"
    show wolf annoyed
    wolf "Shut it."
    show lion smile
    lion "Well, not tonight. It's more than just nine episodes so if you want to binge it, probably best we save it for another day."
    mc "Oh, well... What should we do now?"
    show wolf neutral
    wolf "Dunno."
    if wolfroute == True:
        lion "I might go see where Dean ended up, see how the crops are going too."
        show wolf pout
        wolf "Really?"
        show lion neutral
        lion "Gotta do something until it's time for dinner. What are you two planning on doing?"
        if TysonAsked == True:
            "I craned my neck to look at Tyson, seeing him thoughtful."
        else:
            "I looked across to Tyson, him scratching his neck as he thought."
        wolf "Just gonna chill with [mcname], probably."
        lion "Sweet. Well you two have fun, I'll see you at dinner."
        if HossAsked == True:
            "I moved so Hoss could stand, and watched as he left the room."
        else:
            "I watched as Hoss wandered off with a wave, stretching as he crossed the threshold and disappeared out of sight."
            stop music fadeout 2.0
        hide lion with dissolve
        jump Day9Tyson
    if lionroute == True:
        wolf "Any ideas?"
        lion "Oh, I had one. But that's more a [mcname] and me thing."
        show wolf neutral
        wolf "What do you mean?"
        show lion laugh
        lion "Nothing bad. Promise."
        show wolf pout
        wolf "Well don't let me stop you."
        mc "No, no. We can do something as a group. Just lemme think a minute."
        show wolf neutral
        wolf "Pup."
        mc "Yeah?"
        wolf "Stay out of trouble. I'm gonna go for a walk of my own, so I'll see you guys at dinner."
        if TysonAsked == True:
            "Tyson stretched, lifting his arm from under my head and jumping up."
        else:
            "Tyson pushed himself up out of his beanbag and stretched, joints popping as he did so."
        wolf "Oh, and Hoss."
        show lion smile
        lion "Hm?"
        show wolf smile
        wolf "...{w=0.5}Thanks."
        hide wolf with dissolve
        jump Day9Hoss
#Sal/Orlando/Roswell - "Board Game" (Except they just play Uno)
else:
    scene conservatory with dissolve
    "We'd split up for a couple of minutes to round up some games. With the rec room being taken up with the others watching TV, we figured we'd take another room just so we weren't talking over their show."
    show croc neutral with dissolve
    mc "Oh, Sal! What did you grab?"
    show croc pout
    croc "I... don't know. I just grabbed one at random from the shelf."
    mc "What shelf?"
    show croc neutral
    croc "The one in the rec room. The others were talking about what to watch so I went and took one before they could notice."
    "He held out the box in his hands, rattling it gently as he did so."
    mc "Boggle? Does this... count as a board game?"
    show croc pout
    croc "Not really, but... I know how to play this one. You roll the dice in the box, and make words with the letters."
    mc "Oh... Neat, I guess? I don't know how well I'd go with something like that."
    show croc sad
    croc "I could... go grab another one?"
    show boar neutral at left
    show dragon grin at right
    with dissolve
    boar "No need, Sal! We have alternatives!"
    dragon "Yeah! Check it out!"
    "The other two flashed boxes of their own."
    show boar grin
    boar "I figured that we're in a mansion, I grabbed Clue."
    show croc pout
    croc "Isn't that being a little insensitive?"
    show boar scared
    show dragon sad
    boar "W-What? No, I like this game! What's wrong with this one?"
    "I felt the eyes fall to me, making me sigh out. Sure, the idea of a murder in a mansion was a little too close to home, but I hadn't thought anything of it given it was just a game."
    show dragon pout
    dragon "Well uh... I grabbed Mouse Trap."
    show croc smile
    croc "Oh, I've played that before. I like putting all the pieces together when you set it up."
    show dragon scared
    dragon "You mean, while you play, right?"
    show croc sad
    croc "No... You set up all the pieces before you can play, right?"
    show boar pout
    boar "Is... the game all that complicated? I haven't played it before."
    mc "You put together a little machine and try not to get caught I think. It's... kinda neat, but I think the copy I had was missing a few parts."
    boar "Oh... Well... Where does this leave us? You grabbed Boggle, [mcname]?"
    show boar grin
    boar "Because if this is a contest of words, prepare to lose."
    mc "Oh, no. This was Sal's."
    "Roswell turned to Sal suddenly, grin unwavering."
    boar "You dare challenge me to a game of words, Sal?"
    show croc neutral
    croc "Oh. Okay."
    "I looked to Orlando, confused."
    mc "Uhhh..."
    boar "I admit, I don't expect you to keep up, but let's try an easy one. What's an oenophile, Sal?"
    "Without even thinking about it, Sal replied."
    croc "That's a lover of wine."
    boar "Okay, perhaps that was too easy. How about Chthonic?"
    mc "Bless you."
    show boar pout
    boar "I didn't sneeze."
    show croc smile
    croc "Anything that relates to the underworld, or just underground things depending on how you're using it."
    show boar scared
    "I think his quick replies had stunned Roswell. Perhaps he'd just not expected it to come from Sal of all people."
    boar "I... uh..."
    show croc grin
    croc "What's the matter?"
    boar "I... honestly didn't imagine your vocabulary was so broad. You barely talk."
    show croc neutral
    croc "Just because I don't talk, doesn't mean I don't know words."
    show boar pout
    boar "I... I guess not."
    boar "Sorry, I just assumed wrong."
    croc "I don't mind. If you'd started giving me advice then we might've had some issues."
    show dragon scared
    dragon "Anyway... What did you bring, [mcname]? Anything good?"
    mc "Oh! Um... I just had a pack of Uno cards in my bag so I grabbed that."
    show dragon sad
    dragon "So the only actual board games are Clue and Mouse Trap?"
    show croc neutral
    croc "I'm happy to play Uno. I know how to play that."
    dragon "And no offense, but I'd much rather play Uno than Clue, knowing how Sal's interpreted how Mouse Trap works."
    "Roswell, seemingly still awestruck by what Sal came out with, sat down on the floor cross-legged and Sal joined him. Orlando sat the games we'd collected off to the side and joined them on the floor."
    "I shuffled the cards and took a seat, dealing them out. To my left was Roswell, to my right was Orlando, and Sal sat across from me."
    show boar grin
    boar "Play proceeds to the left of the dealer, right? Which means I go first..."
    "He placed a card down, passing his turn to Sal."
    show croc smile
    croc "Skip."
    show dragon scared
    dragon "What do you mean, skip?"
    show croc neutral
    croc "Skip. I skip you."
    mc "So that's my turn, right? Uhh... Reverse?"
    show boar scared
    show dragon grin
    boar "Wait, no! Now you're skipping me!"
    show croc pout
    croc "Oh no."
    show dragon mad
    dragon "Draw. Two."
    show croc neutral
    croc "Draw Two as well."
    show boar pout
    boar "Wait, what? Are we playing with those rules?"
    show dragon scared
    dragon "I'm fairly certain you can't do that."
    mc "That's how we played at home. I think?"
    show dragon mad
    dragon "But those aren't the {i}rules!{/i}"
    show boar sad
    boar "And I don't {i}really{/i} want to be picking up four cards so... Draw Two. Sorry, [mcname]."
    mc "Wait, now I have to draw six!?"
    "I sucked it up and drew more cards as Orlando placed another cards down."
    show boar neutral
    show dragon neutral
    show croc neutral
    "We went around a few times before it was clear that someone was about to win."
    boar "Uno."
    "Roswell placed a card down, flashing his last card in hand. What it was, I wasn't sure but I caught that it was red."
    croc "Uno."
    "Sal's poker face was strong. I didn't know what he had remaining as he placed his last card down."
    dragon "Uno."
    "Same for Orlando."
    "I looked at the cards in my hand, and no matter what I played, it seemed as though the game was probably going to be over by the time my turn rolled around again."
    "I could play a wild card and keep the color red, meaning Roswell would win."
    "Alternatively, I could skip Roswell and see if Sal had something to play."
    "Or, I could reverse it back to Orlando and hand him the victory."
    "My brow furrowed as I looked over my cards, thinking it over."
    show boar grin
    boar "Come on, [mcname]. It's your turn."
    show croc pout
    croc "So close..."
    show dragon sad
    dragon "And I was a bit too slow I guess. Oh well."
    "I looked at each of them in turn before deciding."
    mc "I play..."
    menu:
        "...Skip.":
            $ croclove += 1
            show boar scared
            "I placed the card down, shooting Roswell an apologetic look."
            mc "Sorry, Roswell."
            show croc smile
            "Sal's face lit up slowly as he eased his final card down. A skip card as well, just a different color."
            croc "I win."
            show boar pout
            boar "Drat. I was so close..."
            dragon "At least you were closer than me. Only way I was going to win was if neither of you had anything, even then it would've been dicey."
            mc "Oh, well... shall we go again?"
        "...Wild.":
            $ boarlove += 1
            show boar smile
            boar "Game, set, and match."
            "I'd barely put the card down and looked to Roswell, a broad grin on his face even before I'd made eye contact."
            "Flicking over the card in his hand, Roswell showed us the red card in his hand, casually placing it down on the pile atop the card I played."
            show croc neutral
            croc "Good game."
            show dragon neutral
            dragon "Next one will go to me, Roswell. Just you wait."
        "...Reverse.":
            $ dragonlove += 1
            show boar pout
            show dragon grin
            show croc pout
            "I placed the card down, looking to Orlando. He could barely sit still it seems, and it was hardly a surprise."
            dragon "Yes! Perfect!"
            boar "You can't be serious."
            show dragon laugh
            dragon "Yup! I win!"
            "Orlando slammed down his final card, also a reverse card just in a different color."
            show croc smile
            croc "Well done."
            boar "Yeah. Good game. That was close."
    "I gathered up the cards and shuffled, only noticing halfway through that Roswell had his hand out for the deck."
    show boar smile
    boar "My turn to deal, [mcname]."
    hide boar
    hide croc
    hide dragon
    with dissolve
    "We played game after game each one seemingly revealing that none of us had the same understanding of what the rules were."
    "At some point I remembered looking behind me to see Ty and Dean walking by talking about something but I didn't catch the details of the conversation."
    "I must've been zoning out as the next thing I knew, Orlando was nudging me with the deck of cards."
    show dragon neutral with dissolve
    dragon "Earth to [mcname]! It's your turn to shuffle."
    show croc neutral at right
    show boar neutral at left
    with dissolve
    mc "Oh, sorry. I guess I must've been daydreaming."
    show boar smile
    boar "About what? Anything good?"
    mc "I don't know... Maybe I'm just tired."
    croc "Is it time for a break? I wouldn't mind one."
    show dragon smile
    dragon "Then let's have a break. Give us a chance to get a drink and maybe do something else for a bit?"
    show boar neutral
    boar "That sounds less like a break and more like just stopping entirely."
    show dragon scared
    dragon "Oh... Well I guess it does."
    show dragon neutral
    dragon "Not that that's a bad thing. Might not be a bad idea to check in with the others, anyway."
    if crocroute == True:
        croc "If that's the case... I think I might go to the pool."
        show boar pout
        boar "The pool? Really?"
        show croc pout
        croc "Right. I have... Things I need to think about. The water might do me some good."
        boar "Did you want... some company?"
        show dragon sad
        dragon "Yeah! I mean I know I'm probably not the best choice, but I'm happy to be a sounding board if you need it, Sal."
        croc "No. But thank you.{w=0.5} Both of you."
        "I felt Sal's eyes on me briefly before he looked away. I wasn't sure if that was an invitation, or a sign that I shouldn't bother asking. I stayed quiet all the same."
        hide croc with dissolve
        "Watching him go, he shot me the same look as he left, disappearing out of sight."
        mc "I... think I might go for a wander too. Maybe go enjoy the hot tub before dinner."
        show dragon neutral
        dragon "Not going to give Sal his space?"
        mc "Oh, no I figure he can swim or whatever and I'll just sit in the hot water. There's enough space where he can be undisturbed while I just... hang out, right?"
        show boar neutral
        boar "The pool area {i}is{/i} pretty big. I'm sure it'll be fine. Besides, just in case he decides he wants to talk through what's bothering him, then [mcname] is nearby."
        show dragon sad
        dragon "True..."
        mc "Well, I better go get changed and I'll see you guys at dinner?"
        show dragon neutral
        show boar neutral
        boar "Yup! See you then!"
        jump Day9Sal
    show boar neutral
    boar "Well, if it's a break we're doing, I think I might head down to the kitchen for a snack."
    dragon "Hrm... In that case..."
    show dragon neutral
    dragon "I might head downstairs too. Maybe go sit outside for a bit?"
    scene foyer with dissolve
    "We headed downstairs, and I noticed that without breaking stride, Orlando and Roswell split off in different directions."
    if boarroute == True:
        jump Day9Roswell
    if dragonroute == True:
        jump Day9Orlando

#consult DD for afternoon activities
#Tyson
label Day9Tyson:
    if TysonAsked == True:
        "Cuddled up to Tyson, the two of us sat there in silence for a few moments."
    else:
        "After Hoss left, Tyson and I looked at one another in silence."
        "Moments passed before he broke the quiet voice held low."
    show wolf sad
    wolf "So..."
    play music relaxed fadein 2.0
    mc "Yeah?"
    if TysonAsked == True:
        "He kneaded my shoulder, jaw clenched."
    wolf "Did I do alright?"
    mc "What do you mean?"
    show wolf neutral
    wolf "Making friends, I mean."
    mc "Well... I think so? But you don't just become friends with someone after hanging out once. It takes a few times at least."
    wolf "Oh."
    "I expected a follow up but there wasn't. Instead he sighed out, shaking his head."
    show wolf sad
    wolf "Makes sense, I shouldn't... Y'know."
    mc "I really don't, Ty. Come on, tell me."
    show wolf neutral
    wolf "I was hoping this would be easy."
    mc "Well... it's a good start. Plus Hoss is sharing things with you, too."
    wolf "Yeah."
    mc "And... I guess worst case scenario you still have a back up."
    show wolf scared
    wolf "A back up? Dean?"
    show wolf pout
    wolf "Don't know how much your future boyfriend is a sure thing, friend-wise."
    if TysonAsked == True:
        "I sat up, rolling over so I was sitting in Ty's lap facing him, hands supporting me up by finding purchase on his chest."
    else:
        "From my beanbag I lunged at him, knocking him backwards off his so we ended up in a heap on the floor."
    show wolf scared
    mc "I mean {i}me{/i}, Ty."
    wolf "You?"
    mc "Of course! Always!"
    show wolf aroused
    "Ty laughed, taking one of my hands in his and giving it a squeeze."
    wolf "You fuckin' dork."
    show wolf laugh
    wolf "You're already {i}my{/i} best friend. Don't care if you're the only one. You're enough."
    mc "That wasn't..."
    show wolf smile
    wolf "Then..."
    show wolf neutral
    stop music fadeout 2.0
    "His smile faded fast, looking at me as the frown starting to form. It eased back, settled, and then eased back until he just looked at me with an expression I couldn't place."
    wolf "You didn't mean that, did you?"
    mc "O-Oh! No, I meant it. Friends, right?"
    show wolf annoyed
    wolf "Don't lie to me."
    play music tense fadein 2.0
    if TysonAsked == True:
        "I suddenly felt myself falling backwards as he shoved me onto my back, pinning me down by the shoulders."
    else:
        "The next moment he was rolling me over so he was on top, straddling my waist almost."
    wolf "Don't. Lie."
    "I squeaked under his frown."
    mc "What... What did you want me to say?"
    wolf "What about your fuckin' want for me to be honest?"
    wolf "Don't I get the same thing?"
    mc "I... I don't know!"
    "He grabbed me roughly by the wrist, pinning me further to the floor."
    mc "I don't know, Ty!"
    show wolf yell
    wolf "The fuck do you want, [mcname]?"
    "I quaked under him, stammering."
    mc "I... I don't..."
    show wolf mad
    wolf "Say you don't know one more time, pup. {i}Say it{/i}."
    "It was a dare, one that I was scared to follow through with. There were few things that were able to make me cry these days, but Ty was one of them."
    "Not out of the same sort of fear that came with fear of being bullied or physically harmed. Something deeper. Something darker."
    mc "Ty! You're scaring me!"
    stop music fadeout 2.0
    show wolf scared
    "No sooner than I'd said it he froze, eyes wide in shock looking down at me."
    wolf "I..."
    "He eased off, delicate, almost as if he was scared that he was about to break something and was doing what he could to stop that from happening."
    "I breathed out, heart beating fast in my chest."
    show wolf sad
    wolf "I'm sorry, I..."
    "But he didn't let me up. I was still under him, though I had the impression that he wouldn't have been hard to move if I really wanted him to move."
    mc "Tyson."
    wolf "Yes?"
    mc "What's the matter? Really?"
    mc "Did I do something?"
    wolf "No."
    mc "Was it something I said?"
    wolf "Not that either."
    mc "Then..."
    "In a cruel twist of irony, I laughed at what Tyson came out with next."
    wolf "I don't know."
    show wolf mad
    "I was too late to stifle my laughter with my hand, instead coming out closer to an amused snort."
    "Still, I was thankful that Ty didn't make another move on me for doing it."
    wolf "Okay, fine. I do know, alright?"
    show wolf sad
    wolf "You're not the only one that's been out of it lately, yeah?"
    mc "Why didn't you say anything?"
    show wolf neutral
    wolf "And what would you have done?"
    show wolf pout
    wolf "Probably tell me, 'it's alright Ty'."
    wolf "Or 'if you want to talk, I'll listen'."
    mc "It's true though."
    show wolf annoyed
    wolf "That's probably the worst part. I bring it up, you'll be upset, and then where will that get us?"
    mc "You mean..."
    show wolf sad
    play music sad fadein 2.0
    wolf "It's your dad."
    "I fell limp, gulping."
    wolf "Look, you're not the only one that misses him, alright?"
    wolf "He was more of a dad than mine was to me, anyway."
    if wolflove >= 17:
        wolf "So when you say you want your dad because you're confused, I get it."
        wolf "What I wouldn't give for some advice right now."
    else:
        wolf "He'd just know what to do, and what to say, right?"
    "I was almost scared to ask."
    mc "About... what?"
    show wolf neutral
    wolf "You really wanna know?"
    mc "Of course I do, Ty."
    show wolf sad
    wolf "I'd ask him if I was... good. If I was worth something."
    "As I went to say something he cut me off, continuing."
    show wolf pout
    wolf "I know I'm worth {i}something{/i}. I meant... more than that."
    wolf "If it was alright to be... {i}feeling{/i} things."
    mc "Like what?"
    show wolf neutral
    wolf "Don't worry about it."
    mc "{i}Ty.{/i}"
    show wolf pout
    wolf "Fine."
    wolf "It's you. I don't get how or why you do these things to me, but you do."
    show wolf annoyed
    wolf "It hurts in a way that I don't know how to hurt anyone. Like you're under my fur. Under my fuckin' skin."
    show wolf sad
    wolf "And... sometimes I don't want that feeling to go. Other times I try clawing it out with how much it hurts."
    mc "So... it's a bad feeling?"
    wolf "Sometimes."
    if DeanAsked == True:
        wolf "Like when you were sitting in Dean's lap."
        show wolf mad
        wolf "You should've sat with me. I {i}wanted{/i} you to sit with {i}me{/i}."
    if HossAsked == True:
        wolf "Like when you were getting comfortable with Hoss."
        show wolf annoyed
        wolf "If you wanted a massage that bad, you could've asked me. I would've done it if you asked nice."
    else:
        wolf "Doesn't happen all the time."
        wolf "It's only been happening lately. I don't get it."
    mc "Are you just jealous?"
    show wolf scared
    wolf "The fuck would I be jealous for?"
    mc "I dunno... That maybe you want something you don't know you want? I get that sometimes."
    show wolf pout
    wolf "I don't get it."
    mc "Okay... You know how sometimes I get cranky and you seem to know what I need to make me feel better?"
    wolf "Yeah? You're not that hard to figure out."
    mc "Well it's like that but for you. I need help figuring out what you need I guess."
    show wolf scared
    wolf "Oh."
    mc "But what I {i}think{/i} you need, and what I can give you are two different things."
    show wolf sad
    wolf "Oh..."
    mc "But Ty?"
    wolf "Yeah?"
    mc "Did you... tonight... um..."
    show wolf scared
    wolf "What?"
    mc "Would you... spend the night with me?"
    wolf "I... Yeah! Of course!"
    show wolf sad
    wolf "Sorry, I... I'm a mess."
    show wolf pout
    wolf "Ugh... Hold on, lemme think."
    mc "Can... you get off me first?"
    stop music fadeout 5.0
    "Ty rolled off so he was laying on his side on the floor, looking at me."
    mc "I had an idea."
    show wolf neutral
    wolf "Oh yeah?"
    mc "How about... a shower.{w=0.5} Together?"
    show wolf pout
    wolf "I dunno..."
    mc "It'd help me get that spot on my back, plus you'd be there to check, right?"
    wolf "Still... naked. Together."
    mc "Well... it's just an idea. We could get clean separately, I could brush you before bed, you could brush me and we could just... I dunno, chill?"
    show wolf neutral
    wolf "..."
    "Ty sighed out heavily, eyes drawn to the floor before they flicked up to me."
    show wolf smile
    play music relaxed fadein 2.0
    wolf "Yeah. {w=0.5}Yeah, alright."
    show wolf pout
    wolf "I'll decide later if I'll join you but... yeah. That sounds nice."
    mc "Just like back home. Nothing has to change, nothing has to be different."
    show wolf smile
    mc "We can... I dunno, watch videos on my phone or something. Just..."
    "I rolled forward into him sighing out and covering my face with my hands."
    mc "I'm starting to break. I need something that's familiar again."
    show wolf neutral
    wolf "Alright."
    wolf "Then... what should we do until it's time for dinner?"
    show wolf pout
    wolf "With how late you slept, you're not having another nap."
    mc "Well... We're... y'know, already here. Could play games, could watch something."
    if DeanAsked == True:
        show wolf neutral
        wolf "Alright, go pick out a game, and you can sit on my lap while you play."
        mc "What, you're not going to play?"
        wolf "Nah. I just wanna watch for now."
        mc "And on your lap?"
        show wolf pout
        wolf "Are you going to be a brat about it? Sit on my damn lap."
        mc "Okay! Fine!"
    elif HossAsked == True:
        wolf "Want a massage?"
        mc "What?"
        show wolf neutral
        wolf "Like what Hoss was doing to you."
        mc "Oh. Nah, that's alright. Did you want one?"
        show wolf pout
        wolf "With your scrawny arms?"
        mc "Hey!"
        wolf "Just go pick out a game and I'll watch you play. You could use the practice."
        mc "And what will you do?"
        show wolf neutral
        wolf "Dunno. Be a cushion if you want it."
        mc "You're sure?"
        show wolf pout
        wolf "Just go pick a damn game and come back already."
        mc "Geez, alright. Okay."
    else:
        show wolf sad
        wolf "I dunno... Sure, I guess?"
        mc "No? I don't want to force you to do anything you don't want, Ty. That should go without saying."
        show wolf annoyed
        wolf "Geez, that's not what I meant."
        show wolf pout
        wolf "What I meant was that you should be the one playing the game."
        mc "And what will you be doing?"
        show wolf neutral
        wolf "Probably just sit next to you watching."
        mc "Aww... Come on, Ty. Play with me."
        show wolf pout
        wolf "Nope. Just wanna watch."
        show wolf grin
        wolf "Besides, you need the practice."
    "I wandered over to the games and picked something out. Something easy."
    "I don't know why, but I think part of me wanted to try and impress Ty despite not being the best at games to begin with."
    "It was hardly new information to him anyway; the few times he'd watched me play games it was just simple ones, or ones that were more about just making stuff at a leisurely pace."
    "There were a few times where he'd gotten me to try something scary, but after the first time one got me to the point of crying he promised he wouldn't make me do that again."
    scene black with dissolve
    "Wearing a fond smile on my face, I wandered back over with a wireless controller and sat with Ty, whittling the time down until it was time for dinner."
    jump Day9Dinner
#Dean (Medal)
label Day9Dean:
    scene foyer with dissolve
    "Dean led the way out from the rec room, down stairs towards the back door."
    scene mansionback
    show bear smile
    with dissolve
    bear "Y'know..."
    "I turned to look at him as we stood on the back porch."
    if TysonAsked == True:
        bear "I half expected you to say you'd rather stay with Tyson and Hoss."
        mc "Why's that?"
        show bear laugh
        bear "You looked comfortable. Have to admit I was a little jealous that you didn't sit with me, but no harm done."
    if HossAsked == True:
        bear "With how you were melting into Hoss, I'm surprised you were wanting to come with me."
        mc "Why wouldn't I?"
        show bear laugh
        bear "Hey, no judgements here. Getting a good massage is a hard thing to pass up. I'm just glad you did!"
    else:
        bear "I'm happy you decided to join me."
        mc "Well, you were nice enough to be a chair for me, it's the least I could do."
        show bear laugh
        bear "Oh? Was that the only reason?"
        mc "Well no..."
        mc "I do like spending time with you, too."
    "Dean stretched out his arms, yawning."
    bear "I guess it's just nice having that reassurance that you're interested in what I'm into."
    show bear grin
    bear "Unless...?"
    "He nudged me gently, wriggling his eyebrows."
    bear "You had other reasons for joining me?"
    "I smirked back at him."
    mc "What, here? What if someone sees, Dean? I guess we'd better be quick."
    show bear aroused
    bear "Oh? Well I think I can be quick."
    "The moment he went for his fly I reached out to grab his arm, stopping him. I should've known better than to call his bluff."
    show bear grin
    bear "What, not interested after all?"
    mc "Not right now. I should've known better than to try copying you."
    show bear smile
    bear "Well, what is it that they say about mimicry and flattery?"
    bear "I'm not going to catch you wearing my shirts next, am I?"
    "I laughed and he patted me on the back before we set off towards the greenhouse."
    scene greenhouse with dissolve
    "The moment we stepped foot inside I breathed in deep."
    "It was a mix of scents that I was slowly becoming fond of. That mix of loamy soil and slightly damp air that made the place feel and smell fresh."
    mc "So what should I do?"
    show bear smile with dissolve
    bear "Oh, nothing. Not if you don't want to."
    mc "And if I {i}do{/i} want to?"
    show bear grin
    bear "Well in that case, come on over here."
    "He gestured for me to follow over to some pots, where he looked around for a bit before taking up a pair of snippers."
    bear "I want you to hold something, lemme just get it for you."
    "He turned, and with a quick motion with his hand, turned back around with a freshly cut flower."
    show bear smile
    bear "Here. Hold this for me."
    "I felt my cheeks go red under my fur as I carefully took the flower from him."
    mc "Why do I get the impression that you're not going to be asking for this one back?"
    show bear laugh
    bear "Am I that obvious?"
    mc "A little, but... I don't mind. I don't think so, at least."
    mc "But when I say I want to help, I mean it."
    show bear neutral
    "Dean straightened up, looking serious."
    bear "Well, I hate to break it to you but there really isn't anything to do."
    bear "I planted some onions, but they're going to take a few weeks to be ready. Otherwise everything else just needs water, which I did before we came in for lunch."
    mc "Oh, so... Why did we come in here?"
    show bear pout
    bear "Well, I just like checking up on them. They're like..."
    mc "Kids?"
    bear "Something like that."
    bear "I can keep plants alive and healthy. I can dote and care for them and they'll bloom."
    "There was a bit of hesitation on his face, as if he wanted to continue but didn't quite know how to phrase it."
    mc "Dean, are you alright?"
    show bear neutral
    bear "I'm fine."
    bear "This is just a harsh reminder that it's a lot harder to nurture and care for something than it is to destroy."
    show bear sad
    bear "For example, growing a tree takes years. Cutting it down is a matter of minutes with a chainsaw."
    mc "That's true, but... it's worth it, right?"
    show bear neutral
    bear "What do you mean?"
    mc "Well... It's the same with vegetables, right? Like the pumpkin."
    mc "I don't know how long that took to grow, but in a day it was gone. But even then, it'll keep feeding us and we had fun so... it was worth it."
    show bear pout
    bear "Hrm... Maybe..."
    "Dean seemed to consider what I'd said a bit more than I'd intended."
    show bear smile
    bear "No, you're right. People are sort of the same."
    mc "Same? In what way?"
    show bear pout
    bear "Not that I really plan for it to happen, but let's say I make you upset."
    show bear neutral
    bear "I made that happen. But what if the thing I made you upset about kept you from getting hurt, or sick? That seems like a fair trade-off to me."
    mc "Right."
    bear "So just because a bad thing happens, doesn't mean that it's all doom and gloom. It could just be what comes before something happier, right?"
    "I frowned, looking at Dean."
    mc "Are you...?"
    bear "Am I what?"
    "I shook my head quickly, dismissing the thought. There was no way Dean was plotting something to hurt me intentionally, at least not at the moment."
    show bear annoyed
    bear "[mcname]. Come on, talk to me. What's on your mind?"
    mc "Are you talking about... me? Us, I mean."
    show bear neutral
    bear "...Not exactly, but not entirely inaccurate."
    "He seemed tense, standing there with his gaze fixed on me."
    menu:
        "Kiss Dean.":
            $ bearlove += 2
            "I edged forward, placing my hands on his chest."
            show bear scared
            bear "What?"
            "I wasn't sure if it was learned behavior at this point, but I knew Dean responded well to kisses. Or at least liked them with how often he kissed me."
            show bear smile
            "So I leaned up as best I could given out height difference and kissed him softly on the mouth. He didn't reciprocate though."
            mc "Did I do it wrong?"
            bear "Not at all."
            "In one quick motion he had me around the waist, roughly pulling me in close and kissing me back."
            "The suddenness of it made me jump, but it was clear that he was much better at this than I was."
            show bear grin
            bear "It was good that you made the first move. Very good."
            mc "Very good why?"
            show bear laugh
            bear "Just a sign that I'm probably doing right by you."
            mc "Of course you are, Dean. If you weren't, you'd know."
            show bear neutral
            bear "What, you'd tell me?"
            mc "Well yeah!"
            mc "Even then... I dunno, I would've thought that it'd be obvious if I wasn't interested."
            show bear smile
            "Dean hugged me close, and I squeezed him back. It felt right, at least in this very moment there was nowhere else I'd rather be."
            mc "Did you feel up for that walk still?"
            bear "Sure. That'd be nice."
        "Change subject.":
            $ bearlove += 1
            "I needed him to loosen up, or at least I wanted him to."
            mc "Dean? How about we go for a walk? Together."
            show bear smile
            bear "Oh?"
            mc "Yeah. You said you wanted to, right? Why not now?"
            mc "We could treat it like a date if you want?"
            show bear laugh
            bear "A date, huh?"
            mc "Sure! Why not?"
            show bear smile
            bear "Maybe because you deserve better than that; but a walk sounds nice."
    mc "Where did you want to go?"
    show bear neutral
    bear "Hrm... Given how you went wandering off in the woods unsupervised, I don't know if trekking through there is a good idea."
    bear "Where did you wander off to this morning? Towards the main road, right?"
    mc "Yeah, but I didn't get very far."
    show bear pout
    bear "Well... If that's the case then I think the woods might be our only bet unless you wanted to do laps of the house."
    mc "I don't really mind. Where were you planning on going, Dean?"
    show bear neutral
    bear "Was probably going to go into the woods. But if we go, you can't go wandering off again, alright?"
    mc "Okay, promise."
    show bear smile
    bear "Well alright then. Let's head on out."
    stop music fadeout 2.0
    scene black with dissolve
    play audio forest fadein 2.0
    "Dean led the way out of the greenhouse with me close behind."
    "It felt familiar, a mix between dread and excited that I wasn't sure I liked. My hesitation must've been clear as Dean took my hand in his, leading forward."
    scene woods with dissolve
    "It was quiet here. Peaceful."
    "Dean just kept on trekking forward as if he knew where to go. There was no road, no path to follow, and occasionally he'd stop to look at a tree or something before continuing on."
    "I didn't question the destination, but at some point I had to stop."
    mc "Dean, wait."
    show bear neutral with dissolve
    bear "What's wrong?"
    mc "Just... a small break. Please."
    show bear smile
    "He didn't let go of my hand, looking around before a smile broke out on his face and my world was flipped on its head as he picked me up onto his shoulders."
    mc "Whoa!"
    "He wandered a few steps through a bush and sat me down on a stump."
    show bear laugh
    bear "Take a breather, it's alright. We're almost there, anyway."
    mc "Where are we going?"
    show bear grin
    bear "What, don't want it to be a surprise?"
    mc "I didn't realize it was going to be a surprise. But we're going to be back in time for dinner, right?"
    show bear smile
    bear "Of course. Can't do much anyway, not without bringing the others to come see as well."
    show bear grin
    bear "But we can check it out first, anyway."
    hide bear with dissolve
    "Dean wandered off for a bit, checking out some of the trees and running his hands through the foliage."
    "He didn't wander out of sight. Occasionally flashing me a smile before going about his own investigation."
    scene black with dissolve
    "After a couple of minutes I joined him, and taking his hand again he led the way forward."
    scene river with dissolve
    mc "Oh!"
    show bear smile with dissolve
    bear "Yup!"
    "I wandered over to the river's edge, looking down into the water. All things considered it looked clear, cleaner than I would've assumed."
    mc "How'd you know this was here?"
    bear "I had a hunch given the layout of the forest, plus a few other things that I'd picked up from when Roswell and I were out here."
    "I'd half forgotten Roswell had been out here with Dean. I kept thinking back to him getting lost out here alone, but maybe Dean picked up on more things being out here twice in one day."
    bear "So I figure we can sit here for a bit before heading back. Sound good?"
    mc "Sure!"
    "Dean was already moving over to the river and kicked his boots off, sticking his feet into the water before just laying back."
    show bear laugh
    bear "Water's nice. Good on the feet after walking so much."
    mc "Really?"
    show bear smile
    "He looked over to me, looking relaxed."
    bear "Why would I lie about it? Kick those sneakers off and dip your feet in, [mcname]."
    "I nodded slowly, taking my shoes off and sitting on the edge of the river before following suit."
    "It was cold, but refreshing."
    mc "Oh... You're right."
    show bear laugh
    bear "What, you think I'd lie about that?"
    mc "Okay, you're right. I'm sorry."
    mc "But do you think the others would like this?"
    show bear neutral
    bear "Probably. Sal would like it, if only because there's water. But it's quiet."
    mc "I get the impression he'd like to just sit here and watch the water given how peaceful it is."
    show bear laugh
    bear "Probably. He was like that when we went to the beach one time."
    mc "You two went to the beach? Without me?"
    show bear smile
    bear "Not everything needs to involve you, [mcname]. I'm allowed to hang out with my friends."
    mc "I just assumed... Well..."
    show bear grin
    bear "What, that Sal and I didn't know each other?"
    mc "I mean I guess. Especially given he was ready to punch you. Plus you'd never really brought it up before."
    show bear neutral
    bear "Well you never asked. Plus, we've been friends for years. Rarely do I get him so worked up that he's ready to lay into me, but it's happened a couple times. I don't hold it against him though."
    mc "I never knew...{w=0.5} But still!"
    mc "Friends shouldn't hurt each other."
    bear "What about you and Tyson? He ever hurt you?"
    mc "I... uh..."
    "The answer was obviously yes, but I hadn't expected to be blindsided like that."
    show bear smile
    bear "End of the day, if you apologize to one another and move forward from it, typically things work out."
    show bear sad
    bear "...{i}If{/i} you can apologize for it."
    mc "You can't apologize for everything?"
    show bear neutral
    bear "Not everything, no. Some wounds can't survive that sort of thing. You can try, but it's hard."
    mc "Oh..."
    "We sat in quiet for a while longer before my curiosity got the better of me."
    mc "What... sort of things can't you apologize for?"
    if bearlove == 15:
        show bear pout
        bear "Well..."
        "I felt that I must've hit a nerve, but Dean continued to speak all the same."
        bear "Before I go into this, I'm trusting you with this, alright? No telling the others."
        mc "How come?"
        show bear neutral
        bear "It's serious. I mean it, [mcname]. No telling the others."
        mc "Oh... okay..."
        show bear pout
        "Dean sat up, scratching his neck and sighing out."
        bear "It goes without saying that if someone's dead, you can't apologize. Right?"
        mc "Dean..."
        "My heart started to race, looking him over expecting the worst."
        show bear neutral
        bear "Speaking from experience, coming close to that is just as hard. Difficult to apologize for, I mean."
        show bear pout
        bear "I didn't kill anyone, no. But someone's life was ruined because of me."
        mc "What happened to them?"
        bear "Hopefully doing better. I've told you about them before. The one that moved away."
        mc "The one that..."
        show bear neutral
        bear "The one that tried to kill himself. Yes."
        mc "Oh..."
        "I felt like I now knew something I shouldn't. I hadn't had to have a conversation like this before, so it was hard to know what to say, or what to ask."
        "Not that I didn't have questions, but the whole topic seemed like a taboo to even bring up."
        bear "What I would give to have a do-over, or at least run into him again and try to apologize."
        mc "I'm sorry, Dean."
        show bear scared
        bear "What for?"
        mc "I want to help but... I don't know how. Can I have a hint?"
        show bear smile
        "He wore a tired smile, looking up at me from his spot on the forest floor and reaching out carefully for my hand. I took it eagerly, giving it a reassuring squeeze assuming that's what he wanted."
        bear "You're doing plenty, honeybee. Thank you."
    else:
        show bear sad
        bear "There are things, [mcname]. Heavy things."
        show bear neutral
        bear "Things that I'm not sure I want to put you through."
        mc "But I can help, right? Somehow?"
        show bear smile
        bear "You do. Of course you do."
        mc "But...?"
        show bear pout
        bear "But some things you can't change. Some things only I can deal with, and as much as I'd like to magically fix it, we can't."
        bear "As much as it keeps me up at night. As much as it makes me worry that I'm going to do wrong by you as well, it's..."
        "He shook his head, sighing out."
        bear "It's just something you work through."
        show bear mad
        bear "Just promise me something."
        mc "Anything. What is it?"
        bear "That if push comes to shove, you do the right thing."
        mc "But I'd always do the right thing!"
        show bear pout
        bear "Even if you were in danger? Even if it meant you were going to get hurt?"
        mc "I... I think so..."
        show bear neutral
        bear "I don't expect you to know right now, but when the time comes I get the feeling you're going to need to make a tough decision, [mcname]."
        bear "You're the kind of person that wants to do right by everyone, and that's a big draw for someone that wants to take advantage."
        mc "You're scaring me a little, Dean. What are you trying to say? That I'll need to potentially get hurt to... 'do the right thing'?"
        bear "Hopefully not, but maybe. I'm sure as hell going to do my hardest to make sure that doesn't happen."
        show bear sad
        bear "But there are just some things that I just can't protect you from. Even if you're my boyfriend. I'd try even if you weren't, but still..."
        mc "Hey... Dean, it's okay."
        mc "Sure, the last few days have been rough, but... I mean it when I say that you've done a great deal in keeping me sane."
        mc "It's hard, but I'm not looking for any fights. The opposite, really. You know that, right?"
        show bear smile
        bear "I do. But it's always nice to hear. Thank you."
    "Dean sat up and put an arm around me, holding me close."
    bear "I mean it. Thank you, [mcname]."
    "I didn't realize until it happened again just how often I sat in absolute silence with people."
    "But it wasn't a bad thing. There was something nice about not needing to say anything and to just... enjoy the time with someone else."
    "Dean was someone that I didn't mind sitting together with. I wasn't sure if it was because it was a break from him being so flirty, or if I just liked having some quality alone time."
    "It was probably a combination of both given how much I did like cuddling up with Orlando, but there was something about Dean that was different."
    "As I wriggled my toes in the water, my mind wandered as to what things would mean moving forward."
    "Was I going to be a good boyfriend? Would {i}he{/i} make a good boyfriend? As if feeling my uncertainty, he leaned over and kissed me on the cheek."
    bear "You doing alright, handsome?"
    "I nodded slowly."
    mc "Yeah..."
    "I smiled gently, looking down into the water as it flowed over my feet. But that's when I saw it."
    mc "Wait... What's that in the water?"
    "I leaned forward, peering at the glint I saw peeking out from behind my foot."
    mc "Dean, is that... Right there."
    show bear neutral
    "Dean leaned in, frowning as I pointed out what I'd seen."
    show bear scared
    bear "You're kidding me. Out here? Really?"
    "He shuffled across slightly to reach for a fallen branch, using it to fish out the object out of the water."
    show bear neutral
    "Dean picked it up and wiped it on his shirt, looking it over before handing it over to me."
    bear "Take a look."
    "He handed me the medal, and I turned it over in-hand."
    mc "Why is this out here? Seems like this task was almost impossible, huh?"
    show bear pout
    bear "No kidding. But I suppose if we found it, no harm done. Chances are we might've found it if we came out this way to do some fishing. {w=0.5} Assuming it didn't drift downstream."
    mc "Right, right..."
    "I looked at the emblazoned 'H' on the surface, going through the names of the zodiac in my head."
    show bear neutral
    bear "What's the matter?"
    mc "Oh...Just trying to figure out which one this is."
    bear "Any ideas?"
    mc "Well... I don't think any of them start with the letter 'H', so... I'm kinda stumped."
    show bear smile
    bear "Something to ask the others at some point then. Aside from the mystery of the random medal, are you at least having a good time?"
    mc "I think so. But I might be getting a little cold? And..."
    show bear grin
    bear "And what?"
    mc "Well..."
    "I raised my feet out of the water, wiggling my toes for him to see, watching them drip."
    show bear scared
    mc "We didn't bring anything to wipe our feet with."
    bear "Oh shoot. Right. Well... That's on me, so... Ah!"
    show bear grin
    bear "How about I just carry you back? {i}On{/i} my back, even!"
    mc "Wait, really?"
    show bear smile
    bear "Sure! I don't mind getting a little dirty, even my feet. Nothing a shower won't fix anyway."
    bear "It's about that time anyway, so..."
    "Dean jumped to his feet, offering a hand out to me and helping me up."
    show bear grin
    bear "Come on, honeybee."
    scene black with dissolve
    "Dean turned around and I jumped up, again reminded about how broad he was compared to me. Beneath all of his fur, he felt solid, strong, and I felt safe."
    "And sure enough he carried me the whole way back, not breaking stride once."
    jump Day9Dinner
#Hoss
label Day9Hoss:
    "I watched Ty leave before I turned back to Hoss, who was stroking his mane."
    lion "Another successful conversion."
    mc "Who, Tyson?"
    show lion neutral
    lion "Yup. Didn't think he'd be that into the first part. A few people find it a bit... odd, given how it develops later."
    show lion laugh
    lion "I suppose it helps that you didn't taint his impression by showing him what you watch."
    if HossAsked == True:
        "I flipped around, sitting back on my ankles to give Hoss a look."
    else:
        "From my beanbag I shot him a look, arms folded and sinking further into my seat."
    mc "There's nothing {i}wrong{/i} with what I watch."
    show lion pout
    lion "Uh huh, and I'm a beaver."
    mc "What's {i}that{/i} supposed to mean?"
    show lion smile
    lion "Look, you're sweet, but when it comes to anime it's probably better you leave it to me to pick out what others might like."
    mc "But what if I wanna share what {i}I{/i} like?"
    show lion grin
    lion "Then by all means! But you really think Tyson would like what you watch?"
    mc "Well..."
    "I grumbled, finding myself having to concede the point."
    show lion neutral
    lion "Nothing wrong with what you like. Nothing wrong with what {i}I{/i} like. But Tyson's allowed to like what he likes too, right?"
    mc "Of course he is."
    show lion smile
    lion "Good."
    if HossAsked == True:
        "I moved to my own beanbag, sighing out."
    mc "So... What was that idea you had for something we could do?"
    show lion neutral
    lion "Oh. That's an easy one. I was going to teach you to lie."
    "I narrowed by eyes at him, pouting."
    mc "Lying's bad, Hoss."
    show lion laugh
    lion "I thought you'd say that. But... especially after yesterday, I think it's best that we get your tells under control at the very least."
    mc "But why would I need that skill?"
    show lion annoyed
    lion "Let's test, shall we?"
    if HossKiss == True:
        lion "Say [mcname], what's it like kissing Hoss?"
        "My cheeks immediately felt hot, and the corners of my mouth twitched upwards into a dopey smile."
        lion "Uh huh."
        mc "No, wait, but I didn't say anything!"
        lion "Alright, that's true but your face told me everything I needed to know anyway. Even if you were to say that you hadn't, that smile tells me not only that it happened, that you liked it."
        show lion aroused
        lion "Which, is extremely flattering by the way."
    else:
        lion "Hey [mcname], know of any secret places in the mansion?"
        "My eyes went wide and I looked away, half chuckling."
        mc "Nope!"
        lion "Busted."
        show lion laugh
        lion "But I figured that'd be the case. It's your laugh buddy. That more than anything gives you away."
    "I huffed, crossing my arms tight across my chest."
    mc "Well alright, what are we going to do about it?"
    show lion neutral
    lion "We're going to break it down to a few things. Then maybe we'll go find someone you can practice on."
    mc "I can't practice on you?"
    show lion laugh
    if HossKiss == True:
        lion "Unless you're talking about practicing your kissing, I'm not a good partner for this when you're so obvious."
    else:
        lion "Really think that's a good idea?"
        lion "Remember, I know your tells already."
    mc "But how will you know what I say is a lie? You don't know everything about me."
    show lion smile
    lion "Well that's true. Does that mean you're going to tell me all of your secrets now or what?"
    show lion grin
    lion "Already managed to get out of you what sort of guys you like."
    mc "Hey, yeah! You never told me what sort of guys you like."
    show lion annoyed
    lion "This isn't about me."
    mc "Now that's just not fair."
    if HossKiss == True:
        lion "I thought that'd be pretty clear based on what happened in the library yesterday."
        "I felt my cheeks tingle, and I couldn't help but chuckle to myself thinking back."
        mc "I was... uh... I was meaning to ask about that."
        show lion neutral
        lion "What do you mean?"
        mc "Well..."
        mc "I suppose I just don't know where that puts us?"
        show lion scared
        lion "Oh! That."
        show lion sad
        lion "I don't know either, really."
        lion "You're cute, if things were different I'd consider asking you out."
        mc "Different how?"
        show lion pout
        lion "You {i}know{/i} how."
        show lion neutral
        lion "Plus, you already have someone else vying for your attention. Not going to step in the way there unless you say otherwise."
        mc "Really?"
        show lion pout
        lion "Bit of a jerk move if you and Dean are trying to date and I swoop in and take you for myself."
        show lion neutral
        lion "So unless you decide that you're not interested in Dean and speak up, I'm not even going to consider anything beyond something casual."
        mc "So like um..."
        mc "Friends with benefits?"
        show lion laugh
        lion "I feel like I'd be meeting expectations if I were to say yes to that."
        lion "Besides, I think that's going a bit far for you, isn't it?"
        mc "Probably. I haven't fooled around with anyone before."
        show lion neutral
        lion "Right."
    else:
        lion "What, did you really want to know?"
        mc "I mean, fair's fair."
        show lion smile
        lion "Even when you're giving different people different looks?"
        lion "Honestly, I'm not even convinced you know what you like and you're still stuck in that horny teenager phase."
        mc "Wow. Rude much?"
        show lion laugh
        lion "Hey, Dean's still in that phase too from how he behaves, although I don't think it's entirely genuine. Not all the time at least."
        mc "So now I'm like Dean?"
        show lion neutral
        lion "I think it's more, and I'll tell you now that I'm speaking from experience, when you get your first taste of sex it's like a drug."
        lion "You want it more than you ever thought you did even with your hormones all over the place."
        mc "What, so you're saying I'm going to like sex?"
        lion "No guarantee, but probably."
        lion "But I mean more that you're not likely to know what you like until you get there."
        mc "Oh... I mean, there are things I want to try, sure but..."
        lion "But what?"
        mc "I dunno. It's hard to really know where to start when you haven't fooled around with anyone."
    lion "That right there. There you were telling the truth."
    mc "Why would I lie about that?"
    show lion smile
    lion "You tell me. For all I know you could just be trying to impress me."
    mc "Hey! I could impress you for sure!"
    show lion scared
    lion "What?"
    mc "Yeah! Just you watch."
    "I wasn't sure what had done it, but Hoss was stunned, looking me over. It was only for a few moments before he started laughing, wiping his eyes."
    show lion laugh
    lion "Okay, maybe you {i}are{/i} good at lying."
    mc "I wasn't lying!"
    lion "What, and if I called your bluff right now to see if you could impress me with a blowjob, would you?"
    mc "I...{w=0.5} Uh..."
    show lion smile
    lion "See?"
    show lion neutral
    lion "But we're getting off track again."
    lion "I was teaching you to lie, right? Turns out you might be better at it than I thought."
    mc "What makes you say that?"
    lion "Well... A good lie is made up of a few things, the rest just being body language."
    lion "The main few things being: Simplicity, Singularity, and Safe."
    "The look I was giving him hopefully was one of me understanding, but so far those were just words that sounded cool but didn't mean much."
    show lion sad
    lion "Alright, let me explain."
    lion "You want your lies to be simple. If you start going into all the details you're going to find it harder to keep track of everything you've said."
    mc "So... like what though?"
    show lion neutral
    lion "Like how I had some toast and an apple for breakfast."
    mc "Oh!"
    show lion pout
    lion "But I didn't."
    mc "Oh."
    show lion neutral
    lion "But that was also the second thing too. Notice how my lie didn't involve anyone else?"
    mc "But... Didn't you eat breakfast with everyone else?"
    show lion laugh
    lion "And that's the third."
    show lion smile
    lion "I got the first two, but you picked out that my lie wasn't 'safe'. A safe lie is one that's seeded in truth, and typically that there's someone there to corroborate at least part of it."
    mc "But... If Orlando saw you at breakfast and saw you eating a banana, would that be so bad?"
    show lion neutral
    lion "Not for something about breakfast at least. But then you'd be asking yourself why I lied in the first place. Having suspicion placed on you is the last thing you want if you're trying to get away with a lie."
    show lion grin
    lion "In fact, an advanced trick is to offer the information first. You're less likely to have someone question you if you're freely giving them information that's the least bit plausible."
    mc "Huh..."
    "It made me think back to every interaction now, wondering if there were any lies I just hadn't noticed."
    show lion neutral
    lion "Another thing to keep in mind is to watch someone's hands. Someone lying is more likely to touch their face."
    mc "What should I do then? Keep my hands in my pockets?"
    mc "Cause if I just do that every time I'm going to lie then that's just going to make it obvious, right?"
    show lion smile
    lion "Bingo."
    show lion neutral
    lion "Not that you should be lying unless it's necessary. But sometimes it is, and it's better that you don't get found out when you do."
    "I nodded slowly."
    mc "So if that's the case, can I ask you something, Hoss?"
    show lion smile
    lion "Sure. What's up?"
    mc "I've been confused about this for a bit but... Did you like me? As more than a friend?"
    show lion sad
    "I watched as Hoss's eyes darted down. He looked me in the eye before messing with his mane, a slight smile on his face."
    show lion smile
    lion "And if I do?"
    mc "That's not an answer!"
    show lion laugh
    "I was certain that Hoss was messing with me now. He had just told me about touching your face as a tell, so now I wasn't sure if he was doing it on purpose or not."
    lion "Hey, maybe it is, maybe it isn't."
    show lion grin
    lion "It's not all that important. Not yet anyway. Why, do you like me in that way?"
    menu:
        "Answer.":
            $ lionlove += 1
            "I frowned, almost copying what Hoss did before speaking."
            mc "And if I do?"
            show lion neutral
            lion "Then I'd probably have to tell Dean that you're no longer available for dating. At least until I get a shot at it."
            mc "Wait, really?"
            lion "Sure. If you're interested, why not?"
            show lion grin
            lion "Unless I'm lying."
        "Stay quiet.":
            "I looked away, not wanting to give him the satisfaction. If he wasn't going to give me a straight answer, I wasn't going to give him one back."
            "Plus, with how much we'd been talking about detecting lies, I don't think I could convincingly tell him a lie even if I wanted to."
            show lion neutral
            lion "Hello? Earth to [mcname]. Got an answer for me?"
            mc "Nope!"
            "I shook my head quickly, looking him in the eye."
            mc "No answer from me."
            show lion grin
            lion "No answer, huh? Is this where I should point out that sometimes saying nothing says just as much as lying?"
    "I groaned, burying my face in my hands."
    mc "Why teach me to lie, anyway?"
    show lion neutral
    lion "It's a good skill to have under your belt. Both to keep secrets and also to know when someone else is lying to you."
    show lion sad
    lion "Gonna take some practice, but it should keep you safe."
    mc "You say that like I'm in danger, Hoss."
    lion "What, and you wanting to know about the library and you freaking out about a gun isn't enough cause to worry about?"
    show lion neutral
    lion "Whether you're aware of it or not, you're breaking and could do with just... something to keep you safer. Just in case one of us isn't around."
    mc "You say I'm breaking but..."
    show lion sad
    lion "Well adjusted people don't sleep in and then go for a walk by themselves with droopy ears, [mcname]."
    lion "I meant it though, if you want to talk, I'll listen."
    mc "I know... Thanks, Hoss."
    mc "But not now. I wanna keep my mind off it for a bit longer so... could we do something to pass the time until dinner?"
    show lion neutral
    lion "Like what?"
    mc "Anything really. We could join the others for a board game? I'd say take a nap but I'm not all that tired."
    lion "What about if I brush you while we watch a movie or something?"
    "I could feel my ears stand upright at the prospect of a brushing."
    mc "That works!"
    show lion laugh
    lion "Well alright. You pick something out and I'll be back with some stuff."
    mc "Don't you just need a brush? I have one of those in my room I think."
    show lion smile
    lion "With how much you seemed to like the fur balm I let you smell I figured I can get some more of that, if you wanted."
    "I cooed at the prospect, nodding eagerly."
    mc "Yeah!"
    show lion grin
    lion "Well alright. You find something to watch and I'll be right back."
    scene black with dissolve
    "It didn't take me long to pick something out to watch, and no sooner had I finished getting it ready to play did Hoss return with brush in hand."
    "To be honest, I didn't pay much attention to the movie I put on, but it was nice to just relax and not have to worry about anything going on if only for a little bit."
    jump Day9Dinner
#Sal (Medal)
label Day9Sal:
    stop music fadeout 2.0
    scene pool with dissolve
    play audio outside fadein 2.0
    "After swinging by my room to get changed, I headed over to the pool. I could already see Sal, although he didn't seem to be here to swim."
    show croc sad with dissolve
    "Instead, he seemed to be sitting by the edge of the pool with his feet in the water, splashing gently."
    "As I entered, he looked up before turning his attention back towards the water. He didn't say anything, and instead just sat there as if I wasn't around."
    "I sat down next to him, slipping my feet into the water and splashing about in the same way."
    croc "I was hoping you'd come."
    mc "I can still leave if you'd rather be alone though."
    show croc neutral
    croc "No. It's alright."
    croc "I think I have the words to talk about what I've been thinking about these past couple of days."
    mc "Oh... Well... I'm able to listen if you want."
    show croc sad
    "Sal breathed in deep, shaking his head. He didn't say anything, instead he seemed to just watch his reflection in the water."
    "Minutes passed, and just as I was about to get up he spoke again, voice held low."
    croc "So my sister..."
    "I froze, sneaking a glance at him before returning my attention to the water. He was staring at his reflection still, and something told me that this was the time to be quiet, rather than but in with questions."
    croc "I've been trying to come out with this for a while, or at least talk about it, but people keep cutting me off."
    croc "And... with what happened to Orlando, I had to tell him to contextualize what my reaction was like."
    "He sighed again, pulling his gaze up to the sky."
    show croc pout
    croc "Anyway... I think I know what's bothering you, [mcname]."
    "There were a few moments silence before he looked at me, a cue I took to reply."
    mc "You... do?"
    show croc neutral
    croc "I don't know who it was for you, but for me it was my sister."
    "The comment hung in the air for a while before he spoke again, voice held barely above a whisper."
    show croc sad
    croc "My sister...{w=0.5} is dead."
    "I felt a chill run down my spine, wondering what everything Sal had said about her had meant up until now."
    show croc neutral
    croc "So, when I spoke to Orlando, I had to tell him that the prospect of dating him didn't interest me as much as keeping him as a younger brother of sorts."
    croc "Part of me feels I was being a little unfair. But in the same way, I feel as though he was being unfair too."
    mc "Unfair how?"
    show croc pout
    croc "I get the impression that... he may have been seeking something more from me going into things."
    croc "I'd have considered it too, perhaps, if things were different."
    show croc sad
    croc "It's only a guess, but... did you lose someone dear to you as well, [mcname]? Assuming you want to talk about it."
    "I nodded slowly, although left it there."
    show croc pout
    croc "I see... Recent?"
    "Again I nodded, and soon enough I felt Sal's arm over my shoulder. He didn't pull me close, he didn't rest his weight on me, but it was comforting in its own way."
    croc "For me... It's been years. She died when we were both still young."
    "When I think of Sal, the concept of him dying seems near impossible. He's so big, and resilient at least physically that I just assumed that it was hard to kill a crocodile."
    "My lack of questioning seemed to prompt Sal to explain further."
    stop audio fadeout 2.0
    show croc sad
    croc "It's... not easy to kill a crocodile."
    croc "But... it's possible. We're still mortal."
    "Again there was a pause. Did he want me to ask? Did he just not want to say? I gulped, turning to look at him."
    mc "Sal... How did-"
    play music dark fadein 2.0
    show croc neutral
    croc "I killed her."
    "The comment echoed in my head and I began to shake."
    "He held eye contact with me, face a mix between stoic and grave, but I wasn't sure how much of that was me starting to feel a little scared."
    show croc sad
    croc "I... killed her."
    "As he pulled his eyes away to the reflection in the pool again, he sighed."
    mc "Did... Did you really..."
    stop music fadeout 2.0
    croc "I may as well have."
    croc "She drowned. I was supposed to be watching her. I {i}was{/i} watching her but... something went wrong."
    play audio sad fadein 2.0
    show croc neutral
    croc "It was my fault. I should have gone in to save her and I didn't."
    mc "But... why?"
    show croc sad
    croc "I was scared. The moment she started screaming I seized up. Only after the screaming stopped I realized what had happened and tried to pull her out but..."
    "He left the comment there, trailing off."
    mc "It's not your fault..."
    "It was the first thing that came to mind, and while I meant it even I thought it sounded forced."
    "If what he was saying was true, then it couldn't have been his fault, right?"
    mc "It's not your fault."
    "I felt Sal's hand tense on my shoulder, looking to his face his gaze narrowed at a point far off, somewhere above the line of the water."
    show croc annoyed
    "His expression soured, the frown intensifying and his mouth turning into a snarl."
    croc "Not my {i}fault{/i}?"
    "He growled, turning to me, the grip on my shoulder tightening to the point of being painful."
    show croc yell
    croc "Not my fault!? Do you {i}know{/i} how many times I've heard that? How many people at the funeral told me that?"
    mc "I... I'm sorry!"
    "He grabbed me with his other hand, shaking me roughly."
    croc "And do you know what my parents said?"
    croc "Do you know what they didn't say, [mcname]!?"
    "His voice was loud, desperate. I hadn't heard him bellow like that. Ever. It shook me to the core."
    mc "Sal! I'm sorry! I didn't know!"
    "In the next moment I was roughly handled, the world span, and the next time I had my bearings Sal had lifted me up and was holding me over the surface of the pool."
    "He had me by the collar and I hung there, struggling and holding onto his arms lest he drop me into the water."
    "I could swim, but his snarl was distracting me from such."
    mc "I'm sorry, Sal!"
    show croc mad
    croc "Stop apologizing! Just stop!"
    "He shook me again and I whined, scared."
    mc "I'm... I'm..."
    "I kept telling myself to not cry, so much that my fears manifested instead in an anguished wail instead."
    show croc scared with dissolve
    "I watched as Sal's expression softened slightly at first before snapping to one of fear, staring at me over the pool."
    "In stark contrast to how I ended up suspended over the pool, he eased me back down onto solid ground before releasing me and shuffling back quickly so I was out of arm's reach."
    "We stared at each other for a while, both of us shaking for different reasons it seemed."
    "Sal broke the silence first, his voice breaking, stuttering as he got the words out."
    croc "I...I-I...I'm..."
    "I didn't make a move, watching him try and piece his words together. He took a deep breath, speaking once more in a whisper."
    show croc cry
    croc "...I'm sorry..."
    "Again I was put in an awkward space of wanting to help, and wanting to keep my distance. It was a feeling that I was all too familiar with but even then it wasn't any easier to handle."
    "When Sal dropped to the ground I took a step forward. He sat on the ground, hugging his knees, rocking back and forth gently."
    show croc pout
    mc "Sal...?"
    croc "I shouldn't have done that."
    mc "No, no you shouldn't but... What... happened?"
    croc "Saying it wasn't my fault... It's what you're meant to say. It's what you're meant to say even if it's not true."
    croc "That was the one thing my parents never told me. I apologized over and over but..."
    croc "Eventually I got old enough and I moved out this way."
    mc "And then...?"
    croc "That's it. That's my sin, my guilt, my crime, and I live with it every day."
    croc "It's what caused my hydrophobia, why I don't like talking to people, why I treasure Orlando as a brother."
    mc "But...?"
    show croc neutral
    "He eyed me carefully and I sat down opposite of him, right where he set me back down."
    croc "I work through it. I'm strong. But the guilt wears me down."
    mc "Sal, you're not...?"
    croc "No."
    show croc pout
    croc "Not suicidal. Dean... had the same concerns."
    mc "He knows too?"
    croc "Not specifically, but I mentioned something once to him and he took it poorly. Doesn't matter what it was, but he went on about it for days afterwards."
    mc "At least he cares?"
    show croc neutral
    croc "At least he cares.{w=0.5} Like you."
    "I wondered what I should be doing, sitting there opposite him felt like I should be doing something more, but I also assumed that approaching carelessly might end up with me in the pool."
    menu:
        "Approach.":
            "I edged closer, Sal's eyes on me as I crawled forward."
            "When I was in arm's reach I hesitated for only a moment before going in for the hug."
            if croclove >= 15:
                $ croclove +=1
                "As I reached for him, he opened his arms and embraced me in kind."
                "I felt all the tension ease from him as I hugged him around the neck, and he patted my back with a sigh. For a brief moment I was confused as to who needing comforting but it dawned on me that it was both of us."
                croc "Thank you, [mcname]."
                "We stayed like that for a while before he eased me back, once again sighing out. He looked tired, rubbing his eyes."
            else:
                "As I went to hug him around the neck, he quickly found purchase on my chest and shoved me back. It felt like being punched, except with the palm of his hand instead."
                "I landed hard on my back and it hurt. As I struggled to sit back up, I noticed he backed away a few measures to restore the distance between us we initially had."
            "His voice was distant and he looked away, as if talking to someone else."
            croc "I'm sorry... I should be better.{w=0.5} I need to be better."
        "Talk.":
            $ croclove += 1
            "Staying where I was, I nodded slowly, flashing him a quick smile."
            mc "I... try to, Sal."
            mc "I'm not... the best friend sometimes, I know that."
            show croc pout
            croc "You do alright. Like all of us, you can do better."
            mc "R-Right..."
            mc "But right now, is there anything I can do? I feel like I should, or could be doing something to help."
    show croc pout
    croc "We've spoken about my problems enough. It's not fair."
    mc "Sal..."
    show croc sad
    croc "I... Please, can we change topics?"
    "I looked down, frowning. Whatever I was feeling made me sick to my stomach. That feeling that I should help, that I could if I just had... something more."
    if DavePride >= 1:
        mc "Sal?"
        croc "Yes?"
        mc "I know it's not the same, but... If... If you want to talk about your sister sometime..."
        show croc pout
        croc "Please...{w=0.5} Stop."
        mc "I... Oh..."
        show croc neutral
        croc "But thank you. Really."
    else:
        "I shook my head. I couldn't do it, and just as well. If Sal wanted to change subjects, then it was a blessing in disguise."
        mc "Alright..."
    mc "Sometimes... Sometimes I wish dad were still around. He'd know what to do here."
    show croc scared
    croc "Your... dad? Was he...?"
    mc "Yeah... He was."
    show croc pout
    croc "Unfortunately... Even with all the wisdom in the world, there's nothing that can be done. After all, there's nothing left to help with. Nothing that isn't mine alone to deal with."
    mc "Oh... I guess I always assumed... or hoped, that the police had all the answers. Dad sure did at least."
    show croc neutral
    croc "Your dad was a police officer?"
    mc "Yeah!"
    "I was filled with pride whenever I remembered. Whenever I could find the chance to remember at least."
    "The smile on my face quickly died though. The unfortunate part of remembering those no longer with us was just that. They were gone."
    croc "If... If he had any advice, what do you think he'd say?"
    mc "Oh... I don't... I don't know. He was the one that had the advice..."
    show croc pout
    croc "I see..."
    show croc sad
    croc "I think I'd rather do police work rather than physical therapy."
    "A chill ran down my spine at the thought of Sal joining the police force. What if the same thing happened to him? What if?"
    "I gripped the fur on my head and started to pull, hoping the pain would force me to think of something else."
    mc "Please don't..."
    croc "Why?"
    croc "Healing people is... fine."
    croc "But if I'm being honest, I'd rather protect than heal."
    "I blinked, confused."
    mc "What... do you mean?"
    show croc neutral
    croc "To me, healing people is good but makes me think I failed at keeping them safe."
    show croc pout
    croc "But if I could keep them safe before then..."
    mc "Oh... So when you confronted Dean...?"
    show croc neutral
    croc "I wanted to protect Orlando. I might not be all that great at it, but I want to be."
    croc "Protecting my brother, or a surrogate of one at least, is important to me."
    mc "But... going straight into violence?"
    show croc pout
    croc "If... you could stop something bad happening by being in the wrong, would you?"
    croc "If you had to, would you injure, or even kill to protect those you hold dear?"
    show croc sad
    croc "In all honesty, I don't even know if I would any more. I used to think so."
    mc "Sal..."
    croc "But... it was good to get this off my chest at least."
    show croc neutral
    croc "I have you to thank for that. Even if...{w=0.5} I was a little rough with you."
    stop audio fadeout 2.0
    play music outside fadein 2.0
    mc "Well... You didn't hurt me so I guess it's fine? But it was scary."
    show croc sad
    croc "I know. I'm sorry."
    mc "It's alright. I've been through worse. But uh... What happens now?"
    mc "Should I just give you some space now? I was considering just sitting in the hot tub until dinner but I can leave if you'd rather... y'know."
    show croc neutral
    croc "No. It's alright. In fact, I might join you."
    show croc pout
    croc "You look ready to go, so... let me just... um..."
    hide croc with dissolve
    "Sal got up and wandered over to the lockers and I followed."
    "He seemed to have his own locker, pulling out the key from his pocket and starting to pull out the things he'd stored in there."
    if poolnotexplored == False:
        "As I looked to the other lockers, I noticed that one of the lockers looked... off."
        "The lockers not in use all were open slightly, with a key in the lock for those to just... use them if needed. But one was both closed and still had the key in the lock."
        "I thought back, calling over to Sal."
        mc "Sal...? This locker..."
        show croc swim neutral with dissolve
        croc "Which locker?"
        "Pointing to the locker, I explained."
        mc "Was that the other locker that was taken that day?"
        show croc swim pout
        croc "That locker..."
        show croc swim scared
        croc "Oh! I remember."
        show croc swim neutral
        croc "Yes."
        mc "But the key is back now?"
        croc "I guess so. That's odd."
        mc "Sure but... You haven't noticed anyone using this one, right? You haven't messed with it?"
        show croc swim pout
        croc "No. This one is mine. I don't need to touch the others."
    else:
        "I looked at the others, all of them open except one."
        mc "Guess no one else has claimed a locker yet?"
        show croc swim pout with dissolve
        croc "Not that I know of."
        show croc swim neutral
        croc "I'm the only one that's used them from what I've seen. The rest still have their keys."
        mc "Then... Why is this one closed while the other is open?"
        "With a shrug, Sal continued pulling things out of his locker before wandering closer."
    "With a nod, I reached out for the locker's handle, testing it. Finding it locked, I went to the key and unlocked it before opening it proper."
    "It was empty, shy of a medal placed neatly right in the middle."
    "I stared at it, still holding onto the door. Carefully I reached out for it and took it in hand, pulling it out and closing the locker door."
    mc "Why is this...?"
    show croc swim scared
    croc "Is that...?"
    mc "Yeah. Looks like it."
    show croc swim neutral
    croc "How interesting..."
    mc "Interesting how?"
    show croc swim pout
    croc "Well... I wonder whose locker this is then. Likely Benson's all things considered..."
    mc "Because... why?"
    show croc swim neutral
    croc "If this was locked before the scavenger hunt started, and has a medal inside, it must be him that left the key in there so we could find it, right?"
    croc "Either way... If you hadn't said anything, I wouldn't have thought to check."
    mc "Really? Not even a little bit curious?"
    croc "I have my own locker. Besides... That's invading someone's privacy."
    "I frowned, running my thumb over the engraving."
    mc "I guess so... But what if someone else put it there, and Benson just had the key?"
    show croc swim pout
    croc "Is that... likely? Which medal is it?"
    mc "Uhhh..."
    "I looked at it again and tried to describe it, flashing it to Sal."
    #Capricorn
    show croc swim neutral
    croc "...I don't know this one."
    mc "Is it worth checking with the others?"
    show croc swim pout
    croc "Maybe. It doesn't really matter unless we start making a checklist. I suppose. Right?"
    mc "I guess so..."
    "We stood there in silence for a bit before Sal wandered past me towards the hot tub."
    scene black with dissolve
    "For the rest of the afternoon Sal and I just lounged around in the hot tub. There wasn't really anything more to be said here, but... it was relaxing enough."
    "A few times I thought he'd fallen asleep but no, he was just lounging there looking thoughtful."
    "Leaving enough time to get changed before dinner, I took the medal up with me and stashed it in my room. I could show the others later."
    jump Day9Dinner
#Roswell (Medal)
label Day9Roswell:
    "After glancing between the two, I followed Roswell towards the kitchen."
    scene kitchen
    show boar smile
    with dissolve
    "Roswell wandered over to the pantry, throwing it open and looking around."
    mc "Uhh... Roswell?"
    boar "Yes...?"
    "In the next moment Roswell already had grabbed a bag of chips, turning to me while rummaging still with his free hand."
    mc "What are you doing?"
    show boar neutral
    boar "Stocking up."
    mc "For... what? Won't you spoil your dinner?"
    show boar smile
    boar "Not when I'll be the one making it."
    mc "Wait, since when?"
    show boar grin
    boar "Oh, just now.{w=0.2} Now there's no problem, right?"
    "As if making his point further, he lightly jostled the bag of candy in his other hand."
    mc "I don't think that's how that works. Besides, what do you need all of this for, anyway?"
    show boar neutral
    boar "It's a snack. Y'know, for studying."
    mc "You're studying? But we finished school! We don't need to study!"
    show boar laugh
    boar "Okay, then what if I {i}want{/i} to study?"
    mc "Oh... Well..."
    show boar smile
    boar "Also, I have something I wanted to show you. Something neat."
    mc "This sounds like a ploy to get me to study with you."
    show boar neutral
    boar "I solemnly swear on the candy I hold that I won't make you study."
    mc "Okay, but I do get some of that, right?"
    show boar annoyed
    boar "I dunno, you seem to have issues about it spoiling your dinner..."
    mc "But... But you said...!"
    show boar laugh
    boar "Got you! Now come on, to the study!"
    scene foyer with dissolve
    "Roswell led the way, snacks bundled up in his arms as we made our way back upstairs."
    "Something seemed off, and it was only when we reached the top of the stairs that I realized what the problem was."
    scene museum
    show boar smile
    with dissolve
    mc "Uh... Roswell?"
    boar "What is it, [mcname]?"
    mc "This is the museum. You said... the study, right?"
    boar "Right. That's where we're going."
    mc "Uhh..."
    show boar neutral
    boar "Okay, just... here. Hold these for me."
    "He thrust the snacks at me and I scrambled to keep them from falling."
    show boar smile
    boar "Alright, check this out!"
    "Roswell wandered over to a nearby bookcase and with a confident smile started to push."
    show boar pout
    "Or at least he tried."
    boar "C-Come on... Move already..."
    show boar sad
    "I watched as he strained against the bookcase, trying to push it with seemingly no effect."
    mc "Um..."
    boar "No! I can do this, just... Just..."
    "He doubled over, bracing himself already out of breath."
    mc "Um... What were you trying to do?"
    boar "This... This bookcase is actually a door. I was trying to slide it aside so we could get inside."
    mc "Into... what, the study?"
    show boar neutral
    boar "Exactly."
    mc "Oh... Well now I have questions."
    boar "Questions?"
    mc "Well yeah. Like..."
    if Library == True:
        mc "How did you find out about this, anyway?"
        show boar grin
        boar "Would you believe sheer dumb luck?"
        mc "Oh, well..."
        show boar sad
        boar "Alright, I confess."
        show boar grin
        boar "It was sheer {i}intelligent{/i} luck."
    else:
        mc "I thought you didn't know about any secret passages. At least that's what you told me when I was stumped yesterday."
        boar "That's still true!"
        "I gave him a look, gesturing as best I could to the bookcase with a bag of chips."
        mc "Secret passage. Right there. Right?"
        show boar grin
        boar "Technically speaking... No."
        show boar sad
        boar "But I guess it's sorta true..."
        show boar grin
        boar "But for the sake of the argument, it's still not a secret passage."
    "I gave him a look, trying my best to look unimpressed with what his reasoning was."
    mc "Don't make me drop these snacks, Roswell."
    show boar scared
    boar "Okay! Okay! Fine!"
    show boar sad
    boar "I discovered this... let's see... probably on the first day we got here?"
    boar "There isn't really anything important in there, it's more like... an adjoining room."
    show boar smile
    boar "But very much like a little private study nook."
    mc "I swear Roswell, I will slam dunk these chips so hard."
    show boar scared
    boar "Hey! Wait!"
    boar "I just thought it'd be a neat thing to show you is all!"
    mc "But how are we meant to get in? You sure this is the right bookcase?"
    show boar grin
    boar "Positive."
    show boar pout
    boar "But uh... I don't remember how I opened it last time. Maybe it was already unlocked? I sorta just leaned on it and it was uh... well, it moved aside."
    "I looked over the books and noticed two that seemed familiar."
    mc "I wonder..."
    boar "Wonder what?"
    "If the locking mechanism was the same as the one in the conservatory, then opening it seemed easy enough. Given that one of the books was on a higher shelf, Roswell would've had no chance of opening this without some sort of footstool."
    "I pulled two of the books and heard a familiar click."
    mc "Can I try pushing?"
    show boar neutral
    boar "Why? Think you'll be able to magically open it?"
    show boar smile
    boar "Because I doubt that your magic outstrips mine, [mcname]."
    "I rolled my eyes, taking Roswell's place as he shuffled out of the way. He was more than happy to take his snacks back while I sized up the bookcase."
    show boar grin
    boar "Well, go on then."
    "Giving him a confident smirk, I lightly placed my palms against the bookcase and pushed without breaking eye contact."
    mc "Open says-me."
    "Sure enough, a gentle push was all it needed now that the way forward was unlocked."
    show boar scared
    boar "How!?"
    mc "{i}Magic.{/i}"
    show boar annoyed
    "I chuckled to myself seeing Roswell bothered about my answer, but he seemed intent to stare me down all the same."
    mc "What is it you always told me when I asked you how you did your magic, Roswell?"
    show boar sad
    boar "Yeah, yeah. A good magician never reveals their secrets."
    mc "You would've seen what I did if you were paying attention. It wasn't that complicated really."
    show boar grin
    boar "So it {i}wasn't{/i} magic!"
    mc "Nah, just... a trick though. I'll show you later. For now, just uh... show me what's so special about this study."
    scene study with dissolve
    "Roswell scurried on forward into the next room, gesturing me to follow with the bag of candy."
    "I stepped into the next room and looked around. It looked very much like the private nook that Roswell described; if he hadn't told me that it was just an adjoining room I would've thought it was a completely different one."
    show boar smile with dissolve
    boar "Ta-da! Study."
    mc "Huh. Neat."
    mc "So this was here this whole time?"
    show boar neutral
    boar "Far as I know! There isn't really anything in here of note though."
    "He was right. It was very much just a desk in here with very little else. Given how much material was in the museum itself it was surprising to see even more books on display here, although none seemed to stand out."
    "That said..."
    mc "When was the last time you were in here, Roswell?"
    show boar smile
    boar "Oh... Let's see..."
    boar "Not for a while at least? I was considering coming in here the other day but I couldn't get it open."
    mc "And you thought today would be different?"
    show boar pout
    boar "Hey, that's not fair."
    boar "I could've gotten lucky in it opening this time!"
    mc "Yeah, well... turns out your luck this time was just me knowing how to open it."
    show boar grin
    boar "Hey, I'll count teamwork as a form of luck. Maybe we were just meant to be in here today."
    "I took another look around the room before looking back to Roswell."
    mc "I'm... not too sure about that."
    show boar laugh
    boar "Things just have a way of working out. Maybe it's providence, maybe it's some magic, but it's always been something I've liked about being around you."
    mc "Me? What did I do?"
    show boar smile
    boar "Sometimes nothing at all, but..."
    show boar neutral
    boar "Maybe it's just some guiding force that makes me feel as though you and I were always meant to cross paths."
    mc "Uh... I don't get it."
    "Roswell sat the bag of chips down and opened the bag of candy, digging around for a handful before shoveling it into his mouth."
    show boar pout
    "He chewed, looking thoughtful before turning to me once he'd swallowed."
    boar "Okay, so..."
    boar "Whenever I find myself having trouble, and you show up, a lot of my problems just... disappear, right?"
    mc "Really? Like what?"
    show boar smile
    boar "It's just little things. But let's take the bookcase. I wanted it open so I could show you, and who just so happened to know how to open it after I failed?"
    mc "Oh, I think I get it."
    show boar neutral
    boar "It's always been like that though, ever since the first day we met. You remember, right?"
    mc "Not... really?"
    show boar sad
    boar "You don't?"
    mc "I mean... we were really young, right?"
    show boar pout
    boar "Well... yes, but do you remember specifically?"
    mc "Gimme some candy firs- Oh! Wait, that's it, wasn't it?"
    show boar smile
    boar "Whatever do you mean?"
    stop music fadeout 2.0
    scene black with fade
    "It was a cold winter when Roswell and I first met. {i}Very{/i} cold."
    "But it didn't put a dampener on people's spirits though given Christmas was right around the corner."
    play music calm fadein 2.0
    scene streetsnow with dissolve
    "I still remember how bitter the cold was, but how pretty all the snow made the street look. Maybe it was just Christmas skewing my views on it."
    "As a kid, playing in the snow was something you just looked forward to. Even if it came with being bundled up by your parents."
    "The memory was something that was slowly coming back to me. After all, most days from back then bled together."
    show yroswell neutral with dissolve
    "On one such day, there was someone I hadn't seen before. The house next to us had been empty for a while, but a week or so ago a new family moved in."
    "Dad had let me go outside on my own to play, and what greeted me was a young boar, trying desperately to build something in the snow."
    show yroswell pout
    "As I wandered over, he noticed me, dropping all the snow he'd amassed in his hands."
    boar "O-Oh... Hello."
    mc "H-Hello..."
    "The young boar sniffled, talking in... Well I guess it wasn't any higher than you'd expect from a kid but..."
    boar "Who... are you? Are you..."
    "His eyes darted from me, to the snow structure he was working on, before looking back to me again."
    boar "Are you... here to help?"
    mc "Oh! No, not really."
    boar "Oh. Okay."
    "We stared at one another before I remembered what I'd been taught about good manners, or at least remembered what mom and dad had told me about meeting someone new."
    mc "Oh! I'm [mcname]. Nice to meet you."
    show yroswell smile
    boar "Oh!"
    "There was no follow-up. Just his exclamation as if realizing what had just been said to him, answering his question from before."
    mc "Um... Who are you? Are you... Do you live in that house?"
    show yroswell pout
    boar "Oh! Yeah! Mommy and daddy and me came here before."
    boar "Now it's our house!"
    mc "Oh! I'm your neighbor!"
    mc "I live in this house next to yours!"
    show yroswell grin
    boar "Oh!"
    boar "Then...!"
    show yroswell smile
    boar "Then...!{fast}{w=0.3} We can be friends! I'm Roswell!"
    "Suddenly Roswell had grabbed me and hopped up and down on his feet gesturing to his creation in the snow."
    boar "Mommy and daddy said that I might make a friend when we get to the new house! That's you!"
    mc "Oh! Okay!"
    show yroswell pout
    boar "But... I need help. Can you help me?"
    mc "I can ask my dad! He can help us!"
    show yroswell grin
    boar "He can!? Is he a friend too?"
    mc "Yeah! He's my best friend!"
    show yroswell neutral
    "The comment seemed to turn the boar off, making him shuffle uncomfortably on the spot."
    boar "Oh..."
    "He almost sounded sad at that remark, looking to his snow sculpture."
    boar "I'm making a best friend. I've never had one before. You're' so lucky!"
    mc "Oh! But I can be your best friend!"
    show yroswell grin
    boar "Really!?"
    "Roswell squealed happily, once again hopping up and down."
    boar "And best friends get chocolate!"
    mc "We do!?"
    "Now it was my turn to bounce happily. Dad had always kept sweets high above where I could reach for some reason, so any excuse to have some was fine by me."
    show yroswell smile
    "I remember Roswell holding out his hands expectantly for me to hand him something."
    boar "Chocolate please!"
    mc "Oh... I don't have chocolate!"
    show yroswell neutral
    boar "Oh no! But what will we do without chocolate?"
    show yroswell pout
    boar "First I couldn't make a best friend, now my new best friend doesn't have chocolate, no best friend for Roswell now..."
    "He sniffled, hanging his shoulders. I felt bad, having let my new neighbor down, I didn't see it as blackmail at the time."
    mc "What... What if... We finished making the snow friend?"
    show yroswell neutral
    boar "You'll... help me finish it?"
    mc "Yeah!"
    show yroswell grin
    boar "Oh boy!"
    boar "Then Roswell will have a friend for Christmas!"
    mc "Oh..."
    show yroswell neutral
    boar "What's wrong?"
    mc "I thought... that we could be friends."
    show yroswell grin
    boar "Really?"
    show yroswell smile
    boar "Then let's be best friends!"
    mc "But I don't have chocolate..."
    show yroswell pout
    boar "..."
    show yroswell neutral
    boar "..."
    show yroswell smile
    boar "...I don't mind."
    mc "Oh!"
    hide yroswell with dissolve
    "So the two of us started to assemble this creation he'd planned, scooping snow into a pile until it was too tall for him to reach."
    "This was why he couldn't finish it, without the height to put a head on this thing, he was stuck making something smaller than him, and apparently that wouldn't do?"
    "Sure enough, when the time came I rolled up a ball of snow like dad had shown me and placed it on top."
    "It was wonky, but what we'd made looked... something like a boar to say the least."
    show yroswell smile with dissolve
    boar "Okay! Now we need the teethies!"
    mc "Yeah!"
    boar "Like yours!"
    mc "Or yours!"
    show yroswell pout
    boar "...That's mean!"
    boar "You're a meanie!"
    mc "No I'm not! You're a meanie!"
    boar "No you!"
    hide yroswell with dissolve
    "He pushed on me, trying to knock me over instead falling into the snow, flat on his face."
    boar "O-Ow..."
    mc "Are you okay?"
    boar "I'm... I'm okay!"
    show yroswell neutral with dissolve
    boar "But... what can we use for the teethies?"
    mc "Hrm... Oh! Lemme go get something from my house!"
    show yroswell pout
    boar "You'll... come back?"
    mc "Yeah!"
    show yroswell smile
    boar "Okay!"
    scene black with dissolve
    "I remember running inside and bumping into dad, trying to explain what had happened."
    "He just laughed, and helped me find something to take out to continue playing in the snow."
    "When I got back..."
    scene streetsnow
    show yroswell neutral
    with dissolve
    "...there he was, sitting in the snow."
    mc "I'm back!"
    show yroswell smile
    boar "You're back!"
    "I held up the carrots that dad had given me, one in each hand before plunging them into the head of our creation. They jutted up like tusks, and I turned to see what Roswell thought of my finishing touches."
    show yroswell grin
    "He seemed to gently touch his own tusks before reaching out and lightly poking the carrots, before bouncing on the spot."
    boar "It's done!{w=0.2} It's friend shaped!"
    boar "Thank you, [mcname]! Thank you!"
    mc "Oh, you're welcome."
    show yroswell smile
    boar "You really are the best friend. My best friend!"
    scene study
    show boar aroused
    with fade
    "I had a smile on my face having recalled Roswell and I first meeting. From the looks of things he'd been reminiscing as well, his eyes darting to catch my gaze before looking away just as quick."
    boar "If you remember our first meeting as fondly as I do, [mcname]..."
    mc "It was cold, huh?"
    show boar smile
    boar "R-Right."
    show boar aroused
    "Roswell shoved another fist full of candy into his mouth before holding the bag out to me."
    "They were fruit gummies, so I took a couple and chewed them while Roswell wandered over to the desk in the room."
    boar "[mcname]?"
    mc "Yeah?"
    boar "I just...{w=0.3} You know I...{w=0.2} Um..."
    "He was fidgeting on the spot, unsure of what he should say or do as far as I could tell."
    mc "What's wrong?"
    show boar smile
    boar "Nothing. Nothing at all."
    boar "Just... ever since then, I've always seen you as my best friend. Whether it's more than that, or... only that, I don't know."
    show boar aroused
    boar "So..."
    boar "Even if Orlando's your current best friend... You're still mine. Always have been."
    "I laughed, nervous. Somewhere between flattered and nervous that I didn't really know how best to respond."
    show boar laugh
    "Almost in response to me starting, Roswell started to snicker to himself, moving into a full giggling fit."
    boar "S-So... we should probably get to studying, huh?"
    mc "Oh. Right. You came in here to study and wanted to show me the room, right?"
    show boar neutral
    boar "Right!"
    mc "But what... were you studying?"
    show boar pout
    boar "Oh, uh... Well, I've been trying to find this book that you were telling me about."
    "I gave him a blank stare, confused."
    show boar annoyed
    boar "Y'know, the one you described seeing when..."
    "He finished his thought by tapping his head, getting his point across."
    mc "Oh! Uh... Neat?"
    "Roswell shook his head, sighing out."
    boar "I think I've found it, but I like having a place to sit while I look over books."
    mc "Oh... Well... um..."
    show boar pout
    boar "Here, lemme just... go get it. Just a sec."
    hide boar with dissolve
    "I watched as Roswell abandoned his snacks on the desk, doubling back into the museum to retrieve something."
    "While he hummed to himself in the room next door, I looked at the chips that he'd grabbed."
    "The assumption was that Roswell would've grabbed something he liked, but maybe it was just what was in the pantry. Still..."
    mc "I don't mind BBQ..."
    "I opened the packet and grabbed a few, cradling the packet while I had a snack, watching as Roswell came back into the study."
    show boar annoyed with dissolve
    boar "What are you doing?"
    mc "Chips."
    boar "I can see that!"
    mc "Did you find your book?"
    show boar neutral
    boar "Oh. Right.{w=0.2} Yeah, I think I've found it."
    "He sat a large book down on the desk, patting the dark blue cover."
    boar "This look familiar?"
    mc "Well..."
    "I swallowed, figuring that talking with my mouth full of chips wasn't the way to go."
    mc "Maybe? Remember, I told you the book was open, right?"
    show boar pout
    boar "That does make things harder... Hrm..."
    show boar neutral
    boar "Well anyway, lemme show you what I found."
    mc "When... Did you find this?"
    show boar annoyed
    boar "You seem to be very... uh... keen on asking me when I did anything."
    mc "Can you blame me?"
    show boar sad
    boar "No, I guess not."
    boar "I'd try and find time to come back in here after we did out impromptu investigation."
    show boar neutral
    boar "After all, only way to discount it as a bad dream is to search everything, right?"
    mc "I... guess...? But you seemed a lot more torn up about it when we went looking. What changed?"
    show boar grin
    boar "What, am I not allowed to think about my mortality and choose to face it head on?"
    boar "I doubt any of the others would be so willing to disprove their own demise."
    mc "Uh... Sure?"
    mc "So long as you're okay? I think I'm fine with it. I have other things on my mind to work through anyway, but if you wanted help with your stuff..."
    show boar annoyed
    boar "Come on, [mcname]. It's not all doom and gloom."
    show boar smile
    boar "I just... I don't know, prefer things this way. It's like a game almost."
    mc "Well alright..."
    show boar grin
    boar "Now! Onto the discovery!{nw}"
    show boar pout
    boar "Now! Onto the discovery!{fast} Uh... Forgive the turn of phrase."
    "Roswell flipped open the book he'd found and turned to a page. Sure enough, it looked familiar, the word 'DISCOVERY' right there in plain view."
    mc "That's it! That's the page!"
    show boar smile
    boar "You're certain?"
    mc "Pretty sure, yeah."
    show boar grin
    boar "How fascinating..."
    show boar neutral
    boar "Well... maybe not fascinating so much as just a coincidence."
    mc "Why's that?"
    show boar smile
    boar "This book in particular is about the development of cures for anything and everything going on in the brain. Most of it is just theoretical stuff, but still."
    mc "You've read this whole thing? Already?"
    boar "Don't be silly. I've only skimmed it."
    show boar grin
    boar "But I do have a copy of this book back at my place. I think it belongs to my mom?"
    mc "That's... huh..."
    show boar sad
    boar "The thing is... The section that this is? The one that you're finding familiar?"
    show boar pout
    boar "It's about brain cancer."
    mc "Wait, really?"
    boar "Yeah."
    show boar sad
    boar "Explains how you get diagnosed with it, plus the treatment plans, but it also goes into some theoretical stuff about potentially using plants for new drugs to combat the spread of the cancer cells in your body."
    "I took another hand full of chips, crunching on them loudly."
    show boar annoyed
    "I watched as Roswell's expression shifted as I crunched, shooting him a confused look."
    boar "You {i}are{/i} listening, right?"
    "Nodding quickly, I swallowed."
    mc "Yeah, but... I don't get why it's important."
    show boar pout
    boar "Well..."
    if OzKnown == True:
        boar "It's been making me wonder if the person this house belongs to does something with medicine."
        "I frowned, tilting my head. There wasn't a way that Roswell had spoken to Oswin, was there?"
        mc "What makes you say that?"
    else:
        boar "Just some of the things around here hint that... maybe someone was stockpiling materials to make something like a drug to combat cancer."
        mc "Someone? Like who?"
        "Roswell scratched his chin, thinking."
        boar "Maybe someone that lived here? The person whose house this is makes the most sense to me anyway."
        mc "Sure, but you still haven't said why."
    show boar sad
    boar "A lot of the books here cover medicine, some of them are research reports and others delve into medicinal properties of various plants and fungi."
    show boar pout
    boar "I was curious and took a peek in the greenhouse myself. I even asked Dean what he knew about what was in there and most of what he could identify readily lined up with what I'd seen mentioned in the books."
    boar "If... I had to guess? This mansion doubled as something else. Maybe as a research facility at some point."
    show boar smile
    boar "That, or someone's got a really quirky hobby."
    "My hand was already rummaging in the packet of chips, still waiting for Roswell to tell me how he thought it was important."
    show boar annoyed
    boar "Maybe I just find the irony that I was bludgeoned in the head by a book about curing head-related issues a bit on the nose, honestly."
    mc "Well... I didn't know what the book was about, so..."
    boar "And if I told you that the book was written by my mother?"
    mc "...You can't be serious."
    show boar smile
    "Roswell closed the book and showed me the cover, pointing to the embossed name at the bottom."
    mc "Roswell, that's not your mother's name."
    boar "It totally is!"
    mc "...Your mother's name is 'Guy Mannington'?"
    show boar laugh
    "He just laughed, setting the book down again."
    boar "It could just be a pen name! You never know!"
    scene museum
    show boar smile
    with dissolve
    "Roswell grabbed his candy and shoved another hand full into his mouth."
    "We left the book in the study, heading back into museum."
    mc "So... time to study?"
    boar "Something like that."
    show boar neutral
    boar "I figured I'd maybe do some sleuthing of my own and maybe piece together who actually lives here."
    boar "It's the least I can do for not paying attention to my parents beforehand, right?"
    mc "Oh! Then... can I help?"
    show boar smile
    boar "What happened to not wanting to study?"
    mc "Well... Sure, but this is less studying and more like a game, right?"
    show boar laugh
    boar "Well in that case, grab a book and let's start looking into things."
    mc "Are we just doing it at random like we did the other day?"
    show boar smile
    boar "Well, we {i}could{/i}... But I'd advise against it."
    boar "Chances of you finding anything of worth randomly is... Well."
    "I wiped my hand so it was clean enough to handle books and looked over the bookshelf I was next to."
    mc "All these books look the same, Roswell."
    show boar grin
    boar "Who knows? You might get lucky and pull the right book."
    boar "Here, I'll even let you officially borrow some of my luck if you're that worried."
    mc "Well..."
    "I reached out to the books on the shelf, trying to decide which one to pull out first. Some of them had words on the spines, others were completely blank."
    show boar smile
    boar "Just pick one, [mcname]."
    mc "Okay, okay, fine. How's thi-"
    "I turned to him as I pulled a random book off the shelf, it sliding free easily enough but dragging something along with it that landed on my foot."
    mc "Wh- Oh. Huh."
    show boar neutral
    boar "What i-"
    show boar scared
    boar "You can't be serious."
    "I placed the book down on the floor and picked up the medal that had landed on my foot."
    mc "Guess this was tangled up against the cover or something?"
    show boar annoyed
    boar "Okay, that's enough borrowing of my luck. I want it back now."
    mc "Aren't we on the same team though? This is just... a win for us, right?"
    show boar smile
    boar "True, but I feel like that's maybe a little too convenient. Maybe best if we don't tell the others of this find right away."
    mc "If you say so... Which one is this, anyway? Looks kinda like... uh... Handcuffs maybe?"
    show boar pout
    boar "Handcuffs...? Lemme see."
    show boar annoyed
    "I handed over the medal for Roswell to take and his face scrunched up the moment he flipped it over to see what I was talking about."
    "The next moment he threw the medal down hard, narrowly missing his own foot."
    mc "Um..."
    show boar sad
    boar "I swear, today's... a mess."
    mc "Did I do something?"
    show boar pout
    boar "Of course not."
    mc "Did...{w=0.2} the {i}medal{/i} do something?"
    show boar annoyed
    "Roswell knelt down and picked up the medal, shoving it into my face, lightly brushing against my nose."
    boar "Do you know what sign this is?"
    mc "...Handcuffs?"
    boar "No."
    mc "{i}Space{/i} handcuffs."
    boar "[mcname], come on. Be serious."
    mc "Only trying to lighten the mood! I don't know which one it is."
    show boar sad
    "With a sigh, Roswell shook his head."
    boar "...Cancer. The crab."
    mc "Oh, so it wasn't handcuffs but pinchers?"
    show boar pout
    boar "I... suppose so?"
    "I glanced at the chips in my hand and offered them out to Roswell."
    boar "No... No it's alright."
    show boar mad
    boar "Although..."
    mc "Oh no. What?"
    show boar grin
    boar "[mcname], up for... some fun tonight?"
    mc "Uh... What... What kind of fun?"
    show boar smile
    boar "I think it'd be good if we got to unwind a bit tonight, relive some of the old times."
    show boar grin
    boar "A good old slumber party with just the two of us."
    mc "Didn't we do that the other night?"
    boar "No, no. Something for best friends only."
    mc "So... Orlando's coming?"
    show boar annoyed
    boar "No, [mcname]. Just us. I have the snacks and everything already prepared."
    mc "Well yeah, obviously just us. But where did you get all the snacks from? You didn't bring them with you, did you?"
    show boar smile
    mc "Roswell, tell me you didn't bring them with you."
    boar "Then I won't! But after dinner, let's just... I dunno. Would this be classed as a date?"
    mc "I... don't know? Is it one?"
    show boar neutral
    boar "I'll leave that up to you. But I figure something to take your mind off of things would do you some good. I know it's what I need, and if I can involve you as well, then all the better."
    "I nodded slowly as he reached out and put a hand on my arm, flashing me a smile."
    show boar smile
    boar "So how about we just relax in here until it's time for dinner and then when that's all done we can get this party under way?"
    scene black with dissolve
    "I watched as Roswell poured over books for most of the afternoon. He looked so determined, if troubled by something."
    "He was in the zone though, and I knew better than to take him from it while he frantically searched for answers to questions he hadn't voiced."
    "At some point I moved from playing catch with the medal to pulling out a book from the shelf and settling in."
    "While Roswell had opted to continue to pull books on stuff far too academic for my liking, I started working through easy to read stories."
    if OzPast2 == True:
        "Sure enough, Oswin's dislike of rabbits was coming through with how many of them seemed to be immediately cast as criminals or villains in the stories."
        "It wasn't just one book either, but multiple that I flicked through. I found myself wondering why rabbits of all things."
    else:
        "There was a pattern I soon discovered after flicking through some of the books."
        "In all of them, not one of them seemed to have a rabbit as a good guy; in fact most of them seemed to go out of their way to cast a rabbit as the villain."
        "I looked to Roswell to see if he was in any state of mind to have an opinion on this, but he was still focused on his own reading material."
    "Closing the book I had last grabbed, I leaned back against a bookcase and thought."
    "Were these originals, or edits of originals to cater to someone's racist preference in reading material?"
    "It was something I tucked into the back of my mind, just in case it came up again later."
    jump Day9Dinner
#Orlando
label Day9Orlando:
    "After glancing between the two, I followed Orlando outside."
    stop music fadeout 2.0
    scene mansionback with dissolve
    "The weather seemed nice enough. Mostly clear, the sun was out without it being too warm. If anything it was a little windy but it was a gentle sort of breeze that seemed to perpetually run by us."
    "Orlando, with his hands in his pockets, wandered away from the house towards the trees. I wasn't sure if he was aware I was behind him or not, but I followed all the same."
    scene woods2
    play music forest fadein 2.0
    show dragon neutral
    with dissolve
    "Eventually we came across a clearing and Orlando sat himself down before laying back on the grass with a sigh."
    dragon "Coming?"
    mc "Oh, right. Um..."
    "I followed suit, laying down next to him and looking up at the canopy above."
    dragon "It's nice out here, huh?"
    mc "Under the trees?"
    dragon "Just... out of the city. Away from everything."
    "The breeze continued to blow past us, and for a brief moment I forgot about everything happening back at the mansion."
    show dragon smile
    dragon "So how was your walk?"
    mc "My... Oh.{w=0.5} It was fine, I guess."
    show dragon sad
    "I looked over to Orlando, seeing him troubled and fiddling with his hands."
    mc "What's wrong?"
    dragon "Well... It's alright if I call you out on something, right? Like, I'm not a jerk for doing it?"
    mc "Depends?"
    show dragon pout
    "With a sigh, Orlando looked across to me before dipping his gaze away."
    dragon "To be honest, you're stressing me out a bit."
    dragon "Sure, the thing with the vault, and seeing what we've seen is a good enough reason. But you coming out with potentially being killed after your walk, well..."
    "Normally it'd be me doing the nervous chuckle, but maybe I'd rubbed off on Orlando with how he let one loose, scratching his neck."
    dragon "You say that you could've been killed, but you went off on your own anyway, right?"
    mc "You seemed to know what I was planning this morning though."
    show dragon annoyed
    dragon "Yeah, and what am I supposed to do? Tell you to be a sad sack in bed?"
    mc "Well... No..."
    show dragon sad
    dragon "Look, I'm your {i}best friend{/i}, [mcname]. I {i}know{/i} you."
    dragon "I saw how giddy you got when Dean first asked you out. I saw how distraught you got when you thought you'd forgotten my birthday."
    show dragon pout
    dragon "And now? Now I'm just worried that you're going to shut down like you did when..."
    "He glanced at me, not wanting to say it."
    mc "...when my dad died."
    dragon "Right."
    show dragon sad
    dragon "I haven't forgiven myself for not being more proactive in trying to make you feel better."
    dragon "But to be honest, after you were quiet after a week just sitting in the corner, I was scared."
    dragon "It was bad enough that I couldn't go to the funeral, [mcname]! And now you, I just..."
    show dragon cry
    "I just let him rant, working himself up to tears. I wasn't sure if he was more worried about me or disappointed with himself."
    menu:
        "Hold his hand.":
            $ dragonlove += 2
            "Carefully I reached down and took his hand in mine, giving it a gentle squeeze."
            show dragon scared
            dragon "[mcname]..."
            "I didn't say anything. I didn't need to."
            show dragon sad
            dragon "Sorry..."
            dragon "I'm just worried that I'm going to lose you."
            mc "Lose me?"
            show dragon pout
            dragon "Right. You were such a happy guy. That was the guy that I... uh..."
        "Change subject.":
            mc "Hey, it's alright, Orlando. I'm fine now, right?"
            mc "Besides... you weren't the only one that couldn't be there."
            mc "I didn't hold it against you. And... Well, I could only guess why you couldn't now that I know about your parents."
            show dragon sad
            dragon "It's hard, y'know?"
            dragon "I wanted to be there, but... The heir to a crime syndicate attending a police funeral? Apparently that's just such a bad thing."
            show dragon pout
            dragon "Why can't we do good things? Why?"
            show dragon mad
            dragon "You're my {i}friend{/i}. My {i}best{/i} friend. My parents speak so highly about being loyal but why can't I be loyal to the one guy that..."
    show dragon scared
    dragon "That... I..."
    mc "That you... what?"
    show dragon pout
    "Orlando growled, clutching his head in his hands."
    dragon "I care about you. I care about you a whole lot."
    show dragon sad
    "His voice dropped lower, almost into a terrified whisper, turning his head to look at me proper."
    dragon "[mcname]...?"
    mc "Yeah?"
    dragon "...You're a treasure to me."
    dragon "A treasure that I like seeing shine and sparkle. More than any other gemstone in the family vault. More than any bar of gold I've gotten to polish."
    dragon "Losing you... is terrifying."
    mc "You... see me as a treasure?"
    show dragon pout
    dragon "Yeah... Not... Not like you're an object but just... something I want to keep safe. Call it dragon instincts kicking in."
    dragon "I think... it's my version of Dean tending to flowers I guess? If I smother you that's bad, but look out and care for you? Absolutely."
    mc "I... Orlando..."
    "My thoughts were swimming, a warm feeling welling up in my chest. It was flattering for sure but... maybe it was something more than that."
    show dragon neutral
    dragon "And if that means I need to teach you what I know about landing a man, then I'll do it. Really, I don't mind."
    #NOTE Count from here
    mc "Wait, what?"
    show dragon smile
    dragon "Y-yeah! Y'know, with you and Dean!"
    mc "Oh.{w=0.5} Right..."
    show dragon sad
    dragon "What's wrong?"
    mc "Nothing, just..."
    "I shook my head, the feeling now gone. Or maybe not gone, but buried for the time being."
    mc "You're {i}that{/i} worried about me?"
    show dragon pout
    dragon "Ever since I messed around with the vault... I guess my senses have been in overdrive."
    mc "It's kinda the same as me, really."
    mc "Seen enough from that thing for a lifetime."
    show dragon sad
    dragon "You're braver than me. I stopped after seeing just you. But you went back for a second helping."
    mc "And I don't even know why."
    "Orlando rubbed his neck, shooting me a glance before looking away. He was troubled by something, and I was growing more curious."
    mc "Orlando? What... What did you type into the vault?"
    show dragon annoyed
    "The moment I stopped talking he slowly turned to looked to me, unimpressed."
    dragon "If you're asking what I think you're asking..."
    mc "I am. I want to know."
    dragon "I'm not telling you. End of story."
    mc "But what about what you saw?"
    dragon "I'm not telling you that either."
    mc "But why? How can I keep myself safe if I don't know what's dangerous?"
    dragon "Because {i}I'll{/i} keep you safe. {i}You{/i} don't need to worry."
    mc "So what, you're just going to keep watch over me every second of every day?"
    show dragon pout
    dragon "No, I guess not..."
    mc "So... I told you what {i}I{/i} saw. Why can't you tell me?"
    show dragon sad
    "Orlando brought a hand up to his mouth as he thought, brow furrowed. His gaze was drawn elsewhere, almost as if he was trying to focus."
    "When he spoke, his voice was quiet but level. Slowed as if he was readying himself for what he was about to say."
    dragon "Alright."
    dragon "It's burned into my mind so... I can remember."
    mc "Was it... bad? You said hanging by the rafters, so..."
    show dragon pout
    dragon "No... I don't think it was suicide. Not with how you were looking."
    mc "How... {i}was{/i} I looking? If not a noose, then..."
    "I could barely hear what he came out with next, his voice cracking and trembling."
    dragon "Meat hook.{w=0.5} Right through... y'know?"
    "He pointed to his neck, shuddering."
    "I found myself paling at the thought too. It was one thing to assume it was a noose, but a meat hook?"
    "Remembering when sometimes dad would go to the butcher and bring me along, with the big hunks of meat suspended from the ceiling. Sausages too."
    "Mentally putting myself in the place of anything I remembered from that shop made me whimper softly."
    "My eyes darted around, wondering if I'd just misheard him."
    mc "A... meat hook?"
    show dragon sad
    dragon "It was gross and scary, but there is an upside."
    mc "About... the meat hook?"
    dragon "Kinda."
    dragon "I've been looking around the mansion for any room that looks similar, or even a meat hook and nothing."
    show dragon neutral
    dragon "So... Maybe we're safe?"
    mc "What... did the room look like?"
    show dragon scared
    dragon "Oh, well..."
    show dragon pout
    dragon "Old. Run down. I almost would've guessed it to be somewhere in the basement with how dirty it was."
    mc "But no luck?"
    show dragon sad
    dragon "No luck. Which is a good thing, right?"
    show dragon smile
    dragon "So long as I don't find a room like that, we should be in the clear. But... please, maybe don't go wandering off by yourself?"
    mc "I'll... try and remember?"
    show dragon annoyed
    dragon "If you're going to kick up a fuss about everyone sticking together, and don't for a second think that that wasn't the reason you wanted to do pumpkin carving, then at least don't be a hypocrite about it."
    "I chuckled, nervous, grimacing upwards while I kept my gaze away from Orlando's judging stare."
    mc "Okay, fine, I promise."
    mc "But what word was it, anyway? The one I used for you didn't work when you typed it in, so no harm in telling me, right?"
    show dragon pout
    dragon "Well... I suppose given that there's no harm in it..."
    dragon "Still... If it {i}does{/i} work, just don't freak out, alright?"
    mc "Okay...?"
    show dragon sad
    dragon "Sacrifice."
    mc "Sacrifice? Why that?"
    dragon "I was thinking along the lines of... what sort of things you'd need to give up to get something of value."
    dragon "I tried the obvious first, but when I thought about it in gaming terms, well..."
    "He sighed out, reaching up above and flexing his fingers, his tone shifting towards sadness."
    dragon "Then I blacked out, saw that, and when I came too I was laying on the floor with the start of a headache."
    mc "Did you hit your head?"
    dragon "No... No, I don't think so. It was more like when I've been listening to music too loudly."
    show dragon pout
    dragon "Only lasted a little bit, a minute at most, then it was gone."
    dragon "Have you... gone back since?"
    "I shook my head, shifting uncomfortably on the grass."
    mc "Not since Benson. Why?"
    show dragon sad
    dragon "I've snuck back a couple of times, only to try one word at a time but nothing."
    mc "Okay, but {i}why{/i}? If you were so uncomfortable the first time, what made you go back?"
    dragon "Sometimes... the scariest thing is not knowing."
    dragon "It's why all the stuff that Roswell is into is so... creepy? Is it real? Is it not?"
    mc "You take less issue with them being scary than just... being real?"
    show dragon pout
    dragon "If I knew that ghosts were real, I'd... y'know, maybe try talking to my ancestors? They might know what to do."
    dragon "Or if demons were real, I'd know what to prioritize as far as keeping myself and other safe, right?"
    mc "I... guess so?"
    show dragon mad
    dragon "A gun, or a knife, it doesn't matter; but a weapon used without purpose and against a foe you know nothing about is a fool's errand."
    show dragon sad
    dragon "It'd be like... I don't know..."
    dragon "Attacking a werewolf with just a butter knife. I think I remember Roswell mentioning you need silver for that?"
    mc "I... see."
    mc "I guess that makes sense. But can I ask you something?"
    show dragon neutral
    dragon "Anything."
    show dragon scared
    mc "You're not scared of Ty because of werewolves, are you?"
    dragon "N-No...?"
    dragon "Okay, maybe a little bit. "
    show dragon sad
    extend "Is that... silly? Roswell put the idea into my head one day."
    "I laughed, grinning broadly."
    mc "Ty doesn't get any crankier than I do if I don't get my coffee. Promise."
    dragon "If you say so..."
    "He trailed off, leaving us in silence for a moment. That moment stretched into minutes before Orlando spoke again, his voice soft and calm."
    show dragon neutral
    dragon "Hey, [mcname]?"
    mc "What?"
    dragon "I'm glad we're friends."
    "He took my hand in his, a peaceful smile on his face."
    scene black with dissolve
    stop music fadeout 2.0
    "We lay like that for a while, just enjoying each other's company."
    "Occasionally I'd look over to see him either looking up at the leaves and watching them sway, or with his eyes closed as if resting."
    "Eventually the wind started to grow cold as it got closer to dinner time."
    "While it wasn't overly late, we didn't want to be out here when it went dark, and headed back inside to eat."
    jump Day9Dinner

##Dinner
label Day9Dinner:
if lionroute == True:
    pass
else:
    stop music fadeout 2.0
"By the time dinner rolled around..."
if boarroute == True:
    #We're making mushroom something alright
    play audio light fadein 2.0
    scene kitchen
    show boar smile
    with dissolve
    "Roswell and I filed into the kitchen, a notable spring in his step with him leading the way. Seemed like he was serious about taking charge of dinner tonight."
    mc "Still riding high from before? Looking forward to this uh... slumber party?"
    boar "Of course!"
    show boar neutral
    boar "Why wouldn't I be?"
    "Roswell wandered around the kitchen, picking up bits and pieces from the pantry before turning back to me."
    boar "Y'know, I think today turned out pretty well. Don't you?"
    mc "I wasn't expecting you to apologize to Ty so quickly, and then all the co-incidences in the study."
    show boar sad
    "That seemed to be the wrong thing to say, as his expression soured quickly."
    mc "That is to say, I think it was good that you did though! Thank you for that."
    boar "Well, you're welcome."
    boar "After thinking about it a bunch, I asked myself what you'd do."
    mc "Me? If it were me I'd try avoiding the fight if I could."
    show boar pout
    boar "Sure, but that's not what I meant."
    boar "I just asked myself what you would do, and the only thing that I could imagine is you chiming in with: 'Do the right thing, Roswell!'"
    mc "I mean yeah, I'd probably say that."
    show boar neutral
    boar "See? So I thought about it and I figured that the right thing to do would be to apologize. I've taken the first step, but I still want to see... {i}something{/i} from him."
    mc "But..."
    boar "No buts! I'm willing to give him a chance, but you can't fight his battles for him."
    show boar smile
    boar "But enough about that. We have dinner to make, and a party to get to."
    mc "You sure, Roswell? Like... we can reschedule if that's better."
    show boar annoyed
    boar "Of course I'm sure. You mean well, and it's awesome that you'll jump in to defend those you care about, but you can't always be throwing yourself in danger like that."
    show boar sad
    boar "It'll be the death of you if you're not careful."
    show boar scared
    boar "Uh... Forgive the turn of phrase."
    mc "No! I mean okay, fine, but that's not what I meant."
    show boar pout
    boar "What {i}did{/i} you mean?"
    mc "I meant about dinner to make."
    if BensonAround == True:
        mc "We have Benson around so..."
        show boar annoyed
        boar "True, but I can pull my weight too. Besides, I cooked with Dean once, I can do it by myself just fine."
        mc "And how much of that did Dean do?"
        show boar scared
        boar "A-Ah... Well, you see he may have done most of the work. But I did boil the pasta!"
    else:
        mc "You sure you can manage?"
        show boar annoyed
        boar "What, expect me to go ask Benson or Orlando for help?"
        mc "Well you could ask Orlando at least?"
        show boar pout
        boar "Not that I'm going to, we can't rely on Benson? That's what you're implying, anyway."
        mc "Oh, well... he left on vacation this morning."
        show boar scared
        boar "What!? Why?"
        mc "Apparently he was given sudden vacation time?"
        show boar pout
        boar "And you only bring this up now?"
        mc "I'm sorry! I had other stuff on my mind!"
        boar "I guess it doesn't really matter. We can fend for ourselves."
    mc "R-Right..."
    show boar smile
    "Once more Roswell started wandering around the kitchen collecting things before setting them on the counter."
    boar "I had an idea for dinner anyway. Should be easy enough to make."
    mc "Okay, but what is it? I came to help but uh... what should I be doing?"
    boar "Can you steam rice?"
    mc "Uh... Maybe?"
    show boar pout
    boar "Maybe? I assumed you could do that."
    mc "And you don't?"
    show boar sad
    boar "I... sorta know? I think I could figure it out."
    mc "Okay, so skipping the rice, what are we having with it?"
    show boar grin
    boar "Mushroom curry."
    mc "You can curry mushrooms?"
    show boar pout
    boar "Is 'curry' even a verb here?"
    mc "That doesn't matter! Just... how do we make the thing?"
    show boar grin
    boar "Well, I was thinking we could just make it like a spicy stew, right? That's basically the same thing."
    mc "Not... too spicy I hope."
    show boar annoyed
    boar "Of course not. But that'll be up to you."
    mc "Why me?"
    show boar sad
    boar "Look, if it wasn't clear by the other night, my nose isn't as good as I gave it credit for. Yours is much better."
    mc "Oh. I guess it's pretty good, but... what makes you think I'd be good with spices?"
    show boar pout
    boar "Is that not how it works?"
    boar "Well shoot, I'm sorry. There goes me assuming things I shouldn't."
    mc "Well... I'm happy to give it a try? What's the worst that could happen?"
    show boar grin
    boar "Well, the worst case scenario would be we set the place on fire, right? Or at the very least burn dinner."
    mc "Yeah, let's... let's aim for better than that."
    show boar laugh
    boar "Agreed!"
    show boar smile
    "Roswell went about chopping up some mushrooms and I started peeling potatoes. If we were making a curry, or like a stew, we'd need potatoes."
    "By the time I had done, Roswell was already throwing things into a large pot along with other bits that he'd pulled from the pantry."
    show boar neutral
    boar "Alright, [mcname]. Time for you to add your special touch on this."
    mc "Oh, no, I don't have any special touches."
    show boar annoyed
    boar "I didn't... I just..."
    "He rubbed his temples before going back to stir the pot further."
    boar "What else should we add to this?"
    mc "Well I added potatoes. What did you add?"
    show boar neutral
    boar "I cut up some of the mushrooms I brought in from the forest. Nothing overly fancy, but there were some in the pantry too."
    mc "And you sure that's safe?"
    show boar smile
    boar "Positive."
    mc "What about onion?"
    boar "Could do onion."
    mc "Salt? Pepper? Nutmeg?"
    show boar pout
    boar "Does... nutmeg go in stew?"
    "I pulled a face and shrugged, only clutching at straws. I didn't really know and it seemed as though Roswell didn't know either."
    show boar laugh
    boar "Well let's wing it! How bad it can be? I'll do the onion and you do the rice."
    mc "Oh! Maybe we can add stuff to the rice to make that tasty too. Like uh... Garlic?"
    show boar smile
    boar "{i}Butter{/i}."
    mc "Both!"
    show boar grin
    boar "Both is good."
    scene diningroom with dissolve
    "After a little bit of trial and error, the two of us managed to get dinner sorted, and brought it out so we could all eat."
else:
    if lionroute == True:
        pass
    else:
        play audio light fadein 2.0
    show diningroom with dissolve
    "We all filed into the dining room and sat down."
    "I felt... happier. At ease based on just how the day had turned out. It started low, but it ended up going alright."
    show dragon smile at left
    show bear neutral at right
    with dissolve
    mc "So what's for dinner?"
    bear "Good question.{w=0.5} Orlando?"
    dragon "Roswell volunteered to cook. Making what, I don't know but he seemed ready to try at least."
    show bear pout
    bear "He's not going to burn the place down is he?"
    show dragon scared
    dragon "Oh, I hope not!"
    show dragon sad
    dragon "Worry enough about that whenever Sal's in the kitchen."
    hide bear
    show croc sad at right
    with dissolve
    mc "Harsh..."
    croc "I'm not... that bad, am I?"
    show croc pout
    croc "I'm not the best, sure but... How hard is it really to set fire to the place?"
    show lion laugh with dissolve
    lion "Surprisingly easy."
    "I looked to Dean who seemed primed to say the same thing, but backed down after Hoss spoke up."
    lion "You weren't so bad though. You can do chicken."
    show dragon grin
    dragon "That's right! You can do hot oil, so you're fine!"
    show croc neutral
    croc "Is hot oil that dangerous?"
    show lion pout
    lion "Oh boy."
    hide dragon
    show wolf neutral at left
    with dissolve
    wolf "But can he cook though?"
    mc "I... think so?"
    mc "You could always go in and give him a hand, Ty."
    show wolf pout
    wolf "Nope. I'll take my turn cooking later."
    show croc neutral
    croc "What can you cook, Tyson?"
    show wolf neutral
    wolf "Nothing fancy, but I get by."
    show lion neutral
    lion "But what though?"
    show wolf neutral
    wolf "Stew. Toast. Scrambled eggs. I guess I can grill meat?"
    show lion sad
    lion "That's... a pretty limited range."
    hide croc
    show dragon sad at right
    with dissolve
    dragon "Well... at least you can make burgers."
    mc "They're good burgers at least."
    show wolf smile
    show lion smile
    lion "Hey, I like a good burger."
    lion "Reckon we can put you on dinner tomorrow?"
    show wolf scared
    wolf "Seriously?"
    show dragon smile
    dragon "Yeah!"
    dragon "And if you need help I'm sure someone will be willing to lend a hand."
    if wolfroute == True:
        mc "I'll help. It's only burgers, right?"
        show wolf smile
        wolf "Sure. That works. Thanks, pup."
    else:
        lion "Put me down to help."
        show wolf smile
        wolf "Really?"
        show lion neutral
        lion "Of course. shouldn't be too hard, right?"
    dragon "There's what..."
    "Orlando started to count on his fingers."
    if OzKnown == True:
        show dragon neutral
        dragon "Nine, right?"
        mc "Nine? Why nine?"
        dragon "Well the seven of us, plus Benson, plus uh... Well the owner of the house, right?"
        mc "Oh. {i}Right{/i}. Did I not say?"
        show dragon scared
        dragon "Say what?"
        mc "Oh, I ran into Benson this morning and apparently he's gone on vacation."
        show wolf neutral
        wolf "Just like that?"
        mc "Apparently. Yeah."
        show dragon annoyed
        dragon "Well that would've been nice to know. Why didn't you say earlier?"
        mc "I guess I just got distracted. But good thing we know now, right?"
        show lion sad
        lion "Well... Can't complain about him getting some time off. Life of a butler must be a full-time gig after all, right?"
        show dragon neutral
        dragon "That's true."
    else:
        show dragon grin
        dragon "Eight!"
        dragon "All of us, plus Benson, right?"
        "My eyes narrowed, nodding slowly."
        "There was only eight. Oswin didn't exist. It was a lie that I had decided to keep for now."
        if lionroute == True:
            "I looked quickly across to Hoss and away again before he noticed. He was going to be the one I needed to be careful about."
            "He hadn't called me on it once, so maybe I'd be in the clear if it came up again."
        mc "Right."
    dragon "Okay. Eight people. That's easy."
    show wolf pout
    wolf "Given how much Dean can put away, and how big Sal is, probably going to be making enough for more like ten."
    show lion sad
    lion "Probably."
    mc "Is... That bad though?"
    show lion neutral
    show wolf neutral
    wolf "Doesn't bother me."
    hide wolf
    hide dragon
    hide lion
    with dissolve
    "We continued chatting around the table until Roswell brought out food. Some sort of mushroom dish with rice. Apparently this was from the stuff he'd gathered when he was out in the woods?"
"Having eaten our fill, Dean leaned back in his chair, sighing out and looking to Roswell."
show boar smile
show dragon pout at left
show bear neutral at right
with dissolve
bear "So what was in that, anyway?"
if bearroute == True:
    boar "You can't tell?"
    show bear pout
    bear "Should I be able to tell?"
    boar "Given we picked some of these, yeah. I used some paddy straws along with what I found in the kitchen."
else:
    boar "Just some of the mushrooms I picked in the woods."
    show dragon scared
    dragon "Nothing dangerous I hope?"
    show bear pout
    bear "Given how much I ate, I might be in trouble."
    show boar annoyed
    boar "They were {i}fine{/i}. I promise you."
    show boar neutral
    boar "Just some paddy straws. Nothing fancy, I promise. The rest were from the kitchen, from the grocery store I'm assuming."
if boarroute == True:
    show bear pout
    bear "What about the rice?"
    mc "Oh! We added butter and garlic to it before steaming it."
    show boar smile
    boar "Yeah! Thought it'd be a little more rounded out than just normal plain rice."
    show dragon annoyed
    dragon "What's wrong with normal steamed rice? This stew stuff was heavy enough as it was."
    show boar sad
    boar "I was just trying to be fancy. That's all."
    boar "There's not really enough for another whole meal anyway, so I guess it works out."
else:
    mc "What about the rice though?"
    show dragon pout
    dragon "Garlic and butter, right? Otherwise it was just steamed rice, I think?"
    show boar grin
    boar "Yup!"
    mc "So it was like... a mushroom curry?"
    show boar sad
    boar "More like a stew, I think. I sorta panicked and threw everything into a pot and tried to figure out what to make. There's still a little bit left, but probably not enough for another meal."
hide dragon
hide bear
show wolf pout at left
show croc smile at right
with dissolve
wolf "I dunno, it tasted fine to me."
show boar annoyed
"I saw Roswell start to say something before forcing himself back, scratching his head instead."
show boar sad
croc "I'm not picky.{w=0.5} I would eat that again."
show wolf neutral
wolf "Same here."
mc "In any case, thanks for dinner Roswell!"
show boar aroused
boar "Thanks, [mcname]..."
show boar smile
boar "Well, I'm going to clean up dinner. I made the mess, so may as well clean it."
show croc pout
croc "...Can I help? It doesn't seem fair for you to do all the work."
show boar scared
boar "Oh, well... If you want to. I'm not going to say no, but don't feel pressured to. Honest!"
show croc smile
croc "It'll get done faster that way. I'll meet you in the kitchen."
if boarroute == True:
    mc "I'll help you out too, Roswell. No point in going on ahead."
    show boar pout
    boar "Are you sure?"
    mc "Absolutely. Between the three of us it shouldn't take too long. Just as Sal said."
    show boar smile
    boar "Can't argue with that! Alright, let's get this done and settle in for the night."
    scene kitchen
    show croc grin at right
    show boar neutral at left
    with fade
    "We brought everything into the kitchen, ready to start cleaning."
    mc "Okay! Time for the dishes!"
    show boar laugh
    boar "Yeah! I'll wash the plates, and then Sal can do the glass later! But first, you're on rinsing duty, [mcname]."
    show croc pout
    croc "You wash the glass first."
    show boar pout
    boar "What...?"
    croc "You wash the glass first."
    show boar annoyed
    boar "It doesn't matter that much, does it?"
    "I started rinsing the plates as Sal looked Roswell over, sizing him up."
    show croc neutral
    croc "It matters. If you do the glass first, then the water is clear."
    croc "If you do the plates first, all the grime gets on the glass and makes it cloudy."
    show boar pout
    boar "I... It can't really be that noticeable, is it?"
    show croc pout
    croc "Fine. Do the plates first."
    show boar scared
    boar "No! Wait, I'll listen!"
    "Sal threw his arms up in a shrug and started bringing more things over to me to rinse, with Roswell close behind."
    boar "Sal! Teach me how to clean dishes properly!"
    scene black with dissolve
    "After I rinsed the dishes, I stood back while Sal taught Roswell to do dishes. I just assumed that Roswell would know and Sal wouldn't, but maybe this was just another thing that Roswell was eager to know."
    "It was him to a fault, always learning, always seeking out new bits of knowledge."
    "Still, Sal seemed to be a good teacher, but I got the impression that maybe he was treating Roswell a little too much like a younger sibling with how he was phrasing his instructions."
    "Not that Roswell seemed to mind, at least."
    jump Night9Roswell


show boar neutral
boar "Well, that makes things easy."
hide boar
hide croc
hide wolf
with dissolve
"There was some showing of people stacking their plates to make the trip into the kitchen easier before people started to peel away."
if wolfroute == True:
    show wolf neutral with dissolve
    "Tyson wandered up to me, looking me over before keeping his voice held fairly low. It was unclear if he didn't want anyone else hearing or not, but he was focused only on me."
    wolf "...I'm gonna get ready for bed."
    mc "Oh, alright Ty."
    "There was more hesitation, Tyson looking me over carefully."
    wolf "See you upstairs?"
    "I nodded slowly."
    show wolf smile
    wolf "Good."
    "There were a few more moments before he came in again, patting me on the head before walking by."
    hide wolf with dissolve
    "I watched him go, his hands buried in his pockets and his tail wagging behind him. If I didn't know better, he looked excited."
    "Truth be told I was looking forward to it as well, some sense of normalcy after a few crazy days."
    stop audio fadeout 2.0
    jump Night9Tyson

stop music fadeout 2.0
scene foyer with dissolve
play audio calm fadein 2.0
"With dinner behind me, I yawned. I didn't feel like I did much today, but I was for sure ready for bed."
if bearroute == True:
    show bear smile with dissolve
    "As I was rubbing my eyes, Dean stopped before me, looking me over."
    bear "Tired?"
    mc "I guess so. Maybe the walk took more out of me than I thought."
    show bear grin
    bear "Want me to carry you up to bed?"
    mc "Oh. No. That's alright, I just... I dunno. Might take a shower and get comfortable."
    show bear neutral
    bear "Well alright."
    bear "See you in the morning then?"
    mc "Well... I was assuming that I'd see you when I got out of the shower."
    show bear grin
    bear "Oh really now."
    mc "I mean, if you're interested? I don't know how much I'll be up for, but... The offer is there?"
    show bear smile
    bear "Well alright. I'll see you upstairs."
    mc "Not heading up just yet?"
    show bear grin
    bear "If we're doing a do-over from last time, I should probably go get you another flower, right?"
    mc "Oh, no that's alright. I don't need another flower."
    show bear neutral
    bear "But did you {i}want{/i} one? It's no bother, really. You seemed to like the last one."
    mc "I did! But uh... I don't want another flower, not right now anyway."
    bear "Anything else I can bring you instead? Bit late for coffee."
    "I laughed, wondering if I should make some sort of lewd comment and risk him taking it too far."
    mc "You don't need to bring me anything, Dean."
    show bear grin
    bear "But if I {i}want{/i} to?"
    mc "Then... surprise me?"
    show bear laugh
    bear "Alright. I can do that. You sleeping in my bed or am I sleeping in yours?"
    "I thought back, thinking about what might happen and the implication of using my room. The fact that my room was bugged made me hesitant to really want to do anything there if I could avoid it."
    mc "Uh... Yours, I think."
    show bear grin
    bear "Then I guess I'll see you when you get out of the shower."
    jump Night9Dean
if lionroute == True:
    "I was halfway up the stairs before..."
    show lion neutral with dissolve
    lion "Heading to bed?"
    "I looked behind me and sure enough there was Hoss, still standing at the bottom."
    mc "Considering it, I'm beat."
    show lion laugh
    lion "Still relaxed from the brushing I gave you?"
    mc "Oh, well... That helped for sure."
    show lion smile
    lion "Well {i}I{/i} know what you were up to today, and I can't say you were all that busy."
    "I wandered back down the stairs to stand in front of Hoss, scratching my head."
    mc "It was exhausting, still. Not physically, but uh..."
    show lion neutral
    lion "Mentally? Emotionally?"
    mc "First one, then the other. Right."
    show lion sad
    lion "Well... Alright then. Don't worry about it. You could probably do with the rest."
    mc "Did you need me for something?"
    show lion smile
    lion "I mean it, don't worry about it. You go get some rest."
    "I gave him a look but his smile was unflinching. Part of me wondered if this was another test and I felt it wouldn't hurt to call him out on it just in case."
    mc "Hrm..."
    show lion neutral
    lion "What's wrong?"
    "He wasn't touching his face and he was keeping eye contact. So I felt that he was being genuine about me not wanting to worry about whatever it was he raised. Was this even how lying worked on a deeper level?"
    show lion grin
    lion "I'm not lying. Or am I?"
    "My eyes went wide, stunned at how transparent I must've been for him to know where my mind was at."
    lion "Go to bed, [mcname]. I'll see you later."
    "I hesitated but ultimately turned away, hitting the half way mark again before looking down the stairs to see if Hoss was still there."
    show lion smile
    "He was, and he just waved me off before he wandered away towards the kitchen again."
    jump Night9Hoss
if crocroute == True:
    "I trudged out of the dining room towards the stairs, reaching the bottom before I heard the footsteps behind me."
    show croc pout with dissolve
    croc "Um..."
    mc "Oh. Hey Sal."
    "He was fidgeting on the spot, playing with his hands and keeping his gaze averted."
    mc "Is... everything alright?"
    croc "Yes..."
    mc "That's... good?"
    croc "Right..."
    "I gave him a look, trying to figure out what was up. The only thing I noticed was that whenever I tried to catch his eye he shifted it somewhere else."
    mc "Well... I was gonna go to bed. Maybe just lounge around and watch things on my phone."
    show croc sad
    croc "Oh... "
    extend "Alright. I understand. "
    show croc neutral
    extend "Sorry to bother you."
    hide croc with dissolve
    "Sal scurried back towards the dining room, leaving me behind. Something seemed off, although I had very little to actually go off of."
    jump Night9Sal
if dragonroute == True:
    show dragon neutral with dissolve
    "I looked to my left and Orlando was standing next to me, stretching out his back. He shot me a smile and I looked away, remembering what we had talked about earlier."
    dragon "What's the matter?"
    mc "Nothing, just tired. Y'know."
    show dragon smile
    dragon "What, after we took it easy today? I thought that would've been enough to let you recover from your walk."
    mc "Well... It's a different sort of tiredness."
    dragon "Ah."
    show dragon neutral
    dragon "Sorry, I just thought... Y'know what, it doesn't matter. If you're tired, you deserve the rest."
    mc "No, what's up?"
    show dragon pout
    dragon "To be honest, I wanted to run through some more things with you, but if you're tired they can wait."
    mc "What... sort of things?"
    if OrlandoKiss == True:
        mc "It's not... kissing practice, is it?"
        show dragon scared
        dragon "No! Not... this time at least?"
    else:
        show dragon scared
        dragon "Oh, uh..."
    show dragon neutral
    dragon "I promise it's only nice things. Things to maybe help you on your way to land Dean."
    "I looked around quickly to make sure Dean wasn't in earshot and shot Orlando a look."
    show dragon annoyed
    dragon "What? He's into you. If anything I would think he'd be excited to hear you getting ready for him."
    mc "What makes you say that?"
    "With an emphatic sigh, Orlando shook his head and grabbed my arm, guiding me upstairs."
    jump Night9Orlando
return
##Night time
label Night9Tyson:
    scene bedroom with dissolve
    "I wasn't sure which room I should be going to, as that was the one thing that I hadn't pitched to him."
    "He wasn't in mine, so I grabbed what I needed and wandered over to his room."
    play music calm fadein 2.0
    show wolf shirtless neutral with dissolve
    "He didn't seem to flinch as I entered, in fact it didn't seem to register that I'd entered with how he was looking at his phone while he sat on the edge of the bed."
    mc "Ty...?"
    show wolf shirtless smile
    wolf "Hey, pup. C'mere."
    "I wandered closer, what I'd brought from my room bundled up in my arms. Nothing overly out of the ordinary. A fresh change of clothes, my toothbrush; just basic things."
    "Ty patted the bed and I sat down next to him, putting my things off to the side, near the end of the bed."
    "He put an arm over my shoulders and pulled me in close so we were properly side by side, resting his head against mine."
    show wolf shirtless sad
    wolf "Crazy couple of days, huh?"
    mc "Yeah..."
    wolf "Reckon this would've all gone down the same way if we'd just stayed at home?"
    mc "What do you mean?"
    show wolf shirtless neutral
    wolf "Say you invited me here and your friends said no. I would've just stayed at home or hit the road."
    wolf "But if {i}you{/i} stayed with me, pup..."
    "He trailed off, sighing out."
    wolf "I guess... Reckon I'd be just this much of a mess if we were just hanging out at yours for a month?"
    mc "I dunno, Ty. I really don't."
    mc "Maybe it'd just be like old times and we'd stay up eating pizza. Maybe it'd be more like what happened a few days ago, I really don't know."
    show wolf shirtless sad
    "I looked over to the door to the room upon seeing Tyson's ears droop."
    "We were safely alone, so I felt comfortable enough to speak my mind. Or at least comfortable enough to steel my nerves to start speaking it."
    mc "Ty?"
    show wolf shirtless neutral
    wolf "Yeah?"
    if wolflove >= 18:
        "I breathed out a breath I hadn't realized I was holding onto."
        mc "I like it when I'm around you."
        show wolf shirtless scared
        wolf "What...?"
        mc "Even when it hurts."
        mc "It's not the same as what you described before but... it's close."
        wolf "[mcname]..."
        show wolf shirtless annoyed
        wolf "Fuck, this wasn't meant to happen."
        mc "What do you mean?"
        wolf "I did want... I didn't mean to..."
        mc "Ty... It's okay."
        show wolf shirtless mad
        wolf "No it fuckin' isn't."
        wolf "You need someone who'll treat you right. {i}That{/i} isn't me."
        show wolf shirtless sad
        wolf "But..."
        mc "But what?"
        mc "You {i}do{/i} treat me right, Ty. You always have."
        show wolf shirtless scared
        mc "Even before... y'know. What we started with was rough, sure. But..."
        "I turned my body to face him properly, letting his arm fall from my shoulders so it hung limply next to him instead."
    elif wolflove >= 15:
        mc "Even... Even if we stayed back at mine... I think I'd have been happy."
        show wolf shirtless scared
        wolf "Even though you'd miss this?"
        mc "It's just a mansion, Ty."
        show wolf shirtless annoyed
        wolf "{i}Just{/i} a mansion."
        mc "I mean it. Compared to you, it's just a mansion, Ty."
        mc "You probably think I'm lying, or just being silly but... I dunno..."
        show wolf shirtless scared
        mc "I'd pick you over a mansion. You're worth more to me than some big house, anyway."
        wolf "[mcname]..."
        mc "I mean it Ty."
    else:
        "I nodded slowly to myself, looking to meet his gaze."
        mc "I think I'd be alright with that."
        show wolf shirtless scared
        wolf "What?"
        mc "Yeah. I know it might not seem as exciting as having a whole mansion to ourselves for a month but..."
        mc "I liked those nights we just lounged around on the sofa and ordered pizza."
        show wolf shirtless sad
        wolf "You deserve better than that."
        mc "Probably."
        mc "But that's why I have you."
        show wolf shirtless scared
        wolf "What...?"
    mc "You make me happy."
    "In a flash he was upon me pinning me down for the second time today. But this time was different, I could feel his shoulders shaking as he held onto me, tight."
    mc "Ty..."
    "He mumbled something right next to my ear and even then I couldn't make it out."
    "It didn't matter though, as he soon got up enough so I could look at him properly."
    show wolf shirtless smile
    wolf "You make me happy too, [mcname]. You fuckin' dork."
    "He pulled me into a hug again."
    show wolf shirtless mad
    wolf "You know how it is, right?"
    mc "That you've got my back?"
    show wolf shirtless smile
    wolf "That's right. But..."
    show wolf shirtless neutral
    wolf "That's not all."
    mc "There's more?"
    "We looked at each other for a bit, Ty pulling his gaze away first, clearing his throat."
    show wolf shirtless pout
    wolf "Yeah, but it's not important."
    mc "Come on, Ty. Don't leave me hanging like that."
    wolf "Fine. I was going to say it's time for a shower. See? Not important."
    "I frowned at him, unconvinced."
    mc "Yeah right."
    wolf "If you're lucky I'll come join you. So get your butt clean and then we can jump in bed."
    mc "This early?"
    show wolf shirtless neutral
    wolf "After a good brushing, yeah."
    "I felt my cheeks burn, wondering if what I assumed he meant was going to happen. I hopped up and wandered over to the shower."
    #NOTE: Count from here
    scene daveshower with dissolve
    "There was something nice about hot water. Or maybe it was just water in general."
    "As I lathered up, running my digits through my fur, I sighed out and closed my eyes. Just on the other side of the bedroom was Tyson, who had caused me no shortage of grief over the time we'd been here."
    "But at the same time, confused me more than he ever had. Was he jealous? Was he interested in me in... {i}that way?{/i}"
    "I shook my head, pushing the thoughts down. He'd made it clear that he wasn't interested, right? Not only that, but there was Dean to consider."
    "Not that having a talk with Dean wasn't out of the question. He'd likely be disappointed, but..."
    "My eyes flew open when I heard the door to the bathroom open."
    mc "Ty?"
    "I kept facing the wall, still unsure if I wanted to face him in the buff."
    show daveshowerwithtyson with dissolve
    wolf "What?"
    mc "N-Nothing..."
    "My heart began to race, feeling him up close like this. While I couldn't see anything except the tiles in front of me, it was clear that he was just as naked as I was."
    wolf "You missed that spot again."
    mc "I know..."
    wolf "...Want me to get it?"
    "I nodded slowly, feeling his arms tense around me slightly before his hands started to wander from my chest down to my stomach."
    "It was having an effect on me, and I tucked my tail between my legs, embarrassed."
    "Ty's hands lingered there for a moment before scratching lightly and bringing them back up."
    mc "Ty..."
    wolf "I know.{w=0.5} Did you want it?"
    "I gulped, unsure. When my answer didn't come right away, Ty shifted so he wasn't directly behind me anymore."
    wolf "I'll take that as a no. Pass me the soap."
    mc "Wait, I..."
    wolf "What?"
    mc "I'm sorry."
    wolf "Don't be. It's fine."
    mc "What about you though?"
    "I could feel that I wasn't the only one potentially ready to go, but he just huffed."
    wolf "Cum is hard to get out of fur anyway."
    "With my hands still free, I lathered up again this time also running my hands along his arms to get him clean too."
    "He took this as a cue to take the soap from me, digging his fingers into the back of my neck and making me gasp."
    "It was a good gasp though and he knew it, having done this very thing before so he didn't relent until I was properly clean."
    wolf "You're gonna need a boyfriend that can get this spot for you, pup."
    mc "U-Uh huh..."
    "In my stupor I could make out the slightly amused tone Ty used, razzing me as he continued to scrub."
    wolf "Or you could just get good at remembering to use the fucking scrubbing brush."
    "I chuckled, nervous as I let Tyson scrub my back."
    wolf "Alright. You're good to rinse off."
    mc "What about you?"
    wolf "I can do it. Don't worry about it, pup."
    "He guided me more under the water and I rinsed myself off, making note to wash over the spot that Ty said I missed."
    "When I was just about done, a hand came down onto my rear firmly, making me jump. He shot me a toothy smile before waving me off."
    mc "But... Can I wash you next time?"
    wolf "If you're lucky."
    stop music fadeout 2.0
    scene black with dissolve
    "I stepped out of the shower, grabbing a towel and started to dry off. A few times I looked over my shoulder, watching Ty scrub himself facing me while he did so."
    "With the amount of steam, I couldn't make anything out and I was torn about wanting to see in the first place."
    "Hell, part of me was wondering if the expectation was that I should be putting on some sort of show for him but that was probably down to spending too much time with Dean."
    "I gave myself a quick blow dry before heading into the bedroom."
    play music relaxed fadein 2.0
    scene bedroom with dissolve
    "With the towel around my waist I left the bathroom and wandered over to Ty's bed to where my pile of clothes were."
    "We were just going to be lounging around and sleeping, so I pulled on some sleeping shorts and sat my clothes down nearby off the bed."
    "Then began the wait. I wasn't sure if Ty was going to step out of the bathroom in a towel or not so I sat on the side of the bed facing away from the bathroom just to be safe."
    "I heard the water turn off.{w=0.5} Then the sound of the blow-drier."
    "When the bathroom door opened I heard him approach the bed behind me."
    wolf "What are you doing?"
    mc "Just waiting."
    wolf "What, not hoping to catch a peek?"
    mc "Well... I was curious, but... y'know..."
    "I heard some more shuffling around and Ty cleared his throat."
    show wolf underwear neutral with dissolve
    wolf "Better?"
    mc "Okay."
    show wolf underwear smile
    wolf "Not done yet though."
    mc "What do you mean?"
    show wolf underwear pout
    wolf "Brush me."
    mc "Oh, right.{w=0.5} Sure. But then my turn after?"
    show wolf underwear smile
    wolf "Yup."
    scene davebrushtyson with dissolve
    "I came around to the other side of the bed and Ty got into position. He must've already lay out the brush in preparation as it was sitting on his pillow."
    "The moment I put brush to fur, he sighed out."
    wolf "Just like that, pup."
    "His tail started to wag slightly as I brushed down his back."
    mc "I know how you like it. Don't worry."
    "I could feel the tension falling from Ty as I brushed him, stopping only once I heard him moan softly."
    wolf "...Why'd you stop?"
    mc "You... um..."
    wolf "If feels good, pup. You make the same sounds when I do it to you."
    wolf "Should've been able to tell from my tail, right?"
    mc "Well... True, but you don't like talking about it."
    wolf "About what, pup?"
    mc "Anything that's remotely close to you being a dog..."
    scene bedroom
    show wolf underwear neutral
    with dissolve
    "Ty sat up, looking off into the distance."
    wolf "Yeah..."
    mc "Ty?"
    if wolflove >= 10:
        wolf "Sorry, just getting ready for something."
        mc "Oh, my turn for brushing?"
        wolf "Yeah, but that's not all."
        show wolf underwear sad
        wolf "I trust you. So it's about time I tell you why that sets me off."
        wolf "But don't tell anyone, alright?"
        mc "Of course, Ty."
        show wolf underwear neutral
        wolf "Alright. So... I'm a wolf."
        show wolf underwear sad
        wolf "But I'm also... not.{w=0.5} Half, I guess."
        mc "Half?"
        show wolf underwear neutral
        wolf "Mom wasn't a wolf. Don't even remember what she was the more I think about it."
        show wolf underwear mad
        wolf "Bitch walked out on us when I was just a kid. Didn't give a damn about leaving me with dad."
        show wolf underwear sad
        wolf "Not that dad was any better, but he didn't put me up for adoption, so that's something. Sometimes wish he did."
        mc "It wasn't all bad though, right?"
        show wolf underwear neutral
        wolf "I showed you how things were, [mcname]. You tell me."
        show wolf underwear mad
        wolf "You had it so lucky. So damn lucky and I hated you for it."
        show wolf underwear pout
        wolf "At least I did until you started looking out for me. Then I just started hating dad more."
        mc "I'm sorry, Ty. I know..."
        show wolf underwear neutral
        mc "When I started paying more attention I just... I dunno, I guess I just started noticing how sad you were?"
        mc "I wanted to help."
        wolf "You did."
        show wolf underwear smile
        wolf "Trust me, you did."
        show wolf underwear sad
        wolf "But being called a dog just reminds me that I'm related to some bitch that walked out on her kid and it makes me so mad."
        mc "Do you know why though?"
        show wolf underwear neutral
        wolf "Makes me worry I'll do the same thing. Hell, was basically planning on it."
    else:
        wolf "Don't worry about it, pup. Just personal stuff."
        mc "Did you want to talk about it?"
        show wolf underwear pout
        wolf "Not really. Not really all that to tell, anyway."
        wolf "Just feel like I'm doing the same thing even thinking about packing up things."
    "I shot him a look, and he sighed out, continuing."
    wolf "Plan was to pack up and just bail. Come back one day or not, I don't know."
    show wolf underwear sad
    wolf "While on the road I could just... Dunno, sort my shit out. Figure out what I'm into and why."
    wolf "Can't just leave you in the lurch though. Can't take you with me either."
    wolf "So plan was make sure someone's looking out for you while I'm gone. If that means it's a boyfriend or whatever, then fine."
    "I sat there, unsure."
    mc "I don't like the idea of you leaving, Ty."
    show wolf underwear neutral
    wolf "Me neither. Not anymore."
    show wolf underwear mad
    wolf "But what else am I meant to do?"
    "I didn't have an answer for him. I wasn't panicked so much as deflated as he wanted to leave for what seemed like a good reason. And he was open to coming back, so..."
    show wolf underwear sad
    wolf "Look, just..."
    "He took the brush from me carefully, running his hand through the freshly brushed fur on his head."
    wolf "Lemme brush you and we can cuddle."
    mc "Wait, there's something I wanna tell you. Something important."
    show wolf underwear scared
    wolf "What is it?"
    mc "I just want you to know that... Even if you leave, no matter how long it takes you to come home, you have a home to come back to."
    wolf "What...?"
    "He croaked out his response, staring at me."
    mc "You're family, Ty. I don't know if that's as a brother, or... as a close friend, or whatever..."
    "I trailed off, fearing that I'd said something wrong."
    show wolf underwear smile
    "But seeing Ty's face shift towards a smile, but most importantly relaxed, put me at ease."
    wolf "Really?"
    mc "Uh... To which part?"
    wolf "I'm family?"
    mc "Of {i}course{/i}, Ty. If you'd asked me a couple years ago I probably would've said the same thing."
    show wolf underwear cry
    wolf "Thanks..."
    mc "Hey, Ty... Don't cry... It's alright..."
    show wolf underwear pout
    wolf "I'm... I'm not crying. Just something in my eyes is all."
    mc "I meant it though. Everything. If you need to go sort yourself out, I'll be here when you get back."
    show wolf underwear grin
    wolf "You better not need me to get that spot for you when I get back."
    "To emphasize his point he scratched between my shoulders at the point he was referring to."
    show wolf underwear smile
    wolf "Now come on. Your turn, brat."
    scene black with dissolve
    stop music fadeout 2.0
    "After I got my brushing in, Ty hit the lights and we got under the covers."
    "We lay there for a bit before he rolled me onto my side, an arm under my head and his other over my chest."
    "There wasn't anything left to say, I was comfortable and it felt right. It seemed that it was alright for him too based on what I was feeling under my tail."
    "I said nothing of it, wondering if he was going to make the first move but before too long he fell asleep and his breathing was level."
    "It wasn't like the other morning where he seemed to be having a bad dream. If anything, this seemed to be the opposite."
    "And I was glad."
    jump day10morning
    $ renpy.pause(3.0)
    "{color=f00}{b}TO BE CONTINUED: END OF DEMO{/b}{/color}"
    return
label Night9Sal:
    scene bedroom with dissolve
    "As I got changed into a pair of sleeping shorts, I checked my phone. Charged, undoing my mistake from the night before."
    "Rolling onto my back I started to flick through my apps, old photos, and messages."
    "Talking with Sal was bringing things back up, leaving a bitter taste in the back of my throat. I hovered over my voicemail again, contemplating listening to the message again before deflating."
    "With a sigh I dropped my phone next to me and shut off the lights before returning to bed and looking to get some sleep."
    stop audio fadeout 2.0
    scene black with dissolve
    play music vault fadein 2.0
    "I was restless, tossing and turning for what seemed like hours before I found myself awake again."
    scene bedroom with dissolve
    mc "Huh?"
    "I strained my ears to listen. I'd heard something, but I wasn't sure what."
    "As I went to look behind me I heard shuffling, the faintest creak coming from my bedroom door as it closed shut again."
    mc "W-Who's there?"
    show croc shirtless pout with dissolve
    "I peered over my shoulder and saw Sal standing awkwardly by the door. Not that it made me any less on edge, but he seemed to be fidgeting much like he was when I met him at the stairs."
    mc "Sal?"
    croc "Hello, yes, um... Sorry, I could go if that's better."
    "Sitting up now that I was much more awake than I wanted to be, I rubbed my eyes."
    mc "What time is it? What's wrong?"
    "He mumbled, shuffling on the spot."
    mc "Sal, if you're going to come into my room at least come over so I don't have to call out to you."
    "And so he did, shuffling closer."
    mc "So what was it you said?"
    croc "I'm... scared."
    "It wasn't the answer I was expecting and it made me blink. I wondered what it was specifically he was scared about, but he continued."
    croc "If... I sleepwalk, and something goes wrong."
    mc "Is that likely?"
    show croc shirtless sad
    croc "Well no, but..."
    croc "Can... I sleep with you?"
    mc "Uhh..."
    show croc shirtless pout
    croc "Sorry, I understand. Forget about it."
    if croclove >= 15:
        mc "No, wait."
        "I reached out for Sal as he turned to go."
        mc "Stay."
        show croc shirtless sad
        croc "Alright..."
    else:
        "He took a few steps away before turning fully, shoulders slumped."
        mc "Sal?"
        "Looking back at me, he looked tired, or stressed out about something."
        mc "Will... sleeping with me help?"
        show croc shirtless sad
        croc "I don't know... I just thought I'd ask. That's all."
        mc "Well... I can't just leave you in the lurch I guess..."
        show croc shirtless pout
        croc "It was silly of me to invite myself."
        mc "Maybe, but I'd much rather you have told me than something bad happening and me finding out in the morning so... Yeah. I guess it's fine."
    "Sal climbed onto the bed and sat there for a bit, seemingly mulling things over."
    play music calm fadein 2.0
    mc "Was it just trouble sleeping?"
    "He rubbed the back of his head, sighing out."
    show croc shirtless neutral
    croc "There are other things."
    show croc shirtless pout
    croc "But it's not really... important."
    mc "But it was important enough to come into my room in the middle of the night."
    show croc shirtless scared
    croc "Oh. Right, well..."
    show croc shirtless sad
    croc "True. Alright."
    show croc shirtless pout
    croc "I didn't... share too much today, did I?"
    croc "I feel like openly sharing what I did, or rather..."
    "He trailed off, glancing at me to see if I was going to fill in the blank for him. So I nodded, letting him continue."
    croc "Anyway...{w=0.5} I feel like doing {i}that{/i} may have affected me more than I thought it would."
    show croc shirtless sad
    croc "It's times like this that... I feel like it'd be nice to cry."
    show croc shirtless cry
    croc "But alas..."
    mc "You can't cry?"
    show croc shirtless sad
    croc "No. Physically, I can't cry. It seems like it'd be... nice."
    mc "Well... if it makes you feel better, I don't cry anymore."
    show croc shirtless sad
    croc "Do... hyenas grow out of the ability?"
    mc "Oh, no. It's less that and more... I guess I'm all cried out?"
    show croc shirtless pout
    croc "But what if... something bad happened? Would you cry then...?"
    mc "I hope so, but... maybe only so I'd feel normal. I get sad still, but it takes a lot to make me {i}that{/i} upset."
    croc "Like... if Orlando died. Or Roswell."
    mc "Those are... very specific guesses."
    show croc shirtless neutral
    croc "Really?"
    mc "I just assumed..."
    show croc shirtless pout
    croc "That I'd say Tyson? No, I feel like that's... more complicated. But Orlando and Roswell are your best friends, right?"
    mc "A-Ah... Well you see... um..."
    show croc shirtless neutral
    croc "Don't worry, I won't tell them. But honestly I think it's fine for you to have more than one."
    show croc shirtless pout
    croc "But still... I think I've just made myself sad and wondered if it'd help if I had someone nearby that'd... understand."
    croc "Orlando means well, but he's... A bit naïve. Too warm and happy to really understand."
    mc "Well thanks, I guess?"
    show croc shirtless scared
    croc "No, I didn't mean it like that."
    show croc shirtless pout
    croc "Just..."
    show croc shirtless neutral
    if croclove >= 15:
        show croc shirtless pout
        croc "You're more comfortable. Like a teddy bear."
        "I chuckled, nervous."
        mc "Do you mean comforting, or...?"
        show croc shirtless neutral
        croc "No, I was just thinking back to the other night."
        show croc shirtless pout
        croc "You're lighter. Softer. Better to cuddle with."
        show croc shirtless sad
        croc "I don't... want this to come across the wrong way, but I enjoyed the other night."
    else:
        show croc shirtless sad
        croc "There's a comfort in knowing someone can actually understand."
    show croc shirtless pout
    "Sal continued to sit there, once again keeping his gaze averted. I wondered if he wanted me to make the first move here, or just outright invite him into the bed."
    mc "Sal, did you..."
    menu:
        "...want to cuddle?":
            $ croclove += 1
            show croc shirtless sad
            croc "Perhaps..."
            croc "You... don't mind, do you?"
            mc "Not really. I like getting cuddles in. I'm all about the cuddling."
            show croc shirtless pout
            croc "So long as... you know that for me, you're not just someone to get cuddles from."
            mc "Would that be so bad?"
            croc "Well no. But... talking is probably better here."
            mc "We... could do both?"
            croc "Is... that okay?"
            croc "I... do like the cuddles as well. It helps regulate my body heat."
        "...want to talk more?":
            $ croclove += 2
            show croc shirtless neutral
            "He looked me over, curious."
            croc "Is that alright?"
            show croc shirtless sad
            croc "I know it's late, but... it'd be good to just talk things out."
            mc "It's probably not the best timing but... If you need it, I'll listen."
            croc "Can I... cuddle you?"
            "I felt my cheeks burn, making me chuckle slightly."
            mc "I... I guess so? I mean yeah, I'm fine with cuddles. Is that... normally something you like?"
            show croc shirtless pout
            croc "It helps regulate my body temperature. Just..."
    "I shifted across to make room next to me on the bed and Sal crawled over, slipping under the covers and sitting beside me for a few moments."
    show croc shirtless sad
    croc "Thank you..."
    "No sooner than he was under the covers did he yawn, rubbing his eyes much like I did when he woke me up."
    mc "Are you gonna be okay, Sal?"
    croc "Eventually. Likely come morning."
    mc "Is there anything I can do?"
    croc "No, no this is enough."
    show croc shirtless pout
    croc "Besides... it's only for tonight. Tomorrow... might be different. We'll see."
    mc "Well... Just let me know, alright? Maybe next time if you want some cuddle company, let me know before I fall asleep."
    show croc shirtless sad
    croc "Alright. Sorry. I understand."
    "Sal slipped further down the covers and held the blankets just under his chin. The beds were big, but with Sal's size he was already taking up most of the length."
    mc "Comfy?"
    show croc shirtless neutral
    "He rumbled in affirmation, shooting me a look, lifting up the blanket."
    mc "What are you doing?"
    show croc shirtless pout
    croc "Would you... um..."
    mc "Rub... your front?"
    show croc shirtless annoyed
    croc "No."
    mc "Then...?"
    show croc shirtless pout
    croc "Remember...? The other night?"
    mc "You want me... to sleep on you? Is that even comfortable?"
    croc "It's comfortable for me, if it was comfortable for you."
    "It was for sure a new experience. Sal was a lot bigger than anyone else I knew and being able to just use him as a mattress was... a new experience. Not a bad one, just different."
    "As I slid down under the covers I edged closer, nestling my head against his neck and throwing a leg over his waist. As if that wasn't enough, Sal snaked a hand under me, adjusting me so that I was more on top."
    scene black with dissolve
    stop music fadeout 2.0
    "He yawned again and patted my head carefully, prompting me to yawn in kind. Maybe it was just the fatigue catching up to me, but he was comfy."
    "Before I knew it, he was asleep, his whole body rising and falling in time with his breaths."
    "Why was Sal so hard to figure out? Sometimes it was like looking at a much bigger, scaly version of myself. Other times it was as if he was someone with so much more worldly experience."
    "Maybe it was because it seemed he was two people in one that made me confused?"
    "I nestled into his neck, listening to the faint thrumming coming from him as he slept."
    "It wasn't long until I too felt myself drift off fast asleep, my mind still racing trying to figure out the enigma I was sleeping on top of."
    jump day10morning
    $ renpy.pause(3.0)
    "{color=f00}{b}TO BE CONTINUED: END OF DEMO{/b}{/color}"
    return
label Night9Roswell:
    scene bedroom with dissolve
    "At some point I wandered off, figuring that I should get a shower in before whatever Roswell was planning."
    scene daveshower with dissolve
    "Maybe it was just the fact that the museum was a lot dustier than I gave it credit for, but once I stepped into the shower I felt the dirt and grime wash away the longer I stood there."
    "Or maybe it was the idea that Roswell put into my head about it being a potential date, and I found myself scrubbing myself a little bit harder than I normally would just to be sure."
    "After all, if you're going on a date, you may as well look your best."
    scene bedroom with dissolve
    "But was that a bit too presumptuous? Was it just a slip of the tongue?"
    "Even at the thought of tongues made me bring a hand to my mouth, remembering the fact that Roswell and I had kissed and if this was just another escalation from that. Would he be that bold?"
    "If we were just sleeping, I figured I'd throw on a pair of sleeping shorts and grab my toothbrush. I assumed there'd be some level of sharing a bed tonight so best to be prepared."
    scene bedroom
    show boar shirtless smile
    with fade
    "I wandered over to Roswell's room and found him sitting on the bed, checking his phone for something before waving me over."
    show boar shirtless neutral
    boar "[mcname]! I was wondering where you'd ended up!"
    mc "Just... y'know. Shower and junk."
    show boar shirtless smile
    boar "Well, speaking of, I was about to take one myself."
    "He patted some pajamas folded neatly next to him before bundling them up under an arm."
    boar "So... make yourself comfortable, and I shouldn't be too long."
    show boar shirtless grin
    boar "And if you find yourself getting a bit cold, feel free to borrow a shirt, [mcname]. Or use one of the spare blankets. Either works."
    hide boar with dissolve
    "Giggling to himself, he wandered into the bathroom to leave me with my thoughts."
    "Closing the door behind me and shuffling over to the bed, I looked around Roswell's room."
    "It seemed as though he hadn't gone through the effort to clean his room before I arrived, but that hardly mattered."
    "I took a load off by sitting on the bed, grabbing one of the spare blankets and draping it loosely over my head when a brief chill came over me."
    show boar shirtless smile with dissolve #replace with pajama sprite
    "Before too long, Roswell emerged from the bathroom, dressed ready for bed."
    boar "Sorry to keep you waiting! Ready to get this party underway?"
    "I gave him a look, gesturing to his room."
    mc "Looks like someone already had a party, and we weren't invited."
    show boar shirtless pout
    boar "Well... I can sorta change that."
    mc "By cleaning? Cause your room is a pigsty."
    boar "{i}Phrasing{/i}, [mcname]."
    mc "I mean it though! I don't know anyone else this messy!"
    show boar shirtless grin
    boar "Hey, busy room, busy mind. Or however the saying goes. Still, lemme just get the last thing to make this complete and we can get started."
    "I watched from the bed as Roswell started turning over his clothes strewn over the floor, bundling up into his arms bags of snacks and candy as if they were all tucked away for safekeeping."
    mc "Roswell..."
    show boar shirtless smile
    boar "Yes...?"
    mc "Did you deliberately hide things in your clothes or just...?"
    show boar shirtless laugh
    boar "Oh, no. Just where they ended up. But they're all new packets, so no need to worry about that."
    show boar shirtless neutral
    boar "Now..."
    scene slumberparty with dissolve
    "Roswell dropped everything on the bed and got comfortable opposite me, sitting among a nest of snacks."
    boar "{i}This{/i} is a party."
    mc "So we're just going to eat junk food?"
    boar "Yeah? And?"
    mc "I dunno..."
    "He looked around his snacks and unwrapped a lollipop, putting it into his mouth before passing me a cylindrical tube of chips."
    boar "You like these, right?"
    "I smirked, rubbing my thumbs across the label."
    mc "Thanks."
    boar "Aww... What's eating at you, [mcname]?"
    mc "I don't know how you can do it. Flipping between being fine with things one minute, and worried about them the next."
    boar "Maybe that's just one of my super powers?"
    mc "What I wouldn't give to have a super power of my own, y'know?"
    mc "It'd make things easier, that's for sure."
    boar "Are you really sure about that? I think you're plenty special without needing say... laser beam eyes."
    "I chuckled, smirking a little."
    mc "Yeah. Maybe."
    boar "I mean it! You're plenty special. That's one of the reasons I love you, [mcname]."
    "It didn't register immediately after he'd said it, but I did a double take after realizing what he said."
    mc "Did you just...?"
    boar "What?"
    mc "You love me?"
    boar "Well {i}yeah{/i}, obviously."
    mc "Isn't that... I mean... Is that why we kissed?"
    boar "Doesn't have to be."
    "I furrowed my brow, confused at what Roswell was getting at. Thankfully, he seemed to pick up on this and pulled the lollipop from his mouth to explain."
    boar "There... is a lot of different kinds of love. Paternal love, unrequited love, familial love..."
    "He grimaced, looking off to the side while he continued to think, a gesture I mimicked, opting to look instead at the tube of chips in my hands."
    boar "...fraternal love, romantic love, platonic love..."
    mc "Roswell..."
    boar "But then there's also unconditional love, obsessive love, love for sweets..."
    mc "{i}Roswell!{/i}"
    boar "What?"
    mc "What's the point you're trying to make?"
    boar "The point I'm trying to make is... Well, I know I love you, I just don't know where that falls just yet. But do I want to find out? Absolutely."
    boar "What that makes us in the mean time, I don't... really know."
    mc "What about the others? Orlando seems pretty keen on setting me up with Dean."
    boar "I think I'm fine with that. End of the day it's your call, and if by the time I figure it out and it's something more like romantic love? Well, that's just a shame for me."
    mc "But I don't want to... y'know, upset you."
    boar "And I'm not selfish to make you put your life on hold for me to figure it out. No one has time for that."
    boar "Make sense?"
    mc "Yeah... Yeah, I guess so. If I'm being honest, the whole... vault thing? It's really messing with my priorities."
    boar "No kidding.{w=0.2} But still..."
    boar "You really have to loosen up, [mcname]."
    stop audio fadeout 2.0
    scene bedroom
    show boar shirtless sad
    with dissolve
    "Roswell shook his head gently."
    play music calm fadein 2.0
    boar "As much as worrying about how I died is a thing, I feel like you need to maybe do some digging yourself."
    show boar shirtless scared
    boar "Sorry, was that... stepping over the line?"
    "With a sigh I shook my head."
    mc "No, you're probably right. It's been long enough."
    show boar shirtless sad
    boar "I just... miss the happy you, is all."
    mc "I know... Sorry, it's... Well you know enough about it, right?"
    boar "Right."
    show boar shirtless pout
    boar "But you {i}are{/i} working on it, right?"
    mc "...Slowly?"
    show boar shirtless annoyed
    boar "[mcname]."
    mc "I could be doing better. You're right."
    show boar shirtless sad
    boar "What am I going to do with you?"
    mc "He was important to me, Roswell. I can't just..."
    mc "What if I forget about him? What if I don't live up to his expectations?"
    "I deflated, hugging the blanket tighter around me."
    mc "Don't worry, you're not the only one that's told me that they miss the old me."
    "We sat in awkward silence for a while before I popped the lid on the tube I'd been given and tipped the contents unceremoniously into my mouth, half choking from how fast my mouth filled up."
    show boar shirtless smile
    "I munched and chomped, keeping my mouth full. There was something to be said about eating your troubles away, but maybe I just needed to indulge just this once and take a page out of Roswell's book."
    "No sooner had I swallowed, I reached for a bag of candy and Roswell joined in too; both of us ravenously devouring a large part of what he'd provided."
    scene black with dissolve
    stop music fadeout 2.0
    "At some point the sugar rush turned into a sugar crash and we passed out, half cuddled up together on the bed."
    "I felt as though I'd eaten too much, and I didn't brush my teeth, but I felt a little happier."
    "Happier enough that I considered it a win."
    jump day10morning
    $ renpy.pause(3.0)
    "{color=f00}{b}TO BE CONTINUED: END OF DEMO{/b}{/color}"
    return
label Night9Hoss:
    scene bedroom with dissolve
    "I grumbled to myself once I had the door to my room closed."
    "Why was Hoss so hard to figure out? Part of me wanted for it to be like the old days where he'd just rant about anime for a while and then go fix his mane. That was what I was used to."
    "But at the same time, it was nice seeing this more affectionate side of him. Maybe I was just used to it with Tyson, or Dean, but throwing Hoss into the mix too was fine."
    scene daveshower with dissolve
    "I jumped in the shower, thinking the hot water would do me some good. If anything it just made myself think things over more."
    "I liked Hoss, but did I like him {i}in that way?{/i}"
    if HossKiss == True:
        "I grimaced, remembering how he kissed me, half wanting him to do it again."
    else:
        "More importantly, did he like me back? Some of the things he'd said I was now second guessing, wondering if he had been dropping hints."
        "He was handsome enough, very handsome in fact. Then again it could just be because he was the one out of all of us that took care of his appearance and wardrobe."
    "Sighing out I rinsed myself and started getting dry."
    scene bedroom with dissolve
    "First a quick shake before grabbing the towel, then onto the blow drier."
    "Maybe it was just heat that was doing it. The longer I felt exposed to the comforting warmth the more I had to fight back my yawns."
    "Thoroughly clean I changed into some sleeping shorts and collapsed onto my bed, laying on my back and grabbing my phone."
    #NOTE: Count from here
    "I kept it plugged in though. No way I was going to let it run flat on me again."
    "Five minutes into playing games I heard a knock on my door."
    mc "Come in!"
    show lion neutral with dissolve
    "Hoss opened the door and entered soon after, closing the door behind him."
    mc "Oh, Hoss, what's up?"
    show lion smile
    lion "Just checking in."
    "I looked to the two mugs he had in his hands, confused."
    mc "With... two mugs?"
    show lion neutral
    lion "Figured you could use something to help you sleep, or relax a little."
    mc "It's not tea, is it?"
    "Hoss wandered a little bit closer and I sat up quickly as the scent hit my nose. Milky and sweet with those bitter tones that were all too familiar."
    mc "No, it's... Cocoa! Hot Chocolate!"
    show lion grin
    lion "Yup!"
    show lion smile
    lion "Consider it a peace offering given what I gave you this morning."
    "He handed over one of the mugs and I took it eagerly, looking down at the frothy liquid."
    mc "What'd you bribe Orlando with to make this?"
    "I was in the middle of counting how many marshmallows I had when Hoss replied, a sly grin on his face."
    show lion grin
    lion "Absolutely nothing. I made this myself."
    mc "Whoa, really?"
    show lion pout
    lion "Gee, thanks for the vote of confidence [mcname]. I'm able to do stuff in the kitchen too."
    show lion neutral
    lion "I might not be a gourmand like Orlando but I'm more than capable of putting a meal together and I've had plenty of practice making hot chocolate."
    "He took a sip from the mug he was carrying and sat down on the bed, looking between me and the mug I held."
    lion "Also, I got the impression that you liked it less on the sweeter side given how much you like coffee. I had Roswell telling me that the correct 'ratio' of marshmallows was ten and then start counting from there."
    mc "Ten!? That's... Well I guess that's on brand for Roswell at least given his sweet tooth."
    show lion smile
    lion "Right?"
    mc "Not that I mind, but... Why the peace offering in the first place? Did you do something wrong?"
    lion "Well no, but you've had a rough time of things from what I gather. Plus hot milk before bed sometimes helps me and my siblings sleep."
    mc "I'm guessing that's where you got your practice in?"
    "Part of me wanted to ask him if the cats and milk thing rang true here, but instead I opted to just drink from the mug to keep my mouth busy."
    show lion neutral
    lion "Right."
    lion "Besides, believe it or not I'm still trying to... y'know. Be less 'fake'?"
    mc "What do you mean? Is bringing me drinks less fake? I remember you brought us all that fancy drink one time that had the little marble in it."
    show lion pout
    lion "That was different."
    mc "Oh! And then the drinks you got us that had the little jelly things inside."
    show lion annoyed
    lion "That was...{w=0.5} also different!"
    show lion sad
    lion "I do more than bring you things to drink. I just thought you guys would like to try something different. Thankfully Orlando had my back there."
    mc "Then... what?"
    show lion neutral
    lion "So first let's tackle what you mean by fake. What I understood from that was that you wanted me to be less... who I felt I needed to be, and more who I am, right?"
    mc "Right. Like it feels like it's all an act just so you can be popular."
    show lion sad
    lion "Not too wrong I suppose. I wouldn't say 'popular' so much as just wanting to be liked."
    "I gave him a look, not convinced."
    mc "That kinda implies that you're a jerk, Hoss. But... I don't think you're {i}that{/i} bad. Even if you're a good actor."
    show lion smile
    lion "You think I'm a good actor?"
    mc "Well... You practice enough at least. But still, I don't think you should be trying to hard to be someone likable. Just be you."
    mc "The way I see it anyway, is that you must get tired being someone else all the time. And if people like you for the wrong reasons, isn't that bad?"
    show lion neutral
    lion "It makes sense, but begs the question why you know that."
    mc "It's come up a couple of times. Especially with Roswell and Orlando coming from families with a lot of money. More than what my parents made anyway."
    lion "So they thought you were just friends with them to get money?"
    "I nodded meekly. It wasn't the truth, I enjoyed spending time around them and didn't know how wealthy either of them were before we'd been hanging out for a while."
    "In retrospect, it made sense given what they brought for lunch or what presents they got for their birthdays, but I didn't really think anything of it."
    mc "What about you? Is this where I find out that I'm the only one in the anime club that didn't have a wealthy upbringing?"
    show lion laugh
    lion "No, my parents weren't wealthy. Sure, we won the lottery once but it wasn't first place."
    mc "Oh, so second place?"
    show lion smile
    lion "Try maybe eighth."
    show lion neutral
    lion "But as far as being less fake, I guess I'm just treating you like I would one of my siblings."
    if HossKiss == True:
        mc "But... The kiss?"
        lion "What about it?"
        mc "You kiss your siblings?"
        show lion laugh
        lion "Not like I did with you, mostly just on the forehead."
    else:
        mc "Like a little brother?"
        lion "Right."
        show lion sad
        lion "Which has its own problems."
        show lion neutral
        lion "You're cute, but a different kind of cute."
        mc "There are different kinds of cute?"
        if lionlove >= 12:
            lion "Right. There's little sibling cute, and then there's the kind of cute that makes me want to kiss you."
            mc "You want... to kiss me?"
            "He held my gaze for a moment, bringing his mug up to his mouth and drinking without breaking eye contact for a moment."
            lion "...I've thought about it."
        else:
            lion "Well maybe not different kinds of cute, but more... physical attraction."
            lion "Take you for instance. You're cute in the way that you're physically attractive, but also in similar ways to that of a younger brother."
            mc "You think I'm cute in... that way?"
            lion "Sure do."
        "I giggled slightly as I took another drink. Torn between keeping my eyes on the mug and sneaking peeks at Hoss, I wasn't sure what I should say to something like that."
        show lion laugh
        lion "Everything alright?"
    "I nodded slowly, wearing a broad grin."
    mc "Well... That's nice to know."
    show lion smile
    lion "But it wouldn't be a good idea to take me at my word you know."
    show lion neutral
    lion "I could always be just lying to you still."
    mc "Why would you say that?"
    lion "Because it's the truth. I {i}could{/i} be lying."
    mc "No, I mean... Why would you cast suspicion on yourself like that? Why would you raise that now?{w=0.5} {i}Especially{/i} when I'm as tired as I am."
    show lion smile
    lion "Maybe as a reminder to just stay safe, maybe as a hint."
    lion "Maybe..."
    mc "Maybe what?"
    "Hoss placed a hand over the top of my mug, easing it down and out of the way."
    if HossKiss == True:
        "He didn't answer even as he edged in forward, pressing his muzzle against mine to kiss me again. Just like he did in the library, but he didn't hold me this time."
        "I gasped as he played with my tongue, deepening the kiss just a little bit more."
        "But then he pulled away soon after, leaving me in a stupor as I breathed out a happy sigh."
    elif lionlove >= 12:
        $ HossKiss = True
        mc "Hoss...?"
        "He didn't break stride, leaning in and kissing me softly on the mouth. It didn't last more than a couple of seconds, but it was there."
        show lion aroused
        "As he eased off I stared at him, eyes wide and cheeks burning under my fur."
        lion "Maybe that actions speak louder than words sometimes."
        "I gulped, watching him settle back to where he was sitting before and taking another sip of his drink."
        "He watched as my hand went to my mouth, lightly touching the point of contact he held with his kiss. My {i}first{/i} kiss."
    else:
        "He sat up a little higher before planting a kiss atop my forehead."
        "I wondered why he eased my mug down if he wasn't going to kiss me on the mouth, but as he pulled away I leaned forward almost expecting a follow up."
        show lion aroused
        lion "Oh? What's this? Want a proper kiss?"
        mc "Well... I just assumed..."
        show lion grin
        "I chuckled along with him, although I imagine for very different reasons."
    "Hoss drummed his fingers against his mug, looking at me with a satisfied smile, watching as I composed myself."
    show lion neutral
    lion "If you take anything away from this, take that I trust you, [mcname]."
    lion "Whether or not you trust me, or trust that me trusting you is the truth, doesn't matter."
    "I blinked, a little lost."
    show lion sad
    lion "I feel like I keep shooting myself in the foot."
    mc "No, I... I think I get it."
    show lion neutral
    lion "Then good. Well, finish up your cocoa and I'll let you get some sleep."
    mc "Um... Hoss?"
    lion "Yes?"
    "Part of me wanted him to stay. The other part though was unsure if that was a good idea."
    "It was a question of whether I trusted him, right?"
    "Or was it just inappropriate to ask him to share a bed given everything that was going on?"
    mc "I..."
    $ HossAsked = False
    menu:
        "...want you to stay.":
            $ lionlove += 1
            $ HossAsked = True
            show lion scared
            lion "What...? You want..."
            "I nodded slowly."
            mc "If that's alright? Like..."
            mc "I guess I liked sleeping together? You smell nice, and are comfortable, and I dunno..."
            show lion laugh
            "Hoss laughed, shaking his head."
            lion "Well I'm glad you think so."
            show lion smile
            lion "But if you're asking me to spend the night, sorry to say but I can't tonight. Maybe tomorrow?"
            mc "You... can't?"
            show lion neutral
            lion "I've still got a few things I need to take care of, so I don't know how much longer I'll be up for."
            mc "What sort of things? You could always just join me after?"
            show lion laugh
            lion "In that case, bump that no up to a maybe. Careful about being too eager though otherwise I feel you might have something else in mind."
        "...hope you sleep well.":
            $ lionlove += 2
            show lion smile
            lion "And I hope you do too, [mcname]. You reckon you'll get a better night's sleep now?"
            mc "I hope so. The cocoa helped, so..."
            "My sentence was stopped short, a yawn finding me quickly."
            show lion laugh
            lion "I'll take it that the cocoa did its job then."
            show lion smile
            lion "Sometimes all it takes is just a good hot drink before bed.{w=0.5} One {i}without{/i} caffeine, anyway."
    "I finished off my cocoa and he offered out a hand to take the mug from me."
    show lion neutral
    lion "I'll hit the light on my way out if you want. You look comfy."
    mc "Thanks Hoss."
    show lion smile
    lion "Don't worry about it. I'll see you in the morning."
    scene black with dissolve
    stop audio fadeout 2.0
    "Sure enough he left, turning off the light before closing the door behind him. I rolled over and cuddled into my pillow, wondering what to make of Hoss."
    "I felt bad that I was questioning my friendship with him at the same time trying to figure out if he saw me as a little brother or something more."
    if HossKiss == True:
        "Obviously the kiss implied more, maybe. But with everything going on it was hard to say. Maybe he just wanted something casual, maybe it was just worth asking him directly what he wanted."
    else:
        "I don't think I'd mind either one so long as I just knew. There were enough things to figure out already without this adding to the mix."
        "It became clear that maybe the best thing to do would be to ask, be it as a friend or something more just so things were as clear as could be."
    "With another yawn I cuddled in closer to my pillow."
    "It was a job for tomorrow, anyway."
    jump day10morning
    $ renpy.pause(3.0)
    "{color=f00}{b}TO BE CONTINUED: END OF DEMO{/b}{/color}"
    return
label Night9Orlando:
    scene bedroom
    show dragon annoyed
    with dissolve
    mc "H-Hey!"
    "Orlando gently nudged me into my bedroom and closed the door behind us."
    mc "You didn't have to pull me up the stairs."
    dragon "You weren't putting up much of a struggle."
    "With his hands now off me, he looked me over and I looked back in kind. Whether it was the thoughts he'd put into my head or just the light I wasn't sure, but I found myself looking him over."
    "As I did I noticed things I didn't really think anything of before. The way he gently flexed his hand, the way the end of his tail twitched, even the roundness of his front that looked inviting to cuddle into."
    show dragon neutral
    "When my eyes came back up to look at him properly, he had a calm smile on his face. Almost as if we were having a wordless conversation about admiring how the other looked."
    "Then, snapping me out of it, he spoke plainly."
    dragon "So sex."
    "I blinked, shaking my head."
    mc "I... what? Sex? When?"
    show dragon laugh
    dragon "Oh boy, you are tired, huh?"
    mc "I... Hey!"
    "As Orlando chuckled to himself, I found myself following too although he was a lot more entertained than I was."
    show dragon neutral
    dragon "Alright, so... What sorta stuff have you done?"
    mc "You're going to ask me that bluntly?"
    dragon "No point beating around the bush, right?"
    mc "Well... nothing, really."
    show dragon annoyed
    "Orlando huffed, rubbing his head."
    dragon "Nothing at all?"
    mc "Not with anyone else, no."
    show dragon neutral
    dragon "But with yourself?"
    "I felt my cheeks burn under my fur, my tail tucking itself between my legs."
    mc "I... uh... y'know."
    dragon "Better question, you ever explore your body? See what sorta things you like?"
    mc "Not... really?"
    show dragon scared
    dragon "Not even a finger?"
    mc "I've... {i}thought{/i} about it? Does that count?"
    dragon "Oh dear. Alright, well... I didn't think we'd need to get into that much detail but still..."
    mc "Is that bad? I've looked up... stuff before, so I'm sorta ready I guess?"
    show dragon neutral
    dragon "Ready {i}how?{/i}"
    mc "Well... About how to prepare and stuff. I think I understand that much. So if anything was to maybe happen I could probably... y'know."
    dragon "Be ready for the next part?"
    mc "Right."
    show dragon pout
    dragon "Hrm..."
    "Orlando scratched his head, seemingly thinking something over. After the first minute, I figured to take control of the conversation."
    mc "As... much as I'd like to ask how better to prepare, something else has been bothering me."
    show dragon scared
    dragon "What is it?"
    mc "Well..."
    mc "It's mostly about you."
    dragon "Me?"
    show dragon sad
    mc "Yeah, um... Why don't we sit down."
    "I wandered over to the bed and sat down, with Orlando following close behind. As he sat down, I noticed he was playing with his hands."
    mc "So... How are you really? Like with the... um..."
    dragon "With... Oh."
    "Orlando sighed, shaking his head."
    dragon "This is about what happened with Sal, isn't it?"
    mc "Yeah... Like... You're looking out for me as far as setting me up with Dean, is there anything I can do to help uh... return the favor?"
    "He smirked for all of a second before his frown sat back in, looking at me briefly before focusing on his hands with his voice held low."
    dragon "No... Not really..."
    mc "Oh..."
    dragon "I think it's best that I heal a little bit first before attempting anything again, right?"
    mc "With Sal?"
    show dragon scared
    dragon "Oh. No. Not at all. That's something I don't want to go anywhere near anymore. Where Sal and I are at is... fine as it is."
    mc "Is there anyone else you like then? What about Hoss?"
    show dragon annoyed
    "As I looked to Orlando with an encouraging smile, it soon faded when I saw his expression. I didn't understand it, when it should've been quite obvious."
    dragon "Really?"
    mc "Really... what?"
    show dragon pout
    dragon "Don't worry about it."
    "As I went to talk, he put a hand on my shoulder."
    show dragon neutral
    dragon "Tell me, you like Dean, right? Like you actually like him?"
    mc "Come on, Orlando. Of course I do. I mean sure, dating has been hard given... Well, ever since dad... y'know."
    show dragon sad
    "Orlando nodded slowly, staying quiet."
    mc "But yeah, I like him. He's warm, and kind, a bit of a dork. I think we get on well?"
    show dragon smile
    dragon "Right, well... You're lucky. You like him, and he likes you obviously."
    mc "Sure, but... Why's that important? Was it not obvious?"
    show dragon neutral
    dragon "Not that. Just... ah..."
    "He patted me on the back shaking his head, laughing softly."
    dragon "It's not that important. I was just going to say that, sometimes when you like someone, it's better to just... let them go."
    mc "Let them go?"
    dragon "Like... don't pine over them? Give them their space. Don't force them to stay."
    mc "That sounds like Roswell. Like... He said something along those lines."
    show dragon scared
    dragon "He did?"
    mc "Yeah. Like... hoping someone else notices that they like him as much as he likes them? Something like that anyway."
    show dragon neutral
    dragon "Oh. Not like that. It's more like... uh..."
    dragon "Loving someone enough to let them freely go after someone else? Accept that all love is requited."
    mc "Oh..."
    "He held my gaze and I gulped, that feeling coming back. I felt conflicted."
    show dragon smile
    dragon "[mcname]? Um..."
    show dragon laugh
    dragon "Sorry, no, don't worry! I'll let you get some sleep now!"
    hide dragon with dissolve
    "Orlando hopped up off the bed and hurried towards the door."
    mc "Orlando! Wait!"
    "With his hand on the door handle, he froze still looking forward."
    "I followed him, stopping a few paces away feeling unsure of what just happened."
    show dragon sad with dissolve
    dragon "What's wrong?"
    mc "What's wrong with {i}you{/i}? You're acting real funny Orlando. What's wrong?"
    "Again his hands started to fidget, and his voice was quiet."
    dragon "Nothing's wrong..."
    mc "Orlando... Come on. Normally I'd get... I dunno, a hug or something?"
    show dragon pout
    dragon "Maybe... Maybe I'm a little jealous is all. It's just... working out for you and Dean, sort of. Or at least I'm going to be trying to help it work out."
    dragon "But for me? Not so much."
    mc "I'm sorry that... things didn't work out with Sal."
    "I gulped, trembling confused at what was happening, what I should be feeling versus what I was."
    "Still, Orlando wasn't leaving and I wondered if he was waiting for me to say something more, to maybe ask something else."
    menu:
        "Invite him to stay.":
            $ dragonlove += 1
            mc "Did... you want to stay?"
            show dragon scared
            dragon "What...?"
            mc "Yeah! Like... I dunno, we could do a sleepover? Maybe cuddle until you're feeling better?"
            show dragon pout
            dragon "I don't know, [mcname]... I don't think I'm feeling it tonight."
            mc "Come on! It'll be great! We can grab some snacks from downstairs and-"
            show dragon mad
            dragon "I said no."
            show dragon sad
            dragon "Just... No. Sorry, I..."
            mc "Did I do something wrong?"
        "Reassure him.":
            $ dragonlove += 2
            mc "Things... will work out, Orlando. Somehow."
            show dragon sad
            "I saw his shoulders slump, and as much as he could, he whined."
            mc "Is there... anything I can do? You can depend on me, too. Gotta pay you back somehow, right?"
    "Suddenly he stepped forward and hugged me tight, giving me a gentle squeeze."
    mc "Orlando...?"
    dragon "Thank you, [mcname]. You're sweet, but... I think I just need some space to myself for now."
    "As he stepped back, he kissed me gently on the cheek before turning and opening the door."
    hide dragon with dissolve
    "My hand went to my cheek, still sorta stunned as he disappeared out of my room, closing the door behind himself."
    scene black with dissolve
    "In a daze I turned the light off and wandered over to the bathroom."
    "I showered, and stumbling around in the dark afterwards I made it to bed enough to slide on a pair of sleeping shorts and cuddling up under the covers."
    "Something felt off, something was wrong about Orlando's behavior and my heart hurt not knowing how to best help."
    "If anything, I had more questions than I had answers. The worst of it was I was finding myself caring less and less about it in favor of just wanting Orlando to be okay."
    stop music fadeout 2.0
    "He'd been a great friend to me, and it was confusing me as to if I was just as good a friend back. I doubted it."
    "As I cuddled into my pillow I thought about Orlando, resolving myself to do better in the morning. I'd think of something to cheer him back up."
    jump day10morning
    $ renpy.pause(3.0)
    "{color=f00}{b}TO BE CONTINUED: END OF DEMO{/b}{/color}"
    return
label Night9Dean:
    scene bedroom with dissolve
    "I'd detoured to my room first to get myself some fresh clothes, plus a couple other things before heading to Dean's."
    "He still wasn't here, and it seemed as though there were still  a few clothes strewn about the floor rather than having been picked up."
    "I straightened up the bed and sat my pile of clothes near the end, heading towards the bathroom nervously."
    scene daveshower with dissolve
    "The water was nice, and it was enough to settle my nerves. Occasionally I'd look over my shoulder, half expecting Dean to invite himself into the shower too. It seemed like something he'd do anyway."
    "Then my mind started to wander."
    "Dean stepping into the shower behind me, putting his hands on my hips to hold me steady, then he'd probably say something flirty and given he'd be naked, well..."
    "I snuck a peek down and grumbled, realizing I'd quickly riled myself up. Running my hands through my fur I tried to distract myself by cleaning more thoroughly, keeping my hands above my waist."
    "After all, if I tended to myself now, Dean would probably be annoyed after hinting I might be interested in messing around. Then again, he'd probably respect my change of heart enough to not hold it against me."
    scene bedroom with dissolve
    "I stepped out of the bathroom with a towel around my waist. I'd given myself a quick blow dry too, so my fur was fluffy and soft. Dean liked that, right?"
    show bear underwear grin with dissolve
    bear "Well, well."
    "He was sitting on the bed, clad only in his underwear. He'd had a shower when we got in, if only because of his muddy feet needing addressing."
    bear "Nice and clean?"
    "I nodded quickly, shuffling closer."
    show bear underwear laugh
    bear "Up and down?{w=0.5} Inside and out?"
    "He laughed as I nodded again. I wasn't sure if he caught that I'd paid attention to that, but he kept his smile all the same."
    "His hands found my sides, just above the towel and he pulled me forward, pressing his nose against my belly and snuffling around."
    "It tickled, causing me to squirm as he kneaded my sides, hooking a thumb under my towel."
    show bear underwear aroused
    bear "You're only wearing a towel."
    mc "Y-Yeah... I thought, um..."
    show bear underwear grin
    bear "That you'll show me those stripes after all?"
    mc "Well... Maybe a look at least?"
    "I could feel myself getting hard, a small amount of panic forming in the pit of my stomach given how close Dean's chin was."
    "Dean rumbled, half a growl and half chuckle."
    bear "You're eager for this, huh?"
    mc "N-No... I'm just... Ah..."
    "One of Dean's hands wandered higher, cupping the side of my neck. He held his eyes on mine as he pulled away my towel with his other hand, leaving me exposed."
    show bear underwear aroused
    "If he looked down, he'd get an eye full for sure. I wasn't nearly as big as him downstairs, but he was bigger all over in general. Maybe that's why I felt so nervous."
    bear "You doing alright?"
    "Still his eyes were locked on mine, but I felt the hand that removed my towel start to wander lower if slightly to the base of my tail."
    mc "I... I think so..."
    "With his eyes still on mine, Dean stood before turning us around and easing me backwards onto the bed."
    "He was upon me again, kissing me firmly but gentle, coaxing my mouth open and using his tongue to deepen the kiss. I squeaked, gasping out as he pulled away."
    show bear underwear grin
    "That predatory grin made me feel small, but as I watched his eyes drop to look me over, I felt tucking my tail wasn't going to do much anymore. He'd seen it all."
    "His voice had that satisfied rumble to it, quiet without being a whisper."
    bear "Well, well..."
    "Next came a whistle of appreciation and I watched him look me over more thoroughly. When he reached my face, he wriggled his eyebrows at me upon catching my eye."
    "Out of instinct or something else, I don't know, my eyes dipped further down and saw just how riled up he was getting."
    "It was flattering if making me a little more nervous. He was as hard as I was, and it was only going to be a matter of time before something was going to happen."
    bear "Still all good, [mcname]?"
    mc "Y-Yeah... I think so."
    bear "Good. My turn, then?"
    mc "Your turn for what?"
    bear "Well..."
    "With another toothy grin he snapped the waistband of his underwear. I gulped, watching as once again his confidence soared over mine and he bent over slightly, sliding his underwear down."
    scene deandavefrot with dissolve
    "He kicked his underwear away, standing before me just as naked as I was."
    "Standing between my legs like that, Dean let his junk sit beside mine, dwarfing me in all aspects. No kidding that he was big, but having a direct comparison made me feel bad."
    bear "Hey... it's alright. Comes with being a bear."
    "My feelings must've shown through in my expression as he started to cop a feel of what I had, making me gasp."
    bear "Still... Don't know why you were so embarrassed of showing me your stripes before, handsome. You're beautiful."
    "He gave me a few strokes, hands slick from how much he was leaking before. It was different having someone else touch you like this, and it felt good."
    "I looked up at him and he was just watching my face shift as I enjoyed the attention. Dipping my eyes down for only a second to sneak another glance at his junk got me a non-verbal invitation from him to cop a feel."
    "It was warm and heavy, leaking right onto my fur making me wonder if I should've showered after this rather than before."
    bear "What's the matter?"
    mc "Just wondering why you leak so much. That, and thinking maybe I should've had a shower after we did this."
    "He laughed, patting me gently on the thigh."
    bear "It makes for good lube if all you're doing is tending to your own needs."
    mc "I suppose that must be handy."
    bear "Ha! {i}Handy{/i}, huh?"
    bear "Well, if you insist."
    mc "Wait, I didn't..."
    scene deandavehandjob with dissolve
    "Dean shifted his hips, pulling his dick away from my hand and setting it down on mine, taking both in his hand and slowly starting to pump them together."
    "His voice was held low, a satisfied smile on his face as stroke after stroke drew out soft moans from me."
    bear "Feels good, right?"
    "I nodded quickly, unsure of where to put my hands while Dean had everything handled. I adjusted my hips slightly, wrapping my legs around his waist for the time being."
    bear "Just lay back and enjoy, [mcname]."
    "He was getting me close fast, and I think my whimpers were giving it away. I hadn't had a chance to properly tend to myself with everything going on, as it was enough to kill your libido."
    "But even at the faintest thought of that being the case, what Dean was doing to me was drowning out all the worries I had been holding onto."
    mc "Dean..."
    bear "Yeah...?"
    mc "I'm getting close... So..."
    "There was that smile again, that lusty confident smirk that made me realize just how much I was putty in his hands. He eased back, bringing me down from my high and shifting us again."
    bear "Do you trust me?"
    mc "Y-Yes..."
    "He spat in his hand and dipped his spare hand underneath my tail, keeping his eyes on mine."
    bear "Don't worry, I'm gonna go gentle and slow. Just relax and if you're gonna cum, just go for it, alright?"
    "I nodded slowly, only half aware as to what he was getting at before he started pushing in."
    "Much like everything else on him, his fingers were thick, and as Dean started to push in I gasped out, hissing from the sudden intrusion."
    "But he stopped all the same, waiting for me to give him the go ahead to continue. All it took as a nod and he started back up with his strokes, easing more of his finger into me."
    bear "There you go..."
    "I had my eyes covered with an arm while my other was gripping the bedsheets. I was in sensory overload, right down to my toes curled up as Dean worked me over."
    "But then he hit something that made me gasp, drawing out a loud moan from me and making me shrink back down into the bed soon after in shame."
    bear "Did I just...? Well that's good to know..."
    "He chuckled, pressing against that spot again and drawing out another moan from me if slightly more controlled."
    bear "Feel good, handsome? Did I find your button?"
    "I whined as he continued rubbing and pressing it, bringing me closer and closer to climax faster than I could process."
    scene deandavehandjobclimax with dissolve
    "Before I could even get the words out, I was gritting my teeth as it hit, half bucking into Dean's hand as he let me ride out my orgasm. No sooner than I'd sighed out my breath, Dean quickly tended to himself, holding my gaze before adding to the mess on my front."
    "As much as I felt sticky and gross, I felt awesome. A dumb smile plastered on my face as I watched Dean retrieve the towel he'd shed from me and start the clean up on himself before putting his underwear back on."
    scene bedroom
    show bear underwear smile
    with dissolve
    bear "Feel better?"
    mc "Y-Yeah..."
    "I was out of breath, and if I wasn't conscious of how covered I was in the evidence of a good time I'd have rolled over and fallen asleep right then."
    "Dean helped me up and together we toweled me off."
    mc "I'm gonna need a shower in the morning, aren't I?"
    show bear underwear laugh
    bear "Sorry about that, but probably. Unless you wanted to rinse off now just to make sure you don't go around smelling like me tomorrow."
    show bear underwear aroused
    bear "Unless you want to."
    mc "I should probably rinse off, but depending on how much you drool tonight I might just need to shower again in the morning."
    "Dean placed his hands on my shoulders, looking at me seriously if happy."
    show bear underwear smile
    bear "How are you feeling otherwise though?"
    mc "Um... Good, I think. Maybe a little sore, but a good sore?"
    "I gingerly rubbed my butt, the idea that Dean had been able to do that to me still making my head spin."
    bear "Well good. You seemed to enjoy it."
    show bear underwear laugh
    bear "I know {i}I{/I} did!"
    mc "I did, yeah. Um..."
    show bear underwear neutral
    bear "What's wrong?"
    mc "Nothing really, just... wondering what happens next."
    bear "Sleep, depending on if you take that shower first or not."
    mc "Not that, I mean like... doing more of that stuff."
    bear "Well that's mostly up to you. I still reckon we're a ways off me getting under your tail proper though."
    show bear underwear grin
    "Dean smacked me firmly on the rear, holding his hand there."
    bear "But if that's what you want, we'll get there quickly, don't you worry about that."
    "I chuckled, feeling my face go red."
    mc "Well... So long as we take it slow, and have enough lube that should be fine, right?"
    "He leaned down and kissed me atop the head before stepping aside."
    show bear underwear smile
    bear "Go rinse off and I'll meet you in bed. If you wanna go for a round two then we can take it from there. Otherwise, let's just cuddle until we fall asleep."
    mc "A-alright..."
    scene black with dissolve
    stop audio fadeout 2.0
    "After a quick shower I rejoined Dean in bed, opting instead to just stay naked. He'd seen it all now so it seemed like the perfect night to try something different."
    "Having learned from the last time we shared a bed together, Dean seemed to only have a single light sheet covering us, but his body was warm enough to not need anything else."
    "We cuddled for a bit before I realized he fell asleep with his arms around me, cradling me close."
    "It took me a little longer, mind wandering about what we'd just done and if it was right, or what it meant moving forward. Not that I didn't enjoy it, perhaps it was just guilt that I was looking forward to the next time."
    "But eventually sleep found me, and I blacked out, nestled in against his broad chest."
    jump day10morning
    $ renpy.pause(3.0)
    "{color=f00}{b}TO BE CONTINUED: END OF DEMO{/b}{/color}"
return
