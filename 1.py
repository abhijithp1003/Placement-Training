import pandas as pd
import csv
df = pd.read_csv(r'C:\Users\abhij\Desktop\Placement_Trainign_Dlithe\day_14\filename.csv')

df.head()
print("---------------------------------------------------")
print(df.head(5))
print("---------------------------------------------------")
df.tail()
print("---------------------------------------------------")
print(df.tail(5))
print("---------------------------------------------------")


print(df)

print("---------------------------------------------------")
print(df['Name'])
print("---------------------------------------------------")
print(df['Name'][2])
print("---------------------------------------------------")
print(df['Name'][2:5])