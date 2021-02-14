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


# data = input()
#
# result = int(data[0])
#
# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
# print(result)


# data = input()
#
# # 첫 번째 문자를 숫자로 변경하여 대입
# result = int(data[0])
#
# # 두 번째 숫자부터 for 문을 돌림
# for i in range(1, len(data)):
#     # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
#
# print(result)

# # 총 인원
# n = input()
# # 각 인원 공포도
# data = list(map(int, input().split()))
#
# # 현재 그룹에 포함된 모함가 수
# count = 0
# # 총 그룹의 수
# result = 0
#
# for i in data:
#     count += 1
#     if count >= i:
#         result += 1
#         count = 0
# print(result)



# # N 입력 받기
# n = int(input())
# x, y = 1, 1
# plans = input().split()
#
# # L, R, U, D에 따른 이동방향
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']
#
# # 이동 계획을 하나씩 확인하기
# for plan in plans:
#     # 이동 후 좌표 구하기
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     # 공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     # 이동 수행
#     x, y = nx, ny
# print(x, y)


# n = int(input())
# result = 0
#
# for hour in range(n+1):
#     for minutes in range(60):
#         for seconds in range(60):
#             # 시 분초를 모두 더해서 그 중에서 3을 카운트
#             if '3' in str(hour) + str(minutes) + str(seconds):
#                 result += 1
# print(result)


# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1
#
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
#
# result = 0
# for step in steps:
#     next_row = row + step[0]
#     next_column = column + step[1]
#
#     if 1 <= next_row <= 8 and 1 <= next_column <= 8:
#         result += 1
# print(result)

# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1
#
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
#
# result = 0
# for step in steps:
#     next_row = row + step[0]
#     next_column = column + step[1]
#
#     if 1 <= next_row <= 8 and 1 <= next_column <= 8:
#         result += 1
#
# print(result)

# data = input()
# result = []
# value = 0
#
# for x in data:
#     if x.isalpha():
#         result.append(x)
#     else:
#         value += int(x)
#
# result.sort()
#
# if value != 0:
#     result.append(str(value))
# print(result)
# print(''.join(result))


# n = int(input())
# count = 0
# list = [500, 100, 50, 10]
# for coin in list:
#     count += n // coin
#     n %= coin
# print(count)


# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort()
# first = data[-1]
# second = data[-2]
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1
# print(result)



# n = input()
# count = 0
# while n >= 0:
#     if n % 5 == 0:
#         count += n // 5
#         print(count)
#         break
#     n -= 3
#     count += 1
# else:
#     print(-1)


# n = int(input())
# people = list(map(int, input().split()))
# result = 0
# bsum = 0
# sp = sorted(people)
# for i in range(n):
#     if i == 0:
#         result += sp[0]
#         continue
#     for j in range(i):
#         bsum += sp[j]
#     result += sp[i] + bsum
#     bsum = 0
# print(result)

# n = int(input())
# s = list(map(int, input().split()))
#
# s.sort()
# result = 0
# for i in range(n):
#     for j in range(i+1):
#         result += s[j]
# print(result)


# n, total = list(map(int, input().split()))
# count = 0
#
# moneys = []
# for i in range(n):
#     moneys.append(int(input()))
#
# moneys.reverse()
# for money in moneys:
#     if total >= money:
#         count += total // money
#         total %= money
#     if total == 0:
#         break
# print(count)


# n, k = map(int, input().split())
# count = 0
#
# while n >= 1:
#     if n % k != 0:
#         n -= 1
#         count += 1
#     n //= k
#     count += 1
#
#     if n == 1:
#         break
# print(count)



