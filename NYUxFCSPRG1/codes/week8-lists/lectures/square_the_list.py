def main():
    lst = [1, 2, 3]
    # print(create_sqr_list(lst))
    sqr_list_in_place(lst)
    print(lst)

def create_sqr_list(lst):
    return [e ** 2 for e in lst]

def sqr_list_in_place(lst):
    for i in range(len(lst)):
        lst[i] **= 2
    
main()
