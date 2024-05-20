# Project 4 - Fill and Multi

## Programmer Comments
### MULTI
5/17/2024 9:40 PM -- I finished it  in one try! I am really enjoying the assembly language! The program behaved appropriately if there were already values in the registers, if one of the values to be multiplied was zero, or if it was just regular multiplication! I'm very proud of it.  
### FILL
DATE?? TIME?? -- I will finish this project by Wednesday, May 14th  
DATE?? TIME?? -- I needed to update the date I finish the project, I had a roadbump  
DATE?? TIME?? -- UPDATE: I will finish the project on Friday, 5/17/24. Sorry for the continued delays. My fiance went out of town, and I needed to pick up a lot of the chores and animal care while he was gone, and I'm a bit behind now. I also started a new job! Thanks, Kevin, for all you do to keep my ship chugging along.   
DATE?? TIME?? -- Shoot looks like I'm going to need to tackle Fill tomorrow. Very sleepy.   
5/19/2024 10:16 PM -- Finished fill! Sam and I worked on the design together, then ended up combining our code to get a really smooth running fill. Here is a log of that conversation.  
TL;DR After testing Sam's code while running the animation, I noticed that the white summation fully runs if you did not hit a key fast enough while the code ran. We set it up to where the loops check for a keypress at the beginning of each iteration, creating a much smoother and responsive program!  
### Programmer Log
<pre>
evilfrogking — Today at 11:44 AM
have you done fill?
Sam — Today at 11:45 AM
I got distracted and was barely started it 😭 I'm looking at the week 5 videos for help
evilfrogking — Today at 11:48 AM
okay ahaha i feel that
i was thinking about doing two summations? I need to lock in and understand the screen stuff a bit more
Sam — Today at 11:55 AM
Hmmmmm lemme get far enough to where i can understand that 😭, would you be summing the pixles already filled to keep track of how much of the screen is filled?
evilfrogking — Today at 12:03 PM
hahaha thats a great questions
let me review the requirements a lil bit
so, there would be a loop that checks to see if a key is pressed
if not pressed, then the screen does a summation where it check to see if a key is pressed, and does a summation to fill the screen white
so like
(loop)
keypress?
if no
    start filling screen white
    @loop
if yes
    start filling screen black
    @loop
I assume if the key is lifted then it should start filling the screen white right after? like it doesnt complete the black fill screen?
Sam — Today at 12:08 PM
Maybe? I assumed the screen filling would be a process so fast that it would fill the whole thing almost instantly
evilfrogking — Today at 12:08 PM
i think there would maybe also need to be a restart function? for the summation stuff? so it needs to start at the beginning if there is a switch?
oh really?
i was thinking that it was going to be a visable change
huh if its near-instant then thats actually a lot easier
this was my first design thats more like that!
LOOP
    @KBD
    D=M
    // if keypress==false (if D is == 0)
    @WHITE
    D;JEQ
    // if keypress==true (if D>0 or D!=0)
    @BLACK
    D;JGT or D;JNE
WHITE
    // sumation for white screen
    // M=-1 // -1 == 1111111...1
    // goto LOOP
// BLACK
    // summation to black screen
    // M = 1 // is that right?
    // gotto LOOP
sumthin like that
this also needs to reset the variables but i think that could be done at the beginning of the loop
Sam — Today at 12:12 PM
:00000
evilfrogking — Today at 12:13 PM
does that make sense? im more nervous about this one than I was the multi one
but i have practed multipling on a CPU for like 2 years now so it was just writing it in assembly instead of hex so. it was actually nicer 
Sam — Today at 12:14 PM
Yeeee it makes sense!
I was thinking maybe we dont need a check for black though
evilfrogking — Today at 12:15 PM
😮 ?
Sam — Today at 12:15 PM
Like if we check for white, and we dont need to go to white, then maybe we can just continue on to black
evilfrogking — Today at 12:15 PM
but it turns black when the key is pressed? so it is automatically white
then we wouldnt need to check for white!
Sam — Today at 12:16 PM
:0 yaaaa thatd work
evilfrogking — Today at 12:22 PM
hells yea
i was planning on puttin this conversation in my readme to document my design process is that okay with you? i would be down for you to do it as well!
Sam — Today at 12:23 PM
Yeah sure!
evilfrogking — Today at 12:24 PM
oh and then we could reset the summation as a function at the top of the code? so at the end of loop it goes to (reset) which initializes the variables for the summation
------------------------------------------------------------------------
Sam — Today at 5:03 PM
I'm so close! just gotta write the function to turn the screen white
im thinking it's gonna be pretty similar to turning the screen black but just using 0s instead of -1s
evilfrogking — Today at 5:06 PM
yeah thats what I think! I was gonna do it after my calc homework, but I felt like i had a much better understanding after we talked it over
Sam — Today at 7:29 PM
hmmm might be more complicated? it only clears a little with that type of the design so far
my guess is that the zero is represented with less bits than -1 which is why a lot is left uncleared
I'll watch more of session 5 and see if he covers that
evilfrogking — Today at 7:35 PM
hm interesting
Image
Sam — Today at 7:36 PM
hmmmm maybe its the way I coded it then
im gonnna eat some dinner and get back to it, im hoping to finish by tonight tho
evilfrogking — Today at 7:37 PM
okay cool! Im working on it now
evilfrogking — Today at 7:42 PM
wait i think black is represented by 1?
Sam — Today at 7:44 PM
ya but -1 in signed binary is 1111 1111 1111...1111
(the blackscreen worked with -1 so im assuming it works by taking in single bits)
evilfrogking — Today at 7:47 PM
hm well fart hold on i thought i had that figured out earlier
evilfrogking — Today at 7:54 PM
im gonna try setting it up with black and white being written out and then maybe i can simplify from there
Sam — Today at 8:27 PM
:0 i think i got it
0 is valid
Sam — Today at 8:39 PM
omg
i got it 😭
I used the video for help and even with editing my code with his i couldnt get it work 😭 it was all cause of a silly error
I had a 0;JMP instead of a D;JEQ at one single point 😭 that was the reason it was only setting a few pixles back to white
😭 NOOOOOO
just tested it
it would have in fact worked with my early code it was just that one error
(LOOP)

    @position
    M=0

    @KBD
    D=M

    @KBD_PRESSED
    D;JNE

