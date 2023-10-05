import csv, re

fin = open("data.csv", "r", encoding="cp949")
csv_fin = csv.reader(fin)
data = []
for i, line in enumerate(csv_fin):
    if i == 0:
        continue
    # get only number
    line[4] = int(float(re.match(r"\d+\.\d+|\d+", line[4]).group()))
    line[7] = int(float(line[7]))
    data.append(line)


def get_quick_sorted_list(arr, key=None):
    if len(arr) <= 1:
        return arr
    key_func = key if key else (lambda x: x)
    pivot_index = len(arr) // 2
    pivot = key_func(arr[pivot_index])
    l, m, r = [], [], []
    for row in arr:
        x = key_func(row)
        if x < pivot:
            l.append(row)
            continue
        if x > pivot:
            r.append(row)
            continue

        m.append(row)

    return get_quick_sorted_list(l, key_func) + m + get_quick_sorted_list(r, key_func)


sorted_data_by_votes = get_quick_sorted_list(data, key=lambda x: x[7])
sorted_data_by_votes.reverse()
sorted_data_by_strength = get_quick_sorted_list(data, key=lambda x: x[4])

fout = open("sorted_by_votes.csv", "w", encoding="cp949")
fout.write("#,,Whisky,Stated Age,Strength,Size,Rating,Votes,\n")


def convert_to_str_with_double_quotes(x):
    return f'"{x}"'


for row in sorted_data_by_votes:
    fout.write(f"{','.join(map(convert_to_str_with_double_quotes,row))}\n")

fout.close()
fout = open("sorted_by_strength.csv", "w", encoding="cp949")
fout.write("#,,Whisky,Stated Age,Strength,Size,Rating,Votes,\n")
for row in sorted_data_by_strength:
    fout.write(f"{','.join(map(convert_to_str_with_double_quotes,row))}\n")

fout.close()
fin.close()
