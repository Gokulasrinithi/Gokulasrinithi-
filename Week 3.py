3.1 Admission Eligibility
Write a program to find the eligibility of admission for a professional course based on the following criteria:
Marks in Maths >= 65
Marks in Physics >= 55
Marks in Chemistry >= 50
Or
Total in all three subjects >= 180
Sample Test Cases
Test Case 1
Input
70
60
80
Output 
The candidate is eligible
Test Case 2 
Input
50
80
80 
Output
The candidate is eligible
Test Case 3
Input
50
60
40
Output
The candidate is not eligible
For example:
Input	Result
50
80
80	The candidate is eligible

a=int(input())
b=int(input())
c=int(input())
if(a>=65 and b>=55 and c>=50):
    print("The candidate is eligible")
elif(a+b+c>=180):
    print("The candidate is eligible")
else:
    print("The candidate is not eligible")

 
























3.2
A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene. All three sides of an equilateral triangle have the same length. An isosceles triangle has two sides that are the same length, and a third side that is a different length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of the three sides of a triangle from the user. Then display a message that states the triangle’s type.
Sample Input 1
60
60
60
Sample Output 1
That's a equilateral triangle


For example:
Input	Result
40
40
80	That's a isosceles triangle
a=int(input())
b=int(input())
c=int(input())
if(a==b and b==c):
    print("That's a equilateral triangle")
elif(a!=b and b==c or a==b and b!=c):
    print("That's a isosceles triangle")
elif(a!=b and b!=c):
    print("That's a scalene triangle")

 



















3.3 				
					

Electricity Bill
Write a program to calculate and print the Electricity bill where the unit consumed by the user is given from test case. It prints the total amount the customer has to pay. The charge are as follows: 
Unit                                                     Charge / Unit
Upto 199                                             @1.20
200 and above but less than 400        @1.50
400 and above but less than 600        @1.80
600 and above                                    @2.00
If bill exceeds Rs.400 then a surcharge of 15% will be charged and the minimum bill should be of Rs.100/- 
Sample Test Cases
Test Case 1 
Input
50 
Output
100.00 
Test Case 2
Input 
300
Output 
517.50


For example:
Input	Result
500	1035.00

a=float(input())
b=0
if(a<=199):
    b=a*1.2
elif(200<=a<400):
    b=a*1.5
elif(400<=a<600):
    b=a*1.8
elif(a>600):
    b=a*2.0
if (int(b)<100):
    print("{:.2f}".format(100))
else:
    if(b>400.00):
        print("{:.2f}".format((b+(b*0.15))))
    else:
        print("{:.2f}".format(b))

 









3.4

IN/OUT
Ms. Sita, the faculty handling programming lab for you is very strict. Your seniors have told you that she will not allow you to enter the week's lab if you have not completed atleast half the number of problems given last week. Many of you didn't understand this statement and so they requested the good programmers from your batch to write a program to find whether a student will be allowed into a week's lab given the number of problems given last week and the number of problems solved by the student in that week.
 
Input Format: 
Input consists of 2 integers.
 The first integer corresponds to the number of problems given and the second integer corresponds to the number of problems solved.
 Output Format:
 Output consists of the string “IN” or “OUT”. 
 Sample Input and Output:
 Input
 8
 3
 Output
 OUT

For example:
Input	Result
8
3	OUT

a=int(input())
b=int(input())
c=(a/2)
if(c>b):
    print("OUT")
else:
    print("IN")

 



















3.5
In this exercise you will create a program that reads a letter of the alphabet from the user. If the user enters a, e, i, o or u then your program should display a message indicating that the entered letter is a vowel. If the user enters 'y' then your program should display a message indicating that sometimes y is a vowel, and sometimes y is a consonant. Otherwise your program should display a message indicating that the letter is a consonant.
Sample Input 1
i
Sample Output 1
It's a vowel.
Sample Input 2
y
Sample Output 2
Sometimes it's a vowel... Sometimes it's a consonant.
Sample Input3
c
Sample Output 3
It's a consonant.


For example:
Input	Result
y	Sometimes it's a vowel... Sometimes it's a consonant.
u	It's a vowel.
p	It's a consonant.

a=input()
if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
    print("It's a vowel.")
elif(a=='y'):
    print("Sometimes it's a vowel... Sometimes it's a consonant.")
else:
    print("It's a consonant.")
 























 
3.6

Leap Year
Most years have 365 days. However, the time required for the Earth to orbit the Sun is actually slightly more than that. As a result, an extra day, February 29, is included in some years to correct for this difference. Such years are referred to as leap years. The rules for determining whether or not a year is a leap year follow:
• Any year that is divisible by 400 is a leap year.
• Of the remaining years, any year that is divisible by 100 is not a leap year.
• Of the remaining years, any year that is divisible by 4 is a leap year.
• All other years are not leap years.
Write a program that reads a year from the user and displays a message indicating whether or not it is a leap year.
Sample Input 1
1900
Sample Output 1
1900 is not a leap year.
Sample Input 2
2000
Sample Output 2
2000 is a leap year.

