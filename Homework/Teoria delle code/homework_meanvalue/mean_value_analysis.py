import numpy as np
import matplotlib.pyplot as plt

def main():
    n_queue = 2
    max_users = 100
    l_hat = np.array([3, 1])
    mu = np.array([5, 2])

    N = np.zeros((n_queue, max_users + 1))
    T = np.zeros((n_queue, max_users + 1))
    l = np.zeros((n_queue, max_users + 1))

    for i in range(n_queue):
        N[i, 0] = 0
    for i in range(n_queue):
        T[i,0] = 0
    for i in range(n_queue):
        l[i,0] = 0

    for k in range(1,max_users + 1):
        for i in range(n_queue):
            T[i,k] = (1 + N[i,k-1]) / mu[i]
            N[i,k] = k * l_hat[i] * T[i,k] / sum([l_hat[j]*T[j,k] for j in range(n_queue)])
            l[i,k] = N[i,k] / T[i,k]
    
            
    plt.subplot(1,2,1)
    plt.plot(range(max_users + 1), N[0,:], 'r')
    plt.xlabel('Number of users')
    plt.ylabel('Average number of users in the first queue')

    plt.subplot(1,2,2)
    plt.plot(range(max_users + 1), N[1,:])
    plt.xlabel('Number of users')
    plt.ylabel('Average number of users in the second queue')
    plt.show()

    plt.subplot(1,2,1)
    plt.xlabel('Number of users')
    plt.ylabel('Average response time of the first queue')
    plt.plot(range(max_users + 1), T[0,:], 'r')
    plt.subplot(1,2,2)
    plt.xlabel('Number of users')
    plt.ylabel('Average response time of the second queue')
    plt.plot(range(max_users + 1), T[1,:])
    plt.show()

    plt.subplot(1,2,1)
    plt.plot(range(max_users + 1), l[0,:], 'r')
    plt.xlabel('Number of users')
    plt.ylabel('Arrival rate of the first queue')
    
    plt.subplot(1,2,2)
    plt.plot(range(max_users + 1), l[1,:])
    plt.xlabel('Number of users')
    plt.ylabel('Arrival rate of the second queue')
    plt.show()


if __name__ == '__main__':
    main()