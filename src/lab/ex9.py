from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(
        f"today {dt.today().date()}, "
        f"day of week - {dt.today().isoweekday()}"
    )
    n = int(input("enter number of days: "))
    today = dt.today()
    result = today + td(days=n)
    print(
        f"через {n} дней будет{result.date()}, "
        f"day of week - {result.isoweekday()}"
    )

if __name__ == "__main__":
    main()