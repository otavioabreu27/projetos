num_1 = float(input())
num_2 = float(input())
num_3 = float(input())

#1 2 3
if num_1 >= num_2 and num_1 >= num_2 and num_2 >= num_3:
    print(num_1,'',num_2,'',num_3)
#1 3 2
if num_1 >= num_2 and num_1 >= num_3 and num_3 >= num_2:
    print(num_1,'',num_3,'',num_2)
#2 1 3
if num_2 >= num_1 and num_2 >= num_3 and num_1 >= num_3:
    print(num_2,'',num_1,'',num_3)
#2 3 1
if num_2 >= num_1 and num_2 >= num_3 and num_3 >= num_1:
    print(num_2,'',num_3,'',num_1)
#3 1 2
if num_3 >= num_1 and num_3 >= num_2 and num_1 >=num_2:
    print(num_3,'',num_1,'',num_2)
#3 2 1
if num_3 >= num_1 and num_3 >= num_2 and num_2 >= num_1:
    print(num_3,'',num_2,'',num_1)


