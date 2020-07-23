import pandas as pd
cash_bill = 2000
D = pd.read_csv("DIA_USE.csv",index_col="Date")
T = pd.read_csv("assets.csv",index_col="index")
T["last_buy"] = [0]*len(T["Assets"])
def K():
    cash_total = 10000
    V = cash_total/2.5
    for i in range(len(T["Assets"])):
        temp = pd.read_csv(T["Assets"][i] + "_USE.csv", index_col="Date")
        for j in range(0, len(temp["Open"])):
            # Date,Open,High,Low,Close,Adj Close,Volume,STA,LTA,HV,LV
            q = round(V / temp["Close"][j]) - 1
            if T.iat[i, 1] > 0 :
                if temp["Close"][j] >= temp["STA"][j]:
                    cash_total += temp["Close"][j]*T.iat[i, 1]
                    T.iat[i, 1] = 0
                    T.iat[i,2] = 0
                if temp["Close"][j] <= T.iat[i, 2]:
                    if cash_total >= temp["Close"][j] * q:
                        cash_total -= temp["Close"][j] * q
                        T.iat[i, 1] += q

            if temp["HV"][j] and temp["LV"][j]:
                if temp["STA"][j] >= temp["Close"][j] >= temp["LTA"][j]:
                    if cash_total >= temp["Close"][j]*q:
                        cash_total -= temp["Close"][j]*q
                        T.iat[i, 1] += q
                        T.iat[i, 2] = temp["Close"][j]




    print(cash_total)


K()
#print(T)

if __name__ == '__main__':
    pass