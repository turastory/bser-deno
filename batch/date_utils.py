from datetime import datetime, timezone, timedelta
from dateparser import parse


def toKR(epoch):
    KST = timezone(timedelta(hours=9))
    return datetime.fromtimestamp(epoch).astimezone(KST).isoformat()


def toEpoch(timestr):
    return int(parse(timestr).timestamp())


def isNew(last, current):
    # Expect the inputs are in epoch time format
    print(f"Last update: {last} ({toKR(last)})")
    print(f"Current: {current} ({toKR(current)})")
    return last < current
