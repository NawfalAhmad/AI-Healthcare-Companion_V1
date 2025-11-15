async function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value.trim();
    if (message === "") return;

    // Show user message
    addMessage("You", message, "user");

    input.value = "";

    // Send to backend
    const response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    });

    const data = await response.json();

    // Show AI message
    addMessage("AI", data.reply, "bot");
}

function addMessage(sender, text, type) {
    const box = document.getElementById("chat-box");
    const msg = document.createElement("div");
    msg.className = `message ${type}`;
    msg.innerHTML = `<strong>${sender}:</strong> ${text}`;
    box.appendChild(msg);
    box.scrollTop = box.scrollHeight;
}
