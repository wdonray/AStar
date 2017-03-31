#pylint rate: 10/10
'''File that handles the testing of the astar algorithm'''
#Refer to Readme.txt in file for directions on how to use the unit test
import re
from vector import Vector2

class Graph(object):
    '''Graph'''
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = []
        self.gengraph()

    def gengraph(self):
        '''generates the graph'''
        nodecount = 0
        for row in range(0, self.width):
            for col in range(0, self.height):
                self.nodes.append(Node(Vector2(col, row), str(nodecount)))
                nodecount = nodecount + 1

    def getnode(self, nodeval):
        '''Checks to see if a node with the nodevalue passed in is in the graph'''
        for node in self.nodes:
            if node.value == nodeval:
                return node
        return None

class Node(object):
    '''Node'''
    def __init__(self, position, value):
        self.gscore = 0
        self.hscore = 0
        self.fscore = 0
        self.position = position
        self.parent = None
        self.value = value
        self.iswalkable = True

class TestCase(object):
    '''Stores all the data that defines a valid test case'''
    def __init__(self, name, case, answer):
        self.name = name
        self.name = re.sub('name:', "", self.name)
        self.name = ''.join(self.name.split())
        self.case = case
        self.case = re.sub('case:', "", self.case)
        self.case = ''.join(self.case.split())
        self.answer = answer
        self.answer = re.sub('answer:', "", self.answer)
        self.answer = ''.join(self.answer.split())

    def setupgraph(self):
        '''Generates and returns a graph with all of the walls set up and the size of
        the graph all test cases are going to be tested in a 10 x 10 grid'''
        graph = Graph(10, 10)
        for iterator in range(0, len(self.case)):
            if self.case[iterator] == 'W':
                iterator = iterator + 2
                nodevalue = ""
                while self.case[iterator] != ';':
                    nodevalue = nodevalue + self.case[iterator]
                    iterator = iterator + 1
                graph.getnode(nodevalue).iswalkable = False
        return graph

    def getstartandgoal(self):
        '''Returns the start and goal nodes to be used in the algorithm'''
        start = ""
        goal = ""
        for iterator in range(0, len(self.case)):
            if self.case[iterator] == 'G':
                iterator = iterator + 2
                nodevalue = ""
                while self.case[iterator] != ';':
                    nodevalue = nodevalue + self.case[iterator]
                    iterator = iterator + 1
                goal = nodevalue
            if self.case[iterator] == 'S':
                iterator = iterator + 2
                nodevalue = ""
                while self.case[iterator] != ';':
                    nodevalue = nodevalue + self.case[iterator]
                    iterator = iterator + 1
                start = nodevalue
        return (start, goal)

    def getcorrectpath(self):
        '''Gets the expected result for the the algorithm to return'''
        nodes = []
        for iterator in range(0, len(self.answer)):
            nodevalue = ""
            if self.answer[iterator] == '[':
                iterator = iterator + 1
                while self.answer[iterator] != ']':
                    nodevalue = nodevalue + self.answer[iterator]
                    iterator = iterator + 1
                nodes.append(nodevalue)
        return nodes


class UnitTest(object):
    '''Unit Test class responsible for setting up and testing the astar algorithm'''
    def __init__(self, testcasefile):
        self.start = None
        self.goal = None
        self.result = [None]
        self.testfile = open(testcasefile, "r")
        self.testcases = []
        self.gentestcases()

    def gentestcases(self):
        '''Gets all the test cases from the test file specified'''
        linecount = 0
        lines = self.testfile.readlines()
        for line in lines:
            if "#" in line or line == '\n':
                linecount = linecount + 1
                continue
            if "{" in line:
                name = ""
                case = ""
                answer = ""
                while "}" not in lines[linecount]:
                    if "name:" in lines[linecount]:
                        name = lines[linecount]
                    elif "case:" in lines[linecount]:
                        case = lines[linecount]
                    elif "answer:" in lines[linecount]:
                        answer = lines[linecount]
                    linecount = linecount + 1
                self.testcases.append(TestCase(name, case, answer))

    def testastar(self, algorithm):
        '''Loops through all of the testcases we have created and sets up
        a graph based on the case specified in each test case. Returns the
        results and prints them to a file stating weather the algorithm has passed
        the specified case'''
        tests = []
        answersfile = open("results.txt", "w").close()
        answersfile = open("results.txt", "a")
        for testcase in self.testcases:
            answersfile.write("{\n")
            answersfile.write("    name:" + testcase.name + "\n")
            answersfile.write("    case:" + testcase.case + "\n")
            answersfile.write("    expected:" + testcase.answer + "\n")
            environment = testcase.setupgraph()
            points = testcase.getstartandgoal()
            self.start = environment.getnode(points[0])
            self.goal = environment.getnode(points[1])
            path = algorithm(self.start, self.goal, environment)
            response = ""
            for node in path:
                response += "[" + node.value + "]"
            answersfile.write("    result:" + response + "\n")
            correctanswer = testcase.getcorrectpath()
            isvalid = True
            for iterator in range(0, len(correctanswer)):
                if path[iterator].value != correctanswer[iterator]:
                    isvalid = False
                    continue
            tests.append(isvalid)
            answersfile.write("    pass:" + str(isvalid))
            answersfile.write("\n}\n\n")
        answersfile.close()
        return tests
