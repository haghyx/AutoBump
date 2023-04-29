from lolzapi import LolzteamApi
from time import sleep, time

api = LolzteamApi("token", user_id)  # токен и user_id лолза
x = 6  # повторение каждые x часов (x >= 1)
start_time = time()
accounts_bumped = 0

while True:
    if time() - start_time > x * 3600:
        start_time = time()
        accounts_bumped = 0
    accounts = api.itemsUser()
    sleep(3)
    for account in accounts["items"]:
        if accounts_bumped >= 5:
            break
        print(account["item_id"])
        item_id = account["item_id"]
        try:
            bumped = api.market_bump(item_id)
            sleep(3)
            if "errors" in bumped.keys():
                print(f"Произошла ошибка с аккаунтом {item_id}: {bumped['errors'][0]}")
            else:
                print(f"Успешно поднял аккаунт {item_id}")
                accounts_bumped += 1
        except Exception as e:
            print(f"Произошла системная ошибка с аккаунтом {item_id}: {e}")
            if '502' in str(e):
                print("Ошибка 502. Ждем 1 час")
                sleep(3600)
    sleep(3600)
