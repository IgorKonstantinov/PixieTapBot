#Вычисляет стоимость карты на основе начальной цены, коэффициента и уровня.
def calculate_price(price, coef, level):
    return int(price * (float(coef) ** (level - 1)))

