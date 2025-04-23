from kafka import KafkaProducer
import time
import random

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
    temperature = random.uniform(30.0, 100.0)
    message = f"Temperature: {temperature:.2f}°C"
    producer.send('iot-topic', message.encode('utf-8'))
    producer.flush()  # <== أضف هذا السطر لإرسال الرسالة فورًا
    print(f"Sent: {message}")
    time.sleep(2)
