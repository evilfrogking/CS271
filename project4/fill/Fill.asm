// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// Sets the end of the screen as a variable for readability
@24575
D=A
@end
M=D

(LOOP)

    @position
    M=0

    @KBD
    D=M

    @KBD_PRESSED
    D;JNE

    @NONE_PRESSED
    D;JEQ

(NONE_PRESSED)
    //RESETS SCREEN BACK TO WHITE
    @KBD
    D=M
    @LOOP
    D;JNE // if a key is pressed during the loop, goes to loop

    @SCREEN
    D=A //GET ADRESS OF SCREEN

    @position
    D=D+M // GET CURRENT POSITION TO RESET

    A=D //SET CURRENT POSITION
    M=0 //RESET SCREEN AT CURRENT POSITION 

    @end
    D=D-M

    @LOOP //IF AT LAST, LOOP BACK
    D;JEQ

    @position //UPDATE POSITION
    M=M+1

    @NONE_PRESSED //LOOP BACK FOR NEXT POSITION
    0;JMP

(KBD_PRESSED)
    //SETS SCREEN TO BLACK
    @KBD
    D=M
    @LOOP
    D;JEQ // if a key is not pressed during the loop, goes to loop

    @SCREEN
    D=A //GET ADRESS OF SCREEN

    @position
    D=D+M //GET CURRENT POSITION TO FILL 

    A=D //SET THE CURRENT POSITION'S ADDRESS TO EDIT 
    M=-1 //FILL THE SCREEN AT CURRENT POSITION

    @end
    D=D-M

    @LOOP //IF LAST AVAIABLE IS REACHED GO BACK TO INTIAL LOOP 
    D;JEQ

    @position //UPDATE POSITION
    M=M+1

    @KBD_PRESSED //LOOP BACK FOR NEXT POSITION 
    0;JMP

