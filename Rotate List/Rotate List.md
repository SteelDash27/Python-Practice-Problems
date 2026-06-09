# Python List Practice Problems

## Problem 1: Rotate List

**Difficulty:** Easy/Medium

**Description:**  
Write a function `rotate_list(lst, k)` that takes a list `lst` and an integer `k` (non-negative). The function should rotate the list to the **right** by `k` steps. Rotating right by 1 step means moving the last element to the front.

**Constraints:**
- Do not use any built-in rotation functions (like `collections.deque`)
- Try to solve it in **O(n)** time and **O(1)** extra space (modify the list in-place)

**Examples:**
```python
rotate_list([1, 2, 3, 4, 5], 2)   # Returns [4, 5, 1, 2, 3]
rotate_list([1, 2, 3], 5)         # Returns [2, 3, 1]  (k can be larger than list length)
rotate_list([10, 20, 30, 40], 0)  # Returns [10, 20, 30, 40]
rotate_list([], 3)                # Returns []