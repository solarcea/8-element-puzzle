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
   
![image](https://github.com/solarcea/8-element-puzzle/assets/165539627/70c0681c-2daf-49e3-a26c-d6d7e9ef2df5)

For example, if I rotate a valve X, it will affect elements:

![image](https://github.com/solarcea/8-element-puzzle/assets/165539627/3664920a-e1c7-4313-aefe-e935be774d54)

The start of the puzzle is always random, the elements 1, 2, 3, 4 are mixed up. The goal is to set them in the initial order.
