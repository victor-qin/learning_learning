# Key thing to recognize is difference between policy space and value space
# use expected values through it to establish value estimates

import numpy as np
import matplotlib.pyplot as plot

def poisson(lam, n):
    return (np.power(lam, n) * np.exp(-lam) / np.math.factorial(n))

def main():
    car_max = 21
    gamma = 0.9
    delta_lim = 1

    # x axis is cars in 1st location, y axis is cars in second location
    policy_space = np.zeros([car_max, car_max], dtype=int)
    value_space = np.zeros([car_max, car_max])

    # calculate value
    for z in range(0, 10):
        print("Policy Number: ", z)
        exit = 0
        count = 0
        while((exit == 0) and (count < 100)):
            delta = 0
            for i in range(value_space.shape[0]):
                for j in range(value_space.shape[1]):

                    # calculate reward first
                    value = 0
                    reward = 0
                    i_check = 0
                    j_check = 0

                    for k in range(i+1):
                        for l in range(j+1):
                            reward = (k + l) * 10

                            for m in range(i-k, 21):
                                for n in range(j-l, 21):
                                    swap = policy_space[m][n]
                                    value += (reward + gamma*value_space[m-swap][n+swap]) * poisson(3, k) * poisson(4, l) * poisson(3, (m-i+k)) * poisson(2, (n-j+l))

                    # value += gamma * value_space[i_check][j_check]
                    print(i, j, value)
                    if np.abs(value - value_space[i][j]) > delta:
                        delta = np.abs(value - value_space[i][j])
                    value_space[i][j] = value
            print("****COUNT: ", count, "DELTA: ", delta)
            count += 1
            if delta_lim > delta:
                exit = 1
        # print(np.flipud(value_space))

        #update policy space

        for i in range(policy_space.shape[0]):
            for j in range(policy_space.shape[1]):
                max_change = policy_space[i][j]
                max_value = value_space[i-max_change][j+max_change]
                for k in range(-5, 6):
                    if 0 <= i-k < 21 and 0 <= j+k < 21:
                        if (value_space[i-k][j+k] - 2*abs(k)) > max_value:
                            max_change = k
                policy_space[i][j] = max_change
        print(np.flipud(policy_space))

if __name__ == '__main__':
    main()




                # if i >= 3:
                #     value += 30
                #     i_check = i-3
                # else:
                #     value += i*10
                #     i_check = 0
                # i_check += 3
                #
                # if j >= 4:
                #     value += 40
                #     j_check = j-4
                # else:
                #     value += j*10
                #     j_check = 0
                # j_check += 2
