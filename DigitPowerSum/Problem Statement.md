# Digit Power Sum

Write a function `is_armstrong(n)` that checks if a number is an Armstrong number — a number equal to the sum of its own digits, each raised to the power of the number of digits.

Using that function, print all Armstrong numbers in a given range `[lo, hi]`.

---

## Sample Input

```
lo = 1
hi = 500
```

## Sample Output

```
1 2 3 4 5 6 7 8 9 153 370 371 407
```

---

## Constraints

- `1 ≤ lo ≤ hi ≤ 10,000`
- Your solution must use a separate `is_armstrong(n)` function
- Do not use any imports — solve with built-in Python only
- Single-digit numbers (1–9) are always Armstrong numbers

---

## Hint

<details>
<summary>Click to reveal</summary>

Convert the number to a string to count its digits and iterate over each one. Raise each digit (as an integer) to the power of `len(str(n))`, sum them, and compare to the original number.

</details>
