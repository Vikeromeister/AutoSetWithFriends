from PIL import ImageGrab
import numpy as np
import cv2
# import pyautogui
import os
os.environ['DISPLAY'] = ':0'

from time import sleep
# from curtsies import Input
import keyboard
from sys import exit


def get_card_locs():
    global img_rgb
    img_rgb = np.array(ImageGrab.grab(bbox=(0,0,1920,1080)))
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('card3.png', 0)
    mask = cv2.imread('mask2.png', 0)
    global w, h
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCORR_NORMED, None, mask)
    # cv2.imshow("asd", res)
    # print(np.max(res))
    # cv2.waitKey(1)
    threshold = 0.97
    loc = np.where( res >= threshold)
    # for pt in zip(*loc[::-1]):
    #     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    # cv2.imshow('window',cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB))
    # while(True):
    #     if cv2.waitKey(25) & 0xFF == ord('q'):
    #         cv2.destroyAllWindows()
    #         break
    # print(loc)
    return loc

def get_card(pt):
    card_img_ = img_rgb[pt[1]:pt[1]+h, pt[0]:pt[0]+w]
    card_img = cv2.cvtColor(card_img_, cv2.COLOR_BGR2RGB)
    # cv2.imshow('window',cv2.cvtColor(card_img, cv2.COLOR_BGR2RGB))
    # while(True):
    #     if cv2.waitKey(25) & 0xFF == ord('q'):
    #         cv2.destroyAllWindows()
    #         break
    # pass
    threshold = 0.96
    while(True):
        color = 0 # green
        filling = 0 # empty
        shape = 0 # diamond
        template = cv2.imread('green_empty_diamond.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 1 # circle
        template = cv2.imread('green_empty_circle.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 2 # worm
        template = cv2.imread('green_empty_worm.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        
        filling = 1 # striped
        shape = 0 # diamond
        template = cv2.imread('green_striped_diamond.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 1 # circle
        template = cv2.imread('green_striped_circle.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 2 # worm
        template = cv2.imread('green_striped_worm.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        
        filling = 2 # full
        shape = 0 # diamond
        template = cv2.imread('green_full_diamond.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 1 # circle
        template = cv2.imread('green_full_circle.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 2 # worm
        template = cv2.imread('green_full_worm.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        
        
        color = 1 # yellow
        filling = 0 # empty
        shape = 0 # diamond
        template = cv2.imread('yellow_empty_diamond.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 1 # circle
        template = cv2.imread('yellow_empty_circle.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 2 # worm
        template = cv2.imread('yellow_empty_worm.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        template = cv2.imread('yellow_empty_worm_og.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        
        filling = 1 # striped
        shape = 0 # diamond
        template = cv2.imread('yellow_striped_diamond.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 1 # circle
        template = cv2.imread('yellow_striped_circle.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 2 # worm
        template = cv2.imread('yellow_striped_worm.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        
        filling = 2 # full
        shape = 0 # diamond
        template = cv2.imread('yellow_full_diamond.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 1 # circle
        template = cv2.imread('yellow_full_circle.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 2 # worm
        template = cv2.imread('yellow_full_worm.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        
        
        color = 2 # red
        filling = 0 # empty
        shape = 0 # diamond
        template = cv2.imread('red_empty_diamond.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 1 # circle
        template = cv2.imread('red_empty_circle.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 2 # worm
        template = cv2.imread('red_empty_worm.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        
        filling = 1 # striped
        shape = 0 # diamond
        template = cv2.imread('red_striped_diamond.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 1 # circle
        template = cv2.imread('red_striped_circle.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 2 # worm
        template = cv2.imread('red_striped_worm.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        
        filling = 2 # full
        shape = 0 # diamond
        template = cv2.imread('red_full_diamond.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 1 # circle
        template = cv2.imread('red_full_circle.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        shape = 2 # worm
        template = cv2.imread('red_full_worm.png')
        res = cv2.matchTemplate(card_img,template,cv2.TM_CCORR_NORMED)
        if np.any(np.where(res>=threshold)):
            break
        # print("oh-oh, nem találtam semmit ezen a kártyán")
        return np.array([9, 9, 9, 0])
    loc = np.where(res>=threshold)
    number = 0
    # print(*loc[::-1])
    lista = []
    for i in zip(*loc[::]):
        nope = False
        for j in lista:
            if (i[1] > j[1]-10) and (i[1] < j[1]+10):
                nope = True
                # print(i[1], j[1], i[0], j[0])
                break
        if nope:
            continue
        else:
            number += 1
            lista.append(i)
    # print(lista)
    return np.array([color, filling, shape, number])

def check(i, j, k):
    if i != j and j != k and k != i:
        return True
    elif i == j and j == k:
        return True
    else:
        return False


def find_sets(cards):
    sets = []
    for i in range(len(cards)):
        for j in range(len(cards)):
            for k in range(len(cards)):
                if (i!=j) and (i!=k) and (j!=k):
                    if check(cards[i][0], cards[j][0], cards[k][0]) and check(cards[i][1], cards[j][1], cards[k][1]) and check(cards[i][2], cards[j][2], cards[k][2]) and check(cards[i][3], cards[j][3], cards[k][3]):
                        # print(cards[i], cards[j], cards[k])
                        # return i, j, k
                        sets.append([i, j, k])
    return sets

def find_disjunct(sets):
    lista = []
    for i in sets:
        for j in sets:
            if i[0] not in j and i[1] not in j and i[2] not in j:
                lista.append(i)
                lista.append(j)
                return lista
    lista.append(sets[0])
    return lista

if __name__ == "__main__":
    global img_rgb
   
    # keyboard.on_press_key("p", lambda _:exit())
    
    while(True):
        # keyboard.wait('j')
        loc = get_card_locs()
        # cv2.imshow("asd", img_rgb)
        # cv2.waitKey(1)
        print(len(tuple(zip(*loc[::-1]))))
        if len(tuple(zip(*loc[::-1]))) >= 9:
            cards = []
            for i in zip(*loc[::-1]):
                cards.append(get_card(i))
            for card in cards:
                print(card)
            sets = find_sets(cards)
            # kaki = 0
            sets = find_disjunct(sets)
            for Set in sets:
                for asd in Set:
                    if asd == 0:
                        keyboard.press_and_release('1')
                    elif asd == 1:
                        keyboard.press_and_release('2')
                    elif asd == 2:
                        keyboard.press_and_release('3')
                    elif asd == 3:
                        keyboard.press_and_release('q')
                    elif asd == 4:
                        keyboard.press_and_release('w')
                    elif asd == 5:
                        keyboard.press_and_release('e')
                    elif asd == 6:
                        keyboard.press_and_release('a')
                    elif asd == 7:
                        keyboard.press_and_release('s')
                    elif asd == 8:
                        keyboard.press_and_release('d')
                    elif asd == 9:
                        keyboard.press_and_release('z')
                    elif asd == 10:
                        keyboard.press_and_release('x')
                    elif asd == 11:
                        keyboard.press_and_release('c')
                    elif asd == 12:
                        keyboard.press_and_release('r')
                    elif asd == 13:
                        keyboard.press_and_release('t')
                    elif asd == 14:
                        keyboard.press_and_release('y')



        # for asd in zip(*loc[::-1]):
        #     if kaki == i or kaki == j or kaki == k:
        #         print(asd[1],asd[0])
        #         pyautogui.click(asd[0]+w/2,asd[1]+h/2)
        #     kaki += 1
        #     pyautogui.moveTo(asd[0], asd[1])
            
        # os.system('read -sn 1 -p "Press any key to continue..."')
        # sleep(1)
        
        


    
    # print(i, j, k)
    # row = []
    # column = []
    # row.append(i%3)
    # row.append(j%3)
    # row.append(k%3)
    # column.append(int(i/3))
    # column.append(int(j/3))
    # column.append(int(k/3))
    # # print(row, column)
    # oreg = np.zeros((4, 3))
    # for asd in range(3):
    #     oreg[column[asd],row[asd]] = 1
    # print(oreg)
    
    
