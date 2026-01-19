# python3
import sys


def construct_lps(pattern, lps):
    """
    Constructs the Longest Prefix Suffix (LPS) array used in the KMP algorithm.
    lps[i] stores the length of the longest proper prefix of pattern[0..i]
    which is also a suffix of pattern[0..i].

    Args:
        pattern (str): The pattern string.
        lps (List[int]): The array to be filled with LPS values.
    """
    len_ = 0  # Length of the previous longest prefix suffix
    m = len(pattern)

    lps[0] = 0  # lps[0] is always 0
    i = 1

    # Build the lps array from index 1 to m - 1
    while i < m:
        
        # update lcp of pattern[i] by comparing pattern[i] with pattern[i-1]
        if pattern[i] == pattern[len_]:

            len_ += 1
            lps[i] = len_    
            i += 1
        else:
            # Mismatch after len_ matches
            if len_ != 0:
                # Try the previous longest prefix suffix
                len_ = lps[len_ - 1]
            else:
                # No proper prefix-suffix found
                lps[i] = 0
                i += 1

def find_pattern(pattern, text):
    """
    Finds all occurrences of the given pattern in the given text using the KMP algorithm.

    Args:
        pattern (str): The pattern to search for.
        text (str): The text in which to search.

    Returns:
        List[int]: A list of starting indices where the pattern is found in the text.
    """
    n = len(text)
    m = len(pattern)

    lps = [0] * m  # Longest Prefix Suffix array
    result = []    # Stores positions of matches

    # Preprocess the pattern to fill lps[]
    construct_lps(pattern, lps)

    i = 0  # index for text
    j = 0  # index for pattern

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                # A full match of the pattern was found
                result.append(i - j)
                j = lps[j - 1]  # Continue searching for next match
        else:
            if j != 0:
                # Use the lps array to avoid unnecessary comparisons
                j = lps[j - 1]
            else:
                i += 1

    return result



if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

