import random, time

n = 1000000
gpa_list = [round(random.uniform(1, 9), 2) for _ in range(n)] # 학생들의 내신 평균 등급을 랜덤하게 추출. 이때 등급은 1.0 - 9.0 사이의 실수여야 함. 

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] # pivot 설정
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot: # pivot 보다 작을 때
            lesser_arr.append(num)
        elif num > pivot: # pivot 보다 클 때
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr) # 정렬된 상태의 리스트를 return

begin_time = time.time()
sorted_gpa_list = quick_sort(gpa_list)
end_time = time.time()
print(f"elapsed time: {end_time - begin_time}s\n")
print(sorted_gpa_list[58000: 62000]) # 58000등 - 61999등 인 학생들의 평균 등급 출력