#need pyautogui keyboard isnt used
import pyautogui
import keyboard 
import time

print('Open 5 tabs in a chrome based browser')
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
    count = count + 1
    pyautogui.sleep(.5)
    
    #break if q is pressed
    if keyboard.is_pressed('q'):
            print('q pressed')
            print ('Exiting')
            break
	 
    
print('You refreshed about', count, 'times')
    
    
    
	


