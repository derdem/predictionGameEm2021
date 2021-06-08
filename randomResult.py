from scipy.stats import poisson
import random

def random_result():
    mu = 1.3
    x = random.uniform(0, 1)
    result = int(poisson.ppf(x, mu))
    return result

if __name__ == "__main__":
    print(random_result())