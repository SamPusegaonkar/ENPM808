import random

class Graph:

    def __init__(self):
        self.graph = [[0 for _ in range(10)] for _ in range(10)]

    def createRandomRobots(self, K):

        """
        Description: Creates K random robot in self.graph
        """
        robotsCreated = 0
        while robotsCreated < K :
            i = random.randint(0, 9))
            j = random.randint(0, 9))
            if self.graph[i][j] != 1:
                self.graph[i][j] = 1
                robotsCreated += 1
        
    def determineNetworkDelay(self):
        




graph = Graph()



