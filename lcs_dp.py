"""Utility functions for solving Longest Common Subsequence (LCS) via dynamic programming.

The LCS problem demonstrates two important DP traits:
1. Overlapping subproblems: LCS(i, j) reuses the solutions of LCS(i-1, j), LCS(i, j-1),
   and LCS(i-1, j-1) for the same prefixes repeatedly. Memoizing these results in a
   table spares us from recomputing the same sub-strings.
2. Optimal substructure: The optimal LCS for prefixes a[:i] and b[:j] depends on
   optimal solutions to smaller prefixes. If characters match we extend the optimal
   solution of (i-1, j-1); otherwise we pick the longer solution between skipping a
   character from either string.
"""

import os
import time
from typing import List


def build_lcs_table(a: str, b: str) -> List[List[int]]:
    """Construct the DP table where cell (i, j) stores the LCS length for a[:i] and b[:j]."""
    rows = len(a) + 1
    cols = len(b) + 1
    table = [[0 for _ in range(cols)] for _ in range(rows)]

    # The table is filled row by row so that dependencies on upper/left neighbors exist already.
    for i in range(1, rows):
        for j in range(1, cols):
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table


def reconstruct_lcs(table: List[List[int]], a: str, b: str) -> str:
    """Walk the DP table backwards to rebuild one LCS string."""
    i = len(a)
    j = len(b)
    result: List[str] = []

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            result.append(a[i - 1])
            i -= 1
            j -= 1
        elif table[i - 1][j] >= table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(result))


def format_dp_table(table: List[List[int]], a: str, b: str) -> str:
    """Return a human-friendly string representation of the DP table."""
    header = [" ", " "] + list(b)
    lines = []
    header_line = "  ".join(f"{ch:>2}" for ch in header)
    lines.append(header_line)

    for i, row in enumerate(table):
        label = " " if i == 0 else a[i - 1]
        row_values = "  ".join(f"{cell:>2}" for cell in row)
        lines.append(f"{label:>2}  {row_values}")

    return "\n".join(lines)


def build_lcs_table_with_animation(a: str, b: str, delay: float = 0.4) -> List[List[int]]:
    """Fill the DP table while animating progress so the build process is visible."""
    table = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

            _render_animation_frame(table, a, b, i, j)
            time.sleep(delay)

    return table


def _render_animation_frame(table: List[List[int]], a: str, b: str, i: int, j: int) -> None:
    """Clear the terminal and show the current DP table state."""
    _clear_terminal()
    print("Building DP table...\n")
    print(format_dp_table(table, a, b))
    print(
        f"\nFilled cell ({i}, {j}) comparing prefixes a[:{i}] and b[:{j}] - dependencies already solved."
    )


def _clear_terminal() -> None:
    """Reset the terminal view using ANSI codes so the animation feels smooth."""
    if os.name == "nt":
        os.system("cls")
    else:
        print("\033[2J\033[H", end="")
