import pandas as pd

#file_path = "C:/Users/LAPTA/Desktop/BIGDATA/tp_3/2019-Nov-Cleaned.csv"
file_path = "D:/data_Bigdata/2019-Nov-Sample.csv"
df = pd.read_csv(file_path, nrows=100_000)  # تحميل أول مليون صف فقط

# حفظ الملف الجديد
sample_file_path = "D:\data_Bigdata/2019-Nov-sample.csv"
df.to_csv(sample_file_path, index=False)

print(f" تم حفظ عينة البيانات في: {sample_file_path}")
