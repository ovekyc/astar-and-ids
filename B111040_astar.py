#-*- coding: cp949 -*-
"""
    b111040 김영찬

    우선순위 큐를 이용하여 f = h + g 값이 가장 작은 node를 항상 선택하도록 구현
    path의 경우 방문한 노드를 리스트에 모두 추가한 후
    node에 있는 부모노드의 정보를 이용하여 트리의 하위부터 상위로 올라가며 표시하는 형식으로 구현
    evaluation function은 맨하탄 디스턴스를 사용하였음
"""
import copy

class ASTAR :

    def Solve(self, maze) :
        print "Start Searching by Using A Star"
        self.R = [1, 0, -1, 0]              # direction 배열
        self.C = [0, -1, 0, 1]
        self.row = maze.map.__len__()       # 초기화
        self.col = maze.map[0].__len__()
        self.map = copy.deepcopy(maze.map)
        self.visit = copy.deepcopy(self.map)
        self.goal = maze.goal

        pq = PriorityQueue(self.row * self.col)
        path = Path(self.row * self.col)

        current = Node()
        current.location = copy.deepcopy(maze.start)            # 시작지점 설정
        current.g = 0
        current.h = abs(current.location[0] - self.goal[0]) + abs(current.location[1] - self.goal[1])
        current.f = current.g + current.h
        current.level = 0
        current.parent = 0              # root node라고 표시 (path 출력 시 부모를 추적하며 출력하는 형태로 구현)

        pq.insert(current)              # 우선순위 큐에 삽입
        path.add(current)               # path에 삽입
        self.visit[current.location[0]][current.location[1]] = 1    # 방문했다고 표시

        solved = 0                      # solve flag
        cost = -1

        while pq.size > 0 :
            current = copy.deepcopy(pq.delete())            # 우선순위 큐에서 가장 비용이 적은 노드 선택
            cost += 1                                       # increase cost
            if current.location == self.goal:               # find goal
                solved = 1
                iter = current
                while iter.parent != 0:                             # 투트노드일때 까지 반복한다
                    self.visit[iter.location[0]][iter.location[1]] = 2  # mark as real path, 이후에 visit배열이 2로 표시되어있는 것만 real path로 간주하고 출력
                    iter = iter.parent                                  # move to parent node, 부모 노드로 이동
                break
            for i in range(0, 4):                                   # expand up,down,left,right
                temp = copy.deepcopy(current)
                temp.location[0] += self.R[i]
                temp.location[1] += self.C[i]
                if(self.isValid(temp.location) == 0) : continue     # skip if the location is invalid
                temp.g += 1                                         # 현재까지 실제로 사용된 비용 1 증가
                temp.h = abs(temp.location[0] - self.goal[0]) + abs(temp.location[1] - self.goal[1])    # 골 까지의 추정 값 계산
                temp.f = temp.g + temp.h                            # f계산
                temp.level += 1                                     # level + 1
                temp.parent = current
                self.visit[temp.location[0]][temp.location[1]] = 1  # check as visit area
                pq.insert(temp)                                     # insert to pq
                path.add(temp)                                      # path 리스트에 추가

        if solved == 1:
            self.PrintPath(maze.start)          # 출력
            print "Depth is", current.level
            print "Cost is", cost
        #else
            # there is no solution

    def isValid(self, loc):
        if loc[0] < 0 or loc[1] >= self.row or loc[1] < 0 or loc[1] >= self.col : return 0  # maze 의 범위가 넘어서면 무시
        if self.map[loc[0]][loc[1]] == 1                                        : return 0  # 벽이면 무시
        if self.visit[loc[0]][loc[1]] == 1                                      : return 0  # 방문한 곳이면 무시
        return 1

    def PrintPath(self, current):
        self.visit[current[0]][current[1]] = 3  # 출력 할 node의 visit값을 3으로 설정
        for i in range(0, self.row):  # print
            for j in range(0, self.col):
                if self.visit[i][j] == 3:       # 3이면 이동한 곳
                    print "X ",
                elif self.map[i][j] == 1:       # 1이면 벽
                    print "O ",
                elif self.map[i][j] == 0:       # 나머지는 이동하지 않은 곳
                    print "A ",
            print""
        print""
        if (current == self.goal): return       # 골에 도착했다면 리턴

        for i in range(0, 4):
            temp = copy.deepcopy(current)
            temp[0] += self.R[i]                # 4방향으로 확장해가며
            temp[1] += self.C[i]
            if self.visit[temp[0]][temp[1]] == 2:   # visit 값이 2이면 (== 최단 이동경로이면) current를 그 곳으로 설정
                current = temp
                break
        self.PrintPath(current)                 # 다음 node 출력

    def Print(self):    # 경로 test를 위한 함수
        for i in range(0, self.row):
            for j in range(0, self.col):
                if self.map[i][j] == 1:
                    print "O ",
                elif self.visit[i][j] == 1:
                    print "X ",
                else:
                    print ". ",
            print ""
        print ""

class Node :    # node 클래스
    def __init__(self):
        self.f = 0xffffffff # h+g
        self.h = -1         # estimate value from current to goal
        self.g = -1         # real value from start to current
        self.location = [-1, -1]
        self.level = -1
        self.parent = 0

class Path: # path 클래스, 경로를 출력하기 위해 사용, 단순 리스트
    def __init__(self, capacity):
        self.size = 0
        self.arr = [Node()] * capacity
    def add(self, e):
        self.arr[self.size] = e
        self.size += 1

class PriorityQueue : # 우선순위 큐, 가장 비용이 적은 노드를 선택 할 때 사용
    """ leftchild  : 2*i + 1
        rightchild : 2*i + 2
        parent     : (i-1)/2
    """

    def __init__(self, capacity):
        self.size = 0
        self.arr = [Node()] * capacity

    def insert(self, element):      #노드 삽입
        index = self.size
        self.size += 1
        self.arr[index] = element
        if self.size == 1 : return                          # return if first insert
        while self.arr[(index-1)/2].f > self.arr[index].f:
            if index == 0 : return                          # return if root node
            temp = self.arr[index]
            self.arr[index] = self.arr[(index-1)/2]
            self.arr[(index-1)/2] = temp
            index = (index-1) / 2

    def delete(self):               #노드 삭제
        result = self.arr[0]
        self.size -= 1
        index = 0
        self.arr[index] = copy.deepcopy(self.arr[self.size])
        while 2*index+1 < self.size :
            if self.arr[index].f > self.arr[2*index+1].f :
                temp = copy.deepcopy(self.arr[index])
                self.arr[index] = self.arr[2*index+1]
                self.arr[2*index+1] = temp
                index = 2 * index + 1
            elif 2 * index + 2 < self.size and self.arr[index].f > self.arr[2*index+2].f :
                temp = copy.deepcopy(self.arr[index])
                self.arr[index] = self.arr[2 * index + 2]
                self.arr[2 * index + 2] = temp
                index = 2 * index + 2
            else : break
        return result
