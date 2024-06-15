1.Write a code to check whether product of digits at even places is divisible by sum of digits

at odd place of a positive integer.

Input Format:

Take an input integer from stdin.

Output Format:

Print TRUE or FALSE.

Example Input:

1256

Output:

TRUE

Example Input:

1595

Output:

FALSE
def productDigits(n):
    a=n
    temp=[]
    list1=[]
    list2=[]
    rem=0
    while a!=0:
        rem=a%10
        temp.append(rem)
        a=a//10
    for i in range(len(temp)):
        if (i+1)%2==0:
            list1.append(temp[i])
        else:
            list2.append(temp[i])
    pro=1
    sum=0
    for i in list1:
        sum+=i
    for i in list2:
        pro*=i
    if pro%sum==0:
        return True
    else:
        return False

2.complete function to implement coin change making problem i.e. finding the minimum

number of coins of certain denominations that add up to given amount of money.

The only available coins are of values 1, 2, 3, 4

Input Format:

Integer input from stdin.

Output Format:

return the minimum number of coins required to meet the given target.

Example Input:

16

Output:

4

Explanation:

We need only 4 coins of value 4 each

Example Input:

25

Output:

7

Explanation:

We need 6 coins of 4 value, and 1 coin of 1 value
def coinChange(n):
    a=n//4
    b=n%4
    c=a+b
    return c

3.Given a number with maximum of 100 digits as input, find the difference between the sum

of odd and even position digits.

Input Format:

Take a number in the form of String from stdin.

Output Format:

Print the difference between sum of even and odd digits

Example input:

1453

Output:

1

Explanation:

Here, sum of even digits is 4 + 3 = 7

sum of odd digits is 1 + 5 = 6.

Difference is 1.

Note that we are always taking absolute difference

def differenceSum(n):
    a=n
    b=0
    lst=[]
    while(a!=0):
        b=a%10
        lst.append(b)
        a=a//10
    lst2=lst[::-1]
    c=1
    e=0
    o=0
    for i in lst2:
        if(c%2!=0):
            o=o+i
        else:
            e=e+i
        c=c+1
    return e-o

4.An automorphic number is a number whose square ends with the number itself.

For example, 5 is an automorphic number because 5*5 =25. The last digit is 5 which same

as the given number.

If the number is not valid, it should display “Invalid input”.

If it is an automorphic number display “Automorphic” else display “Not Automorphic”.

Input Format:

Take a Integer from Stdin Output Format: Print Automorphic if given number is Automorphic number,otherwise Not Automorphic Example input: 5 Output: Automorphic Example input: 25 Output: Automorphic Example input: 7 Output: Not Automorphic

def automorphic(n):
    a=n*n
    s=a%10
    if s==n:
        return "Automorphic"
    else:
        return "Not Automorphic"

5.REC-OCATS-1
2
G2
CS23221-Python Programming Lab-2023 Batch
Dashboard
My courses
CS23221-PPL-2023
Functions: Built-in functions, User-defined functions, Recursive functions
Week9_Coding
Started on	Saturday, 1 June 2024, 12:02 PM
State	Finished
Completed on	Saturday, 1 June 2024, 12:07 PM
Time taken	4 mins 27 secs
Marks	5.00/5.00
Grade	100.00 out of 100.00
Question 1
Correct
Mark 1.00 out of 1.00
Flag question
Question text
Write a code to check whether product of digits at even places is divisible by sum of digits

at odd place of a positive integer.

Input Format:

Take an input integer from stdin.

Output Format:

Print TRUE or FALSE.

Example Input:

1256

Output:

TRUE

Example Input:

1595

Output:

FALSE

For example:

Test	Result
print(productDigits(1256))
True
print(productDigits(1595))
False
Answer:(penalty regime: 0 %)

def productDigits(n):


 
Feedback
Test	Expected	Got	
print(productDigits(1256))
True
True
print(productDigits(1595))
False
False
Passed all tests!  

Correct
Marks for this submission: 1.00/1.00.
Question 2
Correct
Mark 1.00 out of 1.00
Flag question
Question text
complete function to implement coin change making problem i.e. finding the minimum

number of coins of certain denominations that add up to given amount of money.

The only available coins are of values 1, 2, 3, 4

Input Format:

Integer input from stdin.

Output Format:

return the minimum number of coins required to meet the given target.

Example Input:

16

Output:

4

Explanation:

We need only 4 coins of value 4 each

Example Input:

25

Output:

7

Explanation:

We need 6 coins of 4 value, and 1 coin of 1 value

Answer:(penalty regime: 0 %)
def coinChange(n):
    a=n//4


Feedback
Test	Expected	Got	
print(coinChange(16))
4
4
Passed all tests!  

Correct
Marks for this submission: 1.00/1.00.
Question 3
Correct
Mark 1.00 out of 1.00
Flag question
Question text
Given a number with maximum of 100 digits as input, find the difference between the sum

of odd and even position digits.

Input Format:

Take a number in the form of String from stdin.

Output Format:

Print the difference between sum of even and odd digits

Example input:

1453

Output:

1

Explanation:

Here, sum of even digits is 4 + 3 = 7

sum of odd digits is 1 + 5 = 6.

Difference is 1.

Note that we are always taking absolute difference

Answer:(penalty regime: 0 %)

def differenceSum(n):


Feedback
Test	Expected	Got	
print(differenceSum(1453))
1
1
Passed all tests!  

Correct
Marks for this submission: 1.00/1.00.
Question 4
Correct
Mark 1.00 out of 1.00
Flag question
Question text
An automorphic number is a number whose square ends with the number itself.

For example, 5 is an automorphic number because 5*5 =25. The last digit is 5 which same

as the given number.

If the number is not valid, it should display “Invalid input”.

If it is an automorphic number display “Automorphic” else display “Not Automorphic”.

Input Format:

Take a Integer from Stdin Output Format: Print Automorphic if given number is Automorphic number,otherwise Not Automorphic Example input: 5 Output: Automorphic Example input: 25 Output: Automorphic Example input: 7 Output: Not Automorphic

For example:

Test	Result
print(automorphic(5))
Automorphic
Answer:(penalty regime: 0 %)

def automorphic(n):
Feedback
Test	Expected	Got	
print(automorphic(5))
Automorphic
Automorphic
print(automorphic(7))
Not Automorphic
Not Automorphic
Passed all tests!  

Correct
Marks for this submission: 1.00/1.00.
Question 5
Correct
Mark 1.00 out of 1.00
Flag question
Question text
An abundant number is a number for which the sum of its proper divisors is greater than

the number itself. Proper divisors of the number are those that are strictly lesser than the number.

Input Format:

Take input an integer from stdin

Output Format:

Return Yes if given number is Abundant. Otherwise, print No

Example input:

12

Output:

Yes

Explanation

The proper divisors of 12 are: 1, 2, 3, 4, 6, whose sum is 1 + 2 + 3 + 4 + 6 = 16. Since sum of

proper divisors is greater than the given number, 12 is an abundant number.

Example input:

13

Output:

No

Explanation

The proper divisors of 13 is: 1, whose sum is 1. Since sum of proper divisors is not greater

than the given number, 13 is not an abundance
    def abundant(n):
    lst=[]
    a=n
    b=0
    c=n
    while(a!=0):
        b+=1
        a=int(a/10)
    sum=0
    for i in range(1,c):
        if(c%i==0):
            sum+=i
    if(sum>n):
        return "Yes"
    else:
        return "No"    


                        
    
    
