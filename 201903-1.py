import sys


def run():
    total = int(input())
    data = list(map(int, input().strip().split()))
    # print(data)

    max_n = data[-1]
    min_n = data[0]
    if data[0] > data[-1]:
        max_n = data[0]
        min_n = data[-1]

    middel = 0.0
    if total % 2 == 0:
        middel = (1.0 * data[int(total / 2)] + data[int(total / 2) - 1]) / 2.0

    else:
        middel = data[int(total / 2)]

    # print(middel % 1.0)
    # print(middel % 1.0 == 0.0)
    # print(middel % 1.0 == 0)
    if middel % 1.0 == 0:
        print(max_n, int(middel), min_n)
    else:
    
        print(max_n, "%.1f" % middel, min_n)


if __name__ == "__main__":
    run()