year=int(input())
if(year%400==0):
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")
Month name to days
The length of a month varies from 28 to 31 days. In this exercise you will create a program that reads the name of a month from the user as a string. Then your program should display the number of days in that month. Display “28 or 29 days” for February so that leap years are addressed.


Sample Input 1
February
Sample Output 1
February has 28 or 29 days in it.
Sample Input 2
March
Sample Output 2
March has 31 days in it.
Sample Input 3
April
Sample Output 3
April has 30 days in it.
For example:
Input	Result
February	February has 28 or 29 days in it.
March	March has 31 days in it.


m=input()
if(m=="January"):
    print(m,"has 31 days in it.")
elif(m=="February"):
    print(m,"has 28 or 29 days in it.")
elif(m=="March"):
    print(m,"has 31 days in it.")
elif(m=="April"):
    print(m,"has 30 days in it.")
elif(m=="May"):
    print(m,"has 31 days in it.")
elif(m=="June"):
    print(m,"has 30 days in it.")
elif(m=="July"):
    print(m,"has 31 days in it.")
elif(m=="August"):
    print(m,"has 31 days in it.")
elif(m=="September"):
    print(m,"has 30 days in it.")
elif(m=="October"):
    print(m,"has 31 days in it.")
elif(m=="November"):
    print(m,"has 30 days in it.")
elif(m=="December"):
    print(m,"has 31 days in it.")

 















 
3.8

Pythagorean triple
Three numbers form a Pythagorean triple if the sum of squares of two numbers is equal to the square of the third.
For example, 3, 5 and 4 form a Pythagorean triple, since 3*3 + 4*4 = 25 = 5*5 
You are given three integers, a, b, and c. They need not be given in increasing order. If they form a Pythagorean triple, then print "Yes", otherwise, print "No". 
Sample Input
3
5
4
Sample Output
Yes

For example:
Input	Result
3
4
5	Yes


a=int(input())
b=int(input())
c=int(input())
if(a*a+b*b==c*c):
    print("yes")
elif(a*a+c*c==b*b):
    print("yes")
elif(c*c+b*b==a*a):
    print("yes")
else:
    print("no")
 







 


 
3.9

Second last digit
Write a program that returns the second last digit of the given number. Second last digit is being referred 10the digit in the tens place in the given number.
For example, if the given number is 197, the second last digit is 9.
Note1 - The second last digit should be returned as a positive number. i.e. if the given number is -197, the second last digit is 9.
Note2 - If the given number is a single digit number, then the second last digit does not exist. In such cases, the program should return -1. i.e. if the given number is 5, the second last digit should be returned as -1.
For example:
Input	Result
197	9

a=int(input())
b=str(abs(a))
l=len(b)
if(l>1):
    print(int(b[-2]))
else:
    print(-1)

 






 


 
Ex. No. 	: 	3.10 				Date: 27.03.2024
Register No.: 231501141					Name: Sailesh Rangaraj

Chinese Zodiac
The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is shown in the table below. The pattern repeats from there, with 2012 being another year of the dragon, and 1999 being another year of the hare.
Year Animal
2000 Dragon
2001 Snake
2002 Horse
2003 Sheep
2004 Monkey
2005 Rooster
2006 Dog
2007 Pig
2008 Rat
2009 Ox
2010 Tiger
2011 Hare
Write a program that reads a year from the user and displays the animal associated with that year. Your program should work correctly for any year greater than or equal to zero, not just the ones listed in the table.

Sample Input 1
2010
Sample Output 1
2010 is the year of the Tiger.
Sample Input 2
2020
Sample Output 2
2020 is the year of the Rat.


a=int(input())
b=a%100
c=b%12
if(c==0):
    print(a,"is the year of the Dragon.")
elif(c==1):
    print(a,"is the year of the Snake.")
elif(c==2):
    print(a,"is the year of the Horse.")
elif(c==3):
    print(a,"is the year of the Sheep.")
elif(c==4):
    print(a,"is the year of the Monkey.")
elif(c==5):
    print(a,"is the year of the Rooster.")
elif(c==6):
    print(a,"is the year of the Dog.")
elif(c==7):
    print(a,"is the year of the Pig.")
elif(c==8):
    print(a,"is the year of the Rat.")
elif(c==9):
    print(a,"is the year of the Ox.")
elif(c==10):
    print(a,"is the year of the Tiger.")
elif(c==11):
    print(a,"is the year of the Hare.")

 






 
 
 

 

















