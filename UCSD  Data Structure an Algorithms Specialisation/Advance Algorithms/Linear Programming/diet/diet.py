# python3
from sys import stdin
import itertools
import math
import numpy as np  # Using numpy for matrix ops simplifies things greatly

# --- Gaussian Elimination Solver ---
# Returns: (status, solution_vector)
# status: 1 (unique), 0 (none), 2 (infinite)
# solution_vector: the unique solution, or None
# NOTE: This basic version doesn't return direction vectors for infinite case
#       and might struggle with numerical stability in edge cases.
#       A more robust solver might be needed for all edge cases.
EPS = 1e-9 # Reduced precision slightly for stability

def solve_system(matrix, rhs):
    try:
        # Use numpy's linear algebra solver
        A = np.array(matrix, dtype=float)
        b = np.array(rhs, dtype=float)
        if np.linalg.matrix_rank(A) < A.shape[1]:
             # Potentially infinite solutions or no solution if inconsistent
             # Check for consistency: rank(A) == rank([A|b])
             Ab = np.concatenate((A, b[:, np.newaxis]), axis=1)
             if np.linalg.matrix_rank(Ab) > np.linalg.matrix_rank(A):
                 return (0, None) # No solution (inconsistent)
             else:
                 # Infinite solutions - np.linalg.solve will fail
                 # np.linalg.lstsq can find a particular solution
                 # For this problem, detecting infinity requires more work (finding null space)
                 # Let's treat it as non-unique vertex for now, potentially missing infinity cases
                 # Find a least-squares solution as *one* possible point on the line/plane
                 x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
                 # Check if this least-squares solution actually satisfies Ax=b closely
                 if np.allclose(A @ x, b, atol=EPS*10): # Use slightly larger tolerance after lstsq
                     # Treat this particular solution as a candidate point
                     # We are IGNORING the infinite solutions / unbounded aspect here primarily
                      return (2, list(x)) # Indicate 'infinite', return one solution
                 else:
                      # lstsq found something, but it doesn't solve Ax=b well -> likely inconsistent
                      return (0, None)

        else:
             # Potentially unique solution
             x = np.linalg.solve(A, b)
             return (1, list(x)) # Unique solution
    except np.linalg.LinAlgError:
        # Singular matrix or other linear algebra error
        # Could be no solution or infinite solutions. Let's treat as non-unique vertex.
        # Check consistency again just in case solve failed but lstsq might work
        try:
            A = np.array(matrix, dtype=float)
            b = np.array(rhs, dtype=float)
            Ab = np.concatenate((A, b[:, np.newaxis]), axis=1)
            if np.linalg.matrix_rank(Ab) > np.linalg.matrix_rank(A):
                 return (0, None) # No solution (inconsistent)
            else:
                 x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
                 if np.allclose(A @ x, b, atol=EPS*10):
                     return (2, list(x))
                 else:
                     return (0, None)
        except: # Catch any further errors
            return (0, None) # Failed to solve


def solve_diet_problem(n, m, A, b, c):
    # Combine constraints Ax <= b and -x <= 0 (x >= 0)
    # Add non-negativity constraints to A and b
    A_aug = A + [[(-1.0 if i == j else 0.0) for j in range(m)] for i in range(m)]
    b_aug = b + [0.0] * m
    num_total_constraints = n + m

    best_pleasure = -float('inf')
    best_x = None
    found_feasible_vertex = False

    indices = list(range(num_total_constraints))

    # Iterate through all combinations of m constraints to form potential bases
    for basis_indices in itertools.combinations(indices, m):
        # Form the square matrix A_s and rhs b_s for the system A_s * x = b_s
        A_s = [A_aug[i] for i in basis_indices]
        b_s = [b_aug[i] for i in basis_indices]

        # Solve the m x m system
        status, current_x = solve_system(A_s, b_s)

        # We only care about unique intersection points (vertices) for finding the optimum
        # The infinite solution case is tricky; we primarily check the returned point's feasibility
        if status == 1 or status == 2: # Unique or a point from infinite solutions
            if current_x is None: continue # Should not happen if status is 1 or 2, but safety check

            # Check feasibility against ALL n+m original constraints
            is_feasible = True
            for i in range(num_total_constraints):
                try:
                    lhs = sum(A_aug[i][j] * current_x[j] for j in range(m))
                    # Use tolerance EPS for comparison
                    if lhs > b_aug[i] + EPS:
                        is_feasible = False
                        break
                except IndexError:
                    is_feasible = False # Should not happen with correct indexing
                    break

            if is_feasible:
                found_feasible_vertex = True
                pleasure = sum(c[j] * current_x[j] for j in range(m))

                # Check for potential unboundedness (heuristic: very large pleasure)
                # This is NOT robust. A proper check needs direction vectors.
                if pleasure > 1e17: # Arbitrarily large number - adjust if needed
                     # We guess it might be unbounded
                     # Simplex would detect this properly by finding a column
                     # with negative cost and all non-positive constraint coefficients.
                     return [1, None] # Output Infinity

                if pleasure > best_pleasure:
                    best_pleasure = pleasure
                    best_x = current_x
        # else status == 0 (No solution for this basis) -> ignore

    # --- Final Decision ---
    if not found_feasible_vertex:
        # Check for trivial infeasibility if n=0? Problem says n>=1.
        return [-1, None] # No solution
    elif best_x is None:
         # This might happen if only infinite solutions were found and the check failed,
         # or if numerical issues occurred.
         # If found_feasible_vertex is True, means *some* point worked,
         # but maybe didn't update best_x correctly? Fallback to No solution is safer.
         return [-1, None]
    else:
         # Check if all elements of best_x are non-negative (within tolerance)
         # This should already be covered by feasibility check, but double-check
         final_check_x = np.array(best_x)
         if np.any(final_check_x < -EPS):
              # print("Warning: Optimal x found violates non-negativity slightly.", file=sys.stderr)
              # Decide how strict to be. Might indicate numerical instability.
              # For safety, maybe return No Solution if this happens?
              # Or maybe try to clamp negative values near zero to zero?
              # Clamping: best_x = [max(0.0, val) for val in best_x]
              pass # Let it pass for now, feasibility check should handle it

         # Check if the best pleasure found is still -inf (shouldn't happen if feasible)
         if best_pleasure == -float('inf'):
             return [-1, None]

         return [0, best_x] # Bounded solution

# --- Main execution part ---
try:
    n, m = list(map(int, stdin.readline().split()))
    A = []
    for i in range(n):
      line = list(map(int, stdin.readline().split()))
      if len(line) != m: raise ValueError("Incorrect number of coefficients in A")
      A.append(line)
    b = list(map(int, stdin.readline().split()))
    if len(b) != n: raise ValueError("Incorrect number of elements in b")
    c = list(map(int, stdin.readline().split()))
    if len(c) != m: raise ValueError("Incorrect number of elements in c")

    anst, ansx = solve_diet_problem(n, m, A, b, c)

    if anst == -1:
      print("No solution")
    elif anst == 0:
      print("Bounded solution")
      # Ensure ansx is not None before formatting
      if ansx is not None:
           print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
      else:
           # This case indicates an internal error, should have been caught earlier
           print("Error: Bounded solution state but no solution vector found.")
           # Or maybe revert to No Solution if ansx is None?
           # print("No solution") # Safer fallback?
    elif anst == 1:
      print("Infinity")

except Exception as e:
    # In a contest, might hide the error, but useful for debugging
    # print(f"An error occurred: {e}", file=sys.stderr)
    # Default to "No solution" or another appropriate error state if input fails
    print("No solution") # Safest default on error