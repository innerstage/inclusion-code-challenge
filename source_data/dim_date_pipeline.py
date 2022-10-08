import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from pandas.tseries.holiday import USFederalHolidayCalendar


def create_dim_date_table():
    df = pd.DataFrame({"dateDay": pd.date_range("2008-01-01", "2022-10-06", freq="D")})
    
    df["iMonth"] = df.dateDay.dt.month.astype(str).str.zfill(2)
    df["sMonth"] = df.dateDay.dt.month_name()
    df["iYear"] = df.dateDay.dt.year
    df["iYearDay"] = df.dateDay.dt.dayofyear
    df["iMonthDay"] = df.dateDay.dt.day.astype(str).str.zfill(2)
    df["iWeekDay"] = df.dateDay.dt.dayofweek.astype(str).str.zfill(2)
    df["sWeekDay"] = df.dateDay.dt.day_name()
    df["iYearMonth"] = df.dateDay.dt.year.astype(str) + df.dateDay.dt.month.astype(str).str.zfill(2)

    calendar = USFederalHolidayCalendar().rules
    holidays = {}
    for y in range(2008, 2023):
        holidays.update({str(y) + "-" + str(h.month).zfill(2) + "-" + str(h.day).zfill(2): h.name for h in calendar})

    df["iUSHoliday"] = df.dateDay.isin(holidays.keys()).astype(int)
    df["iWeek"] = df.dateDay.dt.isocalendar().week
    df["sUSHolidayName"] = df.dateDay.dt.strftime("%Y-%m-%d").map(holidays).fillna("")

    return df


def remove_random_entries(df):
    ENTRIES_TO_REMOVE = 31
    df = df.drop(np.random.choice(df.index, ENTRIES_TO_REMOVE, replace=False))

    return df


def load_dim_date_table(df):
    db_engine = create_engine("mysql+mysqlconnector://root:default@localhost:3306/ali")
    df.to_sql(con=db_engine, name='tblDimDate', if_exists='replace')


if __name__ == "__main__":
    df = create_dim_date_table()
    df = remove_random_entries(df)
    load_dim_date_table(df)