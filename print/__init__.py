
_3test = 3*"test" # testtesttest
print(_3test)
print(_3test[0]) ## 正序
print(_3test[-3]) # 倒序
print(_3test[0:2]) # 切割
print(_3test[:3])


print("this"+" is"+" test")

len = len(_3test)
print(len)



sequence = [1,2,3,4,5,6]
print(sequence[0])
print(sequence[-1])
print(sequence[:])
print(['1']+sequence[:])
sequence.append(9)
print(sequence)
sequence.append(3 ** 2)  # 3^2
sequence.append(2 ** 10)
print(sequence)

a, b = 0, 1 # a = 0, b = 1
while a < 1000:
    print(a, end=',')
    a, b = b, a + b
