1.A sentence is a string of single-space separated words where each word consists only of lowercase letters.A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Example 2:



Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"]

 Constraints:

1 <= s1.length, s2.length <= 200

s1 and s2 consist of lowercase English letters and spaces.

s1 and s2 do not have leading or trailing spaces.

All the words in s1 and s2 are separated by a single space.

Note:

Use dictionary to solve the problem
def uncommon_words(s1, s2):
    def count_words(sentence):
        word_count = {}
        for word in sentence.split():
            word_count[word] = word_count.get(word, 0) + 1
        return word_count
    s1_words = count_words(s1)
    s2_words = count_words(s2)
    uncommon_words = []
    for word, count in s1_words.items():
        if count == 1 and word not in s2_words:
            uncommon_words.append(word)
    for word, count in s2_words.items():
        if count == 1 and word not in s1_words:
            uncommon_words.append(word)
    return uncommon_words
s1 =input()

2.Create a student dictionary  for n students with the student name as key and their test mark assignment mark and lab mark as values. Do the following computations and display the result.

1.Identify the student with the  highest average score

2.Identify the student who as the highest Assignment marks

3.Identify the student with the Lowest lab marks

4.Identify the student with the lowest average score

Note:

If more than one student has the same score display all the student names



Sample input:

4

James 67 89 56

Lalith 89 45 45

Ram 89 89 89

Sita 70 70 70

Sample Output:

Ram

James Ram

Lalith

Lalith
n = int(input())
students = {}
for _ in range(n):
    name, tm, am, lm = input().split()
    tm, am, lm = map(int, (tm, am, lm))
    students[name] = (tm, am, lm)
avg_scores = {name: sum(scores) / 3 for name, scores in students.items()}
highest_avg = max(avg_scores.values())
students_highest_avg = [name for name, avg in avg_scores.items() if avg == highest_avg]
highest_assignment = max(student[1] for student in students.values())
students_highest_assignment = [name for name, marks in students.items() if marks[1] == highest_assignment]
lowest_lab = min(student[2] for student in students.values())
students_lowest_lab = [name for name, marks in students.items() if marks[2] == lowest_lab]
lowest_avg = min(avg_scores.values())
students_lowest_avg = [name for name, avg in avg_scores.items() if avg == lowest_avg]
print(' '.join(sorted(students_highest_avg)))
print(' '.join(sorted(students_highest_assignment)))
print(' '.join(sorted(students_lowest_lab)))
print(' '.join(sorted(students_lowest_avg)))

3.Given an array of names of candidates in an election. A candidate name in the array represents a vote cast to the candidate. Print the name of candidates received Max vote. If there is tie, print a lexicographically smaller name.

Examples: 

Input :  votes[] = {"john", "johnny", "jackie",

                    "johnny", "john", "jackie",

                    "jamie", "jamie", "john",

                    "johnny", "jamie", "johnny",

                    "john"};

Output : John

We have four Candidates with name as 'John', 'Johnny', 'jamie', 'jackie'. The candidates John and Johny get maximum votes. Since John is alphabetically smaller, we print it. Use dictionary to solve the above problem

 

Sample Input:

10

John

John

Johny

Jamie

Jamie

Johny

Jack

Johny

Johny

Jackie

 

Sample Output:

Johny
n= int(input())
votes_count = {}
for _ in range(n):
    candidate = input().strip()
    votes_count[candidate] = votes_count.get(candidate, 0) + 1
max_votes = max(votes_count.values())
winners = [candidate for candidate, votes in votes_count.items() if votes == max_votes]
print(sorted(winners)[0])

4.Give a dictionary with value lists, sort the keys by summation of values in value list.

 Input : test_dict = {‘Gfg’ : [6, 7, 4], ‘best’ : [7, 6, 5]}

Output : {‘Gfg’: 17, ‘best’: 18}

Explanation : Sorted by sum, and replaced.

 Input : test_dict = {‘Gfg’ : [8,8], ‘best’ : [5,5]}

Output : {‘best’: 10, ‘Gfg’: 16}

Explanation : Sorted by sum, and replaced.

 Sample Input:

2

Gfg 6 7 4

Best 7 6 5

Sample Output

Gfg 17

Best 18
n = int(input())
test_dict = {}
for _ in range(n):
    key, *values = input().split()
    values = list(map(int, values))
    test_dict[key] = sum(values)
sorted_dict = dict(sorted(test_dict.items(), key=lambda item: item[1]))
for key, value in sorted_dict.items():
    print(key, value)

5.In the game of Scrabble™, each letter has points associated with it. The total score of a word is the sum of the scores of its letters. More common letters are worth fewer points while less common letters are worth more points. The points associated with each letter are shown below:

Points Letters

1 A, E, I, L, N, O, R, S, T and U

2 D and G

3 B, C, M and P

4 F, H, V, W and Y

5 K

8 J and X

10 Q and Z

Write a program that computes and displays the Scrabble™ score for a word. Create a dictionary that maps from letters to point values. Then use the dictionary to compute the score.

A Scrabble™ board includes some squares that multiply the value of a letter or the value of an entire word. We will ignore these squares in this exercise.

Sample Input

REC

Sample Output

REC is worth 5 points.
letter_points = {
    'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}
word = input().upper()
score = sum(letter_points.get(letter, 0) for letter in word)
print(f"{word} is worth {score} points.")

