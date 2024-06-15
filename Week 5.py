1.String should contain only the words are not palindrome.

 

Sample Input 1

 

Malayalam is my mother tongue

 

Sample Output 1

 

is my mother tongue
a=input()
a=a.lower()
b=a.split()
l1=[]
for i in b:
    s=i[::-1]
    if(s==i):
        continue
    else:
        l1.append(i)
for i in l1:
    print(i,end=' ')

2.Find if a String2 is substring of String1. If it is, return the index of the first occurrence. else return -1.

Sample Input 1 

thistest123string

123

Sample Output 1 

8
a=input()
b=input()
if(a.find(b)==-1):
    print(-1)
else:
    print(a.find(b))

3.Assume that the given string has enough memory.

 

Don't use any extra space(IN-PLACE)

 

Sample Input 1

 

a2b4c6

 

Sample Output 1

 

aabbbbcccccc
s=input()
i=0
result=""
while i<len(s):
    if s[i].isalpha():
        char=s[i]
        i+=1
    else:
        c=0
        while i<len(s) and s[i].isdigit():
            c=c*10+int(s[i])
            i+=1
        result+=char*c
print(result)       

4.Write a python to read a sentence and print its longest word and its length


For example:

Input	Result
This is a sample text to test
sample
6
sentence = input()
longest_word = ""
max_length = 0
current_word = ""
for char in sentence:
    if char != " ":
        current_word += char
    else:
        if len(current_word) > max_length:
            longest_word = current_word
            max_length = len(current_word)
        current_word = ""
if len(current_word) > max_length:
    longest_word = current_word
    max_length = len(current_word)
print(longest_word)
print(max_length)

5.Consider the below words as key words and check the given input is key word or not.

keywords: {break, case, continue, default, defer, else, for, func, goto, if, map, range, return, struct, type, var}

Input format:

Take string as an input from stdin.

Output format:

Print the word is key word or not.

Example Input:

break

Output:

break is a keyword

Example Input:

IF

Output:

IF is not a keyword
keywords = {"break","case", "continue", "default","defer","else","for","func","goto","if","map","range","return","struct","type","var"}
a=input()
flag=0
for i in keywords:
    if(a==i):
        flag=1
        break
if(flag==1):
    print(a,"is a keyword")
else:
    print(a,"is not a keyword")

6.Given two Strings s1 and s2, remove all the characters from s1 which is present in s2.

 

Constraints

 

1<= string length <= 200

 

Sample Input 1

 

experience

enc

 

Sample Output 1

 

xpris
1 = input()
s2 = input()
result = ""
for char in s1:
    if char not in s2:
        result += char
print(result)

7.In this exercise, you will create a program that reads words from the user until the user enters a blank line. After the user enters a blank line your program should display each word entered by the user exactly once. The words should be displayed in the same order that they were first entered. For example, if the user enters:

first

second

first

third

second

then your program should display:

first

second

third
unique_words= set()
ordered_words =[]
while True:
    word=input().strip()
    if not word:
        break
    if word not in unique_words:
        unique_words.add(word)
        ordered_words.append(word)
for word in ordered_words:
    print(word)

8.Given a string S which is of the format USERNAME@DOMAIN.EXTENSION, the program must print the EXTENSION, DOMAIN, USERNAME in the reverse order.

Input Format:

The first line contains S.

Output Format:

The first line contains EXTENSION.
The second line contains DOMAIN.
The third line contains USERNAME.

Boundary Condition:

1 <= Length of S <= 100

Example Input/Output 1:

Input:

abcd@gmail.com

Output:

com
gmail
abcd 
s=input()
a=s.find('.')
for i in range(a+1,len(s)):
    print(s[i],end='')
b=s.find('@')
print('\n',end='')
for i in range(b+1,a):
    print(s[i],end='')
print('\n',end='')
for i in range(0,b):
    print(s[i],end='')

9.Given a string S, which contains several words, print the count C of the words whose length is atleast L. (You can include punctuation marks like comma, full stop also as part of the word length. Space alone must be ignored)

Input Format:

The first line contains S.
The second line contains L.

 

Output Format:

The first line contains C

Boundary Conditions:

2 <= Length of S <= 1000

Example Input/Output 1:

Input:

During and after Kenyattas inauguration police elsewhere in the capital, Nairobi, tried to stop the opposition from holding peaceful demonstrations.
5

Output:

13

Explanation:

The words of minimum length 5 are
During
after
Kenyattas
inauguration
police
elsewhere
capital,
Nairobi,
tried
opposition
holding
peaceful
demonstrations
S = input()
L = int(input())
words = S.split()
count = 0
for word in words:
    word_length = len(word.strip(",."))
    if word_length >= L:
        count += 1
print(count)

10.Write a python program to count all letters, digits, and special symbols respectively from a given string
input_string = input()
letter_count = 0
digit_count = 0
special_count = 0
for char in input_string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_count += 1
print(letter_count)
print(digit_count)
print(special_count)


