from flask import Blueprint, request, jsonify, current_app
from bson.objectid import ObjectId
from pydantic import ValidationError
from .db import db
from .schemas import CustomerIn, OrderIn
from datetime import datetime, timezone

bp = Blueprint("api", __name__)

# helpers
def obj_id_to_str(doc):
    if not doc:
        return None
    doc = dict(doc)
    _id = doc.pop("_id", None)
    if _id is not None:
        doc["id"] = str(_id)
    created = doc.get("created_at")
    if created:
        # datetime -> ISO
        doc["created_at"] = created.isoformat() + "Z" if hasattr(created, "isoformat") else created
    return doc

# --- Customers ---

@bp.route("/customers", methods=["POST"])
def create_customer():
    try:
        data = CustomerIn(**request.get_json() or {})
    except ValidationError as e:
        return jsonify({"error": "Validation failed", "details": e.errors()}), 400
    
    existing = db.customers.find_one({"email": data.email})
    if existing:
        return jsonify({"error": "Email already exists"}), 400
    
    res = db.customers.insert_one({
        "name": data.name,
        "email": data.email,
        "created_at": datetime.now(timezone.utc)
    })
    customer = db.customers.find_one({"_id": res.inserted_id})
    return jsonify(obj_id_to_str(customer)), 201

@bp.route("/customers", methods=["GET"])
def list_customers():
    docs = db.customers.find()
    return jsonify([obj_id_to_str(d) for d in docs])

# --- Orders ---

@bp.route("/orders", methods=["POST"])
def create_order():
    try:
        data = OrderIn(**request.get_json() or {})
    except ValidationError as e:
        return jsonify({"error": "Validation failed", "details": e.errors()}), 400

    # Check customer exists
    try:
        cust_oid = ObjectId(data.customer_id)
    except Exception:
        return jsonify({"error": "invalid customer_id"}), 400
    
    if db.customers.count_documents({"_id": cust_oid}) == 0:
        return jsonify({"error": "customer not found"}), 404

    res = db.orders.insert_one({
        "customer_id": str(cust_oid),
        "item": data.item,
        "amount": data.amount
    })
    order = db.orders.find_one({"_id": res.inserted_id})
    return jsonify(obj_id_to_str(order)), 201

@bp.route("/orders", methods=["GET"])
def list_orders():
    docs = db.orders.find()
    return jsonify([obj_id_to_str(d) for d in docs])

@bp.route("/orders/<id>", methods=["GET"])
def get_order(id):
    try:
        oid = ObjectId(id)
    except Exception:
        return jsonify({"error": "invalid id"}), 400
    doc = db.orders.find_one({"_id": oid})
    if not doc:
        return jsonify({"error": "not found"}), 404
    return jsonify(obj_id_to_str(doc))

@bp.route("/orders/<id>", methods=["DELETE"])
def delete_order(id):
    try:
        oid = ObjectId(id)
    except Exception:
        return jsonify({"error": "invalid id"}), 400
    res = db.orders.delete_one({"_id": oid})
    if res.deleted_count == 0:
        return jsonify({"error": "not found"}), 404
    return "", 204