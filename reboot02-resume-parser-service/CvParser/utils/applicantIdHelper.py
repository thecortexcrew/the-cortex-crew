import time
import random
import string
from datetime import datetime


def generate_application_id():
    date_part = datetime.today().strftime("%Y%m%d")
    millis = str(int(time.time() * 1000))[-6:]  # last 6 digits of current timestamp
    rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    return f"APP{date_part}-{millis}{rand}"