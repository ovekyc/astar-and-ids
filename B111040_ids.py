#-*- coding: cp949 -*-
"""
    b111040 �迵��

    Depth First Search�� ��͸� �̿��Ͽ� �����Ͽ���
    Search �Լ��� Ž���� ������ �Լ�, ���ڴ� ù ��° ����
        1. ������ġ
        2. ���� depth
        3. ���� depth
    Solve �Լ� ������ while������ ���� depth�� 1�� �����ϸ� DFS����
    Path�� ����� �� ���� �ϰ� ����Լ��� ���ϵ� �� ��������� ǥ���ϰ� ����
"""
import copy

class IDS :

    def Solve(self, maze) :
        print "Start Searching by Using IDS"

        self.isSolved = 0
        self.R = [1, 0, -1, 0]
        self.C = [0, -1, 0, 1]
        self.row = maze.map.__len__()           # �ʱ�ȭ
        self.col = maze.map[0].__len__()
        self.map   = copy.deepcopy(maze.map)
        self.visit = copy.deepcopy(self.map)
        self.goal = maze.goal

        current = maze.start
        limit = 0                               # depth�� ������ ��Ÿ��
        self.cost = 0
        self.depth = 0

        while self.isSolved == 0 :
            for i in range(0, self.row):        # set all element in visit to 0
                for j in range(0, self.col):
                    self.visit[i][j] = 0        # visit �ʱ�ȭ
            self.Search(current, 0, limit)      # ��θ� ã��
            limit += 1                          # depth�� ������ 1���� ��Ŵ
        self.PrintPath(maze.start)              # ���
        print "Depth is", self.depth
        print "Cost is", self.cost


    def Search(self, current, level, limit):
        if self.isSolved == 1                           : return       # ������ �ذ� �Ǿ��ٸ� ����
        if level > limit                                : return       # depth�� ���Ѻ��� ���� �����̸� ����
        if current[0]<0 or current[0]>=self.row or current[1]<0 or current[1]>=self.col : return;   # �������� ������ �Ѿ�ٸ� ����
        if self.map[current[0]][current[1]] == 1        : return       # ���̸� ����
        if self.visit[current[0]][current[1]] == 1      : return       # �湮�޴� ���̸� ����

        self.visit[current[0]][current[1]] = 1              # visit�� �湮�ߴٰ� ǥ��
        self.cost += 1                                      # increase cost 1
        if current == self.goal :                           # �� ����������
            self.isSolved = 1                               # �ذ�Ǿ��ٰ� ǥ��
            self.visit[current[0]][current[1]] = 2          # check as real path
            self.depth = level                              # ������ ���̴� ���� ����� ���̷� ����
            return

        for i in range(0,4):                                # expand up,down,left,right
            temp = copy.deepcopy(current)
            temp[0] += self.R[i]
            temp[1] += self.C[i]
            self.Search(temp, level+1, limit)               # ��������� Ž�� (stack)

        if self.isSolved == 1 :                             # �� �����ߴٸ� ��������� �����ϸ鼭 ���� ��θ� ǥ����
            self.visit[current[0]][current[1]] = 2          # check as real path

    def PrintPath(self, current):
        self.visit[current[0]][current[1]] = 3  # ���� ����� ����� ���̶�� ǥ��
        for i in range(0, self.row):            # print
            for j in range(0, self.col):
                if self.visit[i][j] == 3:       # ����� ��
                    print "X ",
                elif self.map[i][j] == 1:       # ��
                    print "O ",
                elif self.map[i][j] == 0:       # ���� ������� ���� ������ ��
                    print "A ",
            print""
        print""
        if(current == self.goal) : return       # �� ���������� ����

        for i in range(0, 4):
            temp = copy.deepcopy(current)
            temp[0] += self.R[i]
            temp[1] += self.C[i]
            if self.visit[temp[0]][temp[1]] == 2 : # ���� ��� �� �湮���� ���� �� Ž��
                current = temp                  # ���� ��� ����
                break
        self.PrintPath(current)                 # ��������� ���� ��� �湮

    def Print(self):
        for i in range(0,self.row) :
            for j in range(0,self.col) :
                if   self.map[i][j]   == 1  : print "O ",
                elif self.visit[i][j] == 1  : print "X ",
                else                        : print ". ",
            print ""
        print ""


