# Problem 2: Find Leaders in an Array

**Difficulty:** Medium

**Description:**  
A "leader" in a list is an element that is **greater than all elements to its right**. The rightmost element is always a leader. Write a function `find_leaders(lst)` that returns a **new list** containing all leaders in the order they appear from **left to right**.

**Constraints:**
- Do not use nested loops that run in O(n²) time
- Aim for **O(n)** time complexity
- The original list should not be modified

**Examples:**
- `find_leaders([16, 17, 4, 3, 5, 2])` returns `[17, 5, 2]`
  - 16 is not a leader (17 is greater to the right)
  - 17 is a leader (greater than all to its right: 4, 3, 5, 2)
  - 4 is not a leader (5 is greater to the right)
  - 3 is not a leader (5 is greater to the right)
  - 5 is a leader (greater than 2 to its right)
  - 2 is a leader (last element)

- `find_leaders([1, 2, 3, 4, 5])` returns `[5]`

- `find_leaders([5, 4, 3, 2, 1])` returns `[5, 4, 3, 2, 1]`

- `find_leaders([10])` returns `[10]`

- `find_leaders([])` returns `[]`

**Hint:**  
Traverse the list from right to left. Keep track of the maximum value you have seen so far as you move leftward. When you encounter a value greater than that maximum, it becomes a new leader.

**Function Signature:**
```python
def find_leaders(lst):
    # Your code here
    pass