"""
lcs_dp.py - Longest Common Subsequence using Dynamic Programming

Dynamic Programming Concepts Demonstrated:
-------------------------------------------
1. Overlapping Subproblems:
   The LCS problem can be broken into smaller subproblems: finding the LCS of
   prefixes of the two strings. These subproblems overlap because, for example,
   lcs("ABC", "BD") depends on lcs("AB", "B") and lcs("ABC", "B"), which in turn
   share even smaller subproblems. Instead of recomputing them recursively,
   we store results in a 2D table (memoization/tabulation).

2. Optimal Substructure:
   The solution to the full problem can be constructed from optimal solutions
   to its subproblems:
   - If s1[i-1] == s2[j-1], then dp[i][j] = dp[i-1][j-1] + 1
     (extend the LCS of the smaller prefixes by the matching character).
   - Otherwise, dp[i][j] = max(dp[i-1][j], dp[i][j-1])
     (take the best LCS without the current character from either string).
"""


def build_dp_table(s1: str, s2: str) -> list[list[int]]:
    """
    Build the DP table for the Longest Common Subsequence problem.

    The table has dimensions (m+1) x (n+1), where m = len(s1) and n = len(s2).
    dp[i][j] holds the length of the LCS of s1[:i] and s2[:j].

    Base cases:
        dp[i][0] = 0 for all i  (LCS with empty string is 0)
        dp[0][j] = 0 for all j  (LCS with empty string is 0)

    Recurrence:
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    """
    m = len(s1)
    n = len(s2)

    # Initialise the (m+1) x (n+1) table with zeros.
    # The extra row/column serve as base cases (empty-prefix boundaries).
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                # Characters match: extend the LCS found for the previous prefixes.
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Characters don't match: carry forward the best result obtained
                # by either ignoring s1[i-1] or ignoring s2[j-1].
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp


def get_lcs_length(dp: list[list[int]]) -> int:
    """
    Return the length of the LCS from the bottom-right cell of the DP table.
    dp[-1][-1] holds the LCS length for the full strings.
    """
    return dp[-1][-1]


def backtrack_lcs(dp: list[list[int]], s1: str, s2: str) -> str:
    """
    Backtrack through the DP table to reconstruct the actual LCS string.

    Starting from dp[m][n], we walk back to dp[0][0]:
    - If s1[i-1] == s2[j-1], the character belongs to the LCS; prepend it and
      move diagonally (i-1, j-1).
    - Otherwise, move in the direction of the larger neighbouring value
      (up if dp[i-1][j] >= dp[i][j-1], else left).
    """
    i = len(s1)
    j = len(s2)
    lcs_chars = []

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            # This character is part of the LCS.
            lcs_chars.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            # Move toward the cell with the larger value (upward).
            i -= 1
        else:
            # Move toward the cell with the larger value (leftward).
            j -= 1

    # Characters were appended in reverse order; reverse to get the LCS.
    lcs_chars.reverse()
    return "".join(lcs_chars)


def print_dp_table(dp: list[list[int]], s1: str, s2: str) -> None:
    """
    Print the DP table in a human-readable grid format.

    Rows correspond to characters of s1 (with an empty-string header row),
    and columns correspond to characters of s2 (with an empty-string header column).
    """
    COL_WIDTH = 4    # width of each cell value field (e.g. "   0" or "   4")
    COL_SEP = "  "  # separator between columns

    # Header row: label indent + one empty column for the base case + s2 characters
    header_labels = " " + s2  # leading space represents the base (empty-prefix) column
    header = "     " + COL_SEP.join(f"{c:>{COL_WIDTH}}" for c in header_labels)
    print(header)
    print("  " + "-" * (len(header) - 2))

    for i, row in enumerate(dp):
        # Row label: blank for the base row, or the corresponding character of s1
        label = " " if i == 0 else s1[i - 1]
        row_str = COL_SEP.join(f"{val:{COL_WIDTH}}" for val in row)
        print(f"{label} | {row_str}")
