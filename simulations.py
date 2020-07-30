# Simulate posterial distribution
# With out any statistics knowledge

import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize


def cookie_problem():
    bow_prob = {1:[3/4, 1/4],2:[0.5,0.5]}
    bows = list(bow_prob.keys())

    from_bows = []
    cnt = 0

    # simulate
    for it in range(1000):
        bow = np.random.choice(bows)
        cookie = np.random.choice(['vanilla','chocolate'],
                     p = bow_prob[bow])

        if cookie == 'vanilla':
            from_bows.append(bow)

        if it in [5,10,30,50,100,300,500,900,999]:
            probability = {k:round(v / len(from_bows),2)
                 for k,v in dict(Counter
                                 (from_bows).most_common()).items()}

            print('Iterations: {}, Probability distribution: {}'.format(it, probability))

def mm():
    before = dict(brown = 0.3,
              yellow = 0.2,
              red = 0.2,
              green = 0.1,
              orange = 0.1,
             tan = 0.1)

    after = dict(blue = 0.24,
                  green = 0.2,
                  orange = 0.16,
                  yellow = 0.14,
                  red = 0.13,
                 brown = 0.13)

    probabilities = {}
    observation = 0
    cnt = 0

    for it in range(10000):
        before_choice = np.random.choice(list(before.keys()), p = list(before.values()))
        after_choice = np.random.choice(list(after.keys()), p = list(after.values()))

        choices = [before_choice, after_choice]

        if ('yellow' in choices) and ('green' in choices):
            cnt += 1

            if before_choice == 'yellow':
                observation +=1

            p = observation / cnt

            probabilities[cnt] = p

    plt.style.use('ggplot')
    figsize(12,6)
    plt.plot(list(probabilities.values()))
    plt.title('Probability Convergence Curve')
    plt.xlabel('Number of trials')
    plt.ylabel('Probability')
    plt.show()





if __name__ == "__main__":
    print("Solving cookie problem")
    cookie_problem()
    print('Done')


    print('Solving M & M problem')
    mm()
    print('Done')
