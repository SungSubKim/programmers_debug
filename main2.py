from solution2 import *
from main0 import *

##########코테 보기전 화장실
##########코테 보기전 화장실
##########코테 보기전 화장실
if __name__ == '__main__':
    testcases = [
        [["....", "###.", "###."],1],
        [["....", "###.", "###."],3],
        [[".F.FFFFF.F", ".########.",
          ".########F","...######F","##.######F",
          "...######F",".########F",".########.",
         ".#...####F", "...#......"],6],
        [['.'*50 for _ in range(50)],1]
    ]
    expectations = [4,1,3,49+48]
    cnt=0
    run_test(testcases,expectations,solution)