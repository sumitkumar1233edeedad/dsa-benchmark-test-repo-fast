# Length of Longest Unique Prefix

- **Day:** `Day 01`
- **Level:** `Level 02`
- **Question:** `Question 02`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an array of integers `nums`, find the length of the longest prefix (starting from index 0) that contains **all unique elements**. If the entire array consists of unique elements, return the length of the array.

A prefix is a contiguous subarray starting at index 0.

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

**Example 1:**
```
Input: nums = [1, 2, 3, 2, 4]
Output: 3
Explanation: The prefix [1, 2, 3] has all unique elements. The next element (2) is a duplicate, so the longest unique prefix has length 3.
```

**Example 2:**
```
Input: nums = [5, 5, 5, 5]
Output: 1
Explanation: The first element is unique, but the second element is a duplicate of the first. The longest unique prefix is [5] with length 1.
```

**Example 3:**
```
Input: nums = [10, 20, 30, 40, 50]
Output: 5
Explanation: All elements are distinct, so the entire array is the longest unique prefix.
```

---

## 💻 Starter Function

```python
def longest_unique_prefix_length(nums: List[int]) -> int:
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous two problems in this level focused on detecting duplicates using a Hash Set: 'Find the First Duplicate Element' (returning the duplicate value) and 'Find All Duplicate Numbers In-Place' (using in-place marking). This problem introduces a complementary twist: **edge boundary optimization**. Instead of identifying *which* element is duplicated, we determine the *exact boundary index* where the uniqueness property breaks. This reinforces the Hash Set pattern for tracking seen elements but shifts the output to a length metric, requiring a single linear pass with early termination. It avoids the in-place mutation of the previous problem and the duplicate-value focus of the first, providing a natural progression toward sliding-window techniques where boundary management is key.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
