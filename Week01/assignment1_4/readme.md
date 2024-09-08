### Round 1, exercise 4: Oxygen consumption

Oxygen consumption
------------------

#### This exercise is about the following topics:

*   Using a programming environment
*   Writing and running a simple program
*   Printing on the screen
*   Asking the user for input
*   Using variables
*   Simple arithmetic calculations
*   Submitting the program for grading

#### Initial preparations

Create a new project in PyCharm or another IDE with the name assignment1\_4. In this project, create a module named for example "oxygen\_consumption" (the name of the module does not matter when submitting the exercise).

#### Background

In the Cooper test, a person runs the longest distance possible within 12 minutes. The result of the test is the distance run in meters. In this task, the oxygen consumption is calculated using the formula for [oxygen consumption](https://en.wikipedia.org/wiki/VO2_max) utilized by the American College of Sports Medicine.

#### Description of the exercise

The user wants to know their oxygen consumption during the Cooper test per minute per kilogram of body weight and per minute.

#### Progression of the program

The program asks the user for their Cooper test result in meters as an integer, and the user's body weight in kilograms as a decimal number. Next, the program calculates the user's oxygen consumption per minute per kilogram of body weight and per minute. Finally, the program prints the obtained results.

Oxygen consumption per kg body weight per minute is calculated as follows:

```py
Oxygen consumption = (0.2 \* result (m) / time (min)) + 3.5
```

In this case the time is 12.

#### Error handling

The program doesn't need to check anything in particular when it comes to correct user input. You can assume that the user gives a non-negative integer for the test result and a positive decimal for body weight.

#### Output of the program

Make sure that the program output matches the model output below (the letter case, line breaks, spaces, full stops, commas, exclamation points, or question marks are not checked even though they might be highlighted in the test feedback). The program should not use any formatting when printing the calculated values. Therefore, use the default print format of the print function. As a result, your program might print decimal numbers with a different level of precision compared to the example runs. This does not matter.

However, remember that the running distance in an integer, data type int and body weight is a decimal number, data type float.

#### Submitting

When you have written your program, run it with multiple different user inputs in PyCharm or another IDE and check that the output of the program is correct. For example,

*   In Pycharm: right-click your code and choose "Run module\_name" where module\_name is the name of the module (or "Run file in python console").

When your program seems to work as it should, submit the file `oxygen_consumption.py` to A+.

#### Example of the execution of the program:

```commandline
\[Execution of the program begins\]
Enter Cooper test result (m):
2400
Enter runner's body weight (kg):
64.5
Oxygen consumption per one minute and kilogram is 43.5 ml.
Oxygen consumption for the runner per one minute is 2805.75 ml.
\[Execution of the program ends\]
```

```commandline
\[Execution of the program begins\]
Enter Cooper test result (m):
3000
Enter runner's body weight (kg):
75.6
Oxygen consumption per one minute and kilogram is 53.5 ml.
Oxygen consumption for the runner per one minute is 4044.6 ml.
\[Execution of the program ends\]
```

**Color codes:**  
Blue: User input  
Green: Program output  
Red: Annotation: not printed