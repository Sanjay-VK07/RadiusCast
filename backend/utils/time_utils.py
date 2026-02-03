from datetime import datetime

def get_time_features():
    now = datetime.now()
    return {
        "hour": now.hour,
        "day": now.weekday(),
        "is_weekend": int(now.weekday() >= 5)
    }
