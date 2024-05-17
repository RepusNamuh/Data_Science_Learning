from typing import Tuple, List, Callable
import Vectors

Vector = Vectors.Vector
Matrix = List[List[float]]


def shape(A: Matrix) -> Tuple[int, int]:
    """Returns (# of rows of A, # of columns of A)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of A (as a Vector)"""
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    """Returns the j-th column of A (as a Vector)"""
    return [A_i[j] for A_i in A]

def make_matrix(num_rows: int, 
                num_cols: int, 
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """Returns a num_rows x num_cols matrix
    whose (i, j)-th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j) 
             for j in range(num_cols)] 
                for i in range(num_rows)]   

def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

print(identity_matrix(10000))

