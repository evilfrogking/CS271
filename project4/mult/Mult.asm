// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

//SET UP
//Set Final to Zero
@2
M=0
//Set counter to Zero
@3
M=0

//INPUT SANITATION
//Conditions: If R0 or R1 is zero, then the program ends
@0
D=M
@END
D;JEQ

@1
D=M
@END
D;JEQ

(LOOP)
    //conditional jump?
    //if R3 ==- R0
        //jump to END
    @0
    D=M
    @3
    D=D-M // If R0-R3=0 then program end
    @END
    D;JEQ

    //add R1 to R2
    @1
    D=M
    @2
    D=D+M // R1 + R2
    M=D // put the result in R2

    //counter++
    @3
    M=M+1

    //unconditional jump to address where conditional jump starts
    @LOOP
    0;JMP

//end of program
(END)
    @END
    0;JMP



