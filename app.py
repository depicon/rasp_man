from flask import Flask, render_template, request
from mqtt_client import client as mqtt_client
from flask_socketio import SocketIO, emit
app = Flask(__name__)
socketio = SocketIO(app)

def on_message(client, userdata, msg):
    data = msg.payload.decode()
    print(f"Nouveau message sur {msg.topic}: {data}")
    socketio.emit('mqtt_message', {'topic': msg.topic, 'message': msg.payload.decode()})

@socketio.on('update_threshold')
def update_threshold(value):
    new_threshold = float(value)
    print(f"Seuil de température mis à jour: {new_threshold}")
    mqtt_client.publish("dep/maison/config/temp_seuil", value)

# pour l'écoute des messages MQTT
mqtt_client.on_message = on_message
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
