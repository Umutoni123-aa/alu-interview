# Minimum Operations

Calculate the fewest number of operations to get exactly n 'H' characters in a file, starting with a single 'H'.

## Operations Available
- Copy All — Copy all characters currently in the file  
- Paste — Paste the previously copied characters  

## Problem
Given a number n, calculate the minimum number of operations to result in exactly n 'H' characters.

## Algorithm
Uses prime factorization:  
- Minimum operations = sum of all prime factors of n  
- Each prime factor represents an optimal multiplication step  

Example: n = 12 → 2 × 2 × 3 → operations = 2 + 2 + 3 = 7  

For n = 9:  
- 9 = 3 × 3  
- H → HHH (3 ops) → HHHHHHHHH (3 more ops) → Total 6 ops  

## Files
- `0-minoperations.py` — contains `minOperations()` function  
- `0_main.py` — test file with examples  

## Requirements
- Python 3.4.3  
- Ubuntu 14.04 LTS  
- PEP 8 style compliance  
- All files must be executable  

## Usage
```bash
./0_main.py

