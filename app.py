import os
from flask import Flask, request, abort
from twilio.twiml.messaging_response import MessagingResponse
from twilio.request_validator import RequestValidator
from dotenv import load_dotenv

# Flask is a way to create a web server and handle requests from twilio
app = Flask(__name__)

load_dotenv()  # Load environment variables from .env file

# Create Twilio Auth Token Validator
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
validator = RequestValidator(auth_token)

@app.route("/bot", methods=['GET','POST'])
def bot():
    # Validate the incoming Twilio request
    signature = request.headers.get('X-Twilio-Signature', '')
    if not validator.validate(str(request.url), request.form, signature):
        abort(403)  # Forbidden, validation failed

    incoming_message = request.values['Body']
    print(incoming_message)

    # use the incoming_message to generate a response

    resp = MessagingResponse()
    resp.message("this is the response")

    return str(resp)

    # ngrok communicates with twilio - not necessary for development on a server