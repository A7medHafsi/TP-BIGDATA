import pandas as pd
import dask.dataframe as dd
import time
import os

# تحميل البيانات (تأكد من وجود الملف قبل التشغيل)
data_file = '2019-Nov.csv'  # تأكد من أن هذا هو اسم الملف الصحيح

# قياس أداء Chunking
start_time = time.time()
chunk_size = 10000
chunk_results = []

for chunk in pd.read_csv(data_file, chunksize=chunk_size):
    chunk_results.append(chunk['price'].mean())

chunking_time = time.time() - start_time
chunking_result = sum(chunk_results) / len(chunk_results)

# قياس أداء Dask
start_time = time.time()
df_dask = dd.read_csv(data_file)
dask_result = df_dask['price'].mean().compute()
dask_time = time.time() - start_time

# ضغط البيانات باستخدام Parquet
start_time = time.time()
df_pandas = pd.read_csv(data_file)
compressed_file = '2019-Nov.parquet'  # تغيير اسم الملف المضغوط
df_pandas.to_parquet(compressed_file, compression='gzip')
compression_time = time.time() - start_time

# حجم الملف بعد الضغط
original_size = os.path.getsize(data_file) / (1024 * 1024)  # بالميغابايت
compressed_size = os.path.getsize(compressed_file) / (1024 * 1024)

# حساب استهلاك الذاكرة
data_size_gb = df_pandas.memory_usage(deep=True).sum() / (1024 ** 3)

# إنشاء جدول المقارنة
comparison = pd.DataFrame({
    'Method': ['Chunking', 'Dask', 'Compression'],
    'Processing Time (s)': [chunking_time, dask_time, compression_time],
    'File Size (MB)': [original_size, original_size, compressed_size],
    'Memory Usage (GB)': [data_size_gb, data_size_gb, data_size_gb]
})

print(f"\U0001F50D حجم البيانات في الذاكرة: {data_size_gb:.2f} GB\n")
print(comparison)

