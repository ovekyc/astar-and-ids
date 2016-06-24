#-*- coding: cp949 -*-
"""
    b111040 �迵��

    �켱���� ť�� �̿��Ͽ� f = h + g ���� ���� ���� node�� �׻� �����ϵ��� ����
    path�� ��� �湮�� ��带 ����Ʈ�� ��� �߰��� ��
    node�� �ִ� �θ����� ������ �̿��Ͽ� Ʈ���� �������� ������ �ö󰡸� ǥ���ϴ� �������� ����
    evaluation function�� ����ź ���Ͻ��� ����Ͽ���
"""
import copy

class ASTAR :

    def Solve(self, maze) :
        print "Start Searching by Using A Star"
        self.R = [1, 0, -1, 0]              # direction �迭
        self.C = [0, -1, 0, 1]
        self.row = maze.map.__len__()       # �ʱ�ȭ
        self.col = maze.map[0].__len__()
        self.map = copy.deepcopy(maze.map)
        self.visit = copy.deepcopy(self.map)
        self.goal = maze.goal

        pq = PriorityQueue(self.row * self.col)
        path = Path(self.row * self.col)

        current = Node()
        current.location = copy.deepcopy(maze.start)            # �������� ����
        current.g = 0
        current.h = abs(current.location[0] - self.goal[0]) + abs(current.location[1] - self.goal[1])
        current.f = current.g + current.h
        current.level = 0
        current.parent = 0              # root node��� ǥ�� (path ��� �� �θ� �����ϸ� ����ϴ� ���·� ����)

        pq.insert(current)              # �켱���� ť�� ����
        path.add(current)               # path�� ����
        self.visit[current.location[0]][current.location[1]] = 1    # �湮�ߴٰ� ǥ��

        solved = 0                      # solve flag
        cost = -1

        while pq.size > 0 :
            current = copy.deepcopy(pq.delete())            # �켱���� ť���� ���� ����� ���� ��� ����
            cost += 1                                       # increase cost
            if current.location == self.goal:               # find goal
                solved = 1
                iter = current
                while iter.parent != 0:                             # ��Ʈ����϶� ���� �ݺ��Ѵ�
                    self.visit[iter.location[0]][iter.location[1]] = 2  # mark as real path, ���Ŀ� visit�迭�� 2�� ǥ�õǾ��ִ� �͸� real path�� �����ϰ� ���
                    iter = iter.parent                                  # move to parent node, �θ� ���� �̵�
                break
            for i in range(0, 4):                                   # expand up,down,left,right
                temp = copy.deepcopy(current)
                temp.location[0] += self.R[i]
                temp.location[1] += self.C[i]
                if(self.isValid(temp.location) == 0) : continue     # skip if the location is invalid
                temp.g += 1                                         # ������� ������ ���� ��� 1 ����
                temp.h = abs(temp.location[0] - self.goal[0]) + abs(temp.location[1] - self.goal[1])    # �� ������ ���� �� ���
                temp.f = temp.g + temp.h                            # f���
                temp.level += 1                                     # level + 1
                temp.parent = current
                self.visit[temp.location[0]][temp.location[1]] = 1  # check as visit area
                pq.insert(temp)                                     # insert to pq
                path.add(temp)                                      # path ����Ʈ�� �߰�

        if solved == 1:
            self.PrintPath(maze.start)          # ���
            print "Depth is", current.level
            print "Cost is", cost
        #else
            # there is no solution

    def isValid(self, loc):
        if loc[0] < 0 or loc[1] >= self.row or loc[1] < 0 or loc[1] >= self.col : return 0  # maze �� ������ �Ѿ�� ����
        if self.map[loc[0]][loc[1]] == 1                                        : return 0  # ���̸� ����
        if self.visit[loc[0]][loc[1]] == 1                                      : return 0  # �湮�� ���̸� ����
        return 1

    def PrintPath(self, current):
        self.visit[current[0]][current[1]] = 3  # ��� �� node�� visit���� 3���� ����
        for i in range(0, self.row):  # print
            for j in range(0, self.col):
                if self.visit[i][j] == 3:       # 3�̸� �̵��� ��
                    print "X ",
                elif self.map[i][j] == 1:       # 1�̸� ��
                    print "O ",
                elif self.map[i][j] == 0:       # �������� �̵����� ���� ��
                    print "A ",
            print""
        print""
        if (current == self.goal): return       # �� �����ߴٸ� ����

        for i in range(0, 4):
            temp = copy.deepcopy(current)
            temp[0] += self.R[i]                # 4�������� Ȯ���ذ���
            temp[1] += self.C[i]
            if self.visit[temp[0]][temp[1]] == 2:   # visit ���� 2�̸� (== �ִ� �̵�����̸�) current�� �� ������ ����
                current = temp
                break
        self.PrintPath(current)                 # ���� node ���

    def Print(self):    # ��� test�� ���� �Լ�
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

class Node :    # node Ŭ����
    def __init__(self):
        self.f = 0xffffffff # h+g
        self.h = -1         # estimate value from current to goal
        self.g = -1         # real value from start to current
        self.location = [-1, -1]
        self.level = -1
        self.parent = 0

class Path: # path Ŭ����, ��θ� ����ϱ� ���� ���, �ܼ� ����Ʈ
    def __init__(self, capacity):
        self.size = 0
        self.arr = [Node()] * capacity
    def add(self, e):
        self.arr[self.size] = e
        self.size += 1

class PriorityQueue : # �켱���� ť, ���� ����� ���� ��带 ���� �� �� ���
    """ leftchild  : 2*i + 1
        rightchild : 2*i + 2
        parent     : (i-1)/2
    """

    def __init__(self, capacity):
        self.size = 0
        self.arr = [Node()] * capacity

    def insert(self, element):      #��� ����
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

    def delete(self):               #��� ����
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
