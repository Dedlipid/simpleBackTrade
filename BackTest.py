import pandas as pd
T = pd.read_csv("assets.csv",index_col="index")
T["last_buy"] = [0]*len(T["Assets"])
def K():
    cash_total = 10000 #starting cash 
    V = cash_total*(0.4) #amount of cash available per trade
    for i in range(len(T["Assets"])): 
        temp = pd.read_csv(T["Assets"][i] + "_USE.csv", index_col="Date") #load up individual ETF histories
        for j in range(200, len(temp["Open"])): #has to start at 200, due to 200 day moving average
            # Date,Open,High,Low,Close,Adj Close,Volume,STA,LTA,HV,LV
            q = round(V / temp["Close"][j]-0.5) #the 0.5 is to make round into floor, q determines how many shares we try to buy
            if T.iat[i, 1] > 0 : #satisfied if the closing price is higher then the 5-day average 
                if temp["Close"][j] >= temp["STA"][j]:
                    cash_total += temp["Close"][j]*T.iat[i, 1]
                    T.iat[i, 1] = 0
                if temp["Close"][j] <= T.iat[i, 2] and True: #buys a second unit if price falls under initaill buy in, can be commented our for less risky implemntation
                    if cash_total >= temp["Close"][j] * q: #checks to buy enough cash is available 
                        cash_total -= temp["Close"][j] * q #this whole block can be commented out for a less aggressive version of the strategy
                        T.iat[i, 1] += q

            if temp["HV"][j] and temp["LV"][j]: #checks to see the highs and lows have fallen for two consecutive days
                if temp["STA"][j] >= temp["Close"][j] >= temp["LTA"][j]: #checks to see if the 5 day average > closing price > 200 day average 
                    if cash_total >= temp["Close"][j]*q: #buys into the position if enough cash is available and the conditions are met
                        cash_total -= temp["Close"][j]*q #the cash is removed and the shares are added
                        T.iat[i, 1] += q
                        T.iat[i, 2] = temp["Close"][j]

    print(cash_total) #cash you would have at the end of your fund histories, make sure they end on the same day

    #print(T) #can be uncommented to see if theres any postions you still have'nt exit on

if __name__ == '__main__':
    K()
    
