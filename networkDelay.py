import random
import math

class Graph:

    def __init__(self):
        self.graph = [[0 for _ in range(10)] for _ in range(10)]
        self.robotPositions = {}

    def createRandomRobots(self, K):
        """
        Description: Creates K random robot(s) in self.graph
        Input: K = number of robots
        Output: Modified self.graph
        """
        robotsCreated = 0
        while robotsCreated < K :
            i = random.randint(0, 9)
            j = random.randint(0, 9)
            if self.graph[i][j] != 1:
                self.robotPositions[tuple([i,j])] = True
                self.graph[i][j] = 1
                robotsCreated += 1
        
    def getEuclidianDistance(self, firstRobotPosition, secondRobotPosition):
        """
        Description: Returns the eucllidian distance bewtween 2 robot positions
        Input: Robot positions packed as i,j
        Output: Distance/Delay in units
        """
        x1 = firstRobotPosition[0]
        y1 = firstRobotPosition[1]
        x2 = secondRobotPosition[0]
        y2 = secondRobotPosition[1]
        return math.sqrt((x1- x2)**2 + (y1-y2)**2)
        
    def determineNetworkDelay(self):
        
        
        for firstRobotPosition in  self.robotPositions.keys():
            for secondRobotPosition in self.robotPositions.keys():
                if firstRobotPosition != secondRobotPosition:
                    distance = self.getEuclidianDistance(firstRobotPosition, secondRobotPosition)
                    print("The network delay between the robots is: ", distance, "units")

graph = Graph()
graph.createRandomRobots(3)
graph.determineNetworkDelay()



