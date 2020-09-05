
def run():
    n, a, b = map(int, input().split())
    va = {}

    while a > 0:
        a -= 1
        p, v = map(int, input().split())
        va[p] = v

    va_key = va.keys()

    sum = 0

    while b > 0:
        b -= 1
        p, v = map(int, input().split())

        if p in va_key:
            sum += va[p] * v

    print(sum)

if __name__ == "__main__":
    run()