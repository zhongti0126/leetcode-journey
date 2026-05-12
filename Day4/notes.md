# Day 4 Notes

## Binary Search

### Core Idea
- Search in a sorted array
- Reduce search space by half each time
- Time Complexity: O(log n)

---

## Important Variables

```python
left = 0
right = len(nums) - 1
```

- left = left boundary
- right = right boundary

---

## Find Middle

```python
mid = (left + right) // 2
```

- `mid` = index
- `nums[mid]` = value

---

## Search Logic

```python
if nums[mid] == target:
    return mid

elif target > nums[mid]:
    left = mid + 1

else:
    right = mid - 1
```

---

## Important

### Why use `left <= right`

Because:

```python
left == right
```

means there is still one element left to check.

---

## Common Mistake

❌ Infinite loop:

```python
left = mid
right = mid
```

✅ Correct:

```python
left = mid + 1
right = mid - 1
```

---

## What I Learned Today
- while loop
- Binary Search logic
- left / right boundaries
- mid index
- O(log n)
- Avoid infinite loop

## Binary Search Example
<img width="2566" height="2159" alt="Day4" src="https://github.com/user-attachments/assets/9b7b25b9-70bd-4aff-b8b9-1d4ed377693b" />
