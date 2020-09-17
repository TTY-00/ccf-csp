# import sys

# def run():
#     n = int(input())
#     mmap = []
#     res = [0, 0, 0, 0, 0]
#     pos_x_m = [-1, 0, 1, 0]
#     pos_y_m = [0, 1, 0, -1]
#     pos_x_s = [-1, 1, 1, -1]
#     pos_y_s = [1, 1, -1, -1]

#     for line in sys.stdin:
#         x, y = line.split()
#         mmap.append((int(x), int(y)))

#     mmap_s = set(mmap)
#     # print(mmap_s)

#     for x, y in mmap_s:
#         can_be = 1
#         for i in range(4):
#             xx = pos_x_m[i]
#             yy = pos_y_m[i]
#             if (x + xx, y + yy) not in mmap_s:
#                 can_be = 0
#                 break
        
#         if can_be:
#             count = 0
#             for i in range(4):
#                 xx = pos_x_s[i]
#                 yy = pos_y_s[i]
#                 if (x + xx, y + yy) in mmap_s:
#                     count += 1
                
#             res[count] += 1

#     for i in range(5):
#         print(res[i])

# if __name__ == "__main__":
#     run()



import sys

def run():
    n = int(input())
    mmap = []
    res = [0, 0, 0, 0, 0]
    pos_x_m = [-1, 0, 1, 0]
    pos_y_m = [0, 1, 0, -1]
    pos_x_s = [-1, 1, 1, -1]
    pos_y_s = [1, 1, -1, -1]

    for line in sys.stdin:
        x, y = line.split()
        mmap.append([int(x), int(y)])

    # mmap_s = set(mmap)
    # print(mmap_s)
    mmap_s = mmap

    for x, y in mmap_s:
        can_be = 1
        for i in range(4):
            xx = pos_x_m[i]
            yy = pos_y_m[i]
            if [x + xx, y + yy] not in mmap_s:
                can_be = 0
                break
        
        if can_be:
            count = 0
            for i in range(4):
                xx = pos_x_s[i]
                yy = pos_y_s[i]
                if [x + xx, y + yy] in mmap_s:
                    count += 1
                
            res[count] += 1

    for i in range(5):
        print(res[i])

if __name__ == "__main__":
    run()