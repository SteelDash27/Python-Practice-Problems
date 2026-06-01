# Multiplication Table

Write a function `times_table(n)` that prints an `n x n` multiplication table. Each row should be neatly aligned so that all columns line up regardless of how many digits each product has.

---

## Sample Input

```
n = 5
```

## Sample Output

```
 1  2  3  4  5
 2  4  6  8 10
 3  6  9 12 15
 4  8 12 16 20
 5 10 15 20 25
```

---

## Constraints

- `1 ≤ n ≤ 12`
- Your solution must use a separate `times_table(n)` function
- Columns must be aligned — the output should not be jagged
- Do not use any imports

---

## Hint

<details>
<summary>Click to reveal</summary>

Look into Python's `str.rjust()` method or f-string width formatting (e.g. `f"{value:3d}"`) to pad each number to a fixed width. The width you need depends on the largest possible product in the table, which is `n * n`.

</details>