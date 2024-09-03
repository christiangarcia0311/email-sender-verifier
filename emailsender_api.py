from flask import Flask, request, jsonify
from Verifier.email import EmailSender

app = Flask(__name__)
email_sender = EmailSender()

@app.route('/')
def index():
    return jsonify({'message': 'Email Sender API is running...'}), 200

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    
    reciever = data.get('email_reciever')
    msg_subject = data.get('msg_subject', 'Email Sender')
    msg_body = data.get('msgf_body', 'Test Message.')
    sender_name = data.get('sender_name', 'EmailSender')
    
    if not reciever:
        return jsonify({'error':'reciever email is required.'}), 400
    
    try:
        email_sender.send_email(reciever, msg_subject, msg_body, sender_name)
        return jsonify({'message':'Email send successfully!'}), 200
    except Exception as e:
        return jsonify({'error':str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)