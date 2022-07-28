# N, M, K 를 공백으로 구분하여 입력받기
# n, m, k = map(int, input().split())
#
# # N개의 수를 공백으로 구분하여 입력받기
# data = list(map(int, input().split()))
#
# data.sort()
# first = data[n-1]
# second = data[n-2]
# result = 0
# while True:
#     for i in range(k):
#         if m==0: break
#         result += first
#         m -= 1
#
#     if m==0: break
#     result += second
#     m -= 1
#
# print(result)


# print(data)

# 2번째 방법
# 시간적으로 좀더 효율 적이다.
n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

first = data[n-1]
second = data[n-2]

count = int(m/(k+1))*k + m%(k+1)

result = first*count
result += (m-count)*second

print(result)


