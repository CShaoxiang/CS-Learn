# python3
import sys

def BWT(text):

    n = len(text)

    #Generate all cyclic rotations : list[strings]
    rotations = [text[i:] + text[:i] for i in range(n)]

    # Sort rotations in lexiographical order
    rotations.sort()

    # Extract last column 
    bwt = ''.join(rotation[-1] for rotation in rotations )
    return bwt

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))