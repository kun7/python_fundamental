"""
Semua sintaksis dasar terdiri dari:
1. sekuensial : langkah berurutan
2. percabangan : langkah melompat jika kondisi terpenuhi
3. pengulangan : mengulang langkah yang sama berkali-kali sampai kondisi terpenuhi
"""
# sequential
print("mom said this and that")
print('Virtue replied "yes, mom"')
print('mom said" buy me 1 milk and if there is an egg, buy 6')
print(' Virtue goes to the market')
print('Virtue start shopping')

# Percabangan
sum_milk_bottle = 100
sum_egg = 1574
print(f'milk bottle available {sum_milk_bottle} bottle')
print(f'egg available {sum_egg} egg' )
if sum_milk_bottle > 0:
    print('Virtue buy milk')
    if sum_egg >6:
        print('Virtue buy 6 egg')
    else:
        print('Virtue does not buy egg')
else:
    print('Virtue does not buy a milk')

print('Virtue goes home and give the groceries to mom')