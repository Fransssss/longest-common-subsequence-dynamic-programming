"""Entry point for demonstrating the Longest Common Subsequence dynamic programming solution."""

from lcs_dp import (
    build_lcs_table,
    build_lcs_table_with_animation,
    format_dp_table,
    reconstruct_lcs,
)


def _prompt_animation_choice() -> bool:
    """Ask the user whether to animate the DP table build, defaulting to yes."""
    choice = input("Show animated DP table construction? [Y/n]: ").strip().lower()
    return choice not in {"n", "no"}


def main() -> None:
    print("\n=== Longest Common Subsequence (Dynamic Programming) ===\n")
    first = input("Enter the first string: ").strip()
    second = input("Enter the second string: ").strip()

    show_animation = _prompt_animation_choice()
    if show_animation:
        table = build_lcs_table_with_animation(first, second)
    else:
        table = build_lcs_table(first, second)
    lcs = reconstruct_lcs(table, first, second)

    print("\nDP Table: (rows = prefixes of first string, columns = prefixes of second string)\n")
    print(format_dp_table(table, first, second))
    print(f"\nLength of LCS: {len(lcs)}")
    print(f"LCS: {lcs if lcs else '<empty subsequence>'}\n")


if __name__ == "__main__":
    main()
