"""
A simple program to solve a linear system in 2D using elementary row operations.

The rows are referred to by index, so they are offset by 1, e.g. row 1
is at index 0, row 2 is at index 1. There is no user interface, just sample
cases.
"""

__author__ = 'Hossain, Sadman'


# Optional import
from fractions import Fraction


def swap(m, r1, r2):
    """Swap the rows r1 and r2 in matrix m."""
    tmp = m[r1]
    m[r1] = m[r2]
    m[r2] = tmp
    return m


def multiply_row(m, r, k):
    """Multiply row r by scalar k in matrix m."""
    for i in range(len(m[r])):
        m[r][i] = Fraction(k*m[r][i])
    return m


def divide_row(m, r, k):
    """Divide row r by scalar k in matrix m."""
    for i in range(len(m[r])):
        m[r][i] = Fraction(m[r][i] / k)
    return m


def add_rows(m, r1, r2):
    """Add row r1 and r2 and replace row r1 with the result in matrix m."""
    for i in range(len(m[r1])):
        m[r1][i] = m[r1][i] + m[r2][i]
    return m


def subtract_rows(m, r1, r2):
    """Subrtact row r2 from r1 and replace row r1 with the result in matrix m."""
    for i in range(len(m[r1])):
        m[r1][i] = m[r1][i] - m[r2][i]
    return m

    
def print_solution(m):
    """Determine and print the solution of the linear system represented by
    the augmented matrix m.

    Assume the matrix is in reduced row echelon form:
    ┌               ┐
    │ 1     0     x │
    │ 0     1     y │
    └               ┘
    There can be one solution, no solution, or infinite solutions.
    """
    if m[1][2] != 0 and m[1][1] == 0:
        print('No solutions exist.')
        return

    inf = True
    for val in m[1]:
        if val != 0:
            inf = False
            break
    if inf:
        print('Infinite solutions.')
        return
    
    print('The solution is: x = {}, y = {}'.format(m[0][2],m[1][2]))
        

def print_matrix(m):
    """Print 2 x 3 matrix m nicely.

    Quick-and-dirty matrix brackets. Adjust paramter W as necessary.
    """

    W = 5
    
    print('┌', ' '*W*3, '┐', sep='')
    for row in m:
        print('│', end='')
        for col in row:
            print('{!s:^{width}}'.format(col, width=W), end='')
        print('│')
    print('└', ' '*W*3, '┘', sep='')
    

def main():
    print('One solution example (x = 3, y = 0).')
    M = [[1, 2, 3],
         [2, -1, 6]]
    print('M =')
    print_matrix(M)
    
    print('swap rows:')
    swap(M, 0, 1)
    print('M =')
    print_matrix(M)
    
    print('multiply row 2 by 2:')
    multiply_row(M, 1, 2)
    print('M =')
    print_matrix(M)

    print('subtract row 1 from row 2:')
    subtract_rows(M, 1, 0)
    print('M =')
    print_matrix(M)

    print('divide row 2 by 5:')
    divide_row(M, 1, 5)
    print('M =')
    print_matrix(M)
    
    print('add row 2 to row 1:')
    add_rows(M, 0, 1)
    print('M =')
    print_matrix(M)

    print('divide row 1 by 2:')
    divide_row(M, 0, 2)
    print('M =')
    print_matrix(M)

    print('solve:')
    print_solution(M)

    print()
    
    print('Infinite solutions example (parallel, coincident lines).')
    N = [[1, 0, 3],
         [0, 0, 0]]     # Second equation eqvialent to 0y = 0.
    print('N =')
    print_matrix(N)
    print_solution(N)

    print()
    
    print('No solutions example (parallel, non-intersecting lines).')
    P = [[1, 0, -5],
         [0, 0, 6]]     # Second equation equivalent to 0y = 6.
    print('P =')
    print_matrix(P)
    print_solution(P)

    print()
    
    print('Optional: using Fraction (x = 5/2, y = 1).')
    Q = [[2, 1, 6],
         [2, -3, 2]]
    
    print('Q = ')
    print_matrix(Q)

    print('subtract row 1 from row 2:')
    subtract_rows(Q, 1, 0)
    print('Q = ')
    print_matrix(Q)

    print('divide row 2 by -4')
    divide_row(Q, 1, -4)
    print('Q = ')
    print_matrix(Q)

    print('subtract row 2 from row 1:')
    subtract_rows(Q, 0, 1)
    print('Q = ')
    print_matrix(Q)

    print('divide row 1 by 2:')
    divide_row(Q, 0, 2)
    print('Q = ')
    print_matrix(Q)

    print('solution:')
    print_solution(Q)

    
if __name__=='__main__':
    main()