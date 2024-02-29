import datetime
import random
from time import sleep

def print_current_time() -> None:
    """ Function to print current time.
    Variables:
        now: datetime object with the current time in it.
    Returns:
        
    """
    # populate datetime object with the current time
    now = datetime.datetime.now()

    # make process leep between 0 and 1 seconds
    sleep(random.uniform(0.0, 1.0))
    
    # print time in now, before the sleep occured
    print(now)
    
    return