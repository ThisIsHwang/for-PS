# 첫번째로 table의 블록을 뽑아냄.
# 뽑아낼 때 상하좌우를 최대한 줄여서 뽑아낼 수 있도록함. (xMin, xMax, yMin, yMax로 가능할 것으로 예상)
# 블록들을 dict 형태로 보관
# 블록들을 회전시킬 수 있어야함. (90 180 270)
# game_board를 뽑아내야함. bfs를 통해서 뽑아냄
# 해당 숫자에 맞는 블록들을 돌려가면서 대입함
# 해당 블록의 숫자를 result에 포함함. 그곳은 False로 바꿈

from collections import deque, defaultdict
def getBlocksFromTable(table):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    blocks = defaultdict(dict)
    for i, row in enumerate(table):
        for ii, cell in enumerate(row):
            if cell:
                tempBlock = {(i, ii)}
                queue = deque([(i, ii)])
                table[i][ii] = 0
                minX, minY = ii, i

                while queue:
                    ti, tii = queue.popleft()
                    for x, y in zip(dx, dy):
                        if 0 <= ti + y < len(table) and 0 <= tii + x < len(table) and table[ti + y][tii + x]:
                            minX, minY = min(minX, tii + x), min(minY, ti + y)
                            table[ti + y][tii + x] = 0
                            queue.append((ti + y, tii+x))
                            tempBlock.add((ti + y, tii+x))
                # 여기에서 minX, minY를 통해 x, y를 제일 작은 값으로 맞춰주자.(보정)
                blockSize = len(tempBlock)
                block = tuple(tuple(x-y for x, y in zip(coord,(minY,minX))) for coord in tempBlock)
                blocks[blockSize][block] = blocks[blockSize].get(block, 0) + 1
    return blocks

#rotation해주는 코드 만들자
# input parameter: one block(tuple)
# return parameter: 0, 90, 180, 270 rotated block
def returnRotatedBlocks(one_block):
    return_blocks = [one_block]
    # 90 degrees
    for _ in range(3):
        min_x = float("inf")
        min_y = float("inf")
        temp_block = []
        for point in return_blocks[-1]:
            min_y = min(min_y, point[1])
            min_x = min(min_x, -point[0])
            temp_block.append((point[1], -point[0]))
        return_blocks.append(tuple((x - min_y, y- min_x) for x, y in temp_block))

    return tuple(return_blocks)

#game board에서 bfs로 빈칸을 확인하고 저장된 블록들로 알맞는 곳에 있는지 확인.

#보정하는 함수 따로 뺌.
def adjustIt(tempBlock):
    minX = min(t[1] for t in tempBlock)
    minY = min(t[0] for t in tempBlock)
    newBlock = [(t[0] - minY, t[1] - minX) for t in tempBlock]
    return newBlock


def solveIt(game_board, blocksFromTable):
    result = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i, row in enumerate(game_board):
        for ii, cell in enumerate(row):
            if not cell:
                queue = deque([(i, ii)])
                game_board[i][ii] = 1
                tempBlock = [(i, ii)]
                while queue:
                    y, x = queue.popleft()

                    for yy, xx in zip(dy, dx):
                        if 0 <= y + yy < len(game_board) and 0 <= x + xx < len(game_board) and not game_board[y + yy][x + xx]:
                            queue.append((y + yy, x + xx))
                            game_board[y+ yy][x + xx] = 1
                            tempBlock.append([y + yy, x + xx])
                tempBlock = adjustIt(tempBlock)
                for block in blocksFromTable.get(len(tempBlock), []):
                    for rb in returnRotatedBlocks(block):
                        if set(rb) == set(tempBlock):
                            blocksFromTable[len(tempBlock)][block] -= 1
                            if not blocksFromTable[len(tempBlock)][block]:
                                del blocksFromTable[len(tempBlock)][block]
                            result += len(tempBlock)
                            break
                    else:
                        continue
                    break
    return result


def solution(game_board, table):
    blocksFromTable = getBlocksFromTable(table) # table에서 블록 뽑음
    return solveIt(game_board, blocksFromTable)
##############################
def rotate(table):
    return list(map(list,zip(*table[::-1])))

def dfs(condition,table,key,value,visited):
    i, j, x, y, target = condition
    visited[i][j] = 1
    key.append((i,j))
    value.append((x,y))
    moves = [(-1,0),(1,0),(0,1),(0,-1)] # U D R L
    for move in moves:
        dx, dy = move
        move_x, move_y = i + dx, j + dy
        if move_x < 0 or move_y < 0 or move_x >= len(table) or move_y >= len(table):
            continue
        elif table[move_x][move_y] == target and visited[move_x][move_y] == 0:
            key,value,visited = dfs([move_x, move_y, x+dx, y+dy, target], table, key, value, visited)
    return key, value, visited

def puzzle(table,target):
    visited = [[0]*len(table) for _ in range(len(table))]
    pieces = {} if target == 1 else []
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == target and visited[i][j] == 0:
                key, value, v = dfs([i,j,0,0,target],table,[],[],visited)
                if target == 1:
                    pieces[tuple(key)] = value
                else:
                    pieces.append(value)
                visited = v
    return pieces

def solution2(game_board,table):
    answer = 0
    board = puzzle(game_board,0)
    for _ in range(4):
        table = rotate(table)
        pieces = puzzle(table,1)
        for key,value in pieces.items():
            if value in board:
                board.remove(value)
                answer += len(value)
                for cod in key:
                    i, j  = cod
                    table[i][j] = 0
    return answer

import random

import copy
def generateTest(n):
    while True:
        game_board = []
        table = []
        for i in range(n):
            tempGameBoard = []
            for ii in range(n):
                tempGameBoard.append(random.randint(0, 1))
            game_board.append(tempGameBoard)
        for i in range(n):
            tempTable = []
            for ii in range(n):
                tempTable.append(random.randint(0, 1))
            table.append(tempTable)
        if solution2(copy.deepcopy(game_board), copy.deepcopy(table)) != solution(copy.deepcopy(game_board), copy.deepcopy(table)):
            print(game_board)
            print(table)
            break
#print()

game_board = [[0, 0, 1], [1, 1, 1], [0, 0, 1]]
table = [[1, 1, 0], [0, 0, 0], [0, 1, 1]]
print(solution2(game_board, table))
print(solution(game_board, table))

#generateTest(3)
