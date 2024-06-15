1.Mr.Ram has been given a problem kindly help him to solve it. The input of the program is either 0 or 1. IF 0 is the input he should display "C" if 1 is the input it should display "D".There is a constraint that Mr. Ram should use either logical operators or arithmetic operators to solve the problem, not anything else.

Hint:

Use ASCII values of C and D.

Input Format:

An integer x, 0<=x<=1. .

Output Format:

output a single character "C" or "D"depending on the value of x.

Input 1:
0
Output 1:
C


Input 2:
1

Output 1:
D
i=int(input())
if (i==0):
    print("C")
else:
    print("D")

2.Write a program that returns the last digit of the given number. Last digit is being referred to the least significant digit i.e. the digit in the ones (units) place in the given number.

The last digit should be returned as a positive number.

For example,

if the given number is 197, the last digit is 7

if the given number is -197, the last digit is 7
a=abs(int(input()))
b=a%10
print(b)

3.REC-OCATS-1
2
G2
CS23221-Python Programming Lab-2023 Batch
Dashboard
My courses
CS23221-PPL-2023
Operators and Formatting Output.
Week2_Coding
Started on	Tuesday, 26 March 2024, 11:37 AM
State	Finished
Completed on	Tuesday, 2 April 2024, 11:11 AM
Time taken	6 days 23 hours
Marks	19.00/19.00
Grade	100.00 out of 100.00
Question 1
Correct
Mark 1.00 out of 1.00
Flag question
Question text
Mr.Ram has been given a problem kindly help him to solve it. The input of the program is either 0 or 1. IF 0 is the input he should display "C" if 1 is the input it should display "D".There is a constraint that Mr. Ram should use either logical operators or arithmetic operators to solve the problem, not anything else.

Hint:

Use ASCII values of C and D.

Input Format:

An integer x, 0<=x<=1. .

Output Format:

output a single character "C" or "D"depending on the value of x.

Input 1:
0
Output 1:
C


Input 2:
1

Output 1:
D





For example:

Input	Result
0
C
Answer:(penalty regime: 0 %)
else:
    print("D")


Feedback
Input	Expected	Got	
0
C
C
1
D
D
Passed all tests!  

Correct
Marks for this submission: 1.00/1.00.
Question 2
Correct
Mark 1.00 out of 1.00
Flag question
Question text
Write a program that returns the last digit of the given number. Last digit is being referred to the least significant digit i.e. the digit in the ones (units) place in the given number.

The last digit should be returned as a positive number.

For example,

if the given number is 197, the last digit is 7

if the given number is -197, the last digit is 7



For example:

Input	Result
197
7
-197
7
Answer:(penalty regime: 0 %)
a=abs(int(input()))
b=a%10


Feedback
Input	Expected	Got	
197
7
7
-197
7
7
Passed all tests!  

Correct
Marks for this submission: 1.00/1.00.
Question 3
Correct
Mark 1.00 out of 1.00
Flag question
Question text
Note:

Dont use if-else. Operators alone must be used .



A team from the Rotract club had planned to conduct a rally to create awareness among the Coimbatore people to donate blood. They conducted the rally successfully. Many of the Coimbatore people realized it and came forward to donate their blood to nearby blood banks. The eligibility criteria for donating blood are people should be above or equal to 18 and his/ her weight should be above 40. There was a huge crowd and staff in the blood bank found it difficult to manage the crowd. So they decided to keep a system and ask the people to enter their age and weight in the system. If a person is eligible he/she will be allowed inside.

 Write a program and feed it to the system to find whether a person is eligible or not.

 Input Format:

 Input consists of two integers that correspond to the age and weight of a person respectively.

 Output Format:

 Display True(IF ELIGIBLE)

Display False (if not eligible)

Sample Input

19

45

Sample Output

True
age=int(input())
weight=int(input())
b=age>=18 and weight>40
print(b)

4.In the 1800s, the battle of Troy was led by Hercules. He was a superstitious person. He believed that his crew can win the battle only if the total count of the weapons in hand is in multiple of 3 and the soldiers are in an even number of count. Given the total number of weapons and the soldier's count, Find whether the battle can be won or not according to Hercules's belief. If the battle can be won print True otherwise print False.

Input format:

