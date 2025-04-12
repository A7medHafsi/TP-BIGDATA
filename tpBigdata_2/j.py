import pandas as pd

data_file = '2019-Nov.csv'
df = pd.read_csv(data_file, nrows=5)  # تحميل أول 5 صفوف فقط
print(df.columns)  # طباعة أسماء الأعمدة
