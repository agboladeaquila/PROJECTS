import pandas as pd 
def load_data(file_path):
        data=pd.read_csv(file_path, usecols=["open", "high", "low", "close", "volume"]) 
        return data
markets_data=load_data(input("Enter the path to the markets data CSV file: "))
markets_data["RETURN"] = (markets_data["close"] - markets_data["open"]) / markets_data["open"] * 100
print(markets_data.head())