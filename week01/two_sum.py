# week1/two_sum.py

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Finds the indices of two numbers in a list that add up to a target value.

    Args:
        nums: A list of integers.
        target: The target sum.

    Returns:
        A list containing the indices of the two numbers that sum to the target.
        Returns an empty list if no solution is found (though the problem
        statement assumes exactly one solution exists).

    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
        >>> two_sum([3, 2, 4], 6)
        [1, 2]
        >>> two_sum([3, 3], 6)
        [0, 1]
    """
    seen_map = {}  # Dictionary to store number: index pairs

    for i, num in enumerate(nums):
        complement = target - num
        # Check if the complement needed to reach the target exists in our map
        if complement in seen_map:
            # If yes, we found the pair. Return indices.
            return [seen_map[complement], i]
        # If not, add the current number and its index to the map
        # We add it *after* the check to handle cases like [3, 3], target = 6 correctly
        # and avoid using the same element twice.
        seen_map[num] = i

    # According to the problem statement, a solution always exists,
    # but good practice might include handling the case where no solution is found.
    return [] # Or raise an exception

# --- Example Usage  ---
if __name__ == "__main__":
    # Example 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}") # Expected: [0, 1]
    print("-" * 20)

    # Example 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}") # Expected: [1, 2]
    print("-" * 20)

    # Example 3
    nums3 = [3, 3]
    target3 = 6
    result3 = two_sum(nums3, target3)
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}") # Expected: [0, 1]
    print("-" * 20)