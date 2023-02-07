inputInt = int(input("please input a number"))
if inputInt > 5 :
    print("num is :"+str(inputInt))
elif inputInt <4:
    print("please reinput")
elif inputInt == 4|inputInt==5:
    print("right")


worlds = ['001', '002', '007', '008']
for i in worlds:
    print(i)


# 从0 - 5 遍历
for i in range(5):
    print(i)
    if i >3:
        break #跳出当前循环
        print("over")
    print("ok")
print("bye bye")