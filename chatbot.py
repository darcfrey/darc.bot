"""import pandas as pd
from transformers import pipeline
data=pd.read_csv("book.csv")#the dictionary
print(data)
response={}
for ide, row in data.iterrows():
    user_input=row('INPUT QUESTIONS')
    bot_response=row('BOT RESPONSES')
    response(user_input)== bot_response

while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("AI: Goodbye!")
            break

        bot_response = response(user_input)
        print("AI:", bot_response)"""

import pandas as pd
 #import openai
from transformers import pipeline

# Set up OpenAI API key
#openai.api_key = "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"

# Load data
data = pd.read_excel("chatbot_data.xlsx")

# Extract predetermined responses into a dictionary
responses = {row['user_input'].lower(): row['bot_responses'] for idx, row in data.iterrows()}

# Initialize GPT-3 chatbot
chatbot = pipeline("text-generation", model="gpt2")  

print("Darcbot: Hi! I'm your chatbot")  # Start interaction loop
while True:
    user_input = input("You: ").lower()
    
    if user_input == "exit":
        print("Darcbot: Goodbye!")
        break
    
    # Check if the user input is in the predetermined responses
    if user_input in responses:
        print("Darcbot:", responses[user_input])
    else:
        # If not found in predetermined responses, generate response using GPT-3
        bot_response =  chatbot(user_input, max_length=50)[0]['generated_text']
        print("Darcbot:", bot_response.strip())
        # Add the user input and bot response to the responses dictionary
        responses[user_input] = bot_response.strip()
        # Update data DataFrame
        data = pd.DataFrame(responses.items(), columns=['user_input', 'bot_responses'])
        # Save the responses to the excel file
        data.to_excel("chatbot_data.xlsx", index=False)

        



