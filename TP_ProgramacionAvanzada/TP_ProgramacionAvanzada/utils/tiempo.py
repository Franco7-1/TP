from datetime import datetime, timedelta, timezone

GMT_MINUS_3 = timezone(timedelta(hours=-3))

def fecha_argentina():
    return datetime.now(GMT_MINUS_3)
