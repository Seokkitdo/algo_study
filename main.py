# a = 7
# b = 3
# # 나누기 실수로 계산
# print(a / b)
# # 나머지연산
# print(a % b)
# # 몫 구하기
# print(a // b)

# 리스트 자료형
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a)
#
# #네 번재 원소만 출력
# print(a[3])
#
# # 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
# n = 10
# a = [0] * n
# print(a)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # 여덟 번째 원소만 출력
# print(a[7])
#
# # 뒤에서 첫 번째 원소 출력
# print(a[-1])
#
# # 뒤에서 세 번째 원소 출력
# print(a[-3])
#
# # 네 번째 원소 값 변경
# a[3] = 7
# print(a)

# # 슬라이싱
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # 네 번째 원소만 출력
# print(a[3])
#
# # 두 번째 원소부터 네 번째 원소까지
# # 1번 인덱스부터 3번까지 a[1],a[2],a[3] 출력
# print(a[1:4])

# # 리스트 컴프리헨션
# # 0부터 9까지의 수를 포함하는 리스트 초기화
# # 두 번째 i가 0부터 9까지 매번 증가를 하면서
# # 반복을 할 때마다 그 i의 값을 원소로 설정하여 list로로만듬
# array = [i for i in range(10)]
#
# print(array)

# a = [i for i in range(20)]
# print(a)
#
# # 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
# array = [i for i in range(20) if i % 2 == 1]
# print(array)
#
# # 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
# array = [i*i for i in range(1, 10)]
# print(array)


# array = [i for i in range(20) if i % 2 == 1]
# print(array)
#
# # N x M 크기의 2차원 리스트 초기화
# n = 4
# m = 3
# # n번 반복을 할 때마다 [0] * m을 반복
# array = [[0] * m for _ in range(n)]
# print(array)


# # 반복문에서 _를 사용할 때
# # 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 _를 자주 사용함
# summary = 0
# for i in range(1, 10):
#     summary += i
# print(summary)
#
# for _ in range(5):
#     print("Hello World")

# # 리스트 관련 기타 메서드
# a = [1, 4, 3]
# print("기본 리스트 : ", a)
#
# # 리스트에 원소 삽입
# a.append(2)
# print("삽입 : ", a)
#
# # 오름차순 정렬
# a.sort()
# print("오름차순 정렬 : ", a)
#
# # 내림차순 정렬
# a.sort(reverse = True)
# print("내림차순 정렬 : ", a)

# a = [4, 3, 2, 1]
#
# # 리스트 원소 뒤집기
# a.reverse()
# print("원소 뒤집기 : ", a)
#
# # 특정 인덱스에 데이터 추가
# a.insert(2, 3)
# print("인덱스 2에 3 추가 : ", a)
#
# # 특정 값인 데이터 개수 세기
# print("값이 3인 데이터 개수 : ", a.count(3))
#
# # 특정 값 데이터 삭제
# a.remove(1)
# print("값이 1인 데이터 삭제 : ", a)

# a = [1, 2, 3, 4, 5, 5, 5]
# remove_set = {3, 5} # 집합 자료형
#
# # remove
# result = [i for i in a if i not in remove_set]
# print(result)

# data = 'Hello World'
# print(data)
#
# data = "Don't you know \"Python\"?"
# print(data)

# a = "Hello"
# b = "World"
# print(a + " " + b)
#
# a = "String"
# print(a * 3)
#
# a = "ABCDEF"
# print(a[2:4])

# a = "Hello"
# b = "World"
# print(a + b)
#
# a[2] = 'a'

# a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#
# # 네 번재 원소만 출력
# print(a[3])
#
# # 두 번째 원소부터 네 뻔재 원소까지
# print(a[1:4])

# a = (1, 2, 3, 4)
# print(a)
#
# a[2] = 7

# # dict() 함수로 사전 자료형 초기화
# data = dict()
# data['사과'] = 'Apple'
# data['바나나'] = 'Banana'
# data['코코넛'] = 'Coconut'
#
# print(data)
#
# if '사과' in data:
#     print("'사과'를 키로 가지는 데이터가 존재합니다.")

