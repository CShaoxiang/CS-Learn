# python3
import math

EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

# ---  Reads the matrix A and vector b
def ReadEquation():    
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

# --- Finds the best pivot row for the current step ---
def SelectPivotElement(a, used_rows, used_columns):
    """
    Finds the pivot element for Gaussian Elimination using partial pivoting.
    It determines the current step (column) based on used_columns,
    then finds the row >= step with the maximum absolute value in that column.

    Args:
        a: The coefficient matrix.
        used_rows: Boolean list indicating rows already used as pivot rows.
        used_columns: Boolean list indicating columns already processed.

    Returns:
        Position object containing the column (step) and the best row index.
        Returns Position(-1, -1) if all columns are processed.
    """
    size = len(a)
    # Determine the current column (step) to process
    pivot_col = 0
    while pivot_col < size and used_columns[pivot_col]:
        pivot_col += 1

    if pivot_col == size:
        return Position(-1, -1) # All columns processed

    # Find the row index >= pivot_col with the max absolute value in column pivot_col
    best_row = pivot_col
    max_abs_val = 0.0
    # We need to start search from pivot_col row
    if pivot_col < size: # Ensure we don't access index out of bounds if matrix is singular handled badly before
        max_abs_val = math.fabs(a[pivot_col][pivot_col])

        for r in range(pivot_col + 1, size):
            current_abs_val = math.fabs(a[r][pivot_col])
            # Check if this row 'r' has already served as a pivot row before?
            # No, standard partial pivoting just looks down the column from the current step.
            if current_abs_val > max_abs_val:
                max_abs_val = current_abs_val
                best_row = r
    else:
         # This case should ideally not be reached if called correctly within loop 0..size-1
         return Position(-1,-1)


    # Return the column we are processing and the row index containing the best pivot
    return Position(pivot_col, best_row)


def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column

# --- Performs the elimination step for the current pivot ---
def ProcessPivotElement(a, b, pivot_element):
    """
    Uses the pivot element (now at a[step][step] after swapping) to eliminate
    elements below it in the pivot column.

    Args:
        a: Coefficient matrix (modified in place).
        b: Right-hand side vector (modified in place).
        pivot_element: Position object. pivot_element.column contains the
                       current step index 'k'. The pivot value is a[k][k].
    """
    size = len(a)
    step = pivot_element.column # Current row/column index 'k'

    pivot_value = a[step][step]

    # Check for zero pivot (indicates singular matrix or dependency)
    if math.fabs(pivot_value) < EPS:
        # Cannot eliminate using a zero pivot.
        # If max element in column was zero, this column is dependent.
        # We simply skip the elimination for this column/step.
        # Back substitution will potentially reveal inconsistency or infinite solutions.
        return


    # Eliminate elements below the pivot in the current column ('step')
    for i in range(step + 1, size): # For each row 'i' below the pivot row 'step'
        factor = a[i][step] / pivot_value # Multiplier for the pivot row
        if math.fabs(factor) < EPS: # Skip if element is already effectively zero
            continue

        # Update row 'i' in matrix 'a': R_i = R_i - factor * R_step
        for j in range(step, size): # Iterate from the current column onwards
            a[i][j] -= factor * a[step][j]

        # Update corresponding element in vector 'b'
        b[i] -= factor * b[step]

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    if size == 0:
        return []

    used_columns = [False] * size
    used_rows = [False] * size

    # --- Forward Elimination Phase ---
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
    
     # --- Back Substitution Phase ---
    # Solves the upper triangular system Ax = b for x, storing result in b
    solution = [0.0] * size # Create a separate list for the solution
    for i in range(size - 1, -1, -1): # Iterate rows backward (n-1, n-2, ..., 0)
        if math.fabs(a[i][i]) < EPS:
            # Zero on diagonal after elimination means singular matrix
            if math.fabs(b[i]) > EPS:
                # Form 0 * x = non-zero --> Inconsistent system
               
                # Handle error: return empty list, raise exception, etc.
                return [] # Indicate failure
            else:
                # Form 0 * x = 0 --> Infinite solutions (free variable)
                # The problem asks for *a* solution. A common choice is 0.
              
                solution[i] = 0.0
                # Note: For robustness, one might need to track free variables.
        else:
            # Calculate sum of a[i][j] * x[j] for j > i
            sum_ax = 0.0
            for j in range(i + 1, size):
                sum_ax += a[i][j] * solution[j] # Use already computed solution values

            # Calculate x[i]
            solution[i] = (b[i] - sum_ax) / a[i][i]

    return solution # Return the computed solution vector


   

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    exit(0)
