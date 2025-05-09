import pandas as pd

# 读取数据
file_path = 'data.csv'
df = pd.read_csv(file_path)

# 显示前5行数据
print("Data Preview:")
print(df.head())

# 检查数据类型和缺失值
print("\nData Info:")
print(df.info())

# 统计基本信息
print("\nSummary Statistics:")
print(df.describe())

# 计算年度变化率
df["Temp_Change_Rate"] = df["STATS_VALUE"].pct_change() * 100

print("\nAnnual Temperature Change Rate:")
print(df[["YEAR", "Temp_Change_Rate"]].dropna().head(10))
