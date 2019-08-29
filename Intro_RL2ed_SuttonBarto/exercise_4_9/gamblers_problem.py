#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt

states = np.zeros([1, 101])[0]
policy = np.zeros([1, 101])[0]
states[-1] = 1

delta_lim = 0.0001
gamma = 1

exit = 0
count = 0
p_heads = 0.55
while(exit == 0 and count < 100):
    delta = 0
    for i in range(len(states)):
        action = 0
        value = 0

        for a in range(0, np.amin([i+1, 100-i+1])):
            temp_val = 0
            if(i-a < 0):
                print("****************************")
            # if (i + a) == 100:
            #     temp_val = 1
            temp_val = p_heads * (gamma * states[i + a]) + (1-p_heads) * (gamma * states[i - a])
            if temp_val > value:
                action = a
                value = temp_val
        policy[i] = action
        if np.abs(states[i] - value) > delta:
            delta = np.abs(states[i] - value)
        states[i] = value

    print("****COUNT: ", count, "DELTA: ", delta)
    if delta_lim > delta:
        exit = 1
    count += 1

print(states)
print(policy)

plt.plot(np.arange(101), states)
plt.show()
plt.plot(np.arange(101), policy)
plt.show()
