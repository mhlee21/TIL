# 2022.02.09
# 종이자르기
# https://www.acmicpc.net/problem/2628

w, l = map(int, input().split())
num = int(input())
arr = [list(map(int,input().split())) for i in range(num)]

# 방법 1
# cut_width = sorted([cut[1] for cut in arr if cut[0]==1])
# cut_length = sorted([cut[1] for cut in arr if cut[0]==0])
# 
# max_width = -1
# max_length = -1
# if cut_width:
#     for idx in range(len(cut_width)):
#         if idx == 0:
#             max_width = max(max_width, cut_width[idx])
#         else:
#             max_width = max(max_width, cut_width[idx] - cut_width[idx-1])
#     else:
#         max_width = max(max_width, w - cut_width[-1])
# else:
#     max_width = w

# if cut_length:
#     for idx in range(len(cut_length)):
#         if idx == 0:
#             max_length = max(max_length, cut_length[idx])
#         else:
#             max_length = max(max_length, cut_length[idx] - cut_length[idx-1])
#     else:
#         max_length = max(max_length, l - cut_length[-1])
# else:
#     max_length = l

# print(max_width * max_length)

# 방법 2
cut_width = [0] + sorted([cut[1] for cut in arr if cut[0]==1]) + [w]
cut_length = [0] + sorted([cut[1] for cut in arr if cut[0]==0]) + [l]

wid = [cut_width[idx] - cut_width[idx-1] for idx in range(1,len(cut_width))]
leng = [cut_length[idx] - cut_length[idx-1] for idx in range(1,len(cut_length))]

print(max(wid), max(leng))
print(max(wid) * max(leng))