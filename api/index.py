from flask import Flask, render_template, request, jsonify
from chatbot import SmartBot

app = Flask(__name__, template_folder="../templates", static_folder="../static")
bot = SmartBot()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    response = bot.handle_input(message)
    return jsonify({"response": response})

# This is required for Vercel
def handler(environ, start_response):
    return app(environ, start_response)
