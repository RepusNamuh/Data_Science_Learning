import sys
sys.path.append(r"f:\\Data_Science_Learning")

from typing import Tuple
from matplotlib.pylab import norm
from networkx import sudoku_graph
from library.Probability import normal_cdf, inverse_normal_cdf
import math

def normal_approximation_to_binomial(n: int, p:float) -> Tuple[float, float]:
    """Returns mu and signma corresponding to a Binomial(n, p)"""

    mu = p * n
    sigma = math.sqrt(p * (1-p) *n)
    return mu, sigma

def normal_prob_above(lo: float,
                      mu: float = 0, 
                      sigma: float = 1) -> float:
    """The probability that an N(mu, Sigma) is great than lo"""
    return 1 - normal_cdf(lo, mu, sigma)

def normal_prob_between(lo: float,
                        hi: float,
                      mu: float = 0, 
                      sigma: float = 1) -> float:
    """The probability that an N(mu, sigma) is between lo and hi"""
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

def normal_prob_outside(lo: float,
                        hi: float,
                      mu: float = 0, 
                      sigma: float = 1) -> float:
    """The probability that an N(mu, sigma) is not between lo and hi"""
    return 1 - normal_prob_between(lo, hi, mu, sigma)

def normal_upper_bound(p: float,
                       mu: float = 0,
                       sigma: float = 1) -> float:
    """Returns the z for which P(Z <= z) = p"""
    return inverse_normal_cdf(p, mu, sigma)

def normal_lower_bound(p: float,
                       mu: float = 0,
                       sigma: float = 1) -> float:
    """Returns the z for which P(Z >= z) = p"""
    return inverse_normal_cdf(1 - p, mu, sigma)

def normal_two_sided_bounds(p: float,
                            mu: float = 0,
                            sigma: float = 1) -> Tuple[float, float]:
    
    """Returns the symmetric (about the mean) bounds
        that contain the specified probability
        """
    
    tail_prob = (1 - p) / 2

    upper_bound = normal_lower_bound(tail_prob, mu, sigma)

    lower_bound = normal_upper_bound(tail_prob, mu, sigma)

    return lower_bound, upper_bound

def two_sided_p_value(x: float, mu: float = 0, sigma: float = 1) -> float:
    """How likely are we to see a value at least as extreme as x (in either direction)
    if our valyes are from an N(mu, sigma)
    """
    if x >= mu:
        return 2 * normal_prob_above(x, mu, sigma)
    else:
        return 2 * normal_cdf(x, mu, sigma)
    
def estimated_parameters(N: int, n: int) -> Tuple[float, float]:
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma

def a_b_test_statistic(N_A: int, n_A: int, N_B: int, n_B: int) -> float:
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

def B(alpha: float, beta: float) -> float:
    """A normalizing constant so that the total probability is 1"""
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)

def beta_pdf(x: float, alpha: float, beta: float) -> float:
    if x <= 0 or x >= 1:
        return 0
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)