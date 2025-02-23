from flask import Blueprint, request, jsonify
from models.budget import Budget
from app import db

budget_bp = Blueprint("budget", __name__)

@budget_bp.route("/", methods=["POST"])
def save_budget():
    data = request.json
    new_budget = Budget(**data)
    db.session.add(new_budget)
    db.session.commit()
    return jsonify({"message": "Budget saved successfully!"})
