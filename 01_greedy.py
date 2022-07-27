n = int(input("가격을 입력하세요 >> "))

coin_types = [10, 50, 100, 500]

# set = {1,2,2,2,2,3,4,5,5,5,5,6}
#
# print("list : {0}".format(list))
# print("set : {0}".format(set))
#
# for i in list:
#     print(i)
#
# print("하윙")
#
# int a = input()
coin_types.sort(reverse=True)
# print(list)
cnt = 0

for coin in coin_types:
    cnt += n//coin
    n %= coin

print("총 갯수 : ", cnt)



