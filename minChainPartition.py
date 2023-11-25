from bipartiteMatching import Matching

class MinChainPartition:
    def __init__(self, poset, relation, topologicalKey):
        self.poset = poset
        self.matching = Matching(list(range(len(poset))), \
                                 list(range(len(poset), 2*len(poset))), \
                                 dict([(i,[j+len(poset) for j,q in filter(lambda x: relation(p,x[1]), enumerate(self.poset))]) for i,p in enumerate(self.poset) ]))
        self.relation = relation
        self.topologicalKey = topologicalKey
        self.chained = set()
        self.matches = dict()

    def buildChain(self, ch):
        while ch[-1] in self.matches:
            self.chained.add(ch[-1])
            ch.append(self.matches[ch[-1]])
        self.chained.add(ch[-1])
        return ch


    def solvePartition(self):
        self.matching.solveMatching()

    def getPartition(self):
        '''
        Returns the minimum partition into chains as a list of lists, where the inner lists
        are lists of poset elements, and these represent the chains.
        '''
        self.matches = dict([(self.poset[i],self.poset[j-len(self.poset)]) for (i,j) in self.matching.getMatching()])
        chains = []
        for p in sorted(self.poset, key=self.topologicalKey):
            if not p in self.chained:
                chains.append(self.buildChain([p]))

        return chains
    
    def getNrOfChains(self):
        return len(self.poset) - self.matching.getNrMatches()


