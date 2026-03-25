price = float(input("Введите цену товара: "))
discount = float(input("Введите процент скидки: "))
discount_amount = price * (discount / 100)
final_price = price - discount_amount
print(f"Сумма скидки: {discount_amount:.2f}")
print(f"Итоговая цена товара: {final_price:.2f}")
