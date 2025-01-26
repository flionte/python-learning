# 구구단 표 출력하기

#제목
print(format("구구단표", ">22s"))
print("  |  ", end="")
for i in range(1,10) :
    val = str(i)
    if i != 9 :
        print(format(val, ">4s"), end="")
    else :
        print(format(val, ">4s"))
print("-"*42)
#상단

#출력
for j in range(1,10) :
    print(f"{j} |  ", end = "")
    for i in range(1, 10):
        val = str(i * j)
        print(format(val, ">4s"), end="")
    print("\n")