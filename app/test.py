import paho.mqtt.client as mqtt

# Define MQTT Broker settings
MQTT_BROKER = "localhost"  # Replace with your MQTT broker address
MQTT_PORT = 1883                          # Typically 1883 for non-secure MQTT
TOPIC_WEIGHT_CHANGE = "/weight_change"  # Replace with the actual topic

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker!")
        # Subscribe to the topic
        client.subscribe(TOPIC_WEIGHT_CHANGE)
        print(f"Subscribed to topic: {TOPIC_WEIGHT_CHANGE}")
    else:
        print(f"Failed to connect, return code {rc}")

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic: {msg.topic}")

# Create a new MQTT client instance
client = mqtt.Client()

# Attach callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start the loop to process incoming messages
client.loop_forever()
