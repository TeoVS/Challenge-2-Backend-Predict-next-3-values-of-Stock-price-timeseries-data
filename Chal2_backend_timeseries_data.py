import pandas as pan
import os      
from glob import glob

stocksPath = "your\\path\\here"
extension = "*.csv"
csvDict = {}

for path, subdir, files in os.walk(stocksPath):
    for file in glob(os.path.join(path, extension)):
        fileName = os.path.basename(file)               
        csvDict[fileName.lower()] = file         

print("Files found: ", csvDict)

input = input("Deal Name: ")

if input.isdigit():
    print("Error: Deals must use abbreviations.")
else:
    inputName = input.lower().strip() + ".csv" 

filePath = csvDict[inputName]

df = pan.read_csv(filePath, header=None, names= ["Stock-ID", "Timestamp", "Stock Price"])
df["Timestamp"] = pan.to_datetime(df["Timestamp"], format = "%d-%m-%Y")

#This function selects the sample (10 consecutive points starting from a random point)
def consecutive(df):
    minIndex = 0
    maxIndex = len(df) - 10
    randomIndex = df.sample().index[0]
    randomIndex = min(max(randomIndex, minIndex), maxIndex)
    return df.iloc[randomIndex: randomIndex + 10]

tenPoints = consecutive(df)

#This function applies the prediction logic and writes out the sample plus the extra rows in a new .csv
def next_values(tenPoints):

    n = tenPoints["Stock Price"].iloc[-1]
    n1 = tenPoints["Stock Price"].nlargest(2).iloc[-1]
    n2 = n + (n1 - n) / 2
    n3 = n2 + (n1 - n2) / 4 

    n1row = pan.DataFrame({"Stock-ID": [tenPoints["Stock-ID"].iloc[-1]], "Timestamp": [tenPoints["Timestamp"].iloc[-1] + pan.DateOffset(days= 1)], "Stock Price": [n1]})
    n2row = pan.DataFrame({"Stock-ID": [tenPoints["Stock-ID"].iloc[-1]], "Timestamp": [tenPoints["Timestamp"].iloc[-1] + pan.DateOffset(days= 2)], "Stock Price": [n2]})
    n3row = pan.DataFrame({"Stock-ID": [tenPoints["Stock-ID"].iloc[-1]], "Timestamp": [tenPoints["Timestamp"].iloc[-1] + pan.DateOffset(days= 3)], "Stock Price": [n3]})

    total = pan.concat([tenPoints, n1row, n2row, n3row], ignore_index=True)

    total["Stock Price"] = total["Stock Price"].round(2)

    total.to_csv(input + "_out.csv", index=False)

    return total

resultDF = next_values(tenPoints)

print(resultDF)