(NONE_PRESSED)
    //RESETS SCREEN BACK TO WHITE

    @SCREEN
    D=A //GET ADRESS OF SCREEN

    @position
    D=D+M // GET CURRENT POSITION TO RESET

    A=D //SET CURRENT POSITION
    M=0 //RESET SCREEN AT CURRENT POSITION 

    @24575 //LAST AVAIABLE MEMORY ADDRESS
    D=D-A

    @LOOP //IF AT LAST, LOOP BACK
    D;JEQ

    @position //UPDATE POSITION
    M=M+1

    @NONE_PRESSED //LOOP BACK FOR NEXT POSITION
    0;JMP

(KBD_PRESSED)
    //SETS SCREEN TO BLACK

    @SCREEN
    D=A //GET ADRESS OF SCREEN

    @position
    D=D+M //GET CURRENT POSITION TO FILL 

    A=D //SET THE CURRENT POSITION'S ADDRESS TO EDIT 
    M=-1 //FILL THE SCREEN AT CURRENT POSITION

    @24575 //LAST AVAIABLE MEMORY ADDRESS
    D=D-A

    @LOOP //IF LAST AVAIABLE IS REACHED GO BACK TO INTIAL LOOP 
    D;JEQ

    @position //UPDATE POSITION
    M=M+1

    @KBD_PRESSED //LOOP BACK FOR NEXT POSITION 
    0;JMP

(EXIT_LOOP)
This is what I got
evilfrogking — Today at 9:45 PM
Hey thats awesome!! I ran it, but if i didnt hit a key before it got through the loop, then the white summation runs, then you cant click a key to make it turn black
evilfrogking — Today at 9:55 PM
im trying to fix that, im p close
jospeh said we could work together this term, would you wanna just be collaborators?
Sam — Today at 9:56 PM
Sure!
evilfrogking — Today at 9:57 PM
siiick im p sure im almost done with that
is that (EXIT LOOP) something joseph does? I thought the program was supposed to be infinite
Sam — Today at 9:57 PM
Also I assumed the program ran fast enough that it wasn't an issue 😭 it passed the test but I think it could be fixed by moving the start of the loop to the main loop right?
Oh shoot thats just a byproduct of when I started it 😭
I set up my loops where I thought I'd need them
evilfrogking — Today at 9:58 PM
oh i havent been testing my code with the comparison file, ive just been running it and seeing if it did it correctly after a while hahah
Sam — Today at 9:59 PM
Lol that's fair, I only tested it that way when I thought i had something
evilfrogking — Today at 10:00 PM
that makes sense! hahah i didnt even realise there was a comparison file
okay im gonna run this really fast to see if that helps
i set up the end of the screen to be a variable also 
BOOM IT WORKS
Sam — Today at 10:03 PM
:00000
evilfrogking — Today at 10:03 PM
lemme do the comparison file, and I'll send it to you!
but if you hold down a key, it starts to fill black, and if you are not pressing a key it starts to fill white
Image
hm im getting an error with the comparision
but? it was running well when i did it without the comparision?
Sam — Today at 10:06 PM
ohhhh its the end of the RAM
evilfrogking — Today at 10:06 PM
https://codeshare.io/yNPJm9
Sam — Today at 10:07 PM
its why i have @24575 in my code, its the last adress we can physically access
evilfrogking — Today at 10:07 PM
hm but i made that into a variable? or maybe i messed that up somehow
oh! i might have seen this issue
Sam — Today at 10:08 PM
oooh
would d=d-a have to be changed to d=d-m?
evilfrogking — Today at 10:09 PM
yeah thats what im thinkin
im changin that right now
oh whoa this is the best ive ever seen it run
Sam — Today at 10:11 PM
:00000
its so much snappier!
evilfrogking — Today at 10:11 PM
oh hahahah i was running it "no animation"
no wonder it was taking me FOREVER to test
Sam — Today at 10:11 PM
😭
evilfrogking — Today at 10:12 PM
okay well! this is awesome!
Sam — Today at 10:12 PM
ngl I was wondering how you even noticed the error in my first one, for me it went so fast I didnt notice
but still im glad you changed it! this does feel faster and more responsive
evilfrogking — Today at 10:12 PM
testing with animation on was annoying but im glad i was doing it!
this is so awesome im def gonna add this finding in my readme
do you want to be added to my repo as a collaborator?
Sam — Today at 10:14 PM
oooh sure!
</pre>
