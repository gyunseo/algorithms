# 2019311801 이균서
import sys
import csv
import re
from collections import defaultdict

print = sys.stdout.write
fin = open("data.csv", "r", encoding="utf-8")
csv_fin = csv.reader(fin)
data = []
user_dict = defaultdict(int)
msg_cnt = 0
for i, line in enumerate(csv_fin):
    if i == 0:
        continue
    msg_cnt += 1
    # if line[2] includes "ㅋ" more than 3 times sequentially, then add 1 to user_dict[line[1]]
    if re.search(r"ㅋ{3,}", line[2]):
        user_dict[line[1]] += 1

# print user who has the most high value of user_dict
max_value = max(user_dict.values())
for k, v in user_dict.items():
    if v == max_value:
        print(k + "\n")
# 백분율로 소수점 2번째 자리까지 출력
print(f"{max_value * 100 / msg_cnt:.2f}%\n")
fin.close()
