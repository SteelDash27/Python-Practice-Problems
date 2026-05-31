# Fizz Pyramid

Write a function `fizz_pyramid(n)` that prints a left-aligned triangle of numbers with `n` rows. Each row `i` contains the integers `1` through `i`, except:

- Any multiple of `3` is replaced with `"Fizz"`
- Any multiple of `5` is replaced with `"Buzz"`
- Any multiple of both is replaced with `"FizzBuzz"`

---

## Sample Input

```
n = 5
```

## Sample Output

```
1
1 2
1 2 Fizz
1 2 Fizz 4
1 2 Fizz 4 Buzz
```

---

## Constraints

- `1 ≤ n ≤ 20`
- Your solution must use a separate `fizz_pyramid(n)` function
- Numbers on each row must be separated by a single space
- Do not use any imports

---

## Hint

<details>
<summary>Click to reveal</summary>

Use a nested loop — the outer loop controls how many rows you print, and the inner loop builds each row from `1` to `i`. For each number, check divisibility by `15` first, then `3`, then `5`, then fall back to the number itself.

</details>