#!/usr/bin/python3
"""
Module for calculating rainwater retention between walls.
"""


def rain(walls):
    """
    Calculate how much water will be retained after it rains.

    Given a list of non-negative integers representing wall heights,
    this function calculates the total amount of rainwater that can
    be trapped between the walls.

    Args:
        walls (list): List of non-negative integers representing wall heights

    Returns:
        int: Total amount of rainwater retained (in square units)

    Algorithm:
        For each position, water level is determined by:
        - Maximum wall height to its left
        - Maximum wall height to its right
        - Water trapped = min(max_left, max_right) - current_height

    Example:
        >>> rain([0, 1, 0, 2, 0, 3, 0, 4])
        6
        >>> rain([2, 0, 0, 4, 0, 0, 1, 0])
        6
    """
    if not walls or len(walls) < 3:
        return 0

    n = len(walls)
    total_water = 0

    # Calculate maximum height to the left of each position
    left_max = [0] * n
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Calculate maximum height to the right of each position
    right_max = [0] * n
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate water at each position
    for i in range(n):
        # Water level at position i is the minimum of max heights on both sides
        water_level = min(left_max[i], right_max[i])
        # Subtract the wall height to get water amount
        if water_level > walls[i]:
            total_water += water_level - walls[i]

    return total_water
