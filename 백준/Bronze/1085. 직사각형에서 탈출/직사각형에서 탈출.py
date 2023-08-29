x, y, w, h = map(int, input().split())
len_list = [x, y, abs(x-w), abs(y-h)]

print(min(len_list))