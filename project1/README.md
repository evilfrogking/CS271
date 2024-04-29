# Project 1
>Overall, I felt like there was a steep learning curve.  
>I told Sam:  
>"The chips kinda feel like looking a uniform
> Like, kinda alien and simple but hard to wrap my mind around? 
>and once you walk back from the more familiar way of looking at it, then, you can see how it makes sense. 
> It feels like learning binary all over again."  
## Programmer Comments
Moved to REAMDE for convienience. 
### And.hdl
    // failed first comparison, accidentally set b=a.
    // silly me
### Mux.hdl
    // I'm really proud I did this myself!
    // The more I work with this, the more it makes sense.
### Mux8Way16.hdl
    // I made a tree before I started making the chip!
    // I'm so happy, these are getting so much easier.
### Or.hdl
    // I'm getting messed up on the variables,
    // like when to use in=, a=. or b=
    
    // when a=0 and b=0, i keep getting an output of 1, which is wrong.
    
    // did it using Nand instead, not super happy with that though
    // Nand(a=a,b=a,out=nandA);
    // Nand(a=b,b=b,out=nandB);
    // Nand(a=nandA,b=nandB,out=out);
