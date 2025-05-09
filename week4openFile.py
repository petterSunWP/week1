# import csv
import pandas as pd

# with open("sample_junk_mail.csv", newline='', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)


# 替换成你的实际文件路径
# df = pd.read_csv("sample_junk_mail.csv")

# 显示前5行
# print(df.head())


# 统计 "__" 的数量
with open("sample_text.txt", "r") as f:
    text = f.read()
    count = text.count("__")
print("Number of '__' in the text file:", count)


df = pd.read_parquet('Sample_data_2.parquet')

# Print the number of features
print("Number of features (columns):", df.shape[1])
print("Column names:", df.columns.tolist())

A = {1,2,3,4}