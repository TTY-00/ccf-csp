def run():
    n = int(input().strip())
    s = input().strip()
    output = '1'
    for _ in range(n):
        output = ''.join([str(2**int(x)) for x in output])
        print("== out ==")
        print([output.count('0'), output.count('1'),output.count('2'),output.count('3'),output.count('4'),output.count('5'), output.count('6')])
    return output.count(s) % 998244353


if __name__ == "__main__":
    print(run())