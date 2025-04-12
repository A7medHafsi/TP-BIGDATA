import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# تحميل البيانات من الملف
file_path = "D:/data_Bigdata/2019-Nov-Sample.csv"  # تأكد من صحة المسار
df = pd.read_csv(file_path)

# عرض أول 5 صفوف لفهم بنية البيانات
print(df.head())

# -------------------------------
# **1. تنظيف البيانات**
# -------------------------------

# إزالة القيم الفارغة
df.dropna(inplace=True)

# إزالة القيم المكررة
df.drop_duplicates(inplace=True)

# التأكد من أن عمود التاريخ بصيغة datetime
if 'event_time' in df.columns:  
    df['event_time'] = pd.to_datetime(df['event_time'], errors='coerce')  # تحويل العمود إلى datetime

# -------------------------------
# **2. تحليل مبدئي للبيانات**
# -------------------------------

# عرض معلومات عن الأعمدة
print(df.info())

# الإحصائيات الوصفية للبيانات الرقمية
print(df.describe())

# **تصحيح حساب مصفوفة الارتباط**
plt.figure(figsize=(10, 6))
sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap="coolwarm")  
plt.title("Correlation Matrix")
plt.show()

# -------------------------------
# **3. حفظ الملف بعد التنظيف**
# -------------------------------

# تحديد مسار المجلد الجديد
output_dir = "D:\data_Bigdata"
os.makedirs(output_dir, exist_ok=True)  # إنشاء المجلد إذا لم يكن موجودًا

# تحديد مسار الحفظ
cleaned_file_path = os.path.join(output_dir, "2019-Nov-Cleaned.csv")
df.to_csv(cleaned_file_path, index=False)

print(f"✅ تم حفظ البيانات النظيفة في: {cleaned_file_path}")
