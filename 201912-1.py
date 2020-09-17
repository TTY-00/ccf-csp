import sys

def run():
    n = int(input().strip())
    i = 1
    res = [0, 0, 0, 0]

    while i <= n:
        if i % 7 == 0 or '7' in str(i):
            res[(i - 1) % 4] += 1
            i += 1
            n += 1

        else:
            i += 1

    for r in res:
        print(r)

if __name__ == "__main__":
    run()