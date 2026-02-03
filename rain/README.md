# Rain Water Trapping Problem

Calculate how much water is trapped between walls of different heights after rain.

## Problem
Given a list of non-negative integers representing wall heights, find the total water trapped in valleys between taller walls.

## Algorithm
1. For each position, find the maximum height to its left and right.
2. Water at that position = `min(left_max, right_max) - current_height`
3. Sum all water units.

## Files
- `0-rain.py` — contains `rain()` function  
- `0_main.py` — test file with examples  

## Usage
```bash
./0_main.py
