import pandas as pd
import glob

# قراءة جميع ملفات CSV في المجلد الحالي
files = glob.glob("yellow_tripdata_*.csv")

# دمج جميع الملفات في DataFrame واحد
df_list = [pd.read_csv(file, low_memory=False) for file in files]
df = pd.concat(df_list, ignore_index=True)

# التحقق من الحجم
print(f"إجمالي حجم البيانات: {df.memory_usage(deep=True).sum() / (1024**3):.2f} GB")

# حفظ البيانات المدمجة في ملف جديد
df.to_csv("merged_data.csv", index=False)
print("تم حفظ البيانات في merged_data.csv ✅")
