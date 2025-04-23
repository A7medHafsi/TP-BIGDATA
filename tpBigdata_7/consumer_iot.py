from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'iot-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',     # لقراءة الرسائل القديمة
    enable_auto_commit=True,
    group_id='iot-group-1',             # معرف مجموعة ضروري لفصل جلسات القراءة

)

for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")
