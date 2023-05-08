import os
import openai
# from dotenv import load_dotenv
# load_dotenv('/my_openai_apikey.env')
# my_api_key = os.getenv('my_api_key')

openai.api_key = "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"

message = {
    "role":"user",
    "content": input("Good morning!\n\n Let's start your day off right by organizing your priorities. \nPlease tell me your top three tasks for today, and I'll help you schedule them.\n You can also specify any deadlines or time constraints.\n Once we have a plan, I can send you reminders via Twilio or add the tasks to your Google Calendar.\n Let's get started! \n\nTo exit say 'done!!!' \n Priorities:")
};

conversation = [{
    "role": "system",
     "content": "DIRECTIVE_FOR_gpt-3.5-turbo",
     "prompt": "Prompt user, listen and store input, extract ideas, priorities, and goals, prompt for clarifications if needed, provide feedback and suggestions using algorithms, offer tools and resources, use sentiment analysis and NLG for motivational feedback, thank user and prompt for additional needs, repeat steps 2-8 as needed to help user achieve goals and improve productivity.",
}]

while(message["content"]!="done!!!"):
    conversation.append(message)
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation) 
    message["content"] = input(f"Assistant: {completion.choices[0].message.content} \nYou:")
    print()
    conversation.append(completion.choices[0].message)