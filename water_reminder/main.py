import time
from plyer import notification
while True:
    print("please sip some water")
    notification.notify(
        title="Water Reminder",message="Please drink water now",)
    time.sleep(60*60)



