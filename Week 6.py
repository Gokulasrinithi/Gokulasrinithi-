1.Determine the factors of a number (i.e., all positive integer values that evenly divide into a number) and then return the pth element of the list, sorted ascending. If there is no pth element, return 0.

Example

n = 20

p = 3

The factors of 20 in ascending order are {1, 2, 4, 5, 10, 20}. Using 1-based indexing, if p = 3, then 4 is returned. If p > 6, 0 would be returned.

Constraints

1 ≤ n ≤ 1015

1 ≤ p ≤ 109

The first line contains an integer n, the number to factor.

The second line contains an integer p, the 1-based index of the factor to return.

Sample Case 0

Sample Input 0

10

3

Sample Output 0

5

Explanation 0

Factoring n = 10 results in {1, 2, 5, 10}. Return the p = 3rd factor, 5, as the answer.

Sample Case 1

Sample Input 1

10

5

Sample Output 1

0

Explanation 1

Factoring n = 10 results in {1, 2, 5, 10}. There are only 4 factors and p = 5, therefore 0 is returned as the answer.

Sample Case 2

Sample Input 2

1

1

Sample Output 2

1

Explanation 2

Factoring n = 1 results in {1}. The p = 1st factor of 1 is returned as the answer.
  import math

a = int(input())
b = int(input())

factors = []

