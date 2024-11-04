# Loop-Fun
Repetition structures programming project

The purpose of this assignment is to get some experience working with repetition structures (loops).

## Details

This program will allow you to get some practice using repetition structures (for and while loops).  It will consist of 4 parts.

Part 1 - Get two integer values (a box height and width) from the user.
- The box height should be between between 3 and 10 (inclusive).  If the user enters a number that is out of bounds (less than 3 or greater than 10), continue to prompt them until they enter an appropriate number (use a while loop).
- The box width should be greater than the height, but no larger than 20. If the user enters a number that is out of bounds (<= the box height or greater than 20), continue to prompt them until they enter an appropriate number (use a while loop).

Part 2 - Use a for loop to print out all the numbers (on one line, space delimited) between the 
height and width (inclusive), and then print the average (mean) of those numbers.  

Part 3 - Print a hollow box made of * as shown in the example below. (this could require multiple
loops or one loop and use of some formatting functions). The width and height of the box should be the values entered by the user in part 1.

Part 4 - Use nested loops to print out the triangular shape shown in the example below. The height will be the number entered for the box height.  The first row of the triangle is two asterisks, and each subsequent row should be two asterisks bigger than the previous row. (see example below)

## Sample Output

Output should look *exactly* like this output:

*Enter a box height(between 3 and 10): 2*

*That number is out of bounds: Try again: 5*

*Enter a box width between (6 and 20): 42*

*That number is out of bounds: Try again: 3*

*That number is out of bounds: Try again: 12* 

*The integers from 5 to 12 are:*

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; 5 6 7 8 9 10 11 12 

*and the average of those numbers is 8.5.*
```
************
*          *
*          *
*          *
************
```
```
**
****
******
********
**********
```

## Technical Details
* As with all programs written in this course, maintainability is as important as functionality, so your code should be clear and easy to follow. Make sure it follows the class coding conventions, and double check your code against this checklist before submitting.
* In the example above, the 6 is not a fixed value - it is because the user chose 5. If they had chosen 8, your program should have printed 9 as the lowest possible choice.
* The file *must* be named ```loop_fun.py```
* Copy the code I have given you in ```loop_fun.py```, located in the same repository, and put all of your code inside the ```main``` function.
* You must have a header at the top of your code in the following style
  
```
Name:
Date:
Assignment:
Description:
```

## Grading Details
* This project can be, and is intended to be, completed with tools that we have learned up to this point. Any use of programming concepts that have not been taught at this point will result in a 25% deduction. If you have any questions or doubts about this, it is your responsiblity to ask me before you submit the code.

## Submitting
When complete, submit the following in Google Classroom
- the source code (```loop_fun.py``` file)

