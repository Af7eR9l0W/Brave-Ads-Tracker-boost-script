#lol thx copilot for helping me make this in literally 30 seconds
import pyautogui
import time
import keyboard

print('Open up to 10 tabs in a chrome based browser')
time.sleep(.2)
print('Go to cnn.com or a site with a lot of trackers')
print('spam q to quit or ctrl+c')


print('switch to browser')
time.sleep(2)
print('script started')
count = 0
while (True):    
    
    pyautogui.hotkey('ctrl','1')  #switches to first tab  
    pyautogui.press('f5') #refreshes page
    pyautogui.hotkey('ctrl','2')  #switches to second tab
    pyautogui.press('f5') #refreshes page
    pyautogui.hotkey('ctrl','3')  #switches to third tab
    pyautogui.press('f5') #refreshes page
    pyautogui.hotkey('ctrl','4')  #switches to fourth tab
    pyautogui.press('f5') #refreshes page
    pyautogui.hotkey('ctrl','5')  #switches to fifth tab
    pyautogui.press('f5') #refreshes page
    pyautogui.hotkey('ctrl','6')  #switches to sixth tab
    pyautogui.press('f5') #refreshes page
    pyautogui.hotkey('ctrl','7')  #switches to seventh tab
    pyautogui.press('f5') #refreshes page
    pyautogui.hotkey('ctrl','8')  #switches to eighth tab
    pyautogui.press('f5') #refreshes page
    pyautogui.hotkey('ctrl','9')  #switches to ninth tab
    pyautogui.press('f5') #refreshes page
    pyautogui.hotkey('ctrl','0')  #switches to tenth tab
    pyautogui.press('f5') #refreshes pag
    count = count + 1
    pyautogui.sleep(.5)
    
    #break if q is pressed
    if keyboard.is_pressed('q'):
            print('q pressed')
            print ('Exiting')
            break
	 
    
count = count*10    
print('You refreshed about', count, 'times')
print('in total you blocked around', count*14, 'trackers')
    
    
    
	


