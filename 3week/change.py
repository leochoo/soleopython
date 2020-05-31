"""
만원짜리 지폐를 내고 2650원짜리 과자를 샀다
거스름돈으로 5천원 지폐, 천원 지폐, 5백원 지폐, 백원 지폐, 50원 동전을 몇 개씩 받아야 할지 계산해보자
"""

price = 2650  # 과자가격
paid = 10000  # 지불한 돈

num_bills = [0, 0, 0, 0, 0]  # 5000, 1000, 500, 100, 50 갯수를 나타내는 리스트

change = paid - price  # 거스름돈 10000 - 2650 = 7350


while change > 0:  # 거스름 돈이 있는 한, 이 체크를 반복한다

    if change >= 5000:  # 5000 보다 크니?
        num5000 = change // 5000  # 5000원 짜리가 몇장 필요하니?
        print("number of 5000: ", num5000)  # 1장이요
        change = change % 5000  # 7000 % 5000 = 2350 self update
    elif change >= 1000:  # 1000보다 크니?
        num1000 = change // 1000  # 2장
        print("number of 1000: ", num1000)
        change = change % 1000  # 350
    elif change >= 500:
        num500 = change // 500
        print("number of 500: ", num500)
        change = change % 500
    elif change >= 100:
        num100 = change // 100
        print("number of 100: ", num100)
        change = change % 100  # 3
    elif change >= 50:
        num50 = change // 50
        print("number of 50: ", num50)  # 1
        change = change % 50  # 0

    # 목적: 각각 지폐와 동전을 몇개씩 받아야 하는 지 계산해보자
