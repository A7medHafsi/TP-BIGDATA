from kafka import KafkaProducer

try:
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    print("✅ Connected to Kafka successfully!")
except Exception as e:
    print("❌ Failed to connect to Kafka.")
    print(e)
