"""
main.py - Entry point for the Longest Common Subsequence (LCS) demo.

Run with:
    python main.py
"""

from lcs_dp import build_dp_table, get_lcs_length, backtrack_lcs, print_dp_table


def main():
    # Example strings from the problem statement
    string1 = "ABCBDAB"
    string2 = "BDCAB"

    print("=" * 50)
    print("Longest Common Subsequence — Dynamic Programming")
    print("=" * 50)
    print(f"\nString 1 : {string1}")
    print(f"String 2 : {string2}\n")

    # Step 1: Build the DP table
    # The table stores LCS lengths for every pair of prefixes of the two strings.
    dp = build_dp_table(string1, string2)

    # Step 2: Display the DP table
    print("DP Table:")
    print("-" * 50)
    print_dp_table(dp, string1, string2)
    print()

    # Step 3: Extract the LCS length from the bottom-right cell of the table
    length = get_lcs_length(dp)
    print(f"Length of LCS : {length}")

    # Step 4: Backtrack through the table to find the actual LCS string
    lcs = backtrack_lcs(dp, string1, string2)
    print(f"LCS           : {lcs}")
    print("=" * 50)


if __name__ == "__main__":
    main()
