#CA02 Problem1
#Given an input list remove the element at index 2 and add it at index 4 and also at the end of the list.



def list_function(user_list):
    element= user_list[2]
    user_list.remove(element)
    user_list.insert(4,element)
    user_list.insert(len(user_list )-1, element)
    print(user_list)

user_input = input("Enter the list items separated by spaces: ")
user_list = user_input.split()
print("Your list:", user_list)
a=list_function(user_list)
print(a)