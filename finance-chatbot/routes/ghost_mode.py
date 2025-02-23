from flask import Blueprint, request, jsonify
from cryptography.fernet import Fernet

ghost_bp = Blueprint("ghost", __name__)
encryption_key = Fernet.generate_key()
cipher = Fernet(encryption_key)

@ghost_bp.route("/", methods=["POST"])
def ghost_mode():
    status = request.json.get("status")
    if status:
        return jsonify({"message": "Ghost Mode Activated"})
    else:
        return jsonify({"message": "Ghost Mode Deactivated"})
