# Classroom Seating Analyser

You are given a classroom seating chart represented as a nested list where each inner list is a row of student scores. Write a program that analyses the data using the functions below.

```python
classroom = [
    [85, 90, 78, 92, 88],
    [70, 65, 80, 75, 95],
    [55, 60, 72, 68, 58],
    [91, 84, 77, 89, 93]
]
```

Implement the following four functions:

**`top_students(classroom, threshold)`**
Return a flat list of all scores strictly above `threshold`, preserving row-by-row order. Use a list comprehension.

**`row_averages(classroom)`**
Return a list of the average score per row, rounded to 2 decimal places.

**`last_two_per_row(classroom)`**
Return a new nested list containing only the last two scores from each row. Use slicing.

**`highest_in_each_row(classroom)`**
Return a list of the highest score from each row.

Print the result of each function clearly labelled.

---

## Sample Output

```
Top scores (above 80): [85, 90, 92, 88, 95, 91, 84, 89, 93]
Row averages: [86.6, 77.0, 62.6, 86.8]
Last two per row: [[88, 85], [95, 75], [58, 68], [93, 89]]
Highest in each row: [92, 95, 72, 93]
```

---

## Constraints

- Do not modify the original `classroom` list
- `top_students` must be implemented using a **list comprehension**
- `last_two_per_row` must use **slicing** — no index loops
- Each function must be implemented separately — do not combine logic
- Do not use any imports

---

## Hint

<details>
<summary>Click to reveal</summary>

For `top_students`, a nested list comprehension works like this: `[score for row in classroom for score in row if ...]`. For `last_two_per_row`, slicing a list with `row[-2:]` gives you the last two elements. For averages, sum the row and divide by `len(row)`.

</details>