# data = dict()
# data['사과'] = 'Apple'
# data['바나나'] = 'Banana'
# data['코코넛'] = 'Coconut'
#
# # 키 데이터만 담은 리스트
# key_list = data.keys()
# # 값 데이터만 담은 리스트
# value_list = data.values()
# print(key_list)
# print(value_list)
#
# # 각 키에 따른 값을 하나씩 출력
# for key in key_list:
#     print(data[key])

# a = dict()
# a['홍길동'] = 97
# a['이순신'] = 98
#
# print(a)
#
# b = {
#     '홍길동' : 97,
#     '이순신' : 98
# }
#
# print(b)
#
# a_key_lst = a.keys()
# key_list = list(b.keys())
# print(a_key_lst)
# print(key_list)

# # 집합 자료형 초기화 방법 1
# data = set([1, 1, 2, 3, 4, 4, 5])
# print(data)
#
# # 집합 자료형 초기화 방법 2
# data = {1, 1, 2, 3, 4, 4, 5}
# print(data)

# a = set([1, 2, 3, 4, 5])
# b = set([3, 4, 5, 6, 7])
#
# # 합집합
# print(a | b)
#
# # 교집합
# print(a & b)
#
# # 차집합
# print(a - b)

# data = set([1, 2, 3])
# print(data)
#
# # 새로운 원소 추가
# data.add(4)
# print(data)
#
# # 새로운 원소 여러 개 추가
# data.update([5, 6])
# print(data)
#
# # 특정한 값을 갖는 원소 삭제
# data.remove(3)
# print(data)

# # 데이터의 개수 입력
# n = int(input())
# # 각 데이터를 공백을 기준으로 구분하여 입력
# data = list(map(int, input().split()))
#
# data.sort(reverse=True)
# print(data)

# # 문자열 입력
# data = input()
# print(data)
#
# # 공백을 기준으로 문자열 입력
# data = input().split()
# print(data)

# 입력받은 문자열은 정수로 변환
# data = map(int, input().split())
# print(data)
#
# # 리스트로 형변환
# data = list(map(int, input().split()))
# print(data)


# # 문자열 입력 받기
# import sys
# data = sys.stdin.readline().rstrip()
# print(data)

# # 출력할 변수들
# a = 1
# b = 2
# print(a, b)
# print(7, end=" ")
# print(8, end=" ")
#
# # 출력할 변수
# answer = 7
# print(" 정답은 " + str(answer) + "입니다.")

# x = 15
#
# if x >= 10:
#     print("x >= 10")
# if x >= 0:
#     print("x >= 0")
# if x >= 30:
#     print("x >= 30")


# scores = [90, 85, 77, 65, 97]
# cheating_student_list = {2, 4}
# for i in range(5):
#     if i + 1 in cheating_student_list:
#         continue
#     if scores[i] >= 80:
#         print(i + 1, "번 학생은 합격입니다.")


# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i, "X", j, "=", i * j)
#     print()

# def add(a, b):
#     return a + b
#
#
# print(add(3, 4))

# def add(a, b):
#     print('함수의 결과 : ', a + b)
#
#
# add(3, 7)


# def add(a, b):
#     print('함수의 결과 : ', a + b)
#
#
# add(b = 3, a = 7)


# a = 0
#
#
# def func():
#     global a
#     a += 1
#
#
# for i in range(10):
#     func()
#
#
# print(a)

# def operator(a, b):
#     add_var = a + b
#     subtract_var = a - b
#     multiply_var = a * b
#     divide_var = a / b
#     return add_var, subtract_var, multiply_var, divide_var
#
#
# a, b, c, d = operator(7, 3)
# print(a, b, c, d)

# def add(a, b):
#     return a + b
#
#
# # 일반적인 add() 메서드 사용
# print(add(3, 7))
#
# # 람다 표현식으로 구현한 add() 메서드
# print((lambda a, b: a + b)(3, 7))

#
# array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
#
#
# def my_key(x):
#     return x[1]
#
#
# print(sorted(array, key=my_key))
# print(sorted(array, key=lambda x: x[1]))


# # sum()
# result = sum([1, 2, 3, 4, 5])
# print(result)
#
# # min(), max()
# min_result = min(7, 3, 5, 2)
# max_result = max(7, 3, 5, 2)
# print(min_result, max_result)
#
# # eval()
# result = eval("(3+5)*7")
# print(result)


# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)

#sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)