import pandas as pd
import google.generativeai as genai
#from google.colab import userdata

#userdata.put("API_KEY", "AIzaSyBW76VKaYp3y2Pk7bhMin1KXFrlrdMFoA0")
#print("saved")

# this takes in the users api  to access the gemini model below
# as api can not be uploaded there are instructions for user to get there own personal api key from gemini dashboard  in the readme file
genai.configure(api_key="AIzaSyBW76VKaYp3y2Pk7bhMin1KXFrlrdMFoA0")

# this loads the pre determined user input and bot responses from the excel file
data = pd.read_excel("chatbot_data.xlsx")

# this inputs the predetermined responses into a dictionary called responses
#the keys are user inputs while the values are the bot responses
#  It iterates through each row of the DataFrame data and extracts the user input and bot response
responses = {row['user_input'].lower(): row['bot_responses']
             for idx, row in data.iterrows()}

# this intialises the ai model being used in case of lack of predetermined responses
gemini_model = genai.GenerativeModel('gemini-pro')

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
        # If input is not found in predetermined responses, generate response using Gemini ai uses the text to generaate and the strip to remove all unnecessary characters before and after response text
        bot_response = gemini_model.generate_content(user_input).text.strip()
        print("Darcbot:", bot_response)
        # Add the user input and bot response to the responses dictionary 
        responses[user_input] = bot_response
        # Update data DataFrame
        data = pd.DataFrame(responses.items(), columns=['user_input', 'bot_responses'])
        # Save the responses to the excel file
        data.to_excel("chatbot_data.xlsx", index=False)


        



