# datetime
# 
# Keys:
# {date_YYYY}       The current year (4 digits)
# {date_YY}         The current year (2 digits)
# {date_MM}         The current month (trailing zero)
# {date_M}          The current month
# {date_DD}         The current day (trailing zero)
# {date_D}          The current day
#
# {time_HH}         The current hour (24h format, trailing zero)
# {time_H}          The current hour (24h format)
# {time_hh}         The current hour (12h format, trailing zero)
# {time_h}          The current hour (12h format)
# {time_mm}         The current minute (trailing zero)
# {time_m}          The current minute
# {time_ss}         The current second (trailing zero)
# {time_s}          The current second
# {time_ap}         The current AM/PM
# {time_zone}       The current timezone (e.g. "UTC+2")

import datetime
import vrcosc

def format(text):
    now = datetime.datetime.now()

    return vrcosc.str_replace_bulk(text, {
        "date_YYYY": now.strftime("%Y"),
        "date_YY": now.strftime("%y"),
        "date_MM": now.strftime("%m"),
        "date_M": now.strftime("%m"),
        "date_DD": now.strftime("%d"),
        "date_D": now.strftime("%d"),

        "time_HH": now.strftime("%H"),
        "time_H": now.strftime("%H"),
        "time_hh": now.strftime("%I"),
        "time_h": now.strftime("%I"),
        "time_mm": now.strftime("%M"),
        "time_m": now.strftime("%M"),
        "time_ss": now.strftime("%S"),
        "time_s": now.strftime("%S"),

        "time_ap": now.strftime("%p"),
        "time_zone": now.strftime("%Z")
    })
