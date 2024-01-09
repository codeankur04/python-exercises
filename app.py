price = 100000
is_cradit = False
if is_cradit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment : ${down_payment}")