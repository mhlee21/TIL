'''
BOJ
직사각형에서 탈출
브론즈3
5분
https://www.acmicpc.net/problem/1085
'''
x,y,w,h = map(int, input().split())
res = [x,y,w-x,h-y]
print(min(res))