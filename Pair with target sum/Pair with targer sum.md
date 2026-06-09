# Problem 3: Pair with Target Sum (Return All Indices)

**Difficulty:** Medium

**Description:**  
Write a function `two_sum(lst, target)` that takes a list of integers `lst` and an integer `target`. The function should return a **list of index pairs** `[i, j]` where `i < j` and `lst[i] + lst[j] == target`. If multiple pairs exist, return **all unique pairs** (order of pairs does not matter, but indices within each pair should be in ascending order).

**Constraints:**
- You may **not** use the same element twice in a single pair
- The same index cannot appear in both positions of a pair
- Return an empty list if no pairs sum to the target
- Elements are not necessarily unique (duplicate values may exist)

**Examples:**

Example 1:
Input: lst = [2, 7, 11, 15], target = 9
Output: [[0, 1]]

Input: lst = [3, 2, 4, 3, 6], target = 6
Output: [[0, 3], [1, 2]]

Input: lst = [5, 5, 5, 5], target = 10
Output: [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]

Input: lst = [1, 2, 3, 4, 5], target = 10
Output: []

Input: lst = [], target = 5
Output: []

Input: lst = [1], target = 2
Output: []