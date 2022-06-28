# 입력값 (가치, 무게)
ccargo = [
    (4,12),
    (2,1),
    (10,4),
    (1,1),
    (2,2),
]

def zero_one_knapsack(cargo):
    capacity = 15
    pack = []

    for i in range(len(cargo) + 1): # 짐 개수
        pack.append([])
        for c in range(capacity+1): # 배낭 용량
            if i == 0 or c == 0:
                pack[i].append(0)

            # 짐의 무게가 용량보다 작은 경우
                # 짐의 무게를 뺀 가치 + 짐의 가치와
                # 현재 pack 의 가치를 비교하여 더 큰 값을 저장
            elif cargo[i-1][1] <= c:
                pack[i].append(
                    max(
                        cargo[i-1][0] + pack[i-1][c-cargo[i-1][1]],
                        pack[i-1][c]
                    )
                )

            # 아닌 경우 이전 pack의 값(가치)을 저장
            else:
                pack[i].append(pack[i-1][c])

    return pack[-1][-1]

print(zero_one_knapsack(ccargo))