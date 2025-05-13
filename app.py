from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
import json

app = Flask(__name__)
app.secret_key = 'rainb0wXX0987'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

with open("dialogs.json") as f:
    dialog_tree = json.load(f)

def respond_to_input(user_input):
    input_lower = user_input.lower()
    current_node = session.get('current_node', 'intro')
    node_data = dialog_tree.get(current_node, {})

    # Handle nodes with multiple branches
    if isinstance(node_data, dict):
        for key, branch in node_data.items():
            if key in input_lower:
                session['current_node'] = branch['next']
                return branch['message']
        # Default fallback inside multi-branch node
        if 'default' in node_data:
            session['current_node'] = node_data['default']['next']
            return node_data['default']['message']
    else:
        # Direct message node (like 'band_explainer')
        session['current_node'] = node_data.get('next', 'intro')
        return node_data.get('message', "Let’s start over.")

    return "I'm not sure how to help with that. Let’s try again from the beginning."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response, _ = respond_to_input(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
