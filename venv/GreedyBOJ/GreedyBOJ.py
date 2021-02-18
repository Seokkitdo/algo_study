# 1931 - 회의실 배정
def solution(InputArr):
    answer = 0
    endTime = 0
    for i, j in InputArr:
        if i >= endTime:
            answer += 1
            endTime = j
    print(InputArr)
    return answer

n = int(input())
InputArr = []

for i in range(n):
    a, b = map(int, input().split())
    InputArr.append([a, b])

InputArr.sort(key=lambda x: (x[1], x[0]))

print(solution(InputArr))

