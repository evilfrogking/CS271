// Program: Sum1Ton (R0 represents N)
// Computes R1=1+2+3+.....+R0
// Usage: put a value >=1 in R0

// i=1
// sum=0
// LOOP:
//      if (i > R0) goto STOP
//      sum = sum + i
//      i = i+1
//      goto LOOP
// STOP:
//      R1= sum

// init
@i
M=1
@sum
M=0

// loop
(LOOP)
    // i<R0
    @i
    D=M
    @R0
    D=D-M
    // Exit
    @STOP
    D;JLT // Left Bounded Summation
    // SUM
    @sum
    D=M
    @i
    D=D+M // add sum and i together
    // put the value in sum
    @sum
    M=D
    //incr
    @i
    M=M+1
    // loop jump
    @LOOP
    0;JMP

(STOP)
    @sum
    D=M
    @R1
    M=D

(END)
    @END
    0;JMP
