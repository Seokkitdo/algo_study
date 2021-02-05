# 거스름돈
# n = 1260
# count = 0
# array = [500, 300, 100, 50, 10]
#
# for coin in array:
#     count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
#     n %= coin
# print(count)

# 화폐 종류가 K라고 할 때, 소스코드의 복잡도는 O(K)
# 이 알고리즘의 시간 복잡도는 거슬러줘야 하는 금액과는 무관하며 동전의 종류에 영향을 받음



# 1이 될 때까지
# N, K를 공백을 기준으로 구분하여 입력 받기
# n, k = map(int, input().split())
#
# result = 0
#
# while True:
#     # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
#     # 나누어 떨어지는 수 구하기
#     target = (n // k) * k
#     print('target', target)
#     # 나누어 떨어지는 가장 가까운 수를 뺌으로써 -1연산을 몇 번 수행하는지 확인
#     result += (n - target)
#     print('first', result)
#     n = target
#     # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
#     if n < k:
#         break
#     # K로 나누기
#     result += 1
#     print('result', result)
#     n //= k
#     print('n', n)
# result += (n - 1)
# print('final', result)


data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)

