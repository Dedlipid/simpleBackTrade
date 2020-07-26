import yfinance as yf
import pandas as pd
"""
Gets and updates data of tracked assets, which are kept in assets.csv
As of now, assets in assets.csv have to be initialized or removed by hand
"""

def nDA(n,i,data):
    s = 0.0
    for j in range(n):
        s += data[i-j-1][3]
    return s/n
def HV(n, data):
    return data[n-2][1] > data[n-1][1] > data[n][1]
def LV(n,data):
    return data[n-2][2] > data[n-1][2] > data[n][2]
T = pd.read_csv("assets.csv", index_col="index")
def I():
    for i in range(len(T["Assets"])):
        sta=[]
        lta=[]
        hv=[]
        lv=[]
        temp = yf.download(T.at[i,"Assets"],period="max")
        for k in range(0, len(temp["Open"])):
            sta.append(nDA(5, k, temp.values))
            lta.append(nDA(200, k, temp.values))
            hv.append(HV(k, temp.values))
            lv.append(LV(k, temp.values))
        temp["STA"] = sta
        temp["LTA"] = lta
        temp["HV"] = hv
        temp["LV"] = lv
        # Date,Open,High,Low,Close,Adj Close,Volume
        temp.to_csv(T["Assets"][i] + ".csv")
        print(f'{i + 1}/20')
    return ("DataFetch is done")

if __name__ == "__main__":
    I()