for i in range(1, int(math.sqrt(a)) + 1):
    if a % i == 0:
        factors.append(i)
        
        if i != a // i:
            factors.append(a // i)


factors.sort()

result = factors[b - 1] if b <= len(factors) else 0


print(result)

2.Find the intersection of two sorted arrays.

OR in other words,

Given 2 sorted arrays, find all the elements which occur in both the arrays.

Input Format

The first line contains T, the number of test cases. Following T lines contain:

1.      Line 1 contains N1, followed by N1 integers of the first array

2.      Line 2 contains N2, followed by N2 integers of the second array

Output Format

The intersection of the arrays in a single line

Example

Input:

1

3 10 17 57

6 2 7 10 15 57 246

Output:

10 57

Input:

1

7 

1 

2 

3 

3 

4 

5 

6

2 

1 

6

Output:

1 6
t=int(input())
n=int(input())
l1=list()
for i in range(n):
    a=int(input())
    l1.append(a)
m=int(input())
l2=list()
for i in range(m):
    b=int(input())
    l2.append(b)

for i in l1:
    if i in l2:
        print(i,end=' ')
    else:
        continue

3.Write a Python program to Zip two given lists of lists.

Input:

m : row size

n: column size

list1 and list 2 :  Two lists

Output

Zipped List : List which combined both list1 and list2

Sample test case

Sample input

2

2
1 

3

5

7
2

4

6

8
Sample Output

[[1, 3, 2, 4], [5, 7, 6, 8]]
m=int(input())
n=int(input())
list1=[m]*0
list2=[n]*0
for i in range(m):
    for j in range(n):
        list1.append(int(input()))
    for j in range(n):
        list2.append(int(input()))
print("[[",end="")
for i in range(m*n-1):
    print(list1[i],end=", ")
print(list1[m*n-1],end="")
print("], [",end="")
for i in range(m*n-1):
    print(list2[i],end=", ")
print(list2[m*n-1],end="]]")

4.Write a program to print all the locations at which a particular element (taken as input) is found in a list and also print the total number of times it occurs in the list. The location starts from 1.

 

For example, if there are 4 elements in the array:

 

5

6

5

7

 

If the element to search is 5 then the output will be:

 

5 is present at location 1

5 is present at location 3

5 is present 2 times in the array.

 

Sample Test Cases

 

Test Case 1

 

Input

 

4

5

6

5

7

5

 

Output

 

5 is present at location 1.

5 is present at location 3.

5 is present 2 times in the array.

 

Test Case 2

 

Input

 

5

67

80

45

97

100

50

 

Output

 

50 is not present in the array.

 n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

m= int(input())

locations = []
c= 0
for i in range(len(arr)):
    if arr[i] ==m:
        c += 1
        locations.append(i + 1)
        print(f"{m} is present at location {i + 1}.")

if c>0:
    print(f"{m} is present {c} times in the array.")
else:
    print(f"{m} is not present in the array.")

5.Complete the program to count frequency of each element of an array. Frequency of a particular element will be printed once.

 

Sample Test Cases

 

Test Case 1

 

Input

 

7

23

45

23

56

45

23

40

 

Output

 

23 occurs 3 times

45 occurs 2 times

56 occurs 1 times

40 occurs 1 times
arr = []

n = int(input())

for i in range(n):
    element = int(input())
    arr.append(element)

frequency = {}
for element in arr:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1


for element, count in frequency.items():
    print(f"{element} occurs {count} times")

6.Given two lists A and B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.

We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.

These lists A and B may contain duplicates. If there are multiple answers, output any of them.

For example, given

Input

5

12 28 46 32 50

50 12 32 46 28

Output

1 4 3 2 0

Explanation

A = [12, 28, 46, 32, 50]

B = [50, 12, 32, 46, 28]

We should return

[1, 4, 3, 2, 0]

as P[0] = 1 because the 0th element of A appears at B[1], and P[1] = 4 because the 1st element of A appears at B[4], and so on.

Note:

A, B have equal lengths in range [1, 100].
A[i], B[i] are integers in range [0, 10^5].
def anagram_mapping(A, B):
    # Create a dictionary to map elements of B to their indices
    index_map = {num: i for i, num in enumerate(B)}
    
    # Iterate over A and find the corresponding indices in B using the dictionary
    mapping = [index_map[num] for num in A]
    
    return mapping

# Input
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Output
print(*anagram_mapping(A, B))

7.Consider a program to insert an element / item in the sorted array. Complete the logic by filling up required code in editable section. Consider an array of size 10. The eleventh item is the data is to be inserted.

 

Sample Test Cases

 

Test Case 1

 

Input

 

1

3

4

5

6

7

8

9

10

11

2

 

Output

 

ITEM to be inserted:2

After insertion array is:

1

2

3

4

5

6

7

8

9

10

11

 


Test Case 2

 

Input

 

11

22

33

55

66

77

88

99

110

120

44

 

Output

 

ITEM to be inserted:44

After insertion array is:

11

22

33

44

55

66

77

88

99

110

120
x=[]
for i in range(0,11):
    b=int(input())
    x.append(b)
#a.sort()
print("ITEM to be inserted:",x[-1],sep='')
x.sort()
print("After insertion array is:")
for i in x:
    print(i)

8.Write a Python program to check if a given list is strictly increasing or not. Moreover, If removing only one element from the list results in a strictly increasing list, we still consider the list true

Input:

n : Number of elements

List1: List of values

Output

Print "True" if list is strictly increasing or decreasing else print "False"

Sample Test Case

Input

7

1

2

3

0

4

5

6

Output 

Truedef check_increasing_or_decreasing(lst):
    increasing = True
    decreasing = True
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            decreasing = False
        elif lst[i] < lst[i - 1]:
            increasing = False
    return increasing or decreasing

def check_strictly_increasing_with_removal(lst):
    for i in range(len(lst)):
        temp_lst = lst[:i] + lst[i+1:]
        if check_increasing_or_decreasing(temp_lst):
            return True
    return False


n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

if check_increasing_or_decreasing(lst) or check_strictly_increasing_with_removal(lst):
    print("True")
else:
    print("False")

9.Output is a merged array without duplicates.

Input Format

N1 - no of elements in array 1

Array elements for array 1

N2 - no of elements in array 2

Array elements for array2

Output Format

Display the merged array

Sample Input 1

5

1 

2 

3 

6 

9

4

2 

4 

5 

10

Sample Output 1

1 2 3 4 5 6 9 10
defmerge_arrays(array1, array2):
    merged = []
    i, j = 0, 0
    n1, n2 = len(array1), len(array2)
    
    # Merge both arrays while ensuring no duplicates and maintaining sorted order
    while i < n1 and j < n2:
        if array1[i] < array2[j]:
            if not merged or array1[i] != merged[-1]:  # Avoid duplicates
                merged.append(array1[i])
            i += 1
        elif array1[i] > array2[j]:
            if not merged or array2[j] != merged[-1]:  # Avoid duplicates
                merged.append(array2[j])
            j += 1
        else:
            if not merged or array1[i] != merged[-1]:  # Avoid duplicates
                merged.append(array1[i])
            i += 1
            j += 1
    
    # Append remaining elements from array1 (if any)
    while i < n1:
        if not merged or array1[i] != merged[-1]:  # Avoid duplicates
            merged.append(array1[i])
        i += 1
    
    # Append remaining elements from array2 (if any)
    while j < n2:
        if not merged or array2[j] != merged[-1]:  # Avoid duplicates
            merged.append(array2[j])
        j += 1
    
    return merged

# Main function to process input and output results
def main():
    # Input for array 1
    N1 = int(input())
    array1 = [int(input()) for _ in range(N1)]
    
    # Input for array 2
    N2 = int(input())
    array2 = [int(input()) for _ in range(N2)]
    
    # Merge the arrays and remove duplicates
    merged_result = merge_arrays(array1, array2)
    
    # Print the merged result
    print(' '.join(map(str, merged_result)))

# Run the main function
if __name__ == "__main__":
    main()

10.Program to print all the distinct elements in an array. Distinct elements are nothing but the unique (non-duplicate) elements present in the given array.

Input Format:

First line take an Integer input from stdin which is array length n.

Second line take n Integers which is inputs of array.

Output Format:

Print the Distinct Elements in Array in single line which is space Separated

Example Input:

5

1 

2 

2 

3 

4

Output:

1 2 3 4

Example Input:

6

1 

1 

2 

2 

3 

3

Output:

1 2 3
def print_distinct_elements(arr):
    distinct_elements = set(arr)
    print(" ".join(map(str, distinct_elements)))

# Input array length
n = int(input())

# Input array elements
arr = []
for _ in range(n):
    arr.append(int(input()))

# Print distinct elements
print_distinct_elements(arr)

