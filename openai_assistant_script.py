import os
import openai
from dotenv import load_dotenv
load_dotenv('/my_openai_apikey.env')
my_api_key = os.getenv('my_api_key')

message = {
    "role":"user",
    "content": input("\nGood morning! Let's start your day off right by organizing your priorities. \n\nPlease tell me your top three tasks for today, and I'll help you schedule them.\n\nYou can also specify any deadlines or time constraints.\nOnce we have a plan, I can send you reminders via Twilio or add the tasks to your Google Calendar.\n\nLet's get started! \n\n   To exit say 'done!!!' \n Priorities:")
}

prompt = "Prompt user, listen and store input, extract ideas, priorities, and goals, prompt for clarifications if needed, provide feedback and suggestions using algorithms, offer tools and resources, use sentiment analysis and NLG for motivational feedback, thank user and prompt for additional needs, repeat steps 2-8 as needed to help user achieve goals and improve productivity."
conversation = [{
    "role": "system",
     "content": "DIRECTIVE_FOR_gpt-3.5-turbo"
},
{"role": "system", "content": prompt}
]


while(message["content"]!="done!!!"):
    conversation.append(message)
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation) 
    message["content"] = input(f"Assistant: {completion.choices[0].message.content} \nYou:")
    print()
    conversation.append(completion.choices[0].message)