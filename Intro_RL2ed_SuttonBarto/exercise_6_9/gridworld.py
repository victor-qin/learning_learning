#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt

def actions(position):

    temp = [[], [], []]
    if position[1] + 1 < width:
        temp[0].append(value[position[1] + 1][position[0]])
        temp[1].append(1)
        temp[2].append(0)
    if 0 <= position[1] - 1:
        temp[0].append(value[position[1] - 1][position[0]])
        temp[1].append(-1)
        temp[2].append(0)
    if position[0] + 1 < length:
        temp[0].append(value[position[1]][position[0] + 1])
        temp[1].append(0)
        temp[2].append(1)
    if 0 <= position[1] - 1:
        temp[0].append(value[position[1]][position[0] - 1])
        temp[1].append(0)
        temp[2].append(-1)

    return temp

def main():
    epsilon = 0.1
    length = 10
    width = 7
    start = [0, 3]
    end =  [7, 3]
    wind = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]

    value = np.zeros([width,length, 4]) # up = 0, down = 1, right = 2, left = 3
    print(value)

    count = 0
    while count < 10:
        curPos = start
        nextPos = [0, 0]
        actionNow = 0
        actionFut = 0
        # check the neighboring squares - up, down, left, right
        temp = actions(curPos)

        if np.random.random() < epsilon:
            actionNow = np.argmax(4)
        else:
            actionNow = np.argmax(temp[0])

        # print(action)

        while curPos != end:
            nextPos = curPos + actionNow[temp[1], temp[2]]
            reward = -1

            temp = actions(nextPos)
            if np.random.random() < epsilon:
                actionFut = int(np.random.randint(4))
            else:
                actionFut = np.argmax(temp[0])


        count += 1

    return 0

if __name__ == '__main__':
    main()
