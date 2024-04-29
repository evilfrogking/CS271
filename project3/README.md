# Project 3
I finished this in one day!
I had the most trouble with the program counter.
It wasn't complicated, but getting my brain out of RAM land was hard.
I need to watch sessions 7 and 8 (and probably start project 4) before Monday!
I'll do those tomorrow :)
Yay!!
## Programmer Comments
Moved to README for convenience
### /a
### Bit.hdl
  // the two outs were tricky, but its just outing the same thing
  // under two different variables,
  // one as the actual out
  // and another as the input to the Mux
### PC.hdl
  // oof, i had to really switch up the ways ive been thinking for like 5 chips
  // http://nand2tetris-questions-and-answers-forum.52.s1.nabble.com/PC-Hdl-td4026543.html#a4029050
  // this helped a lot!
  // i get to the first diagram after i got stuck and tried to work from there
### RAM64.hdl
  // RAM8 only allows for 3 bit addresses
  // but this one takes in 6
  // so the addresses need to be divided somehow
  // address[0..2] and address[3..5]
  // but how should they be used?
### RAM8.hdl
  // I was scratching my head trying to figure out how to use 3 addresses
  // before realizing the address is 3 bits, not 3 different addresses
  // oops!
### Register.hdl
  // super easy!
  // these are a lot harder to check the tests for,
  // its not as simple as "test passed!"
  // because the clock goes on forever
### /b
### RAM16K.hdl
  // of COURSE this is the one I copy and paste so I can just edit the addresses
  // it wasnt a big deal
  // but my big clue should have been that 4k*8 does not equal 16k
