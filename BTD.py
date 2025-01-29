# 입력받은 세 개의 숫자를 오름차순으로 정렬하기

def sorting() :
    num1 = int(input("숫자를 하나 입력하세요: "))
    num2 = int(input("숫자를 하나 더 입력하세요: "))
    num3= int(input("숫자를 하나 더 입력하세요: "))

    #버블정렬
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num2:
        num1, num2 = num2, num1

    print(f"입력한 숫자를 오름차순으로 정렬하면 {num1}, {num2}, {num3}입니다.")


sorting()