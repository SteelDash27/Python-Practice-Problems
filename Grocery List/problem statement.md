# Shopping Cart

Write a program that manages a shopping cart using a nested list where each item is stored as `[name, price, quantity]`.

Start with this cart:

```python
cart = [
    ["Apples", 5.99, 3],
    ["Bread", 12.50, 1],
    ["Milk", 8.75, 2],
    ["Eggs", 24.99, 1],
    ["Butter", 45.00, 1]
]
```

Implement the following functions:

**`total_cost(cart)`**
Returns the total cost of all items (`price * quantity` for each item, summed together).

**`most_expensive(cart)`**
Returns the name of the item with the highest individual price (not total).

**`affordable(cart, budget)`**
Returns a list of names of items whose individual price is less than or equal to `budget`, using a list comprehension.

**`summary(cart)`**
Prints each item as: `Item - RX.XX x Q = RX.XX` where the last value is `price * quantity`. Then prints the grand total at the bottom.

---

## Sample Output

```
Apples  - R5.99  x 3 = R17.97
Bread   - R12.50 x 1 = R12.50
Milk    - R8.75  x 2 = R17.50
Eggs    - R24.99 x 1 = R24.99
Butter  - R45.00 x 1 = R45.00

Total: R117.96

Most expensive item: Butter

Affordable items (under R15.00): ['Apples', 'Bread', 'Milk']
```

---

## Constraints

- Do not modify the original `cart` list
- `affordable` must be implemented using a **list comprehension**
- Each item's data must be accessed using indexes — `item[0]`, `item[1]`, `item[2]`
- Each function must be implemented separately
- Do not use any imports

---

## Hint

<details>
<summary>Click to reveal</summary>

Each element in `cart` is a list, so `cart[i][0]` is the name, `cart[i][1]` is the price, and `cart[i][2]` is the quantity. For `total_cost`, loop through the cart and accumulate `price * quantity`. For `most_expensive`, track the highest price seen so far as you loop — similar to how you'd find a maximum manually.

</details>