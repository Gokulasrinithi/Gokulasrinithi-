1.Write a program to convert strings to an integer and float and display its type.
Sample Input:

10

10.9

Sample Output:

10,<class 'int'>

10.9,<class 'float'>
a=int(input())
b=float(input())
b=round(b,1)
print(a,type(a),sep=",")
print(b,type(b),sep=",")

2.Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of his basic salary, and his house rent allowance is 20% of his basic salary. Write a program to calculate his gross salary.
basic_salary=int(input())
dearance_allowance=0.4*basic_salary
rent_allowance=0.2*basic_salary
gross_salary=dearance_allowance+rent_allowance+basic_salary
print(int(gross_salary))

3.Write a simple python program to find the square root of a given floating point number. The output should be displayed with 3 decimal places.

Sample Input:

8.00

Sample Output:

2.828
import math
a=float(input())
b=math.sqrt(a)
print("%.3f"%b)

4.
Alfred buys an old scooter for Rs. X and spends Rs. Y on its repairs. If he sells the scooter for Rs. Z (Z>X+Y). Write a program to help Alfred to find his gain percent. Get all the above-mentioned values through the keyboard and find the gain percent.

Input Format:

The first line contains the Rs X

The second line contains Rs Y

The third line contains Rs Z

Sample Input:

10000

250

15000

Sample Output:

46.34 is the gain percent.
a=int(input())
b=int(input())
c=int(input())
x=a+b
y=c-x
z=y/x*100
print("%.2f is the gain percent."%z)

In many jurisdictions, a small deposit is added to drink containers to encourage people to recycle them. In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit and drink containers holding more than one liter have a $0.25 deposit. Write a program that reads the number of containers of each size(less and more)  from the user. Your program should continue by computing and displaying the refund that will be received for returning those containers. Format the output so that it includes a dollar sign and always displays exactly two decimal places.

Sample Input

10

20

Sample Output

Your total refund will be $6.00.

a=int(input())
b=int(input())
c=a*0.10
d=b*0.25
e=c+d
print("Your total refund will be $%.2f."%e)

5.In many jurisdictions, a small deposit is added to drink containers to encourage people to recycle them. In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit and drink containers holding more than one liter have a $0.25 deposit. Write a program that reads the number of containers of each size(less and more)  from the user. Your program should continue by computing and displaying the refund that will be received for returning those containers. Format the output so that it includes a dollar sign and always displays exactly two decimal places.

Sample Input

10

20

Sample Output

Your total refund will be $6.00.
a=int(input())
b=int(input())
c=a*0.10
d=b*0.25
e=c+d
print("Your total refund will be $%.2f."%e)


6.Justin is a carpenter who works on an hourly basis. He works in a company where he is paid Rs 50 for an hour on weekdays and Rs 80 for an hour on weekends. He works 10 hrs more on weekdays than weekends. If the salary paid for him is given, write a program to find the number of hours he has worked on weekdays and weekends.

Hint:

If the final result(hrs) are in -ve convert that to +ve using abs() function

The abs() function returns the absolute value of the given number.


number = -20
absolute_number = abs(number)
print(absolute_number)
# Output: 20

Sample Input:

450

Sample Output:

weekdays 10.38

weekend 0.38
a=int(input())
b=abs(a-500)/130
c=round(b,2)
d=round(b,2)+10
print("weekdays %.2f"%d)
print("weekend %.2f"%c)
