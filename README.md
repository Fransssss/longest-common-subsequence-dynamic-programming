# Longest Common Subsequence (Dynamic Programming)

## Problem Description
Given two input strings, the Longest Common Subsequence (LCS) problem asks for the longest sequence of characters that appear in both strings while preserving their relative order (not necessarily contiguously). For example, the strings `ABCBDAB` and `BDCAB` share the LCS `BCAB`.

## Why Dynamic Programming?
- **Overlapping subproblems:** When exploring LCS for prefixes of the two strings, the same sub-prefix pairs appear repeatedly. Caching the length for each pair avoids recomputation.
- **Optimal substructure:** The optimal LCS for prefixes `a[:i]` and `b[:j]` depends on optimal LCS lengths of smaller prefixes. If the current characters match, we extend the best solution for `a[:i-1]` and `b[:j-1]`; otherwise, we keep the longer of skipping one character from either string.

## DP Table Explanation
We build a $(m+1) \times (n+1)$ table, where $m$ and $n$ are the string lengths. Cell $(i, j)$ stores the length of the LCS between prefixes `a[:i]` and `b[:j]`. The first row and column represent comparisons with the empty prefix and stay zero. We iterate row by row so that the required neighbors `table[i-1][j]`, `table[i][j-1]`, and `table[i-1][j-1]` are already computed. Walking backwards through the filled table reconstructs one valid LCS.

## Complexity
- **Time:** $O(m \times n)$ because every cell in the table is filled exactly once.
- **Space:** $O(m \times n)$ to store the table that tracks every prefix combination. (It can be reduced to $O(\min(m, n))$ if we only care about the LCS length.)

## Running the Program
1. Ensure Python 3.8+ is installed.
2. From the project root run:
	```bash
	python main.py
	```
3. Choose whether to watch the slow-paced DP table animation (default **Yes**) and enter the two strings when prompted. The script prints the DP table, the LCS length, and one actual subsequence.

## Video Demo
If video not show, open the video directly from the repo (.mp4 file)
