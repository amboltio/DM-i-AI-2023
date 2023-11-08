import datetime
import time

start_time = time.time()

def get_uptime():
    return '{}'.format(datetime.timedelta(seconds=time.time() - start_time))
