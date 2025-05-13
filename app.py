from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Logic to process user input
def respond_to_input(user_input, state={}):
    # Example flow
    if "slow" in user_input.lower():
        return "Are you on Wi-Fi or wired connection?", state
    if "wi-fi" in user_input.lower():
        return "Are you using a SecureNet router like the TP-Link Deco or your own?", state
    # Default fallback
    return "Can you describe your issue in more detail?", state

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
