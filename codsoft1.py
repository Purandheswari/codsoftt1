import re
import random

# Dictionary to store patterns and responses
responses = {
    r'\b(hello|hi|hii|hey)\b': ['Hello!', 'Hi!', 'Hey there!'],
    r'\b(how are you|how\'s it going)\b': ['I\'m doing well, thank you!', 'Great, thanks for asking!'],
    r'\b(goodbye|bye)\b': ['Goodbye!', 'See you later!', 'Bye! Have a great day!'],
    r'\b(thank you|thanks)\b': ['You\'re welcome!', 'No problem!'],
    r'\b(give advice)\b': ['Always remember to stay positive!', 'Take a deep breath and relax. You got this!'],
    r'\b(what do you eat)\b': ['I don\'t eat anything. I\'m just a bot!', 'I consume data and electricity.'],
}

# Function to get response
def get_response(user_input):
    for pattern, responses_list in responses.items():
        if re.search(pattern, user_input.lower()):
            return random.choice(responses_list)
    return "I'm sorry, I didn't understand that."

# Testing the response system
print("Bot: Hello! How can I assist you today?")
while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        print("Bot: Goodbye!")
        break
    print("Bot:", get_response(user_input))
