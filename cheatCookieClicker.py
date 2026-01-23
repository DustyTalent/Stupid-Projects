# Didn't realise how broken my program was until after I uploaded for whatever 
# reason it keeps repeating the "for" loop when it should be finished clicking.
# Will fix later

import pyautogui as pygoo
import sys

pygoo.moveTo(0, 0, 0.5) #Your coordinates here

corner_x1 = 0 #Put in the area you want to click in these 4 variables
corner_x2 = 0 
corner_y1 = 0
corner_y2 = 0

try:
    while True:
        for i in range (0):
            pygoo.click()

            if i == 100:
                print(f'{i} cookies clicked')
            elif i == 500:
                print('500 cookies clicked')

            x, y = pen.position()
            if corner_x1<= x <= corner_x2 and corner_y1 <= y <= corner_y2:
                m = True
                continue
            else:
                m = False
                if m == False: #The program will go CRAZY without this, or else it constantly auto clicks everything
                    print('Program ended since mouse left the area')
                    sys.exit()
                else:
                    continue
                

except KeyboardInterrupt: #Ctrl-C to end program, as per usual
    print('Program Ended\n')


