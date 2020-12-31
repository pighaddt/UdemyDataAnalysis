
import pandas as pd
import datetime


def fix(n):
    year = n.year - 100 if n.year > 2060 else n.year
    return datetime.datetime(year, n.month, n.day)

if __name__ == '__main__':
    URL_Data = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data"
    data = pd.read_csv(URL_Data, sep="\s+", parse_dates=[[0,1,2]])
    # data = pd.read_csv(URL_Data, sep="\s+", index_col=['Yr', 'Mo', 'Dy'])
    data.index = data.Yr_Mo_Dy
    data["Yr_Mo_Dy"] = data["Yr_Mo_Dy"].apply(fix)
    data.describe().to_csv()
    # print()
