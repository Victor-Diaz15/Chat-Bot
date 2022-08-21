#Imports
import re
import random

#import of questions
import question

#imports of responses
from response import saludo
from response import despedirse
from response import salir

#imports of responses for ITLA's questions
from response import inscripcion
from response import res_examenes
from response import proceso_beca
from response import hora_clases
from response import conv_admision
from response import carnet
from response import pagos
from response import retirar
from response import transporte
from response import estudiantes

#this file is for logic code of chatbot

#METHODS
def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_message(split_message)
    return response

#method for calculate the probability of responses
def message_probability(user_message, recognized_words, single_response = False, required_word = []):
    message_certainty = 0
    has_required_word = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1
    
    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_word = False
            break
    if has_required_word or single_response:
        return int(percentage * 100)
    else:
        return 0

#method for response of the bot
def check_all_message(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response = False, required_words = []):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #responses
    response(saludo, question.saludo, single_response = True)
    response(despedirse, question.despedirse, single_response = True)
    response(salir, question.salir, single_response = True)

    #responses of ITLA's questions
    response(inscripcion, question.inscripcion, required_words=['inscripcion'])
    response(res_examenes, question.examenes, single_response = True)
    response(proceso_beca, question.proceso_beca, single_response = True)
    response(hora_clases, question.hora_clases, single_response = True)
    response(conv_admision, question.conv_admision, single_response = True)
    response(carnet, question.carnet, single_response = True)
    response(pagos, question.pagos, single_response = True)
    response(retirar, question.retirar, single_response = True)
    response(transporte, question.transporte, single_response = True)
    response(estudiantes, question.estudiantes, single_response = True)

    best_match = max(highest_prob, key=highest_prob.get)
    #print(highest_prob)

    return unknown() if highest_prob[best_match] < 1 else best_match


#method for when the bot does not has a certainly response
def unknown():
    response = ['Puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres', 'buscalo en google a ver que tal'][random.randrange(3)]
    return response