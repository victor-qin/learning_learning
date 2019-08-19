#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt

# Constants
limit = 100000    # iterations
epsilon = 0.1   #epsilon selection
sigma = 0.1     #variation in reward
kappa = 0.01
k = 10  #arms

# true reward
q_star = np.zeros([1, k])[0] #+ sigma * np.random.randn(k)

# 1st row is action, 2nd row is Q(A), 3rd row is N(A)
Q_est_avg = np.zeros([3, k])
Q_est_const = np.zeros([3, k])
for i in range(k):
    Q_est_avg[0][i] = i
    Q_est_const[0][i] = i

# Iterate
avg_reward_est = np.zeros([1, limit])[0]
const_reward_est = np.zeros([1, limit])[0]
for i in range(limit):
    # Shuffle the matrix
    Q_est_avg = Q_est_avg[:, np.random.permutation(k)]

    # W/ probability epsilon pick a random index
    if np.random.random() < epsilon:
        index = int(np.random.randint(k))
    else:
        index = int(Q_est_avg[0][np.argmax(Q_est_avg[1, :])])

    # Get a reward from an arm
    reward = q_star[int(Q_est_avg[0][index])] + np.random.normal(0, sigma)
    if(i > 1):
        avg_reward_est[i] = Q_est_avg[1].sum()/k * epsilon + Q_est_avg[1][np.argmax(Q_est_avg[1, :])] * (1 - epsilon)

    # Change estimates of arms
    Q_est_avg[2][index] += 1
    Q_est_avg[1][index] += (reward - Q_est_avg[1][index]) / Q_est_avg[2][index]


    """Constant Step Size """
    # Shuffle the matrix
    Q_est_const = Q_est_const[:, np.random.permutation(k)]

    # W/ probability epsilon pick a random index
    if np.random.random() < epsilon:
        index = int(np.random.randint(k))
    else:
        index = int(Q_est_const[0][np.argmax(Q_est_const[1, :])])

    # Get a reward from an arm
    reward = q_star[int(Q_est_const[0][index])] + np.random.normal(0, sigma)
    if(i > 1):
        const_reward_est[i] = Q_est_const[1].sum()/k * epsilon + Q_est_const[1][np.argmax(Q_est_const[1, :])] * (1 - epsilon)

    # Change estimates of arms
    Q_est_const[2][index] += 1
    Q_est_const[1][index] += (reward - Q_est_const[1][index]) * 0.1

    for j in range(k):
        q_star[j] += np.random.normal(0, kappa)


# plot
plt.plot(np.arange(limit), avg_reward_est)
plt.plot(np.arange(limit), const_reward_est)
plt.legend(("avg", "const"))
plt.show()
