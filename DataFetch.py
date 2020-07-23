import yfinance as yf
import pandas as pd
"""
Gets and updates data of tracked assets, which are kept in assets.csv
As of now, assets in assets.csv have to be initialized or removed by hand
"""
T = pd.read_csv("assets.csv", index_col="index")
def I():
    for i in range(len(T["Assets"])):
        name = T["Assets"][i] + ".csv"
        temp = yf.download(T.at[i,"Assets"],period="5y").to_csv(name)
    return ("DataFetched is done")

# Date,Open,High,Low,Close,Adj Close,Volume
def STA(n,data):
    s = 0.0
    for i in range(5):
        s += data[n-i-1][3]
    return s/5

def LTA(n,data):
    s = 0.0
    for i in range(200):
        s += data[n-i-1][3]
    return s/200


def HV(n,data):
    return data[n-2][1] >= data[n-1][1] >= data[n][1]
def LV(n,data):
    return data[n-2][2] >= data[n-1][2] >= data[n][2]

def J():
    for j in range(len(T["Assets"])):
        temp = pd.read_csv(T["Assets"][j] + ".csv", index_col="Date")
        sta = []
        lta = []
        hv = []
        lv = []
        for k in range(0,len(temp["Open"])):
            sta.append(STA(k, temp.values))
            lta.append(LTA(k, temp.values))
            hv.append(HV(k, temp.values))
            lv.append(LV(k, temp.values))
        temp["STA"] = sta
        temp["LTA"] = lta
        temp["HV"] = hv
        temp["LV"] = lv
        temp.to_csv(T["Assets"][j] + "_USE" + ".csv")
        print(j,"/20")



if __name__ == "__main__":
    I()
    J()
