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

// do I want to use variables?
// LOOP
    // @KBD
    // D=M
    // if keypress==false (if D is == 0)
        // @WHITE
        // D;JEQ
    // if keypress==true (if D>0 or D!=0)
        // @BLACK
        // D;JGT or D;JNE
// WHITE
    // sumation for white screen
    // M=-1
    // goto LOOP
// BLACK
    // summation to black screen
    // M = 0 // is that right?
    // gotto LOOP
