
n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
for i in student_marks:
    if i==query_name:
        print('%.2f'%(sum(student_marks[i])/3))



