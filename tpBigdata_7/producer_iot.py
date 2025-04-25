from kafka import KafkaProducer
import time
import random

# اتصل ببروكر Kafka على 127.0.0.1:9092
producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])

while True:
    # محاكاة قراءة درجة حرارة
    temperature = random.uniform(30.0, 100.0)
    message = f"Temperature: {temperature:.2f}°C"
    # إرسال الرسالة للـ topic
    producer.send('iot-test', message.encode('utf-8'))
    producer.flush()  # لضمان الإرسال الفوري
    print("Sent:", message)
    time.sleep(2)
