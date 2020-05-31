# pseudocode - 가짜코드


# fizz buzz test

# 1부터 100까지 숫자를 출력하되/돼 ✅

for i in range(1, 101):  # 1이상 101미만 1 ... 100 범위
    # FizzBuzz: 3과 5로 둘 다 나눠 떨어지면
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Fizz: 3의 배수 = 3으로 나눠서 나머지가 0이면 ~ 라면 if
    elif i % 3 == 0:
        print("Fizz")
    # Buzz: 5의 배수 = 5으로 나눠서 나머지가 0이면
    elif i % 5 == 0:
        print("Buzz")
    else:  # 숫자를 출력
        print(i)
