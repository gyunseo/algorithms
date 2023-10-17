#!/usr/bin/zsh

# 반복문을 사용하여 여러 입력 파일 실행
for ((i=0; i<6; i++))
do
    input_file="input${i}.txt"
    output_file="output${i}.txt"
    
    # 입력 파일을 python3 스크립트에 전달하고 결과를 출력 파일에 저장
    python3 week6_assignment.py < "$input_file" > "$output_file"
    
    # 실행 결과 출력
    echo "Running python3 week6_assignment with $input_file, output saved to $output_file"
done