Line 1 has the total number of weapons

Line 2 has the total number of Soldiers.

Output  Format:

If the battle can be won print True otherwise print False.

Sample Input:

32

43

Sample Output:'

False
a=int(input())
b=int(input())
if (a%3==0) and (b%2==0):
    print("True")
else:
    print("False")

5.An online retailer sells two products: widgets and gizmos. Each widget weighs 75 grams. Each gizmo weighs 112 grams. Write a program that reads the number of widgets and the number of gizmos from the user. Then your program should compute and display the total weight of the parts.

Sample Input:

10

20

Sample Output:

The total weight of all these widgets and gizmos is 2990 grams.
a=int(input())
b=int(input())
a=a*75
b=b*112
c=a+b
print(f"The total weight of all these widgets and gizmos is {c} grams.")

6.In London, every year during Dasara there will be a very grand doll show. People try to invent new dolls of different varieties. The best-sold doll's creator will be awarded with a cash prize. So people broke their heads to create dolls innovatively. Knowing this competition, Mr.Lokpaul tried to create a doll that sings only when an even number is pressed and the number should not be zero and greater than 100.

 IF Lokpaul wins print true, otherwise false.

Sample Input

10

Sample Output

True

Explanation:

Since 10 is an even number and a number between 0 and 100, True is printed
a=int(input())
if (a%2==0) and (a<=100):
    print("True")
else:
    print("False")

7.The program that you create for this exercise will begin by reading the cost of a meal ordered at a restaurant from the user. Then your program will compute the tax and tip for the meal. Use your local tax rate (5 percent) when computing the amount of tax owing. Compute the tip as 18 percent of the meal amount (without the tax). The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip. Format the output so that all of the values are displayed using two decimal places.

Sample Input

100

Sample Output

The tax is 5.00 and the tip is 18.00, making the total 123.00
a=int(input())
b=0.05*a
c=0.18*a
d=a+b+c
print(f"The tax is {b:.2f} and the tip is {c:.2f}, making the total {d:.2f}")

8.Mr. X's birthday is in next month. This time he is planning to invite N of his friends. He wants to distribute some chocolates to all of his friends after the party. He went to a shop to buy a packet of chocolates. At the chocolate shop, 4 packets are there with different numbers of chocolates. He wants to buy such a packet which contains a number of chocolates, which can be distributed equally among all of his friends. Help Mr. X to buy such a packet.

 Input Given: 

N-No of friends

P1,P2,P3 AND P4-No of chocolates

OUTPUT:

 "True" if he can buy that packet and "False" if he can't buy that packet.

SAMPLE INPUT AND OUTPUT:

5

25

12  

10  

9

OUTPUT

True False True False
n=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if(a%n==0):
    print(True,end=' ')
else:
    print(False,end=' ')
if(b%n==0):
    print(True,end=' ')
else:
    print(False,end=' ')
if(c%n==0):
    print(True,end=' ')
else:
    print(False,end=' ')
if(d%n==0):
    print(True,end=' ')
else:
    print(True,end=' ')

9.Write a python program that takes a integer between 0 and 15 as input and displays the number of '1' s in its binary form.(Hint:use python bitwise operator.

Sample Input

3

Sample Output:

2

Explanation:

The binary representation of 3 is 011, hence there are 2 ones in it. so the output is 2.

a=int(input())
b=bin(a)
c=b.count("1")
print(c)

10.Pretend that you have just opened a new savings account that earns 4 percent interest per year. The interest that you earn is paid at the end of the year, and is added to the balance of the savings account. Write a program that begins by reading the amount of money deposited into the account from the user. Then your program should compute and display the amount in the savings account after 1, 2, and 3 years. Display each amount so that it is rounded to 2 decimal places. Sample Input: 10000 Sample Output: Balance as of end of Year 1: $10400.00. Balance as of end of Year 2: $10816.00. Balance as of end of Year 3: $11248.64.
a=int(input())
b=(0.04*a)
c=b+a
d=(0.04*c)+c
e=(0.04*d)+d
print(f"Balance as of end of Year 1: ${c:.2f}.")
print(f"Balance as of end of Year 2: ${d:.2f}.")
print(f"Balance as of end of Year 3: ${e:.2f}.")
