from kafka import KafkaConsumer

# اتصل ببروكر Kafka على 127.0.0.1:9092 واستمع للـ topic
consumer = KafkaConsumer(
    'iot-test',
    bootstrap_servers=['127.0.0.1:9092'],
    auto_offset_reset='earliest',   # لقراءة كل الرسائل من البداية
    enable_auto_commit=True,
    group_id='iot-group'
)

print("🚀 Listening for messages…")
for msg in consumer:
    print("✅ Received:", msg.value.decode('utf-8'))
