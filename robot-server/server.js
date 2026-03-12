const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8080 });

console.log("WebSocket server running on port 8080");

wss.on('connection', function connection(ws) {
    console.log("Client connected");

    ws.send("Connected to Pi robot server");

    ws.on('message', function incoming(message) {
        console.log("Received:", message.toString());

        // Echo back for now
        ws.send("Pi received: " + message);
    });

    ws.on('close', () => {
        console.log("Client disconnected");
    });
});
