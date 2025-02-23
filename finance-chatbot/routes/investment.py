from flask import Blueprint, jsonify

investment_bp = Blueprint("investment", __name__)

@investment_bp.route("/", methods=["GET"])
def get_investments():
    investments = ["Stock A", "Crypto B", "Fund C"]
    return jsonify({"suggestions": investments})
