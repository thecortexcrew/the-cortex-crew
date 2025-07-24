import time
import random
import string
from datetime import datetime

def generate_identification_id():
    date_part = datetime.today().strftime("%Y%m%d")
    millis = str(int(time.time() * 1000))[-6:]  # last 6 digits of timestamp
    rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    return f"ID{date_part}-{millis}{rand}"
