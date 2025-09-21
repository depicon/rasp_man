import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connecté au broker MQTT")
    client.subscribe("dep/maison/temperature")
    client.subscribe("dep/maison/humidite")
    client.subscribe("dep/maison/led")
    client.subscribe("dep/maison/ventilateur")

def on_message(client, userdata, msg):
    print(f"Nouveau message sur {msg.topic}: {msg.payload.decode()}")

# Configuration du client MQTT avec ID unique et bien determiné
client = mqtt.Client(client_id="rasp_man_server_417")
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)

client.loop_start()
