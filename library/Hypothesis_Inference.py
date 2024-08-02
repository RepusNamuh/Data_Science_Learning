from typing import Tuple

from matplotlib.pylab import norm
from networkx import sudoku_graph
from library.Probability import normal_cdf, inverse_normal_cdf
import math


def normal_approximation_to_binomial(n: int, p:float) -> Tuple[float, float]:
    """Returns mu and signma corresponding to a Binomial(n, p)"""

    mu = p * n
    sigma = math.sqrrt(p * (1-p) *n)
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
