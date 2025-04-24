from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'iot-topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='iot-debug-group'
)

print("🚀 Listening for messages...")

for message in consumer:
    print(f"✅ Received: {message.value.decode('utf-8')}")