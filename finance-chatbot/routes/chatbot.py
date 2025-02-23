from flask import Blueprint, request, jsonify

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/", methods=["POST"])
def chatbot():
    user_input = request.json.get("message")
    response = {"reply": f"AI Response to: {user_input}"}
    return jsonify(response)
