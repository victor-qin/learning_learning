#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt

def actions(pos, value):
    position = [int(pos[0]), int(pos[1])]
    epsilon = 0.1
    index = 0
    temp = np.zeros([4, 4], dtype=float)
    random = []

    # print(value.shape)
    if (position[1] + 1) < value.shape[1]:
        # print(position[1], value.shape[1])
        # print(value[0][position[1]][position[0]])
        temp[0][0] = value[0][position[1]][position[0]]
        temp[1][0] = 1
        temp[2][0] = 0
        temp[3][0] = 0
        random.append(0)
    else:
        temp[0][0] = -np.inf

    if 0 < position[1]:
        temp[0][1] = value[1][position[1]][position[0]]
        temp[1][1] = -1
        temp[2][1] = 0
        temp[3][1] = 1
        random.append(1)
    else:
        temp[0][1] = -np.inf

    if position[0] + 1 < value.shape[2]:
        temp[0][2] = value[2][position[1]][position[0]]
        temp[1][2] = 0
        temp[2][2] = 1
        temp[3][2] = 2
        random.append(2)
    else:
        temp[0][2] = -np.inf

    if 0 < position[0]:
        temp[0][3] = value[3][position[1]][position[0]]
        temp[1][3] = 0
        temp[2][3] = -1
        temp[3][3] = 3
        random.append(3)
    else:
        temp[0][3] = -np.inf

    if np.random.random() < epsilon:
        index = np.random.choice(random)
    else:
        index = np.argmax(temp[0])

    # print(temp)
    return [int(temp[2][index]), int(temp[1][index]), int(temp[3][index])]

def return_path(value, start):
    move = [0, 0]
    # print(start, value[:, start[1], start[0]])
    action = np.argmax(value[:, start[1], start[0]])

    if action == 0:
        move = [0, 1]
    elif action == 1:
        move = [0, -1]
    elif action == 2:
        move = [1, 0]
    elif action == 3:
        move = [-1, 0]

    return (action, move)

def main():
    epsilon = 0.3
    alpha = 0.5
    gamma = 1

    length = 10
    width = 7
    start = [0, 3]
    end =  [7, 3]
    wind = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]

    q_est = np.zeros([4, width,length], dtype=float) # up = 0, down = 1, right = 2, left = 3
    # print(value)

    count = 0
    while count < 1000:
        curPos = start
        nextPos = [0, 0]
        actionNow = [0, 0, 0]
        actionFut = [0, 0, 0]
        # check the neighboring squares - down, up, left, right
        actionNow = actions(curPos, q_est)

        # print(action)

        while not np.array_equal(curPos, end):
            nextPos = np.add(curPos, actionNow[0:2])
            # print(nextPos)
            if(0 < nextPos[1] <= width):
                nextPos[1] -= wind[curPos[0]]
            if(nextPos[1] < 0):
                nextPos[1] = 0

            reward = -1

            actionFut = actions(nextPos, q_est)
            q_est[actionNow[2]][curPos[1]][curPos[0]] += alpha * (reward + gamma * q_est[actionFut[2]][nextPos[1]][nextPos[0]] - q_est[actionNow[2]][curPos[1]][curPos[0]])

            curPos = nextPos
            actionNow = actionFut
            # print(curPos, nextPos, actionNow)

        count += 1

    q_est = np.where(q_est==0, -np.inf, q_est)
    for i in range(4):
        # q_est[i][start[1]][start[0]] = 0
        q_est[i][end[1]][end[0]] = 0
    for i in range(length):
        if wind[i] == 0:
            q_est[0][width-1][i] = -np.inf
    print(q_est)

    testPos = start
    search_actions = []
    while not np.array_equal(testPos, end):
        (action, move) = return_path(q_est, testPos)
        testPos = np.add(testPos, move)
        testPos = np.add(testPos, np.array([0, -wind[testPos[0]]]))
        if(testPos[1] < 0):
            testPos[1] = 0
        print(testPos)
        search_actions.append(action)

    print(search_actions)

    return 0

if __name__ == '__main__':
    main()
