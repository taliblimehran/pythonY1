### Round 1, exercise 3: Sales discount

Sales discount
--------------

#### This exercise is about the following topics:

*   Using a programming environment
*   Writing and running a simple program
*   Printing on the screen
*   Submitting the program for grading
*   Asking the user for input
*   Using variables
*   Simple arithmetic calculations

#### Initial preparations

Start PyCharm or another development environment if it is not already running. Create a new project named assignment1\_3. In this project, create a module named for example "sales\_discount" (the name of the module does not matter when submitting the exercise).

#### Description of the exercise

The customer is inquiring about the impact of discounts on product prices. Write a module called 'sales\_discount' that calculates the impact of the discount on the total price of the products, the price of individual products, and the amount of money saved.

#### Progression of the program

The program asks the user for the price of the product as a decimal number. Next, the program asks how many items of the product the customer is purchasing. After this, the program asks the user for the discount as a percentage. The quantity of products and the discount percentage are given as integers. The program calculates the total price of the products and the price of a single product after the discount, as well as the amount of money saved due to the discount. The program prints these values in euros.

The amount of money saved is calculated by subtracting the discounted total price from the total price without the discount.

#### Error handling

The program does not need to check the validity of the user input. You can assume that the user enters the price of the product as a positive decimal number, and the quantity of the products and the discount percentage as positive integers.

#### Output of the program

Make sure that your program's output matches the template below in terms of wording (letter sizes, line breaks, spaces, dots, commas, exclamation points, and question marks are not checked, even if they might be highlighted in the test feedback). The program doesn't need to (and should not) use formatting when printing numbers, but print the numbers as the print command defaults. Therefore, your program may print a different number of decimals for the numbers than the example runs. It doesn't matter.

#### Submitting

When you have written and saved your program, run it multiple times with different inputs, for example,

*   In PyCharm: right-click the code and click "Run 'module\_name'" (or: "Run File in Python Console")

and check that the program output is correct. When your program appears to work correctly, submit the file `sales_discount.py` to A+.

### Examples of the execution of the program:
```commandline
\[Execution of the program begins\]
Enter the price of the product:
5.5
Enter the number of the products:
3
Enter the discount percentage:
30
Price of the products after discount: 11.549999999999999
Price of one product after discount: 3.8499999999999996
You saved together 4.950000000000001 euros.
\[Execution of the program ends\]

\[Execution of the program begins\]
Enter the price of the product:
10.7
Enter the number of the products:
8
Enter the discount percentage:
15
Price of the products after discount: 72.75999999999999
Price of one product after discount: 9.094999999999999
You saved together 12.840000000000003 euros.
\[Execution of the program ends\]
```