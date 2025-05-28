
from datetime import datetime

def make_api_call(start_date: str, end_date: str):
    print(f"API Call from {start_date} to {end_date}")

def iterate_yearly_api_calls(start_year: int):
    today = datetime.today()
    current_year = today.year
    current_month = today.month
    print(f'current month is: {current_month}')

    year = start_year

    while year < current_year:
        start = f"{year}-01"
        end = f"{year + 1}-01"
        make_api_call(start, end)
        year += 1

    # Final call in current year if month > 1
    if current_month > 1:
        start = f"{current_year}-01"
        end = f"{current_year}-{current_month:02d}"
        make_api_call(start, end)


if __name__ == '__main__':
    iterate_yearly_api_calls(2021)