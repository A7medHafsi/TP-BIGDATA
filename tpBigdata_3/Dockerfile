FROM python:3.9-slim
WORKDIR /app

# نسخ ملفات المشروع كاملةً إلى المجلد /app في الحاوية
COPY . .

# تثبيت المكتبات المطلوبة مباشرةً
RUN pip install --no-cache-dir pandas numpy matplotlib seaborn

# تشغيل السكريبت cleaned.py عند بدء تشغيل الحاوية
CMD ["python", "cleaned.py"]