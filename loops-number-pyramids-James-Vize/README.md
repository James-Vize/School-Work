# Lab: Number Pyramids

## Description

Write a program in Python that builds a number pyramid based on a given height.

Name your file "number_pyramid.py". Be sure that your output matches the example format exactly, including any spacing and punctuation.

**Bonus (+10)**

Modify the program to create an inverted pyramid below the original, as shown in the bonus output.

_Example runs:_

```
Enter the height of the pyramid: 2
 1
123
```

```
Enter the height of the pyramid: 4
   1
  123
 12345
1234567
```

Bonus:

```
Enter the height of the pyramid: 4
   1
  123
 12345
1234567
 12345
  123
   1
```

## Planning Tips

- You will need an outer loop to go through the rows, and two inner loops:
   - The first will print padding spaces, ' '. Note that each row has `total rows - current row` spaces padding the start...
   - The second will print the numbers for the current row. Note that each row has `row * 2 - 1` numbers in it...
- Remember that you can specify the end parameter for the `print` function so that it does not create a newline by passing in an `end=''` argument.

## Grading Tips
- Use appropriate comments and code style. 
- Check your program every time you make a change; don't wait until the end to test.
- Make use of the debugger to step through your code.
- Match the formatting from the example run exactly, including spacing and punctuation.
- Test all combinations of inputs that lead you through the various paths of the program.
- Make sure that your program doesn't crash - programs that don't run can't be graded!

