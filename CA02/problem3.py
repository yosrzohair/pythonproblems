#CA02 Problem3
#Given a list slice it into a three equal slices and then print each slice reversed.


list = [1,2,3,4,5,6,7,8,9]
step = int (len(list)/3)

first_thrid= list[:step]
second_third= list[step:step*2]
third_thrid = list[step*2 :]

first_thrid.reverse()
second_third.reverse()
third_thrid.reverse()

print(first_thrid)
print(second_third)
print(third_thrid)