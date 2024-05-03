
# Timeline

1st todos:
Next time: work on editing the flashcards and try to read in a csv final and add the data to flash cards so hit a bottom and flashcards are made
Next time: edit the reading in a picture and then work on possibly working with a github repo to switch files over png to text, none of the github files I've found have worked


-------------------------------------------------------------------------------------------------------------------------------

May 2nd:

tyring to use this github library to analyze a picture
https://github.com/BoXiao123/simple-chinese-ocr-with-opencv

1st issue:
mxnet not installed

2nd issue: 
need a more deprecated version of mxnet
command: `pip3 install mxnet-mkl==1.6.0 numpy==1.23.1`
result: this fixed the problem

Issue:

todo: look more into removing an image background as a way to crop it
https://stackoverflow.com/questions/56501702/how-to-get-background-image-in-opencv-python
https://docs.opencv.org/3.4/d1/dc5/tutorial_background_subtraction.html

what is PIL - a resource

a_readin work: the picture isn't opening, resovle the size to find the max and height also find teh ratio of the sides to each other, can't crop a type numpy
https://docs.opencv.org/4.x/d6/d50/classcv_1_1Size__.html

trying to find where cv2 is installed so that I can add it to my pyproject.toml file, I want to use ruff format and addd more checks to the gator grade

search for cv2 and where it's installed
command: `apt search` + `opencv`
explain: there were lots of results for opencv and none for some other search queries

command: `pip show` + `numpy`
explain: numpy was the example and then it showed all the information about that package but I couldn't find the open cv because I don't know the exact name of it

-------------------------------------------------------------------------------------------------------------------------------


April 29th:
Run java script using node 
Run mneomsye - by just running that command

Looking into and exploring cv
Convo w obc - have to adapt and remodel the inkstone platform - this might be my comp
Right now for this portotype the plan is to take a file and to read it analyze it and make flashcards from it, or just work with reading the file and analyzing it. I could also use an online lanugae dictionary for this too
Notes and ideas from obc - object detector, detecting stuff in graphics, this is all a converstaion of how the computer relates/reads images, for this projedt obc said I can do something as basic as i can make somehting recognizes shapes in graphics, he also had the idea of working with google language translation api or something like that
Google search: basics of opn cv tutorial, youtube video on the basics: https://www.youtube.com/watch?v=-Ig2ibBkc7Q 
Reminder of sckritter and how it works


Open CV:
https://opencv.org/
Tutorials
Installing - did c build but not sure what that did
Cascade classifier - looks like the different character section/area boxes
Training it - https://docs.opencv.org/4.x/dc/d88/tutorial_traincascade.html
Might help with recognizing parts or strokes - https://docs.opencv.org/4.x/d1/dee/tutorial_introduction_to_pca.html
(and later idea but adding and translating to ios) - https://docs.opencv.org/4.x/d5/da3/tutorial_ios_install.html
Image processing module - https://docs.opencv.org/4.x/d7/da8/tutorial_table_of_content_imgproc.html

Extracting horizontal and vertical lines
Detecting objects (could be used for detecting strokes) - https://docs.opencv.org/4.x/da/ddc/tutorial_generalized_hough_ballard_guil.html

2d model features - https://docs.opencv.org/4.x/d9/d97/tutorial_table_of_content_features2d.html
Finding corners - i know there was talk about this in different articles - https://docs.opencv.org/4.x/d4/d7d/tutorial_harris_detector.html
More about finding corners - https://docs.opencv.org/4.x/d8/dd8/tutorial_good_features_to_track.html
Finding genreal feature detection - https://docs.opencv.org/4.x/d7/d66/tutorial_feature_detection.html
Finding an unknow part of a mostly seen object - https://docs.opencv.org/4.x/d7/dff/tutorial_feature_homography.html
(i wonder and I bet fuzzy matching of some kind could be used for this)
Detecting planar objects - https://docs.opencv.org/4.x/dd/dd4/tutorial_detection_of_planar_objects.html
*Detecting objects acrossing frames - i bet the svg could be frames and this could connet in some way to the users iput althought the users input is probably the next step - https://docs.opencv.org/4.x/dc/d16/tutorial_akaze_tracking.html 


