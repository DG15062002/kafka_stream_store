import uuid

import json
from confluent_kafka import Producer

producer_config = {
    "bootstrap.servers": "localhost:9092"
}
producer = Producer(producer_config)

def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered {msg.value().decode("utf-8")}")
        print(dir(msg))
        print(f"✅ Delivered to {msg.topic()}: partition {msg.partition()} : at offset {msg.offset()}")
order = {
    "order_id" : str(uuid.uuid4()),
    "user" : "skumar",
    "item" : "Mercedes-Benz S-Class",
    "quantity" : 2
}

value = json.dumps(order).encode("utf-8")
if producer is None:
    print("Failed to create producer")
    exit(1)
producer.produce(
    topic="orders",
    value=value,
    callback=delivery_report
)
producer.flush()