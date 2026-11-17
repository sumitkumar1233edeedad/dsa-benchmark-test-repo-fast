# Sort Array by Parity II

- **Day:** `Day 01`
- **Level:** `Level 03`
- **Question:** `Question 02`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an array of integers `nums`, half of the integers are even, and half are odd. Sort the array so that whenever `nums[i]` is even, `i` is even, and whenever `nums[i]` is odd, `i` is odd. Return any answer array that satisfies this condition. You must solve this in-place with O(1) extra memory.

**Constraints:**
- 2 <= nums.length <= 2 * 10^4
- nums.length is even.
- Half of the integers in nums are even.
- 0 <= nums[i] <= 1000

**Example 1:**
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: Even indices (0,2) have even numbers (4,2), odd indices (1,3) have odd numbers (5,7). Other valid outputs include [4,7,2,5].

**Example 2:**
Input: nums = [2,3]
Output: [2,3]

**Example 3:**
Input: nums = [1,2,3,4,5,6]
Output: [2,1,4,3,6,5]
Explanation: Any arrangement where even numbers are at even indices and odd numbers at odd indices is accepted.

---

## 💻 Starter Function

```python
def sortArrayByParityII(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous problem (Partition Array by Parity) practiced the fundamental two-pointer partitioning technique: grouping all even elements before odd elements using a left/right pointer approach. This problem serves as the complementary twist by requiring a more precise in-place arrangement: even numbers must occupy even indices and odd numbers must occupy odd indices. This variation introduces dual-pointer traversal where one pointer scans even indices and the other scans odd indices, swapping only when both pointers find misplaced elements. It reinforces in-place swapping logic, boundary condition handling (pointer increments by 2), and the concept of maintaining two independent invariants simultaneously. It avoids duplication by changing the partitioning criterion from value-based grouping to index-parity alignment, while still operating within the same two-pointer in-place paradigm.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
