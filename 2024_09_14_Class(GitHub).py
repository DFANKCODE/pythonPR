# def calculate_total_price(quantity, price):
#     total = price*quantity
#     print(total)
#
# calculate_total_price(price=25.5 ,quantity=10)
#


#
# def calculate_total_price(quantity, price,**kwargs):
#     total = price*quantity*(1-kwargs["vip"])*(1-kwargs["sale20"])
#     print(total)
#
# calculate_total_price(price=30 ,quantity=10 ,vip=0.1 ,sale20=0.2)
#
#



# def calculate_simple_interest(principal, rate, time=1):
#     ans = principal*rate*time
#     print(ans)
#
#
# calculate_simple_interest(principal=1000, rate=0.05)
# calculate_simple_interest(principal=1000, rate=0.05, time=2)



# def filter_positive_integers(my_list):
#     NewMy_list = my_list.copy()
#     for i in NewMy_list:
#         if i <= 0:
#             NewMy_list.remove(i)
#     print(NewMy_list)
#
#
# numbers = [-10,3,2,0,-9,-15,-21]
# filter_positive_integers(numbers)
#
#
#
#
#
# def sumsumsusmum(x, y): # 相乘
#     sum = x * y
#     print(sum)
#
# sumsumsusmum(20, 20) # print


# x= 20j 
# y= 20.
# sum = x * y
#
#
# print(sum)


# weight=input("請問體重多少:")
# height=input("請問身高多少:")
#

#
# data = []
#
# with open('food.txt', 'r') as f:
#     for line in f:
#         data.append(line.strip())
# print(data)

data = []
count = 0

with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0 :
            print(len(data))
print("檔案讀取完了,總共有",len(data),'筆資料')

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)

print("每筆留言平均長度是",sum_len/len(data))

# print(data[0])
# print('----------------')
# print(data[1])