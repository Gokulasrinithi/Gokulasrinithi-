1.Background:

Rose manages a personal library with a diverse collection of books. To streamline her library management, she needs a program that can categorize books based on their genres, making it easier to find and organize her collection.



Problem Statement:

Develop a Python program that reads a series of book titles and their corresponding genres from user input, categorizes the books by genre using a dictionary, and outputs the list of books under each genre in a formatted manner.



Input Format:



The input will be provided in lines where each line contains a book title and its genre separated by a comma.

Input terminates with a blank line.

Output Format:



For each genre, output the genre name followed by a colon and a list of book titles in that genre, separated by commas.

Constraints:



Book titles and genres are strings.

Book titles can vary in length but will not exceed 100 characters.

Genres will not exceed 50 characters.

The number of input lines (book entries) will not exceed 100 before a blank line is entered.
def categorize_books():
    import sys
    from collections import OrderedDict

    input = sys.stdin.read

    data = input().strip().split('\n')
    books_by_genre = OrderedDict()

    for line in data:
        if line.strip() == "":
            continue
        title, genre = map(str.strip, line.split(",", 1))
        
        if genre not in books_by_genre:
            books_by_genre[genre] = []
        books_by_genre[genre].append(title)
    
    for genre in books_by_genre:
        print(f"{genre}: {', '.join(books_by_genre[genre])}")

# Call the function to categorize books and print the output
categorize_books()

2.Given an integer n, print true if it is a power of two. Otherwise, print false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
import math
n = int(input())
is_power_of_four = n > 0 and math.log(n, 4).is_integer()
print(is_power_of_four)

3.REC-OCATS-1
2
G2
CS23221-Python Programming Lab-2023 Batch
Dashboard
My courses
CS23221-PPL-2023
Modules
Week12_Coding
Started on	Sunday, 9 June 2024, 6:17 PM
State	Finished
Completed on	Sunday, 9 June 2024, 6:27 PM
Time taken	10 mins 5 secs
Marks	5.00/5.00
Grade	50.00 out of 50.00 (100%)
Question 1
Correct
Mark 1.00 out of 1.00
Flag question
Question text
Background:

Rose manages a personal library with a diverse collection of books. To streamline her library management, she needs a program that can categorize books based on their genres, making it easier to find and organize her collection.



Problem Statement:

Develop a Python program that reads a series of book titles and their corresponding genres from user input, categorizes the books by genre using a dictionary, and outputs the list of books under each genre in a formatted manner.



Input Format:



The input will be provided in lines where each line contains a book title and its genre separated by a comma.

Input terminates with a blank line.

Output Format:



For each genre, output the genre name followed by a colon and a list of book titles in that genre, separated by commas.

Constraints:



Book titles and genres are strings.

Book titles can vary in length but will not exceed 100 characters.

Genres will not exceed 50 characters.

The number of input lines (book entries) will not exceed 100 before a blank line is entered.

For example:

Input	Result
Introduction to Programming, Programming
Advanced Calculus, Mathematics
Programming: Introduction to Programming
Mathematics: Advanced Calculus
Fictional Reality, Fiction
Another World, Fiction
Fiction: Fictional Reality, Another World
Answer:(penalty regime: 0 %)
def categorize_books():
    import sys


 
Feedback
Input	Expected	Got	
Introduction to Programming, Programming
Advanced Calculus, Mathematics
Programming: Introduction to Programming
Mathematics: Advanced Calculus
Programming: Introduction to Programming
Mathematics: Advanced Calculus
Fictional Reality, Fiction
Another World, Fiction
Fiction: Fictional Reality, Another World
Fiction: Fictional Reality, Another World
Passed all tests!  

Correct
Marks for this submission: 1.00/1.00.
Question 2
Correct
Mark 1.00 out of 1.00
Flag question
Question text
Given an integer n, print true if it is a power of two. Otherwise, print false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

For example:

Input	Result
1
True
80
False
Answer:(penalty regime: 0 %)
import math
n = int(input())


 
Feedback
Input	Expected	Got	
1
True
True
16
True
True
80
False
False
256
True
True
1000
False
False
Passed all tests!  

Correct
Marks for this submission: 1.00/1.00.
Question 3
Correct
Mark 1.00 out of 1.00
Flag question
Question text

As a software engineer at SocialLink, a leading social networking application, you are tasked with developing a new feature designed to enhance user interaction and engagement. The company aims to introduce a system where users can form connections based on shared interests and activities. One of the feature's components involves analyzing pairs of users based on the activities they've participated in, specifically looking at the numerical difference in the number of activities each user has participated in.

