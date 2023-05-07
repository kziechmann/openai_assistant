import openai
pip install dotenv
from dotenv import load_dotenv
load_dotenv('/my_openai_apikey.env')

my_api_key = os.getenv('my_api_key')

openai.api_key = my_api_key # supply your API key however you choose

message = {"role":"user", "content": input("This is the beginning of your chat with AI. [To exit, send \"###\".]\n\nYou:")};

conversation = [{"role": "system", "content": "DIRECTIVE_FOR_gpt-3.5-turbo"}]

while(message["content"]!="###"):
    conversation.append(message)
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation) 
    message["content"] = input(f"Assistant: {completion.choices[0].message.content} \nYou:")
    print()
    conversation.append(completion.choices[0].message)