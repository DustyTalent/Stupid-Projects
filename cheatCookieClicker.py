import pyautogui as pen
import sys

pen.moveTo(2200, 400, 0.5)

corner_x1 = 1930
corner_x2 = 2500
corner_y1 = 160
corner_y2 = 1000

try:
    while True:
        for i in range (5510):
            pen.click()

            if i == 100:
                print(f'{i} cookies clicked')
            elif i == 500:
                print('500 cookies clicked')
            elif i == 800:
                print('800 cookies clicked')
            elif i == 1000:
                print('1000 cookies clicked')
            elif i == 1500:
                print(f'{i} cookies clicked')
            elif i == 2000:
                print(f'{i} cookies clicked')
            elif i == 2500:
                print(f'{i} cookies clicked')
            elif i == 3000:
                print(f'{i} cookies clicked')
            elif i == 4000:
                print(f'{i} cookies clicked')
            elif i == 5000:
                print(f'{i} cookies clicked')
            elif i == 6000:
                print(f'{i} cookies clicked')
            elif i == 7000:
                print(f'{i} cookies clicked')
            elif i == 8000:
                print(f'{i} cookies clicked')
            elif i == 9000:
                print(f'{i} cookies clicked')
            elif i == 10000:
                print('10000 cookies clicked program complete')
            elif i > 10001:
                print('Too many cookies something has gone terribly WRONG')

            x, y = pen.position()
            if corner_x1<= x <= corner_x2 and corner_y1 <= y <= corner_y2:
                m = True
                continue
            else:
                m = False
                if m == False:
                    print('Program ended since mouse left the area')
                    sys.exit()
                else:
                    continue
                

except KeyboardInterrupt:
    print('Program Ended\n')
