from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('iot-topic', b'Test from Python!')
producer.flush()
print("✅ Message sent.")
