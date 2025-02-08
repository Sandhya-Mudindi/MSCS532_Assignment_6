# MSCS532_Assignment_6

This repository contains implementations of algorithms and data structures as part of Assignment 6. Each file demonstrates a specific concept with example usage and performance analysis.

---

## Files and How to Run Them

### 1. **`Data_Structure_Implementations.py`**
- **Description:** Implements Data Structures(Array,Matrices,Stacks,Queues,Linked Lists, and Rotted Tree) with basic oprations.
- **How to Run:**
  ```bash
  python Data_Structure_Implementations.py

### 2. **`Deterministic_Algorith.py`**
- **Description:** Implements Daterministic alogorithm for selection in worst case time(Median of Medians)..
- **How to Run:**
  ```bash
  python Deterministic_Algorith.py

### 3. **`Randomizied_Alogorithm.py`**
- **Description:** Implements Randomized Algorithm for selection in expected time(Ramdomizied Quicksort) ..
- **How to Run:**
  ```bash
  python Randomizied_Alogorithm.py

###  **`Summary of Findings`**
The deterministic selection algorithm, also known as the Median of Medians, ensures worst-case linear time complexity by carefully selecting a balanced pivot. It works by dividing the array into small groups, determining the median of each, and recursively selecting the median of these medians to partition the array efficiently. In contrast, the randomized Quickselect algorithm selects a pivot randomly, achieving an expected time complexity of O(n), though in rare cases, it may degrade to O(n²). While Quickselect is generally faster for moderate input sizes, it lacks the deterministic guarantees of the Median of Medians. Both algorithms have an O(n) space complexity due to the auxiliary arrays used for partitioning, though an optimized in-place version of Quickselect can reduce extra space usage to O(1). When implementing data structures, arrays provide O(1) access time, making them ideal for quick lookups, whereas linked lists allow efficient insertions and deletions at O(1) when modifying the head. Stacks and queues also exhibit different trade-offs: arrays efficiently support LIFO operations, while linked lists excel in FIFO implementations. These structures have numerous real-world applications, including arrays in image processing, linked lists in dynamic memory allocation, queues in scheduling tasks, and trees in file system organization.
