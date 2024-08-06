import json
import heapq

#Вычисляет стоимость карты на основе начальной цены, коэффициента и уровня.
def calculate_price(price, coef, level):
    return int(price * (float(coef) ** (level - 1)))

### [UPGRADE] ###
with open('../prices_data.json', 'r') as openfile:
    prices_data = json.load(openfile)
print(prices_data)

with open('../levels_data.json', 'r') as openfile:
    levels_data = json.load(openfile)
print(levels_data)
levels_data = json.loads(levels_data)
#print(levels_data['data'])

balance = 1500000

# Создаем словарь для уровней
levels = {card_id: info['level'] for card_id, info in levels_data['data'].items()}
print(levels)

queue = []

for card in prices_data:
    card_id = str(card['id'])

    if card_id in levels:
        level = levels[card_id]
        price = card['price']
        coef = card['price_coef']
        calculated_price = calculate_price(price, coef, level)

        if calculated_price <= balance:
            print(card_id, level, calculated_price)
            heapq.heappush(queue, (calculated_price, card_id, level))

print(queue)

minings_upgrade = heapq.nsmallest(1, queue)[0]
print(minings_upgrade)

minings_upgrade_id = minings_upgrade[1]
minings_upgrade_level = int(minings_upgrade[2])

print(minings_upgrade_id, minings_upgrade_level)