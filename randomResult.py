from scipy.stats import poisson
import random

def random_result():
    mu = 1.3
    x = random.uniform(0, 1)
    result = int(poisson.ppf(x, mu))
    return result

def random_between_0_and_5():
    goals = 0
    for i in range(5):
        x = random.uniform(0, 1)
        if x > .25:
            goals += 1
    return goals

if __name__ == "__main__":
    print(random_result())