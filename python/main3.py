from solution3 import *
from printResult import runTest

##########코테 보기전 화장실
##########코테 보기전 화장실
##########코테 보기전 화장실
if __name__ == '__main__':
    testcases = [[[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]],
                 [[[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]], [[[1, 1, 1, 1, 1]], [0, 0], [0, 4]],
                 [[[1]], [0, 0], [0, 0]]]
    expectations = [5, 4, 4, 0]
    runTest(testcases, expectations, solution)