# 8-element-puzzle

There is surely a way to find the pattern mathematically, but I just wanted to make a solution that would automize the actions of a real human - bruteforcing it until the solution is found.

The repository contains 3 files:
1. iqdam.py - it's the puzzle itself, but in the form of code. It can be played through the console.
2. iqdampuzzle.py - it's the solution of the puzzle in the form of code. It also contains the double-check algorithm that runs the found solution through the code of the first puzzle.
3. ui.py - this file visualizes the program by using the tkinter library.

There's a puzzle I've seen in a game that works by this logic:
1. Two pipes A and B exist in parallel.
2. Each pipe has 4 elements: 1, 2, 3, 4
3. Near the pipes, there are three valves: Z, X, C
4. A valve rotates 4 adjacent elements clockwise.

   The whole puzzle looks like this:
   
A: 1, 2, 3, 4

     Z  X  C 
     
B: 1, 2, 3, 4

For example, if I rotate a valve X, it will affect elements:

2, 3

  X
  
2, 3

And make them into this:
2, 2

  X
  
3, 3

The start of the puzzle is always random, the elements 1, 2, 3, 4 are mixed up. The goal is to set them in this order:

A: 1, 2, 3, 4

     Z  X  C 
     
B: 1, 2, 3, 4
