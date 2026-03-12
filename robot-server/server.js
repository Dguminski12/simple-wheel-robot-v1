const WebSocket = require('ws');
const http = require("http");

const wss = new WebSocket.Server({ port: 8080 });

console.log("WebSocket server running on port 8080");

wss.on('connection', function connection(ws) {
    console.log("Client connected");

    ws.send("Connected to Pi robot server");

    ws.on('message', function incoming(message) {

        const cmd = message.toString();
        console.log("Received:", cmd);

        const ESP_IP = "192.168.1.xxx"; // ← put your ESP IP here

        http.get(`http://${ESP_IP}/move/?cmd=${cmd}`, (res) => {
            console.log("Sent to ESP:", cmd);
        }).on("error", (err) => {
            console.error("ESP request failed:", err.message);
        });
    });

    ws.on('close', () => {
        console.log("Client disconnected");
    });
});
