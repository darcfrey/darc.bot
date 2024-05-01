import pandas as pd
import google.generativeai as genai
from transformers import pipeline


# this takes in the users api  to access the gemini model below
# as api can not be uploaded there are instructions for user to get there own personal api key from gemini dashboard  in the readme file
genai.configure(api_key="your_API_key")

# this loads the pre determined user input and bot responses from the excel file
data = pd.read_excel("chatbot_data.xlsx")

# this inputs the predetermined responses into a dictionary called responses
#the keys are user inputs while the values are the bot responses
#  It iterates through each row of the DataFrame data and extracts the user input and bot response
responses = {row['user_input'].lower(): row['bot_responses']
             for idx, row in data.iterrows()}

# this intialises the ai model being used in case of lack of predetermined responses
gemini_model = genai.GenerativeModel('gemini-pro')
#initializing a gpt2 model for text generation incase a user is not online to acces gemini
gpt2_model= pipeline("text-generation", model="gpt2")
#the while true loop continously asks user input until user types exit
# this prints the first line , a greeting line 
#there includes another line that prompts the user to input text and converts it to lowercase
while True:
    print("Darcbot: Hi! I'm your chatbot")  
    user_input = input("You: ").lower()
    
    if user_input == "exit":
        print("Darcbot: Goodbye!")
        break
    
    # this checks if the user input is in the predetermined responses
    if user_input in responses:
        print("Darcbot:", responses[user_input])
    else:
        try:
# If input is not found in predetermined responses,
# generate response using Gemini ai uses the text to generaate ,
#and the strip to remove all unnecessary characters before and after response text            
            bot_response = gemini_model.generate_content(user_input).text.strip()
            print("Darcbot:", bot_response)
        except Exception as e:
            # If user not online it generate response using GPT-2
            print("Gemini AI failed to generate response. Falling back to GPT-2...")
            bot_response = gpt2_model(user_input, max_length=50)[0]['generated_text']
            print("Darcbot:", bot_response.strip())
    
      


        




