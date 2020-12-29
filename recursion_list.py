def recursion(a_list, i):
    print(a_list[i])
    
    if(i + 3 < len(a_list)):
        recursion(a_list, i + 3)

i = 2
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
recursion(some_list, i)
