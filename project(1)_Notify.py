from time import sleep
import  notify2
import random

msglist = ['Adult humans are 60 percent water, and our blood is 90 percent water.','There is no universally agreed quantity of water that must be consumed daily.','Water is essential for the kidneys and other bodily functions.','When dehydrated, the skin can become more vulnerable to skin disorders and wrinkling.','Drinking water instead of soda can help with weight loss.']
ico = '/home/mojo/Desktop/water_bottle.ico'


notify2.init("Notify Water")

while True:
    msg = random.choice(msglist)
    n = notify2.Notification(summary="----Drink Water----",message=msg,icon=ico)
    n.set_timeout(5000)
    n.show()
    sleep(10) #in secs (3600 in case of 1hour)