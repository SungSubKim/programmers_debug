from solution2 import *
from printResult import runTest

##########코테 보기전 화장실
if __name__ == '__main__':
    testcases = [
        [[0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]]
        ,

        [[0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]]
        ,
    ]
    expectations = [
        5,5
    ]
    runTest(testcases, expectations, solution)