import os
import pywhatkit as kit
import time
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()

phone_number = os.getenv("PHONE_NUMBER")
message = os.getenv("MESSAGE")

def is_within_active_hours():
    current_hour = datetime.now().hour
    return 9 <= current_hour < 23  # Lembretes só das 9h às 22h

while True:
    if is_within_active_hours():
        current_time = time.localtime()
        kit.sendwhatmsg(phone_number, message, current_time.tm_hour, current_time.tm_min + 2)
        time.sleep(5400)  # Pausa de 1 hora e meia (5400 segundos)
    else:
        time.sleep(3600)  # Pausa de 1 hora durante a madrugada 
