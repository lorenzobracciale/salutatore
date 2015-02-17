 _____       _              _ _   _____       _       _        _                 
 /  ___|     | |            (_) | /  ___|     | |     | |      | |                
 \ `--.  __ _| |_   _____    _| | \ `--.  __ _| |_   _| |_ __ _| |_ ___  _ __ ___ 
  `--. \/ _` | \ \ / / _ \  | | |  `--. \/ _` | | | | | __/ _` | __/ _ \| '__/ _ \
  /\__/ / (_| | |\ V / (_) | | | | /\__/ / (_| | | |_| | || (_| | || (_) | | |  __/
  \____/ \__,_|_| \_/ \___/  |_|_| \____/ \__,_|_|\__,_|\__\__,_|\__\___/|_|  \___|

!!!Under Contruction!!!

Salvo is a funny humanoid robot.

Salvo source code is composed by three main parts:
- Actions: for moving the head or speaking
- Triggers: when something happen call a function i.e. a callback
- Behaviours: classes with that implement those callbacks

== How to create new behaviours ==
Suppose you want Salvo speaks any new twitter.

- You need to add a TwitterTrigger class in the trigger directory (see for instance triggers/nfc.py). This should be a thread an periodically poll for new tweet, calling a callback and passing data (e.g. the list of the tweets) as argument.
- Then you should add a behaviour class in the behaviours dir and implement a callback method that accepts data as an argument. Then do whatever you want, for instance:
salvo.speak.say('New tweet') or salvo.head.raw_rotate(10, 44000, 'cw'). 
- The salvo instance is passed to your contructor and stored as behaviour attribute


                                                                                                                                                                    