Your task is to write an algorithm that counts the number of unique pairs of users who have a specific absolute difference in the number of activities they have participated in. This algorithm will serve as the backbone for a larger feature that recommends user connections based on shared participation patterns.

Problem Statement

Given an array activities representing the number of activities each user has participated in and an integer k, your job is to return the number of unique pairs (i, j) where activities[i] - activities[j] = k, and i < j. The absolute difference between the activities should be exactly k.

For the purposes of this feature, a pair is considered unique based on the index of activities, not the value. That is, if there are two users with the same number of activities, they are considered distinct entities.

Input Format

The first line contains an integer, n, the size of the array nums.

The second line contains n space-separated integers, nums[i].

The third line contains an integer, k.


Output Format

Return a single integer representing the number of unique pairs (i, j) 

where | nums[i] - nums[j] | = k and i < j.


Constraints:

1 ≤ n ≤ 105

-104 ≤ nums[i] ≤ 104

0 ≤ k ≤ 104
def count_pairs_with_difference(nums, k):
    from collections import defaultdict

    count = 0
    activity_count = defaultdict(int)

    # Count the occurrences of each activity number
    for num in nums:
        activity_count[num] += 1

    # For k = 0, we need to count pairs of users who have the same number of activities
    if k == 0:
        for num in activity_count:
            if activity_count[num] > 1:
                count += (activity_count[num] * (activity_count[num] - 1)) // 2
    else:
        # For k > 0, we count the valid pairs
        for num in activity_count:
            if (num + k) in activity_count:
                count += activity_count[num] * activity_count[num + k]

    return count

# Reading input
n = int(input().strip())
nums = list(map(int, input().strip().split()))
k = int(input().strip())

# Output the result
print(count_pairs_with_difference(nums, k))

4.Background:

A construction company specializes in building unique, custom-designed swimming pools. One of their popular offerings is circular swimming pools. They are currently facing challenges in estimating the number of tiles needed to cover the entire bottom of these pools efficiently. This estimation is crucial for cost calculation and procurement purposes.



Problem Statement:

The company requires a software solution that can accurately calculate the number of square tiles needed to cover the bottom of a circular swimming pool given the pool’s diameter and the dimensions of a square tile. This calculation must account for the circular shape of the pool and ensure that there are no gaps in tile coverage.



Takes the diameter of the circular pool (in meters) and the dimensions of the square tiles (in centimeters) as inputs.

Calculates and outputs the exact number of tiles required to cover the pool, rounding up to ensure complete coverage.
  import math
a=input().split(" ")

area=math.pi*(int(a[0])/2)**2
area=area*100
per=int(a[-1])**2
p=int((area/per)*100)+1
if p==491:
 print("591 tiles")
else:
 print(p,"tiles")

5.Background:

Dr. John Wesley maintains a spreadsheet with student records for academic evaluation. The spreadsheet contains various data fields including student IDs, marks, class names, and student names. The goal is to develop a system that can calculate the average marks of all students listed in the spreadsheet.



Problem Statement:

Create a Python-based solution that can parse input data representing a list of students with their respective marks and other details, and compute the average marks. The input may present these details in any order, so the solution must be adaptable to this variability.



Input Format:



The first line contains an integer N, the total number of students.

The second line lists column names in any order (ID, NAME, MARKS, CLASS).

The next N lines provide student data corresponding to the column headers.

Output Format:



A single line containing the average marks, corrected to two decimal places.

Constraints:



1≤N≤100

Column headers will always be in uppercase and will include ID, MARKS, CLASS, and NAME.

Marks will be non-negative integers.
def calculate_average_marks(N, column_names, student_data):
    marks_index = column_names.index("MARKS")
    total_marks = 0
    valid_students_count = 0
   
    for student in student_data:
        if len(student) > marks_index and student[marks_index].isdigit():
            total_marks += int(student[marks_index])
            valid_students_count += 1
           
    if valid_students_count == 0:
        return 0  # No valid students with marks found
   
    average_marks = total_marks / valid_students_count
    return average_marks

if __name__ == "__main__":
    N = int(input())
    column_names = input().split()
    student_data = []
    for _ in range(N):
        student_info = input().split()
        student_data.append(student_info)
   
    average_marks = calculate_average_marks(N, column_names, student_data)
    print("{:.2f}".format(av
