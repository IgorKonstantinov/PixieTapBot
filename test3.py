import json

data = {
    "data": {
        "mines": [
            {
                "mineId": "blockchain",
                "currentLevel": 5,
                "currentValue": 16,
                "dependencyMineId": None,
                "dependencyMineLevel": 0,
            },
            {
                "mineId": "bitcoin",
                "currentLevel": 4,
                "currentValue": 0,
                "dependencyMineId": "blockchain",
                "dependencyMineLevel": 3,
            },
            {
                "mineId": "ethereum",
                "currentLevel": 0,
                "currentValue": 0,
                "dependencyMineId": "bitcoin",
                "dependencyMineLevel": 3,
            },
            {
                "mineId": "ripple",
                "currentLevel": 0,
                "currentValue": 0,
                "dependencyMineId": "ethereum",
                "dependencyMineLevel": 6,
            },
            {
                "mineId": "cardano",
                "currentLevel": 0,
                "currentValue": 0,
                "dependencyMineId": "ripple",
                "dependencyMineLevel": 10,
            }
        ]
    }
}


def can_update_mine(mine_id, mines):
    mine = next((mine for mine in mines if mine['mineId'] == mine_id), None)
    if not mine:
        return False

    dependency_id = mine['dependencyMineId']
    if not dependency_id:
        return True

    dependency_mine = next((mine for mine in mines if mine['mineId'] == dependency_id), None)
    if not dependency_mine:
        return False

    # Проверяем, достаточно ли текущий уровень у зависимости
    if dependency_mine['currentLevel'] < mine['dependencyMineLevel']:
        return False

    # Проверяем рекурсивно зависимость
    return can_update_mine(dependency_id, mines)


# Пример использования функции
mine_id_to_check = "ethereum"
mines_data = data["data"]["mines"]
result = can_update_mine(mine_id_to_check, mines_data)
print(f"Можно ли обновить {mine_id_to_check}? {'Да' if result else 'Нет'}")
