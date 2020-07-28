import numpy as np
from scipy import stats

def z_freq(x, P, alpha = 0.05):

    '''
        x: sample
        P: population
        alpha: significance level

        Test: x is from population p
    '''
    # Z statistic - StandardScaler
    Z = (x.mean() - P.mean()) / P.std()

    p = 1 - stats.norm.cdf(Z)
    reject = p < alpha

    print('Z statistic: {}'.format(Z))
    print('P value is : {}'.format(p))

    if reject:
        print('Reject null hypothesis')
    else:
        print('Unable to reject null hypothyesis')


def ztest_simu(x, P,alpha = 0.05 ,n_simus = 1000):

    # simulation
    mean_diffs = np.random.choice(x, size = (n_simus, len(x)), replace = True).mean(axis = 1) - \
    np.random.choice(P,size = (n_simus,len(P)), replace = True).mean(axis = 1)

    reject = np.percentile(mean_diffs, alpha * 100) > 0


    if reject:
        print('Reject null hypothesis')
    else:
        print('Unable to reject null')



if __name__ == '__main__':
    # the population
    N = 1000
    P =np.random.randn(N)

    # the sample
    n = 20
    x = np.random.randn(n) + 2

    z_freq(x, P, 0.05)
    ztest_simu(x, P)
