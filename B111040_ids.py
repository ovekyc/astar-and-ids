#-*- coding: cp949 -*-
"""
    b111040 김영찬

    Depth First Search를 재귀를 이용하여 구성하였음
    Search 함수가 탐색을 구현한 함수, 인자는 첫 번째 부터
        1. 현재위치
        2. 현재 depth
        3. 제한 depth
    Solve 함수 내에서 while문으로 제한 depth를 1씩 증가하며 DFS수행
    Path의 출력은 골에 도착 하고 재귀함수가 리턴될 때 재귀적으로 표시하게 구현
"""
import copy

class IDS :

    def Solve(self, maze) :
        print "Start Searching by Using IDS"

        self.isSolved = 0
        self.R = [1, 0, -1, 0]
        self.C = [0, -1, 0, 1]
        self.row = maze.map.__len__()           # 초기화
        self.col = maze.map[0].__len__()
        self.map   = copy.deepcopy(maze.map)
        self.visit = copy.deepcopy(self.map)
        self.goal = maze.goal

        current = maze.start
        limit = 0                               # depth의 제한을 나타냄
        self.cost = 0
        self.depth = 0

        while self.isSolved == 0 :
            for i in range(0, self.row):        # set all element in visit to 0
                for j in range(0, self.col):
                    self.visit[i][j] = 0        # visit 초기화
            self.Search(current, 0, limit)      # 경로를 찾음
            limit += 1                          # depth의 제한을 1증가 시킴
        self.PrintPath(maze.start)              # 출력
        print "Depth is", self.depth
        print "Cost is", self.cost


    def Search(self, current, level, limit):
        if self.isSolved == 1                           : return       # 문제가 해결 되었다면 종료
        if level > limit                                : return       # depth의 제한보다 깊은 레벨이면 종료
        if current[0]<0 or current[0]>=self.row or current[1]<0 or current[1]>=self.col : return;   # 메이즈의 범위를 넘어섰다면 종료
        if self.map[current[0]][current[1]] == 1        : return       # 벽이면 종료
        if self.visit[current[0]][current[1]] == 1      : return       # 방문햇던 곳이면 종료

        self.visit[current[0]][current[1]] = 1              # visit에 방문했다고 표시
        self.cost += 1                                      # increase cost 1
        if current == self.goal :                           # 골에 도달했으면
            self.isSolved = 1                               # 해결되었다고 표시
            self.visit[current[0]][current[1]] = 2          # check as real path
            self.depth = level                              # 정답의 깊이는 현재 노드의 깊이로 설정
            return

        for i in range(0,4):                                # expand up,down,left,right
            temp = copy.deepcopy(current)
            temp[0] += self.R[i]
            temp[1] += self.C[i]
            self.Search(temp, level+1, limit)               # 재귀적으로 탐색 (stack)

        if self.isSolved == 1 :                             # 골에 도달했다면 재귀적으로 리턴하면서 실제 경로를 표시함
            self.visit[current[0]][current[1]] = 2          # check as real path

    def PrintPath(self, current):
        self.visit[current[0]][current[1]] = 3  # 실제 경로중 출력한 것이라는 표시
        for i in range(0, self.row):            # print
            for j in range(0, self.col):
                if self.visit[i][j] == 3:       # 출력한 곳
                    print "X ",
                elif self.map[i][j] == 1:       # 벽
                    print "O ",
                elif self.map[i][j] == 0:       # 아직 출력하지 않은 나머지 길
                    print "A ",
            print""
        print""
        if(current == self.goal) : return       # 골에 도달했으면 종료

        for i in range(0, 4):
            temp = copy.deepcopy(current)
            temp[0] += self.R[i]
            temp[1] += self.C[i]
            if self.visit[temp[0]][temp[1]] == 2 : # 실제 경로 중 방문하지 않은 곳 탐색
                current = temp                  # 다음 노드 선택
                break
        self.PrintPath(current)                 # 재귀적으로 다음 노드 방문

    def Print(self):
        for i in range(0,self.row) :
            for j in range(0,self.col) :
                if   self.map[i][j]   == 1  : print "O ",
                elif self.visit[i][j] == 1  : print "X ",
                else                        : print ". ",
            print ""
        print ""


