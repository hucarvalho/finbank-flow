from flask import Blueprint, request, jsonify
from app.controllers import saldo_controller


bp = Blueprint('saldo', __name__, url_prefix='/api/saldo')

@bp.route("/", methods=["GET"])
def get_saldo():
    try:
        saldo = saldo_controller.get_saldo()
        return jsonify({"saldo": saldo}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route("/", methods=["POST"])
def depositar():
    try:
        data = request.get_json()
        valor = data.get("valor")
        if valor is None:
            return jsonify({"error": "Valor é obrigatório"}), 400
        saldo_controller.depositar(valor)
        return jsonify({"message": "Depósito realizado com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
