1.Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.There is only one repeated number in nums, return this repeated number. Solve the problem using set.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
def find_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

# Input
l = input()
nums = list(map(int, l.split()))

# Output
print(find_duplicate(nums))

2.There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

Example 1:

Input: text = "hello world", brokenLetters = "ad"

Output: 

1

Explanation: We cannot type "world" because the 'd' key is broken.
a=input().lower()
b=input()
a=a.split()
c=0
for i in a:
    flag=0
    for j in i:
        if j in b:
            flag=1
            break
    if(flag==0):
        c+=1
print(c)

3.Write a program to eliminate the common elements in the given 2 arrays and print only the non-repeating

elements and the total number of such non-repeating elements.

Input Format:

The first line contains space-separated values, denoting the size of the two arrays in integer format respectively.

The next two lines contain the space-separated integer arrays to be compared.

Sample Input:

5 4

1 2 8 6 5

2 6 8 10

Sample Output:

1 5 10

3

Sample  Input: 

5 5

1 2 3 4 5

1 2 3 4 5

Sample Output:

NO SUCH ELEMENTS
def find_non_repeating_elements(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    unique_to_set1 = set1.difference(set2)
    unique_to_set2 = set2.difference(set1)
    non_repeating_elements = unique_to_set1.union(unique_to_set2)
    
    return non_repeating_elements
size1, size2 = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

non_repeating_elements = find_non_repeating_elements(arr1, arr2)
if non_repeating_elements:
    print(' '.join(map(str, sorted(non_repeating_elements))))
    print(len(non_repeating_elements))
else:
    print("NO SUCH ELEMENTS")

4.Coders here is a simple task for you, Given string str. Your task is to check whether it is a binary string or not by using python set.

Examples:  

Input: str = "01010101010"

Output: Yes



Input: str = "REC101"

Output: No
s=input()
l=len(s)
c=0
for i in s:
    if i in ('0','1'):
        c+=1
if(c==l):
    print("Yes")
else:
    print("No")

5.The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 def findRepeatedDnaSequences(s):
    if len(s) < 10:
        return []

    sequences = {}
    result = []

    for i in range(len(s) - 9):
        substring = s[i:i+10]
        if substring in sequences:
            sequences[substring] += 1
        else:
            sequences[substring] = 1

    for sequence, count in sequences.items():
        if count > 1:
            result.append(sequence)
    for i in result:
        print(i)

s1=input()

findRepeatedDnaSequences(s1)
