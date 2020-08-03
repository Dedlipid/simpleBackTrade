import yfinance as yf
import pandas as pd
"""
Gets and updates data of tracked assets, which are kept in assets.csv
As of now, assets in assets.csv have to be initialized or removed by hand
"""


def nda(n, i, data):
    s = 0.0
    for j in range(n):
        s += data[i-j-1][3]
    return s/n


def hv(n, data):
    return data[n-2][1] > data[n-1][1] > data[n][1]


def lv(n, data):
    return data[n-2][2] > data[n-1][2] > data[n][2]


T = pd.read_csv("assets.csv")


def init():
    for i in range(len(T["Assets"])):
        sta = []
        lta = []
        h = []
        l = []
        temp = yf.download(T.at[i, "Assets"], period="max")
        for k in range(0, len(temp["Open"])):
            sta.append(nda(5, k, temp.values))
            lta.append(nda(200, k, temp.values))
            h.append(hv(k, temp.values))
            l.append(lv(k, temp.values))
        temp["STA"] = sta
        temp["LTA"] = lta
        temp["HV"] = h
        temp["LV"] = l
        # Date,Open,High,Low,Close,Adj Close,Volume
        temp.to_csv(T["Assets"][i] + ".csv")
        print(f'{i + 1}/20')
    return "DataFetched"


if __name__ == "__main__":
    print(init())
