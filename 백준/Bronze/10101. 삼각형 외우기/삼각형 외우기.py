x_list = []

for i in range(3):
    x_list.append(int(input()))

if sum(x_list) != 180:
    print("Error")
else:
    for i in range(3):
        if x_list.count(x_list[i]) == 3:
            print("Equilateral")
            break
        elif x_list.count(x_list[i]) == 2:
            print("Isosceles")
            break
        else:
            if x_list.count(x_list[i+1]) == 2:
                print("Isosceles")
                break
            else:
                print("Scalene")
                break