# Computer Architecture/ Assembly Language Final Project - The Assembler
## Table of contents
1. [Assignment Instructions](https://www.nand2tetris.org/project06)
2. [Program Description](https://github.com/evilfrogking/CS271/blob/main/project6/README.md#program-description)
3. [Programmer Comments](https://github.com/evilfrogking/CS271/blob/main/project6/README.md#programmer-comments)


## Program Description
> hack_assembler.py is the Hack Assembler for Nand2Tetris's project 6. The program inputs an assembly file using the sys library, converts it to hack line by line, then writes it to a new hack file. That hack file can then be run on the provided CPU simulator.
> The pre-translated files are stored in their folders.
>
To compile:  
- Main program: python .\hack_assembler.py Prog.asm


## Programmer Comments
### Aspen
**6/8/24 10:55 PM --** Using Session 12, I set up the basic code for the Assembler using Python. Sam and I had discussed writing the Assembler in C++. However, I am looking to finish the term strong. While I enjoy coding in C++ more, I can get much more done quickly in Python. I set up the basics for the program and the README yesterday and today.  
**6/10/2024 10:56 PM—-** I really dug into the book and started my design today; I am going to work on coding more functional code tomorrow. I will probably move everything into a class, but we will see. I am very sleepy. Also, Sam is going to code his project in C++, and I will do mine in Python. We will compare the codes and help each other troubleshoot.  
**6/11/2024 5:34 PM --** I plan to finish the project today. I will turn it into a class, maybe two, and have those in separate files and then the main file. The way we set the parser up in class requires the file to be in the same folder, with no opportunity for searching a directory (or at least I don't know of one), but I don't mind that. I prefer to tackle some of those dangling issues in normal circumstances. But, I am ready to move on with the term since I am going to Costa Rica on the study-abroad trip. I need to start prepping for that and commencement. Whew, I am worn out. My design file is kinda a mess, but that's standard for me.  
**6/12/2024 12:55 AM --** Got the c instructions working! Now I need to do A instructions, worry about variables, label, and write it to a new file. I'm sure I'm going to be up late tonight.  
**6/12/2024 2:01 AM --** Finished testing files without symbols. time to include some symbols. Godspeed.  
**6/12/2024 4:58 AM--** Okay, so I ran into a weird issue. I was getting an extra leading zero on variables—not the first variable, but every variable after the first one. It wasn't present in the symbols table but would appear in the binary script at some point, so by the time it was written to the file, there would be an extra zero. I spent a long time trying to solve this and ended up writing a function to trim the extra zeroes.
As I was typing this, I was really unsatisfied with that solution. So, I went back and dug through the code again. I uncovered everything. I fixed it. Everything works. I need to clean things up and add documentation. I'm so happy.  
