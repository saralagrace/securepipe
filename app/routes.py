from flask import Blueprint, jsonify, request

tickets_bp = Blueprint("tickets", __name__)

tickets = []
counter = {"id": 1}

@tickets_bp.route("/tickets", methods=["GET"])
def get_tickets():
    return jsonify(tickets), 200

@tickets_bp.route("/tickets", methods=["POST"])
def create_ticket():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "title requis"}), 400
    ticket = {"id": counter["id"], "title": data["title"], "status": "open"}
    tickets.append(ticket)
    counter["id"] += 1
    return jsonify(ticket), 201

@tickets_bp.route("/tickets/<int:ticket_id>", methods=["GET"])
def get_ticket(ticket_id):
    ticket = next((t for t in tickets if t["id"] == ticket_id), None)
    if not ticket:
        return jsonify({"error": "non trouvé"}), 404
    return jsonify(ticket), 200