price = 2650
paid = 10000
change = paid - price

fivethousandwon = change // 5000
change = change - 5000
onethousandwon = change // 1000
change = change - (1000*(onethousandwon))
fivehundredwon = change // 500
chang = change - (500*(fivehundredwon))
onehundredwon = change // 100
change = change - (100*(onehundredwon))
fifitywon = change // 50
change = change - (50*(fifitywon))

print(fivethousandwon)
print(onethousandwon)
print(fivehundredwon)
print(onehundredwon)
print(fifitywon)
