from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "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"  # استبدل هذا بالمفتاح

def generate_response(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    return response.choices[0].message['content']

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_message = data['entry'][0]['messaging'][0]['message']['text']
    bot_response = generate_response(user_message)
    return jsonify({"text": bot_response})

if __name__ == '__main__':
    app.run(port=5000)