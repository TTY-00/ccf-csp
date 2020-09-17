from sys import stdin


def run():
    num = int(input())

    for line in stdin:
        # ops = [line[1], line[3], line[5]]
        # nnum = list(map(int, [line[0], line[2], line[4], line[6]]))
        nnum = []
        ops = []
        used = [1 for i in range(7)]

        for i, c in enumerate(line):
            if c >= '0' and c <= '9' and used[i] != 0:
                nnum.append(int(c))
            elif c == "x":
                num1 = nnum.pop()
                # num2 = nnum.pop()
                num2 = int(line[i + 1])
                used[i + 1] = 0

                new = num1 * num2
                nnum.append(new)
            elif c == "/":
                num1 = nnum.pop()
                num2 = int(line[i + 1])
                used[i + 1] = 0

                new = int(num1 / num2)
                nnum.append(new)

            elif c in ['+', '-']:
                ops.append(c)

        print(nnum)
        print(ops)
        k = 0
        for i, op in enumerate(ops):
            if op == '+':
                num1 = nnum[k]
                num2 = nnum.pop()

                new = num1 + num2
                nnum.append(new)
            elif op == '-':
                num1 = nnum.pop()
                num2 = nnum.pop()

                new = num1 - num2
                nnum.append(new)    

        print(nnum)
        # if nnum[0] == 24:
        #     print('Yes')
        # else:
        #     print('No')


if __name__== "__main__":
    run()