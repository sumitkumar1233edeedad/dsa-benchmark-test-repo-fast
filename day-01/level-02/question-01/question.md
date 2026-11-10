# Find the First Duplicate Element

- **Day:** `Day 01`
- **Level:** `Level 02`
- **Question:** `Question 01`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an array of integers `nums`, find the first element that appears at least twice. The "first" duplicate is defined as the element whose second occurrence has the smallest index. If there are no duplicates, return -1.

**Constraints:**
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

**Example 1:**
Input: nums = [2, 5, 1, 2, 3, 5]
Output: 2
Explanation: The duplicates are 2 and 5. The second occurrence of 2 is at index 3, while the second occurrence of 5 is at index 5. Since 3 < 5, the first duplicate is 2.

**Example 2:**
Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: No element appears more than once.

**Example 3:**
Input: nums = [1, 1, 2, 2, 3, 3]
Output: 1
Explanation: The second occurrence of 1 is at index 1, which is the earliest second occurrence.

---

## 💻 Starter Function

```python
def find_first_duplicate(nums: List[int]) -> int:
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> Previous problems (Level 01) focused on linear traversal without auxiliary data structures, finding min index and local maximum. This problem introduces the Hash Set for duplicate detection, a core mechanic of the Frequency & Hash Sets pattern. It avoids duplication by not being a simple boolean 'Contains Duplicate' (which is avoided) but instead returns the specific duplicate element with the earliest second occurrence, requiring a single pass with a set. It reinforces the canonical algorithmic approach of using a hash set for O(1) lookups during traversal.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
