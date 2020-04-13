import statsmodels.api as sm
from matplotlib import pyplot as plt
import random

heads_tails = [0, 0]

trials = 100
trial = 0
while trial < trials:
    trial += 1
    toss = random.randint(0, 1)
    heads_tails[toss] = heads_tails[toss] + 1

print(heads_tails)

plt.pie(heads_tails, labels=['heads', 'tails'])
plt.legend()
plt.show()