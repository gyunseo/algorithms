import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
print = sys.stdout.write

course_dict = {
    "집합론": 0,
    "미분적분학1": 1,
    "대수학": 2,
    "미분적분학2": 3,
    "이산수학": 4,
    "선형대수학": 5,
    "해석학1": 6,
    "미분방정식": 7,
    "응용수학개론": 8,
    "선형대수학의응용": 9,
    "해석학2": 10,
    "정수론": 11,
    "벡터해석학": 12,
    "일반기하학": 13,
    "수학교육론": 14,
    "미분기하학1": 15,
    "위상수학1": 16,
    "추상대수학1": 17,
    "확률통계학1": 18,
    "수학교재연구및지도법": 19,
    "학교수학교재연구": 20,
}
in_degree = [0 for _ in range(21)]
adjacent_lists = [[] for _ in range(21)]


def link_two_nodes(src, dsts):
    for dst in dsts:
        adjacent_lists[course_dict[src]].append(course_dict[dst])
        in_degree[course_dict[dst]] += 1


link_two_nodes("집합론", ["위상수학1", "응용수학개론"])
link_two_nodes("미분적분학1", ["미분적분학2"])
link_two_nodes("미분적분학2", ["미분기하학1", "해석학1", "미분방정식", "응용수학개론", "일반기하학", "확률통계학1"])
link_two_nodes("선형대수학", ["선형대수학의응용", "일반기하학"])
link_two_nodes("해석학1", ["해석학2"])
link_two_nodes("응용수학개론", ["벡터해석학"])
link_two_nodes("선형대수학의응용", ["미분기하학1"])
link_two_nodes("해석학2", ["위상수학1"])
link_two_nodes("정수론", ["추상대수학1"])
link_two_nodes("수학교육론", ["학교수학교재연구"])
print("수강한 과목을 적으시오: ")
taken_courses = [*map(str.strip, input().rstrip().split(","))]
print("\n")


def get_in_degree(course):
    return in_degree[course_dict[course]]


taken_courses.sort(key=get_in_degree)
for taken_course in taken_courses:
    linked_courses = [*adjacent_lists[course_dict[taken_course]]]
    for linked_course in linked_courses:
        in_degree[linked_course] -= 1

iteration_trigger = True
while iteration_trigger:
    print("수강하고 싶은 과목을 적으시오(종료를 원하면 x입력): ")
    to_be_taken_course = input().rstrip()
    print("\n")
    if to_be_taken_course == "x" or to_be_taken_course == "X":
        iteration_trigger = False
        continue

    if in_degree[course_dict[to_be_taken_course]] == 0:
        print("수강 가능\n")
    else:
        print("수강 불가\n")
