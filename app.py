from flask import Flask, request, jsonify

from langchain_ollama import OllamaLLM
from langchain_community.tools import DuckDuckGoSearchRun

app = Flask(__name__)

llm = OllamaLLM(model="phi3")

search = DuckDuckGoSearchRun()

HTML = """
<!DOCTYPE html>
<html>

<head>

<title>Divij AI Search Assistant</title>

<script src="https://cdn.tailwindcss.com"></script>

</head>

<body class="bg-black text-white">

<div class="h-screen flex flex-col">

    <div class="p-5 border-b border-zinc-800">

        <h1 class="text-3xl font-bold text-center text-purple-500">
            Divij AI Search Assistant
        </h1>

    </div>

    <div id="chatBox" class="flex-1 overflow-y-auto p-5 space-y-5">
    </div>

    <div class="p-5 border-t border-zinc-800 flex gap-3">

        <input
            id="message"
            class="flex-1 p-4 rounded-xl bg-zinc-900"
            placeholder="Ask anything..."
        >

        <button
            onclick="sendMessage()"
            class="bg-purple-600 px-8 rounded-xl"
        >
            Send
        </button>

    </div>

</div>

<script>

async function sendMessage() {

    const input = document.getElementById("message")

    const message = input.value

    if(message.trim() === "") return

    const chatBox = document.getElementById("chatBox")

    chatBox.innerHTML += `
        <div class="flex justify-end">
            <div class="bg-purple-600 p-4 rounded-2xl max-w-xl">
                ${message}
            </div>
        </div>
    `

    input.value = ""

    chatBox.innerHTML += `
        <div id="loading" class="flex justify-start">
            <div class="bg-zinc-800 p-4 rounded-2xl animate-pulse">
                Searching...
            </div>
        </div>
    `

    chatBox.scrollTop = chatBox.scrollHeight

    const response = await fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })

    })

    const data = await response.json()

    document.getElementById("loading").remove()

    chatBox.innerHTML += `
        <div class="flex justify-start">
            <div class="bg-zinc-800 p-4 rounded-2xl max-w-xl whitespace-pre-wrap">
                ${data.response}
            </div>
        </div>
    `

    chatBox.scrollTop = chatBox.scrollHeight
}

</script>

</body>
</html>
"""

@app.route("/")
def home():

    return HTML

@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    user_message = data["message"]

    search_results = search.run(user_message)

    prompt = f"""
    User Question:
    {user_message}

    Internet Search Results:
    {search_results}

    Answer clearly and professionally.
    """

    response = llm.invoke(prompt)

    return jsonify({
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True)