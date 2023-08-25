grade_list = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
total_score = 0
total_point = 0

for _ in range(20):
    name, point, grade = input().split()

    if grade != 'P':
        total_point += float(point)
        for i in grade_list:
            if i == grade:
                total_score += float(point) * score_list[grade_list.index(i)]
                break

print(total_score / total_point)