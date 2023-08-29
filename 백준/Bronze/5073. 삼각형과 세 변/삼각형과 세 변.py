while True:
    len_list = list(map(int, input().split()))
    if len_list == [0, 0, 0]:
        break
    else:
        if max(len_list) >= sum(len_list) - max(len_list):
            print("Invalid")
        else:
            if len_list.count(len_list[0]) == 3:
                print("Equilateral")
            elif len_list.count(len_list[0]) == 2 or len_list.count(len_list[1]) == 2:
                print("Isosceles")
            else:
                print("Scalene")