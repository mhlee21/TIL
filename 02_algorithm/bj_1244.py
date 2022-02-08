# 2022.02.08
# 스위치 켜고 끄기
# https://www.acmicpc.net/problem/1244

switch_num = int(input())
switch_status = [0] + list(map(int,input().split()))
student_num = int(input())
student = [list(map(int,input().split())) for i in range(student_num)]

for s in student:
    # 남학생
    if s[0] == 1:
        # 스위치 1~n
        for idx in range(s[1],switch_num+1, s[1]):
            switch_status[idx] = 1 if switch_status[idx]==0 else 0

    # 여학생
    if s[0] == 2:
        # 자기가 받은 수와 같은 번호 스위치 상태 바꾸기
        switch_status[s[1]] = 1 if switch_status[s[1]]==0 else 0
        i = 1
        # 좌우가 대칭인 스위치 구간 상태 바꾸기
        while True:
            # 인덱스값 벗어나면 while 문 종료
            if s[1]-i < 1 or s[1]+i > switch_num:
                break

            if switch_status[s[1]-i] == switch_status[s[1]+i]:
                switch_status[s[1]-i] = 1 if switch_status[s[1]-i]==0 else 0
                switch_status[s[1]+i] = 1 if switch_status[s[1]+i]==0 else 0
            else:
                break
            i += 1

for status in switch_status[1:]:
    print(status)