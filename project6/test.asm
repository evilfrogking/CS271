
// Sets R2 to R0 + R1 +17
@i
M=1
@sum
M=0

@R0
D=M

@R1
D=D+M // R1<- R0+ R1

@17
D=D+A // All added together in D

@R2
M=D // Store in R2
