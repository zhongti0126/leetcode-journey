### Heap / Priority Queue

## What is a Heap?

- A special data structure
- Automatically keeps the smallest element at the top
- Python uses a Min Heap by default

## Import
import heapq

## Create a Heap
heap = []

## Push Element
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)

## Pop Smallest Element
heapq.heappop(heap)

Returns:

2

## Peek Smallest Element
heap[0]

Returns the smallest element without removing it.

##  Important Operations
|         Operation       |     Meaning     |
|-------------------------|-----------------|
| heapq.heappush(heap, x) |    Add element  |
| heapq.heappop(heap)     | Remove smallest |
| heap[0]                 | Peek smallest   |
