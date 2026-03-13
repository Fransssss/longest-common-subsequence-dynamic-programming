# Longest Common Subsequence — Dynamic Programming

## Problem Description

Given two strings, find the **Longest Common Subsequence (LCS)**: the longest sequence of characters that appears in the same relative order in both strings, but not necessarily contiguously.

**Example**

```
string1 = "ABCBDAB"
string2 = "BDCAB"

LCS = "BCAB"  (length 4)
```

Other valid LCS answers of length 4 exist (e.g. "BDAB"), because there can be multiple optimal subsequences.

---

## Why Dynamic Programming?

The naïve recursive approach recomputes the same subproblems many times, leading to exponential time complexity. Dynamic Programming (DP) solves this by storing intermediate results so each subproblem is computed only once.

Two key DP properties are satisfied:

1. **Overlapping Subproblems** – The LCS of two strings depends on the LCS of their shorter prefixes, and those shorter-prefix subproblems are reused many times across the full computation.

2. **Optimal Substructure** – The optimal solution to the full problem is built from the optimal solutions to its subproblems:
   - If `s1[i-1] == s2[j-1]`, extend the LCS of the previous prefixes by 1.
   - Otherwise, take the maximum of ignoring the last character of either string.

---

## Project Structure

```
.
├── lcs_dp.py   # Core DP logic: build table, get length, backtrack LCS
├── main.py     # Entry point — sets up inputs and prints results
└── README.md
```

---

## How to Run

```bash
python main.py
```

**Expected output**

```
==================================================
Longest Common Subsequence — Dynamic Programming
==================================================

String 1 : ABCBDAB
String 2 : BDCAB

DP Table:
--------------------------------------------------
            B    D    C    A    B
  ------------------------------------------
  |   0    0    0    0    0    0
A |   0    0    0    0    1    1
B |   0    1    1    1    1    2
C |   0    1    1    2    2    2
B |   0    1    1    2    2    3
D |   0    1    2    2    2    3
A |   0    1    2    2    3    3
B |   0    1    2    2    3    4

Length of LCS : 4
LCS           : BCAB
==================================================
```

---

## Explanation of the DP Table

The table is `(m+1) × (n+1)` where `m = len(string1)` and `n = len(string2)`.

| Cell `dp[i][j]` | Meaning |
|---|---|
| 0 (first row/column) | Base case: LCS with an empty prefix is always 0 |
| `dp[i][j]` (interior) | LCS length of `string1[:i]` and `string2[:j]` |

**Filling the table:**

```
if string1[i-1] == string2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1   # characters match — extend previous LCS
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])   # take the best without current char
```

The actual subsequence is recovered by **backtracking** from `dp[m][n]` to `dp[0][0]`, following diagonal moves when characters match.

---

## Video Demo

Watch the LCS Dynamic Programming demonstration below:

[LcsDP.mp4](LcsDP.mp4)

---

## Complexity

| | Complexity |
|---|---|
| **Time** | O(m × n) — fill every cell of the `(m+1) × (n+1)` table once |
| **Space** | O(m × n) — store the full DP table; reducible to O(min(m, n)) if only the length is needed |

where `m` and `n` are the lengths of the two input strings.