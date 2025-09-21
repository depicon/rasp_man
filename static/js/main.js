const socket = io();

socket.on("mqtt_message", function (msq) {
    console.log("Nouveau message MQTT reçu:", msq);
    const messageList = document.getElementById("message-list");
    const listItem = document.createElement("li");
    listItem.textContent = `Topic: ${msq.topic}, Message: ${msq.message}`;
    messageList.appendChild(listItem);
});

function updateThreshold() {
    const thresholdInput = document.getElementById("thresholdInput");
    const newThreshold = thresholdInput.value;
    socket.emit("update_threshold", { threshold: newThreshold });
    console.log("Seuil mis à jour:", newThreshold);
}