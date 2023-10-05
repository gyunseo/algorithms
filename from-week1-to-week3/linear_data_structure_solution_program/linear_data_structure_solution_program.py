import sys, re

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
print = sys.stdout.write


def trimString(to_be_trimmed_str):
    return re.sub(
        "[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`'…》\”\“\’·]",
        "",
        to_be_trimmed_str.replace(" ", ""),
    ).lower()


input_str = input().rstrip()

while input_str:
    input_str = trimString(input_str)

    def is_palindrome():
        stack = [*input_str[:]]
        str_len = len(input_str)
        if str_len <= 0:
            return False

        for i in range(str_len):
            if input_str[i] != stack.pop():
                return False

        return True

    if is_palindrome():
        print(f"Yes\n")
    else:
        print(f"No\n")

    input_str = input().rstrip()
