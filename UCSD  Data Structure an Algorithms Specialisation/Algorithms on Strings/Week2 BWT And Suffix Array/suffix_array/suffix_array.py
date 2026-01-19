# python3
import sys



def sort_characters(S : str):
  """
    Sorts the characters of the string S using counting sort and returns their order in sorted lexicographic order.

    :param S: The input string
    :return: The order array, where order[i] gives the index in S of the ith smallest character.
  """
  n = len(S)
  alphabet_size = 256  # basic ASCII character class size 
  order = [0] * n
  count =[0] * alphabet_size

  # Count Occurrences
  for i in range(n):
    count[ord(S[i])] += 1 

  # Compute cumulative sum ,start at index 1 
  for i in range(1,alphabet_size):
    count[i] += count[i-1]

  # Step 3: Place indices in correct position
  for i in range(n - 1, -1, -1):  # Traverse string in reverse
      c = ord(S[i])  # Get ASCII value
      count[c] -= 1
      order[count[c]] = i  # Place character index in sorted order


  return order 

def compute_char_classes(S,order):
  '''
  Assign class labels to suffixes based on their first character.

  - After sorting single characters, identical characters should belong to the same equivalence class.
  - Each distinct character is assigned a unique class number.
  - Steps:
    1. Initialize `class[order[0]] = 0`.
    2. Traverse `order` and assign a new class number whenever a new character appears.
    3. Otherwise, inherit the previous class.

    Returns:
      list: An array where each index represents the class of the suffix 
            starting at that index in `S`.
'''
  n = len(S)
  char_class = [0] * n 
  char_class[order[0]] = 0 

  for i in range(1,n):

    if S[order[i]] != S[order[i-1]]:
      char_class[order[i]] = char_class[order[i-1]]+1

    else:
      char_class[order[i]] = char_class[order[i-1]]

  return char_class


def sort_double(S, L ,order,char_class):
  n = len(S)
  count = [0] * n
  new_oder = [0] * n

  for i in range(n):
    count[char_class[i]] += 1

  # Compute cumulative sum
  for i in range(1,n):
    count[i] += count[i-1]

  for i in range(n-1,-1,-1):
    start = (order[i] - L + n) % n 

    c1 = char_class[start]
    count[c1] -=1
    new_oder[count[c1]] = start 

  return new_oder

def update_classes(new_order , char_class , L):
  n = len(new_order)

  new_class = [0] * n 
  new_class[new_order[0]] = 0

  for i in range(1,n):
    cur,prev = new_order[i], new_order[i-1]

    mid,mid_prev = (cur + L ) % n , (prev + L) % n 
    if char_class[cur] != char_class[prev] or char_class[mid] != char_class[mid_prev]:
      new_class[cur] = new_class[prev] +1

    else:
      new_class[cur] = new_class[prev]

  return new_class  

def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  order = sort_characters(text)
  char_class = compute_char_classes(text,order)
  L = 1

  while L < len(text):
    order = sort_double(text, L , order , char_class)
    char_class = update_classes(order,char_class,L)

    L = 2 * L
  return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
