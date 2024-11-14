from library.Linear_Algebra import Vector, dot, distance, scalar_multiply, add, vector_mean
from typing import Callable, TypeVar, List, Iterator
import random

def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

def difference_quotient(f: Callable[[Vector], float],
                        i: int,
                        h: float) -> float:
    return (f(i + h) - f(i))/h

def partial_difference_quotient(f: Callable[[Vector], float],
                                v: Vector,
                                i: int,
                                h: float) -> float:
    w = [v_j + (h if j == i else 0)
         for j, v_j in enumerate(v)]
    return (f(w) - f(v))/h

def estimate_gradient(f: Callable[[Vector], float],
                        v: Vector,
                        h: float = 0.0001):
        return [partial_difference_quotient(f, v, i, h)
                for i in range(len(v))]

def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
    """Moves 'step_size' in the 'gradient' direction from 'v'"""
    assert len(v) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(v, step)

def sum_of_squares_gradient(v: Vector) -> Vector:
    return [2 * v_i for v_i in v]

def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
    slope, intercept = theta
    predicted = slope * x + intercept
    error = (predicted - y)
    squared_error = error ** 2
    grad = [2 * error * x, 2 * error]
    return grad

def minibatches(dataset: List[Vector],
                batch_size: int,
                shuffle: bool = True) -> Iterator[List[Vector]]:
    """Generates 'batch_size' batches from the data"""
    batch_starts = [start for start in range(0, len(dataset), batch_size)]

    if shuffle: random.shuffle(batch_starts)

    for start in batch_starts:
        end = start + batch_size
        yield dataset[start:end]

        