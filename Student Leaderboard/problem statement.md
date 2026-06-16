# Student Leaderboard

You are given a nested list where each inner list holds a student's name and their score.

```python
students = [
    ["Alice", 85],
    ["Bob", 92],
    ["Carol", 78],
    ["Dave", 92],
    ["Eve", 65]
]
```

Implement the following three functions:

**`top_scorer(students)`**
Prints the name and score of the student with the highest score. If there is a tie, print the one who appears first in the list.

**`above_average(students)`**
Prints the names of all students who scored strictly above the average, in the order they appear.

**`reverse_leaderboard(students)`**
Prints all students from lowest to highest score using slicing — do not use `.reverse()` or `reversed()`.

---

## Sample Output

```
Top scorer: Bob - 92

Average score: 82.4
Above average: Bob, Dave

Leaderboard (lowest to highest):
Eve    - 65
Carol  - 78
Alice  - 85
Bob    - 92
Dave   - 92
```

---

## Constraints

- Do not modify the original `students` list
- `reverse_leaderboard` must use **slicing** to reverse the order
- Each function must be implemented separately
- Do not use any imports
- Do not use built-ins like `max()`, `min()`, or `sum()` — compute values manually with loops

---

## Hint

<details>
<summary>Click to reveal</summary>

Each element in `students` is a list itself, so `students[i][0]` is a name and `students[i][1]` is a score. To sort students by score without modifying the original, look into how Python's `sorted()` function works with a `key` argument. To reverse with slicing, use `[::-1]`.

</details>