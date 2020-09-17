from sys import stdin
from re import findall, compile

    # ele_p = compile(r"[A-Z][a-z]*")

def count(exp, res):
    # print(exp)
    sub_res = {}
    len_exp = len(exp)
    buffer = ''
    coef = 1
    i = 0
    while i < len_exp and ord(exp[i]) >= ord('0') and ord(exp[i]) <= ord('9'):
        buffer += exp[i]
        i += 1

    if(buffer != ''):
        coef = int(buffer)
    # print('coef:', coef)

    while i < len_exp:
        ord_i = ord(exp[i])

        if exp[i] == '(':
            sub_buffer = ""
            sub_depth = 1
            i += 1
            while sub_depth > 0:
                if exp[i] == '(':
                    sub_depth += 1
                elif exp[i] == ')':
                    sub_depth -= 1

                sub_buffer += exp[i]
                i += 1

            bracket_res = {}
            count(sub_buffer[:-1], bracket_res)
            # print(bracket_res)
            buffer = ''
            times = 1
            while i < len_exp and exp[i] >= '0' and exp[i] <= '9':
                buffer += exp[i]
                i += 1
            if buffer != '':
                times = int(buffer)

            for key, num in bracket_res.items():
                bracket_res[key] = num * times
            # print(bracket_res)

            for key, num in bracket_res.items():
                bracket_res[key] = coef * num

                if key in res:
                    res[key] += bracket_res[key]
                else:
                    res[key] = bracket_res[key]
            

        elif ord_i >= ord('A') and ord_i <= ord('Z'):
            ele = exp[i]
            i += 1

            if i < len_exp and ord(exp[i]) >= ord('a') and ord(exp[i]) <= ord('z'):
                ele += exp[i]
                i += 1

            buffer = ''
            dig = 1
            while i < len_exp and ord(exp[i]) >= ord('0') and ord(exp[i]) <= ord('9'):
                buffer += exp[i]
                i += 1

            # print('dig:', dig)

            if buffer != '':
                dig = int(buffer)

            if ele in sub_res.keys():
                sub_res[ele] += dig
            else:
                sub_res[ele] = dig


        else:
            i += 1

    for key, i in sub_res.items():
        sub_res[key] = coef * i

        if key in res:
            res[key] += sub_res[key]
        else:
            res[key] = sub_res[key]

    return res

def run():
    n = map(int, input())

    for line in stdin:
        exp_l, exp_r = line.split('=')
        len_exp_r = len(exp_r)

        res_r = {}
        for sub_exp in exp_r.split('+'):
            count(sub_exp, res_r)
            # print("expr:", res_r, sub_exp)

        res_l = {}
        for sub_exp in exp_l.split('+'):
            count(sub_exp, res_l)
            # print("expl:", res_l, sub_exp)

        output = 'Y' if res_r == res_l else 'N'
        print(output)
        

if __name__ == "__main__":
    run()