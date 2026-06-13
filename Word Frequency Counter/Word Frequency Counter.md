# Word Frequency Counter

Write a function `word_frequency(text)` that takes a string of words and returns a dictionary where each key is a unique word and its value is how many times that word appears in the string. Then print the results sorted from most frequent to least frequent.

---

## Sample Input

```
text = "the cat sat on the mat and the cat sat"
```

## Sample Output

```
the  -> 3
cat  -> 2
sat  -> 2
on   -> 1
mat  -> 1
and  -> 1
```

---

## Constraints

- All words in the input will be lowercase with no punctuation
- Words are separated by single spaces
- Your solution must use a separate `word_frequency(text)` function that returns a dictionary
- If two words share the same frequency, either order between them is acceptable
- Do not use any imports

---

## Hint

<details>
<summary>Click to reveal</summary>

Use `text.split()` to break the string into a list of words. Loop through the list — if the word is already a key in your dictionary, increment its value; if not, add it with a value of `1`. To sort by frequency, look into passing a `key` argument to Python's `sorted()` function.

</details>
