def test_first_student(students):
    chances = 1
    for i in range(min(len(students), 4)):
        if students[0][1] < students[i][1] and students[0][0] != students[i][0]:
            chances -= 1
    return chances >=0

def test_last_student(students):
    chances = 1
    for i in range(min(len(students), 4)):
        if students[len(students) - 1][1] > students[len(students) - i - 1][1] and students[len(students) - 1][0] != students[i][0]:
            chances -=1
    return chances >=0

def analyse_student(students, i, wrong_rank):
    if i == 0:
        return test_first_student(students)
    if students[i][1] > students[i - 1][1]:
        if i == len(students) - 1:
            return test_last_student(students)
        return (wrong_rank != students[i][0] and wrong_rank != None)  or students[i - 1][0] == wrong_rank or students[i + 1][1] <  students[i][1]
    if i < len(students) - 1:
        if students[i][1] < students[i + 1][1]:
            if i == len(students) - 2:
                return not test_last_student(students) == True 
            return not analyse_student(students, i + 1, wrong_rank) 
    return True

def find_wrong_rank(students):
    for i in range(len(students) - 1):
        if students[i][0] == students[i + 1][0] and students[i][1] == students[i + 1][1]:
            students.remove(students[i])
            return None
        if students[i][0] == students[i + 1][0] and abs(students[i][1] - students[i + 1][1]) > 0.001:
            return students[i][0]
    return None


def main():
    n = int(input().strip())
    students = list(map(lambda s: (int(s[0]), float(s[1])), (input().split(" ")  for _ in range(n))))
    students = sorted([(*students[i], i + 1) for i in range(n)], key = lambda s: s[0])
    wrong_rank = find_wrong_rank(students); n = len(students)
    for i in range(n):
        if not analyse_student(students, i, wrong_rank):
            print(students[i][2])
            return
    print(0)

if __name__ == '__main__':
    main()