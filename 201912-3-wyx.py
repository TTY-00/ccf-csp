# -*- coding: utf-8 -*-

def parse_formula(item, res, mul=1):
    # print("parse:", item)
    i = 0
    l = 1
    if '/' < item[i] < "@":
        while "/" < item[i] < "@":
            i += 1
        l = int(item[:i])
    key = ''
    r = ""
    LEN = len(item)
    # for x in item[i:]:
    while i < LEN:
        # print("key:", key)
        # print("r:", r)
        # print("res:", res)
        # print("remain:", item[i:])
        x = item[i]
        i += 1
        if x == '(':
            start = i
            brace = 1
            while brace:
                if item[i] == '(':
                    brace += 1
                elif item[i] == ')':
                    brace -= 1
                i += 1
            end = i
            rr = ""
            while i<LEN and '/' < item[i] < "@":
                rr += item[i]
                i += 1
            rr = int(rr) if rr else 1
            res = parse_formula(item[start:end-1], res, mul=rr*l*mul)
        elif '/' < x < "@":
            r += x
        elif x < "[":
            if key:
                r = int(r) if r else 1
                if key not in res:
                    res[key] = 0
                res[key] += l * r * mul
            key = x
            r = ""
        elif x < "{":
            key += x
    if key:
        r = int(r) if r else 1
        if key not in res:
            res[key] = 0
        res[key] += l * r * mul
    # print("return:", res)
    return res

def run():
    n = int(input())
    while n:
        n -= 1
        s = input().strip()
        # print(s)
        left, right = s.split('=')
        left = left.split("+")
        right = right.split("+")
        left_dict = {}
        right_dict = {}
        for item in left:
            res = parse_formula(item, {})
            for key in res:
                if key not in left_dict:
                    left_dict[key] = 0
                left_dict[key] += res[key]
        for item in right:
            res = parse_formula(item, {})
            for key in res:
                if key not in right_dict:
                    right_dict[key] = 0
                right_dict[key] += res[key]
        output = "Y" if left_dict == right_dict else "N"
        print(output)
        # print(left_dict, right_dict)


def main():
    run()

if __name__ == "__main__":
    main()
