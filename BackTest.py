import pandas as pd
T = pd.read_csv("assets.csv")
T["Quantity"] = T["last_buy"] = T["last_price"] = 0  # Ass_Name, Quantity, Last_buy,last_price
C_0 = 15000
cash_total = C_0
cash_add = 0
cash_out = 0
for i in range(len(T["Assets"])):

    temp = pd.read_csv(T["Assets"][i] + ".csv", index_col="Date")
    his = len(temp["Open"])

    if cash_total < C_0/5 and cash_out >= max(C_0/4, 2500) and False:
        cash_total += max(C_0/4, 2500)
        cash_out -= max(C_0/4, 2500)

    if cash_total > C_0*1.1 and False:
        cash_out = C_0*0.1
        cash_total -= cash_out

    for j in range(his-250, his):  # RUNNING PERIOD
        # Date,Open,High,Low,Close,Adj Close,Volume,STA,LTA,HV,LV
        V = cash_total/2
        q = max(round(V/temp["Close"][j])-1, 0)
        T.iat[i, 3] = temp["Close"][j]

        if T.iat[i, 1] > 0:  # if any of the asset is owned, we check whether to buy or sell
            if temp["Close"][j] >= temp["STA"][j]:  # sells if the price is higher then
                cash_total += temp["Close"][j]*T.iat[i, 1]  # the 5 day average
                T.iat[i, 1] = 0
            if temp["Close"][j] <= T.iat[i, 2] and True:  # if true the risky strategy
                if cash_total >= temp["Close"][j] * q:  # will buy an additional unit
                    cash_total -= temp["Close"][j] * q
                    T.iat[i, 1] += q

        if temp["HV"][j] and temp["LV"][j]:  # if the high and low have fallen for two consecutive days
            if temp["STA"][j] >= temp["Close"][j] >= temp["LTA"][j]:  # if the price is higher then the
                if cash_total >= temp["Close"][j]*q:  # long term but bellow the short term average
                    cash_total -= temp["Close"][j]*q
                    T.iat[i, 1] += q
                    T.iat[i, 2] = temp["Close"][j]
T["V"] = T["Quantity"]*T["last_price"]
assets = T["V"].sum()

if __name__ == '__main__':
    print(f'cash={cash_total + cash_out},'
          f'assets={assets},'
          f'profit={(cash_total + cash_out + assets - cash_add - C_0) / C_0]}')
