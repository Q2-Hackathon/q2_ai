import os
import langchain
import openai
from langchain.chains import LLMMathChain, LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ChatMessageHistory
from langchain.prompts import (
    ChatPromptTemplate,
)
import playsound
# from langchain.callbacks.stdout import StdOutCallbackHandler
# from langchain.chains import


import config
import openai
openai.api_key = config.OPENAI_API_KEY

history = ChatMessageHistory()
user_chat = []
ai_chat = []
voice = "Brian"
from pathlib import Path
from openai import OpenAI

client = OpenAI()
speech_file_path = Path(__file__).parent / "speech.mp3"


def make_speech(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    response.stream_to_file(speech_file_path)
    playsound.playsound(speech_file_path)

def fun():
    user_query = input()
    llm = ChatOpenAI(temperature=0.6)
    prompt = ChatPromptTemplate.from_template(
        """You are a banking assistant. 

        USER INPUT AND CHAT HISTORY: 
        {user}

        INSTRUCTIONS:
        ""
        If user is asking to make transaction then get these informations - 
            Sender: Get the Senders Name
            Amount: how much money to send
        ""

        RESPONSE FORMAT: 
        {{{{
            "chat_reply": If you know senders name and how much money to transfer response with "payment is porcessing"\
                        other wise ask for the detail which you require
            "sender_name" : senders name from user input or chat summary
            "amount": amount of money from user input or chat summary
            "action": if more info required then return "more_info"\
                    if all correct information about user is gathered then return "make_transaction"                     
            "summary": make all the summary of the chat
        }}}}             
        """
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    # And as you get any of these values from user store this in your response dictionary
    response = chain.run("/Chat History: " + str(history.messages) + "User input : " + user_query)
    # response = chain.run(str(history.messages) + user_query)
    ai_chat.append(response)
    history.add_ai_message(response + user_query)
    print(history)
    print(history.messages)
    make_speech(response)
    print(response)

    print("=" * 50)
    fun()


fun()

# text = "Hello, world!"

# Choose a voice from the available presets
