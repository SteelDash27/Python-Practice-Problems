# Student Grade Tracker

Write a program that stores the scores of `n` students in a list, then prints a summary report using a separate function `report(scores)`.

The report must show:
- All scores
- The highest score
- The lowest score
- The average score (rounded to 2 decimal places)
- How many students scored **above** the average

---

## Sample Input

```
Enter number of students: 6
Enter score for student 1: 45
Enter score for student 2: 78
Enter score for student 3: 90
Enter score for student 4: 55
Enter score for student 5: 88
Enter score for student 6: 62
```

## Sample Output

```
Scores: [45, 78, 90, 55, 88, 62]
Highest: 90
Lowest:  45
Average: 69.67
Above average: 3
```

---

## Constraints

- `1 ≤ n ≤ 50`
- `0 ≤ score ≤ 100`
- Your solution must use a separate `report(scores)` function
- Do not use any imports — no `max()`, `min()`, or `sum()` built-ins; find these values manually using loops

---

## Hint

<details>
<summary>Click to reveal</summary>

Use a loop to compute the total, highest, and lowest in a single pass. Once you have the average, make a second loop to count how many scores are strictly greater than it. For rounding, use Python's built-in `round(value, 2)`.

</details>