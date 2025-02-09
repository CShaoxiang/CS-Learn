# python3
import sys

def InverseBWT(bwt):
    
    n = len(bwt)

    # Step 1: Create the First Column by sorting the BWT
    first_column = sorted(bwt)
    
    # Step 2: Create a mapping from Last Column to First Column
    # We need to track the positions of each character in both columns
    last_to_first = []

    # Create a count array to track occurrences of each character
    count = {}
    for char in bwt:

        # get the number of occurence by character keys, if null , return 0 
        count[char] = count.get(char,0) +1

    
    cumulative_count = {}
    total = 0

    #Marks starting position of each char in the first column
    for char in sorted(count.keys()):
        cumulative_count[char] = total
        total += count[char]

    
    # Build the LastToFirst mapping
    last_to_first = []
    for char in bwt:
        last_to_first.append(cumulative_count[char])
        cumulative_count[char] += 1


    # Step 3: Reconstruct the original string
    original_string = []
    current_row = 0  # Start at the row containing '$'
    
    for _ in range(n):
        # Append the character in the First Column at the current row
        original_string.append(first_column[current_row])
        # Move to the next row using the LastToFirst mapping
        current_row = last_to_first[current_row]
    
    # The original string is constructed in reverse order, so reverse it
    original_string = ''.join(original_string[::-1])
    
    return original_string

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))