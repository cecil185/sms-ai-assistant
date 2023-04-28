from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
# flask is a way to create a web server and handle requests from twilio

@app.route("/bot/{key}", methods=['GET','POST'])
def bot():

    incoming_message = request.values['Body']
    print(incoming_message)

    # use the incoming_message to generate a response

    resp = MessagingResponse()
    resp = resp.message("this is the response")
    print(str(resp))
    return str(resp)

    # ngrok communicates with twilio - not necessary for development on a server