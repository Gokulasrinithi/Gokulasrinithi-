1.To find the frequency of numbers in a list and display in sorted order.

Constraints: 

1<=n, arr[i]<=100 

Input: 

1 68 79 4 90 68 1 4 5 

output:

 1 2

 4 2

 5 1

 68 2

 79 1 

90 1
list=[int(x) for x in input().split()]
temp=[]
for i in list:
    if i not in temp:
        temp.append(i)
temp.sort()
list1=[0]*1000
for i in list:
    list1[i]+=1
for i in temp:
    print(i,list1[i])

2.Write a Python program to sort a list of elements using the merge sort algorithm.
n=int(input())
a=[int(x) for x in input().split()]
a.sort()
for i in a:
    print(i,end=" ")

3.Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order. You read an list of numbers. You need to arrange the elements in ascending order and print the result. The sorting should be done using bubble sort.

Input Format: The first line reads the number of elements in the array. The second line reads the array elements one by one.


Output Format: The output should be a sorted list.
      def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Input
n = int(input())
arr = list(map(int, input().split()))

# Sort the array using bubble sort
bubble_sort(arr)

# Output the sorted array
print(*arr)

4.Given an listof integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

1.      List is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.

2.      First Element: firstElement, the  first element in the sorted list.

3.      Last Element: lastElement, the last element in the sorted list.

For example, given a worst-case but small array to sort: a=[6,4,1]. It took  3 swaps to sort the array. Output would be

Array is sorted in 3 swaps.  
First Element: 1  
Last Element: 6   
Input Format

The first line contains an integer,n , the size of the list a .
The second line contains  n,  space-separated integers a[i].

Constraints

·         2<=n<=600

·         1<=a[i]<=2x106.

Output Format

You must print the following three lines of output:

1.      List is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.

2.      First Element: firstElement, the  first element in the sorted list.

3.      Last Element: lastElement, the last element in the sorted list.

Sample Input 0

3

1 2 3

Sample Output 0

List is sorted in 0 swaps.

First Element: 1

Last Element: 3
n=int(input())
a=[int(x) for x in input().split()]
swap=0
temp=0
for i in range(0,n):
    for j in range(0,i):
        if i!=j:
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                swap+=1
print("List is sorted in",swap+1,"swaps.")
print("First Element:",min(a))
print("Last Element:",max(a))

5.An list contains N numbers and you want to determine whether two of the numbers sum to a given number K. For example, if the input is 8, 4, 1, 6 and K is 10, the answer is yes (4 and 6). A number may be used twice.

Input Format

The first line contains a single integer n , the length of list

The second line contains n space-separated integers, list[i].

The third line contains integer k.

Output Format

Print Yes or No.

Sample Input

7

0 1 2 4 6 5 3 

1 

Sample Output

Yes
 n=int(input())
a=[int(x) for x in input().split()]
k=int(input())
flag=0
if len(a)!=n:
    print("No")
    flag=1
for i in a:
    for j in a:
        if i+j==k and flag==0:
            flag=1
            print("Yes")
            break
        
if flag==0:
    print("No")

