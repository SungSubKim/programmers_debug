from solution4 import *
from main0 import run_test

##########코테 보기전 화장실
##########코테 보기전 화장실
##########코테 보기전 화장실
if __name__ == '__main__':
    testcases = [["02:03:55", "00:14:15",
                  ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                   "01:37:44-02:02:30"]], ["99:59:59", "25:00:00",
                                           ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59",
                                            "11:00:00-31:00:00"]],
                 ["50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]],
                 ["99:59:59","00:00:05",["99:59:58-99:59:59" for _ in range(300000)]]
                 ]
    expectations = ["01:30:59", "01:00:00", "00:00:00","99:59:54"]
    run_test(testcases,expectations,solution)