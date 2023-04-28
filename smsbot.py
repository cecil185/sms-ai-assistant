import os
import openai
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file
OPENAPI_API_KEY = os.environ.get("OPENAPI_API_KEY")

def fetch_twilio_webhook_data():
    """returns Text object 
    """
    pass


def convert_text_to_prompt(text):
    """returns Prompt 
    """

def append_interaction_to_chat_log(text_message, answer, chat_log=None):
    if chat_log is None:
        chat_log = text_message
    return f"{chat_log}Accountant: {text_message}\nSMSBOT: {answer}\n"


def openai_request(question, chat_log):
    """Send prompt 

    returns OpenAI response
    """ 

    #TODO: refactor this into two separate methods

    openai.api_key = OPENAPI_API_KEY

    # prompt = append_interaction_to_chat_log(text_message, answer, chat_log=None)
    prompt = f"{chat_log}Accountant: {question}\nSMSBOT:"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=['\nAccountant']
    )

    answer = response.choices[0].text.strip()
    return answer

def sync_time_to_karbon_api():

    print("hello")

    pass


text_message = "spent 1 hour on training on python this week on wednesday"
answer = openai_request(text_message, chat_log=None) # expecting: the format of a time entry
print(answer)

# take the response and feed it back into chat 
new_chat_log = append_interaction_to_chat_log(text_message, answer, chat_log=None)
print(new_chat_log)

text_message = "create work for client BCCA"
answer = openai_request(text_message, chat_log=new_chat_log) # expecting: the format of a time entry
print(answer)


text_message = "I need to send out the T4 forms for BCCA"
answer = openai_request(text_message, chat_log=new_chat_log) # expecting: the format of a time entry
print(answer)