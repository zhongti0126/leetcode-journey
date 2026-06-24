## Sliding Window

### Core Idea

Maintain a window and move it through the array.

Use two pointers:

```python
left
right
```

---

## LC 121 - Best Time to Buy and Sell Stock

### What I Learned

- Sliding Window pattern
- Two Pointers
- Track minimum buying price
- Update maximum profit

---

### Key Idea

```python
left = buy day
right = sell day
```

If:

```python
prices[right] > prices[left]
```

Calculate profit.

Otherwise:

```python
left = right
```

Use a cheaper buying day.

---

### Time Complexity

O(n)

### Space Complexity

O(1)

---

## What I Learned Today

- Sliding Window
- Two Pointers
- Maximum Profit Pattern
- LC 121