Generagl google search: 
using opencv and chinese characters
Stack over flow on how to print chinese characters in open cv: https://stackoverflow.com/questions/50854235/how-to-draw-chinese-text-on-the-image-using-cv2-puttextcorrectly-pythonopen
*Github reop for taking an image and reading the english and chinese characters from it: https://github.com/BoXiao123/simple-chinese-ocr-with-opencv/blob/master/main.py
Adding chinese characters to an open cv image: http://eadst.com/blog/90
(Chinese video on open cv - fun how much i understand!! https://www.youtube.com/watch?v=QIZ2ssLixFQ)


Investigating simple flashcards: https://github.com/topics/flashcard-application
https://github.com/rh-id/a-flash-deck
XX https://github.com/mnemosyne-proj/mnemosyne?tab=readme-ov-file - much more complicated and involved application - open using the command mnemosyne in the terminal
https://github.com/jotron/StudyMD
https://github.com/thomas-huet/aleth - almost nothing - but a basic outline and website and I coudl take this and the basic formatting and connect the different webpages and use this as a jumping off platform - probably perfect to cobine with what ever I want my project to be
And ai generting flashcar platform - https://www.revisely.com/flashcard-generator - not very good but a good idea for what I want my idea to be and I could use all the different chinese textsbooks - I could look into whihc textbooks are most used in the us right now and then make platforms for them - this could be a cool way to organize and gather all materials that relate to the textsbooks too, like audio and video files etc
How to make my flashcards compatible with anki???

Bigger goal - making inkstone avaible - should be pretty easy if I could just add it to the new meteor and then run it, I think I might have to update the javascript too - imports are old version of writing them i think

-------------------------------------------------------------------------------------------------------------------------------

April 23rd: Reserach Plan:
articles on chinese detection online
R - Open CV
open source chinse dictionaires
*using ai/ml to mkae flashcards sets after uploading a language library
R - streamlit

-------------------------------------------------------------------------------------------------------------------------------

April 17th: need to update the inkstone repository to fit with a more modern version of meteor, the next step combine inkstone and a flashcard app

-------------------------------------------------------------------------------------------------------------------------------

April 10th: Worked on installing meteor and therefore inkstone. Bought materials--screen, and battery-- for in person prototype.

-------------------------------------------------------------------------------------------------------------------------------

March 27th: 3/27:
Google scholar search: using an lcd screen
Google scholar search: technology behind an interactive lcd screen
https://sid.onlinelibrary.wiley.com/doi/full/10.1002/jsid.106 - get instruction from the user, doing the following programming function and then report the according output
https://open.library.ubc.ca/soa/cIRcle/collections/undergraduateresearch/18861/items/1.0108409 - story of a interactive board being used on a college campus
Google scholar: chinese character learning technology
Open source learning platform: https://arxiv.org/abs/2009.11616, Github: https://github.com/HIT-SCIR/ltp 
3- *Article about tecniwues in learning chinese for people who are learning it as a second lanugage (CFL) chinese foreign language: https://commons.erau.edu/publication/1097/ 
1- *Using moblie applications to learn chinese as a second language: https://www.tandfonline.com/doi/full/10.1080/09523987.2014.968448
4- *Multimedia information technology(MIT) https://www.hindawi.com/journals/wcmc/2022/1758129/
2- *Using computers as a technology to help learn chinese: https://dl.acm.org/doi/abs/10.1145/3290607.3312813  
Google scholar search: programming interactive lcd screens like in ipods
Book: Designing Gestural Interfaces: Touchscreens and Interactive Devices 
5- *Swiping techniques on a screen https://www.diva-portal.org/smash/record.jsf?pid=diva2%3A578752&dswid=1796 
Book: Programming the Mobile Web: Reaching Users on iPhone, Android, BlackBerry … (cute book cover!!)
6- *Book: Designing for Small Screens (this looks like it would be useful)
Google scholar search: programming an app (articles about a app that you can program with think elementary school)
Google scholar search: learning chinese character online technology
1- *https://www.tandfonline.com/doi/full/10.1080/17501229.2018.1418633 - specefically stuff and tech that’s evolved for lerning outside of covid
2- * 6 tools for chinese learning https://digitalcommons.unl.edu/nebeducator/30/ 
3- * technology in chinese language learning http://eall.hawaii.edu/yao/TCSL08/TechnologyPaper.pdf
3- * https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0100987

Google search: taking apart an ipod
Watched videos on replaced in ipod nano 7th generation screen, working to reprogram my apple ipod nano 7

-------------------------------------------------------------------------------------------------------------------------------

March 22nd:
Video:
https://www.youtube.com/watch?v=SIo_Gv7K7Fo - how to create a simple touchscreen GUI, arduino lcd & touchscreen tutorial - this video talks about lcd theory, moslty theory making a simple build, simple project turning a light on and off using the touch screen
https://www.youtube.com/watch?v=D-zgtylBKUc - touch screen display for arduino, esp8266, and others: Nextion (nextion seems like a good platform, an online platform that you can preview the screen and practice different things) (this was a really helpful video)
https://www.youtube.com/watch?v=_GT_sgbKQrc - arduino touchscreen display - using a resistive touchscreen - 40min I didn’t watch the whole video or even most of it, I got a good grasp and concept from the other videos
https://www.youtube.com/watch?v=KZdJ31uwioM - 6 cool projects using arduino tft lcd display - uturning lights on - cool new information is that some of these projects use a phone and you call and number and based on phone screen the device will do different thigns.
https://www.youtube.com/watch?v=c_UtYkbjrQY - using dwin 7-inch tft lcd display with arduino to control relay - i didn’t watch this video

Then i started l looking into what is a microchip processor
And what is the difference bwtween a processor and a chip or something


-------------------------------------------------------------------------------------------------------------------------------

March 18th: devling into the watch idea
Watch plan:

Hardware:
Battery
Create the ciurcit boards
Screen to buy - touchable and interactable
Waveshare 2.8inch 320×240 Pixels IPS LCD with 4-Wire Resistive Touch Screen SPI Communication Interface - I like this spacing
https://www.adafruit.com/product/4520?gad_source=1&gclid=Cj0KCQjwhtWvBhD9ARIsAOP0GojQyftf2RXzHODiHM4ciFYGezrsm-AoWi9vXbq4Dc288KVz7yWMoFMaAmWlEALw_wcB - Adafruit 1.3" 240x240 Wide Angle IPS TFT Display

3d print a case
Speaker - bluetooth

Software:
Time
Flashcards
Google search: open source softenware flashcard app
Anki alternatives: https://alternativeto.net/software/anki/?license=opensource (download them on my phone and test them)
Ankidroid: https://alternativeto.net/software/ankidroid/about/
Mnemosyne: https://alternativeto.net/software/mnemosyne/about/
A video review of different flashcard apps: https://www.youtube.com/watch?v=KeT0tM8T-ZU
The github for https://scholarsome.com/: https://github.com/hwgilbert16/scholarsome 

Spotify
Chinese character writing
Google search: testing chinese stroker order open source programs
Github: https://github.com/chanind/hanzi-writer 
The website for it: https://hanziwriter.org/docs.html
The bellow one is the one I want to use
Github: https://github.com/skishore/makemeahanzi
The app: inkstone: https://www.skishore.me/inkstone/ 

Different ideas for platforms for my app/different types of applications: https://www.reddit.com/r/opensource/comments/14azw6d/an_open_source_flashcard_studying_system/

Up next:

https://www.youtube.com/watch?v=ypL5pNuwXSc, https://www.youtube.com/watch?v=H_yaO-nTucY 
ESP32 - wifi and bluetooth (I’m just looking for bluetooth) - arduino nano has no bluetooth or wifi, Raspberry Pi Pico - bluetooth and wifi, STM32 Series # - compatible with popular languages, Teensy, nRF5xxxx
Ki cad - resource - circuit board design
Fusion 360 - a case for the watch - a good resign - grade pro
Programming to the board
Checking funtionality usinga breadboard
Allpcb - to create the boards


Screen set up - https://circuitdigest.com/microcontroller-projects/designing-smartwatch-using-esp32

https://www.youtube.com/watch?v=7wAer7a3tU4 - Pcbs at home 
Pcb fabrication
R - eagle, prouyus, altshow


Bluetooth smart watch - https://www.hackster.io/architborkar9/bluetooth-smart-watch-arduino-afa813

https://www.hackster.io/news/arduino-bluetooth-smartwatch-with-android-notifications-3b52e6753043 - this project used a custom pcb and a ATmega328 chip

https://www.youtube.com/watch?v=yUwk7VrHki0 - watch using the esp32 - 
https://www.hackster.io/news/mutantw-is-an-esp32-powered-open-source-smartwatch-4bc6fc5018b1 - and the attached website
Looks just like and apple watch and usese an apple watch screen and equipment
https://www.hackster.io/news/there-is-finally-a-diy-smartwatch-worth-building-010c003a058d

https://www.youtube.com/watch?v=2GjM8qHWuds - a watch using arduino, and shows the app on the phone and how that part connects
https://technoreview85.com/make-arduino-smartwatch/ - the website for it
https://github.com/godstale/retrowatch - the software for it
https://www.youtube.com/watch?v=uvU8y3JzwWQ - Uploading code to the arduino pro mini using arduino uno, connects ground, pcc, txt to tx, etc

https://www.youtube.com/watch?v=xF_SR6aUKHg 
Open source smart watch, Wearables - 
A popular watch - pebble

https://www.youtube.com/watch?v=EkgdqwPfZx8 - very electrical knowleadgeable, and just made his pcb
Ambient light - controls the light automatically


Do more research with touchable screens

https://www.youtube.com/watch?v=FGf8WH5Je_Y - ipod nano 6th generation screen - what if i revampted this??

Code to an app: https://www.quora.com/How-do-I-convert-my-codes-to-a-programme-or-an-app 
Create an executable file: Once you are satisfied that your code works as expected, you can create an executable file. This file is what you will distribute to others who want to use your program or app.
Package your program or app: To distribute your program or app, you may need to package it appropriately. For example, if you're creating an iOS app, you'll need to package it into an IPA file.
Distribute your program or app: Once you have created an executable file and packaged your program or app, you can distribute it. You can distribute it through various methods, such as uploading it to an app store or sharing it through a website
Package and distribute your program or app: Finally, you'll need to package your program or app into a format that can be distributed to users. This might involve creating an installer, creating an executable file, or deploying your app to a web server or app store.
The specific steps and tools you'll need to use will vary depending on the programming language and platform you're working with. However, following these general steps can help you convert your code into a program or app that can be used by others.

https://www.reddit.com/r/Frontend/comments/pe2eay/how_to_turn_my_code_into_an_app/ - this is helpful and talks about the different kind of web applications and apps
Progressive web apps - https://web.dev/explore/progressive-web-apps
Electron - https://www.electronjs.org/ 
Cordova: https://cordova.apache.org/ 
Resource: create react app


-------------------------------------------------------------------------------------------------------------------------------

March 11th: 
Swift and app building
Installing swift: https://www.swift.org/install/linux/#installation-via-docker
Code academy - learning swfit: https://www.codecademy.com/courses/learn-swift/lessons/swift-hello-world/exercises/review (but this was going too slowly)

Google search: what is python swift client
Using w3schools to explore swift - much better fit: https://www.w3schools.in/swift/literals
Google search: download xcode for linux ubuntu → resources with different methods: https://www.baeldung.com/linux/xcode 

Smart watch
Google search: making your own smartwatch
One video: https://www.youtube.com/watch?v=1Pp5RGtFSrU
Resources from it: working witht he display: https://circuitdigest.com/microcontroller-projects/designing-smartwatch-using-esp32
Ambiant light and heart rate sensor: https://circuitdigest.com/microcontroller-projects/designing-a-smartwatch-part2-ambient-light-and-heart-rate-sensor-with-esp32
Pbc - a place to buy circuit boards: https://www.pcbway.com/?from=circuitdigest05

Building a smart watch part 1: https://www.youtube.com/watch?v=ypL5pNuwXSc 
Cutom smart watch part 2: https://www.youtube.com/watch?v=H_yaO-nTucY 
Resources to make cicuit boards - kicad - google serach: how to use kicad
Resource to design his 3-d printing - google search: fusion 360

Making a watch projector: https://www.youtube.com/watch?v=4PsfLFBdWEw 
Making an interactive watch projector: https://www.youtube.com/watch?v=gTnHEzshdIQ
