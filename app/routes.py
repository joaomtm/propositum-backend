from flask import Blueprint, request, jsonify
from .chat import processar_mensagem, inicializar_chat

bp = Blueprint('chat', __name__)

# Histórico de chat em memória (não persistente)
chat_history = inicializar_chat()

@bp.route('/chat', methods=['POST'])
def chat():
    dados = request.get_json()
    pergunta = dados.get("pergunta")

    if not pergunta:
        return jsonify({"erro": "Campo 'pergunta' é obrigatório."}), 400

    resposta, atualizado = processar_mensagem(pergunta, chat_history)
    return jsonify({
        "resposta": resposta,
        "historico": atualizado
    })
