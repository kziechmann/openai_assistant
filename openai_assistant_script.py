import os
import openai
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv('/my_openai_apikey.env')
load_dotenv('/my_twilio_credentials.env')

my_api_key = os.getenv('MY_OPENAPI_KEY')
account_sid = os.getenv['TWILIO_ACCOUNT_SID']
auth_token = os.getenv['TWILIO_AUTH_TOKEN']

call_from = os.getenv['CALL_FROM_NUMBER']
call_to = os.getenv['CALL_TO_NUMBER']

client = Client(account_sid, auth_token)

message = {
    "role":"user",
    "content": input("""
        \nGood morning! Let's start your day off right by organizing your priorities.
        \n\nPlease tell me your top three tasks for today, and I'll help you schedule them.
        \n\nYou can also specify any deadlines or time constraints.
        \nOnce we have a plan, I can send you reminders via Twilio or add the tasks to your Google Calendar.
        \n\nLet's get started!
        \n\nTo exit say 'done!!!'
        \n Priorities:""")
}

prompt = """Prompt user, listen and store input,
extract ideas, priorities, and goals,
prompt for clarifications if needed,
provide feedback and suggestions using algorithms,
offer tools and resources,
use sentiment analysis and NLG for motivational feedback,
thank user and prompt for additional needs,
reply with "#twilio": prefixed to a message to schedule sending a message to the user via Twilio api,
repeat steps 2-8 as needed to help user achieve goals and improve productivity.
 """

conversation = [
    {
        "role": "system",
        "content": "DIRECTIVE_FOR_gpt-3.5-turbo"
    },
    {   
        "role": "system",
        "content": prompt
    }
]


while(message["content"]!="done!!!"):
    conversation.append(message)
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation) 
    if completion.choices[0].message.content.startswith("#twilio"):
       twilioMessage = client.messages \
        .create(
            body = completion.choices[0].message.content,
            from_= call_from,
            to= call_to
        )
       message["content"] = input(f"Assistant: sheduled the following message -- {completion.choices[0].message.content} \n\nYou:")
    else:
        message["content"] = input(f"Assistant: {completion.choices[0].message.content} \n\nYou:")
    print()
    conversation.append(completion.choices[0].message)