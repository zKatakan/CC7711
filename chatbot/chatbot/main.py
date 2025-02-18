#pip install nltk numpy tensorflow

from chatbot import ChatBot
myChatBot = ChatBot()


#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o modelo, APENAS USAR QUANDO MUDAR O QUE ESTÁ NO INTENTS.JSON!!!
myChatBot.createModel()

# rodar o modelo, USAR QUANDO NÃO TIVER MODIFICADO NADA NO INTENTS.JSON!!!
#myChatBot.loadModel()


print("\nBem vindo ao Chatbot")


pergunta = input("Como posso te ajudar? ")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]")


while (intencao[0]['intent']!="despedida"):
    pergunta = input("\nPosso lhe ajudar com algo a mais? ")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   [" + intencao[0]['intent'] + "]")

print("\nFoi um prazer atendê-lo\n")
