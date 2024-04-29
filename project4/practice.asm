/*Practice Code from class
4/29/2024
Session 9
*/

// Sets R2 to R0 + R1 +17
// @R0
// D=M

// @R1
// D=D+M // R1<- R0+ R1

// @17
// D=D+A // All added together in D

// @R2
// M=D // Store in R2

//---------------------------------------------

// if R0 >=0 then R1=1
// else R1=-1

// @R0
// D=M

// @TRUE
// D;JGE //D >=0

// @R1 // else
// M=-1
// // if false, skips TRUE label,
// // gets stuck in PAST label
// @PAST
// 0;JMP

// (TRUE)
//     @R1
//     M=1
// (PAST)
//     // allows for possible additional code

// (END)
//     @END
//     0;JMP

//---------------------------------------------

// if (R1 > R2) then R0=R1
// else              R0=R2

// Math
// @R1
// D=M

// @R2
// D=D-M // R1-R2
// // Jump? Look before you leap
// @THEN
// D;JLT

// // Else
// @R2
// D=M
// @R0
// M=D
// @END
// 0;JMP

// (THEN)
//     @R1
//     D=M
//     @R0
//     M=D

// (END)
//     @END
//     0;JMP

//---------------------------------------------
