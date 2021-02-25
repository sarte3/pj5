import pyautogui as pag
import time
import pandas as pd
import pyperclip

food = pd.read_csv('data/food.csv')
food = food[['DB군', '상용제품', '식품명']]
food = food[food['DB군']=='음식']
food = food[food['상용제품']=='품목대표']
food = food['식품명']
print(food)
print(food.shape)

for i in range(len(food)):
    pag.click(1300,250)
    str(food[i])
    pyperclip.copy(food[i])
    pag.hotkey("ctrl", "v")
    pag.press('enter')
    time.sleep(5)
    pag.doubleClick()
    pag.press('del')
    if i % 20 == 0:
        pag.press('f5')
