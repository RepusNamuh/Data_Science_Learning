import math, random
from collections import Counter
import matplotlib.pyplot as plt
def uniform_pdf(x: float) -> float:
    if x < 0: return 0
    elif x < 1: return x
    else: return 1

def normal_pdf(x: float, mu:float = 0, sigma: float = 1) -> float:
    above = (x - mu) ** 2
    below = 2 * (sigma**2)
    outside = 1/(math.sqrt(2*math.pi)* sigma)
    return (math.exp(-above/below) * outside)

def normal_cdf(x: float, mu:float = 0, sigma: float = 1) -> float:
    return (1 + math.erf((x- mu) / math.sqrt(2) / sigma)) / 2

def bernoulli_trial(p: float) -> int:
    """Returns 1 with probability p and 0 with probability 1-p"""
    value = random.random()
    print(value)
    return 1 if value < p else 0

def binomial(n: int, p:float) -> int:
    """Return the sum of n bernoulli(p) trials"""
    return sum(bernoulli_trial(p) for _ in range(n))

def binomial_histogram(p: float, n: int, num_points: int) -> None:
    """Picks points from a Binomial(n, p) and plots their histogram"""
    data = [binomial(n, p) for _ in range(num_points)]
    # use a bar chart to show the actual binomial samples
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            0.8,
            color='0.75')
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # use a line chart to show the normal approximation
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
            for i in xs]
    plt.plot(xs,ys)
    plt.title("Binomial Distribution vs. Normal Approximation")
    plt.show()


