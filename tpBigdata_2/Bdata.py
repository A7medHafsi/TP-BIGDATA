import pandas as pd
import dask.dataframe as dd
import time
import os

# تحميل البيانات (تأكد من وجود الملف قبل التشغيل)
data_file = 'D:/data_Bigdata/2019-Nov.csv' 

# قياس أداء Chunking
start_time = time.time()
chunk_size = 10000
chunk_results = []
memory_usage_chunking = []

for chunk in pd.read_csv(data_file, chunksize=chunk_size):
    chunk_results.append(chunk['price'].mean())
    memory_usage_chunking.append(chunk.memory_usage(deep=True).sum() / (1024 ** 3))  # حساب حجم البيانات في كل chunk

chunking_time = time.time() - start_time
chunking_result = sum(chunk_results) / len(chunk_results)
avg_memory_chunking = sum(memory_usage_chunking) / len(memory_usage_chunking)  # متوسط استخدام الذاكرة لكل chunk

# قياس أداء Dask
start_time = time.time()
df_dask = dd.read_csv(data_file)
dask_result = df_dask['price'].mean().compute()
dask_time = time.time() - start_time
dask_memory_usage = df_dask.memory_usage(deep=True).sum().compute() / (1024 ** 3)  # استخدام الذاكرة في Dask

# ضغط البيانات باستخدام Parquet
start_time = time.time()
df_pandas = pd.read_csv(data_file)
compressed_file = 'merged_data.parquet'  # تغيير اسم الملف المضغوط
df_pandas.to_parquet(compressed_file, compression='gzip')
compression_time = time.time() - start_time

# حجم الملف بعد الضغط
original_size = os.path.getsize(data_file) / (1024 * 1024) 
compressed_size = os.path.getsize(compressed_file) / (1024 * 1024)

# إنشاء جدول المقارنة
comparison = pd.DataFrame({
    'Method': ['Chunking', 'Dask', 'Compression'],
    'Processing Time (s)': [chunking_time, dask_time, compression_time],
    'File Size (MB)': [original_size, original_size, compressed_size],
    'Memory Usage (GB)': [avg_memory_chunking, dask_memory_usage, original_size / 1024]  # حجم الذاكرة المستهلكة لكل تقنية
})

print(comparison)

