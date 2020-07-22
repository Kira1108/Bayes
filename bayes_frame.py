
class Pmf(object):
    '''
        Probability distribution function

        Usage:
            pmf = Pmf()
            pmf.setp('a',1)
            pmf.setp('b',2)
            pmf.setp('c',3)
            pmf.normalize()
    '''
    def __init__(self):
        self.dist = dict()

    def setp(self, x, val):
        self.dist[x] = val

    def incr(self,x, increment = 1, default = 0):
        self.dist[x] = self.dist.get(x, default) + increment

    def normalize(self, inplace = True):
        total = sum(self.dist.values())
        if total == 0:
            raise ValueError('sum of probability = 0')

        normalized_dist = {k:v/total for k,v in self.dist.items()}
        if inplace:
            self.dist = normalized_dist
        return normalized_dist

    def multi(self, x, val):
        self.dist[x] = self.dist.get(x,0) * val


class BayesFrame(Pmf):
    '''
        Abstract class
        Bayes frame work, intialize with prior probability - hypothesis priors
        Implement likelihood function
        Use update method to update posteria
    '''

    def __init__(self, hypos):
        '''
            Parameters:
                hypo: iterable, each element will get an equal prior probability
        '''
        super(BayesFrame, self).__init__()

        if isinstance(hypos,(list, str, set)):
            for hypo in hypos:
                self.setp(hypo,1)
            self.normalize()

        elif isinstance(hypos,dict):
            for hypo, prob in hypos.items():
                self.setp(hypo,prob)
            self.normalize()
        else:
            raise ValueError('Hypothesis should be in on of (dict, list, str, set)')


    def likelihood(self):
        raise NotImplementedError('Method not implemented, subclassing and implement it')


    def update(self, data, reset = False):
        orig = self.dist.copy()

        for hypo in self.dist:
            like = self.likelihood(data, hypo)
            self.dist[hypo] = self.dist[hypo] * like
            self.normalize()

        if reset:
            self.dist = orig


class Cookie(BayesFrame):

    edvidence = {
        'Bowl 1':dict(vanilla = 0.75, chocolate = 0.25),
        'Bowl 2':dict(vanilla = 0.5, chocolate = 0.5)
    }

    def likelihood(self, data, hypo):
        return self.edvidence[hypo][data]
