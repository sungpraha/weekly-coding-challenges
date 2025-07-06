# Week 1: Two Sum

## Problem Description

Given an array of integers `nums` and an integer `target`, find the **indices** of the two numbers in the array such that they add up to the `target`.

**Assumptions:**

* You may assume that each input would have **exactly one solution**.
* You may **not** use the same element twice.
* The order of the returned indices does not matter.

## Examples

**Example 1:**

* **Input:** `nums = [2, 7, 11, 15]`, `target = 9`
* **Output:** `[0, 1]`
* **Explanation:** Because `nums[0] + nums[1] == 2 + 7 == 9`, we return `[0, 1]`.

**Example 2:**

* **Input:** `nums = [3, 2, 4]`, `target = 6`
* **Output:** `[1, 2]`
* **Explanation:** Because `nums[1] + nums[2] == 2 + 4 == 6`, we return `[1, 2]`.

**Example 3:**

* **Input:** `nums = [3, 3]`, `target = 6`
* **Output:** `[0, 1]`
* **Explanation:** Because `nums[0] + nums[1] == 3 + 3 == 6`, we return `[0, 1]`.

## Constraints (Optional but good practice)

* `2 <= nums.length <= 10^4`
* `-10^9 <= nums[i] <= 10^9`
* `-10^9 <= target <= 10^9`
* Only one valid answer exists.

## Approach (Hash Map/Dictionary)

A common and efficient approach is to use a hash map (dictionary in Python) to store the numbers encountered so far and their indices.

1.  Initialize an empty dictionary, say `seen_map`.
2.  Iterate through the `nums` array with both index (`i`) and value (`num`).
3.  For each `num`, calculate the complement needed: `complement = target - num`.
4.  Check if `complement` exists as a key in `seen_map`.
    * If yes, it means we have found the two numbers. Return the index stored in `seen_map[complement]` and the current index `i`.
    * If no, add the current number `num` and its index `i` to the `seen_map`.
5.  Since the problem guarantees exactly one solution, the loop will always find a pair.

This approach has a time complexity of $O(n)$ because we iterate through the list once, and dictionary lookups/insertions take average $O(1)$ time. The space complexity is $O(n)$ in the worst case to store the elements in the dictionary.