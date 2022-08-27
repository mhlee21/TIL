import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    answer = float('inf')

    # reverse : 1(오름차순 검사), -1(내림차순 검사)
    def check(card_arr, reverse):
        for idx in range(1, N):
            if card_arr[idx-1] + reverse != card_arr[idx]:
                return False
        return True

    def my_dfs(dep, card_arr):
        global answer
        # 가지치기
        if dep >= answer:
            return
        # 정렬이 불가능한 경우나, 셔플 횟수가 5회 초과하는 경우 더이상 검사하지 않는다.
        if dep > 5:
            return
        # 오름차순이나 내림차순으로 정렬되었을 경우, 셔플 횟수의 최소값을 저장한다.
        if check(card_arr, 1) or check(card_arr, -1):
            if dep < answer:
                answer = dep
            return

        num = N//2
        left = card_arr[:num]
        right = card_arr[num:]
        for x in range(1,N):
            card_tmp = []
            shuffle = num - x

            # shuffle 값이 양수일 경우 왼쪽 카드더미가 위로간다.
            if shuffle > 0:
                card_tmp += left[:shuffle]
                for i in range(num):
                    card_tmp.append(right[i])
                    if shuffle+i < num:     # index 유효성 검사
                        card_tmp.append(left[shuffle+i])

            # shuffle 값이 음수일 경우 오른쪽 카드더미가 위로간다.
            else:
                # shuffle = 0 인 경우에도 오른쪽부터 시작하기 위해 1을 더한다.
                shuffle = shuffle * (-1) + 1

                card_tmp += right[:shuffle]
                for i in range(num):
                    card_tmp.append(left[i])
                    if shuffle+i < num:     # index 유효성 검사
                        card_tmp.append(right[shuffle+i])

            my_dfs(dep+1, card_tmp[:])

    my_dfs(0, cards[:])
    if answer > 5:
        answer = -1

    print(f'#{test_case} {answer}')