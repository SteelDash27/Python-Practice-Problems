# Contact Book

Write a program that manages a simple contact book using a dictionary where each key is a name and its value is a list containing the person's phone number and email address.

Implement the following functions:

**`add_contact(book, name, phone, email)`**
Adds a new contact. If the contact already exists, print `"Contact already exists."` and do not overwrite.

**`find_contact(book, name)`**
Prints the phone number and email of the contact. If not found, print `"Contact not found."`.

**`delete_contact(book, name)`**
Removes a contact by name. If not found, print `"Contact not found."`.

**`list_contacts(book)`**
Prints all contacts sorted alphabetically by name. If the book is empty, print `"No contacts saved."`.

Your `main` should pre-load the book with these three contacts, then call all four functions as shown in the sample below:

```python
book = {
    "Alice": ["0821234567", "alice@email.com"],
    "Bob":   ["0839876543", "bob@email.com"],
    "Carol": ["0711112222", "carol@email.com"]
}
```

---

## Sample Output

```
--- All Contacts ---
Alice  | 0821234567 | alice@email.com
Bob    | 0839876543 | bob@email.com
Carol  | 0711112222 | carol@email.com

--- Find Bob ---
Phone: 0839876543
Email: bob@email.com

--- Add Dave ---
Contact added.

--- Add Alice again ---
Contact already exists.

--- Delete Carol ---
Contact deleted.

--- All Contacts After Changes ---
Alice  | 0821234567 | alice@email.com
Bob    | 0839876543 | bob@email.com
Dave   | 0799998888 | dave@email.com

--- Find Carol ---
Contact not found.
```

---

## Constraints

- Each contact's value must be stored as a **list** with exactly 2 elements: `[phone, email]`
- `list_contacts` must print contacts in **alphabetical order** — use slicing or sorting on the key list
- Each function must be implemented separately
- Do not use any imports

---

## Hint

<details>
<summary>Click to reveal</summary>

Use `name in book` to check whether a contact exists. To print contacts alphabetically, call `sorted(book)` which returns a sorted list of the dictionary's keys — then loop through that list to access each value.

</details>