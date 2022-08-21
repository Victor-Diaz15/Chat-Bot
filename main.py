#Imports
from chatbot import get_response

#flag
run = True
#main infinite loop
while run:
    bot_response = get_response(input('You: '))
    print("Bot: " + bot_response)

    #validacion para detener el bot.
    if bot_response == "terminado":
        run = False