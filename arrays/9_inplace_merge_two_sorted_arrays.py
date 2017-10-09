# Problem: http://www.techiedelight.com/inplace-merge-two-sorted-arrays/


def m_n_solution(X, Y):
    for i in range(len(X)):
        if X[i] > Y[0]:
            X[i], Y[0] = Y[0], X[i]
            for j in range(len(Y)-1):
                if Y[j] > Y[j+1]:
                    Y[j], Y[j+1] = Y[j+1], Y[j]
    return X, Y


# stress test
import random

for _ in range(1000):
    X, Y = m_n_solution(sorted([random.randint(0, 10000) for i in range(random.randint(1, 1000))]),
                        sorted([random.randint(0, 10000) for j in range(random.randint(1, 1000))]))

    merged_lists = sorted(X + Y)

    sorted_X = merged_lists[0:len(X)]
    sorted_Y = merged_lists[len(X):]

    try:
        assert X == sorted_X
        assert Y == sorted_Y
        assert X[-1] <= Y[0]
    except:
        print(X, Y)
