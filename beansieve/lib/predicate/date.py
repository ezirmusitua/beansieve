from datetime import date as Date, timedelta


def get_timedelta(period: str):
    if period.endswith("d"):
        return timedelta(days=int(period[:-1]))
    if period.endswith("w"):
        return timedelta(days=int(period[:-1]) * 7)
    if period.endswith("m"):
        return timedelta(days=int(period[:-1]) * 30)
    raise Exception(f"Invalid period {period}")


class DateLessThanToday():
    def __call__(self, entry, period: str):
        today = Date.today()
        return entry.date < today - get_timedelta(period)
