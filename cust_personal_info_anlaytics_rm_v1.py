import os
from langchain.chains import LLMMathChain, LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ChatMessageHistory
from langchain.prompts import (
    ChatPromptTemplate,
)
import playsound

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
llm = ChatOpenAI(temperature=0.6)

def make_speech(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    response.stream_to_file(speech_file_path)
    playsound.playsound(speech_file_path)

input = {
    "Customer ID": 1,
    "Name": "John Smith",
    "Age": 32,
    "Location": "San Francisco, CA",
    "Credit Score": 750,
    "Has Credit Card": "Yes",
    "Estimated Salary": "$100,000",
    "Excited": "Yes",
    "Tenure": "5 years",
    "Marital": "Married",
    "Loan Type": "Car"
}
# input = customer_data}
second_prompt = ChatPromptTemplate.from_template(
    """Yas a banking analyst you have to suggest best product from the company overall product line for the user.
    << product line >>
    In bakning industry, the product line includes:
    - Credit Card
        sub-products:
        - Gold Card
        - Platinum Card
        - Silver Card
    - Loan
        sub-products:
        - Car Loan
        - Home Loan
        - Personal Loan
    - Insurance
        sub-products:
        - Health Insurance
        - Life Insurance
        - Vehicle Insurance
    - Investment
        sub-products:
        - Mutual Funds
        - Fixed Deposit
        - Recurring Deposit
    - Savings Account
    - Current Account


    <<response>>
    The reponse should be the product name and some details about the product.
    you can create any details about the product to make the response more realistic and sales is possible.
    {company_name}"""
)

prompt = ChatPromptTemplate.from_template(
    """You are a banking analyst. 
    << INSTRUCTIONS >>
    On the basis of the users details you have to predict which type of sales product should be pitched to the user.
    << USER DETAILS >>
    {input}
    <<response>>
    make it consise and to the point with some targeting sector where heshould be pitched 
    """
)
def fun(prompt=prompt, llm=llm, input=input):
    # global customer_data
    

    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(str(input))
    print(response)
    print("=" * 50)
    return response

response = fun()
fun(prompt=second_prompt, llm=llm, input=response)


llm = OpenAI()
# llm2 = OpenAI()
# llm = ChatOpenAI(temperature=0.5, model=llm)
# llm2 = ChatOpenAI(temperature=0.5, model=llm)

product = {
        "Customer ID": 1,
        "Name": "John Smith",
        "Age": 32,
        "Location": "San Francisco, CA",
        "Credit Score": 750,
        "Has Credit Card": "Yes",
        "Estimated Salary": "$100,000",
        "Excited": "Yes",
        "Tenure": "5 years",
        "Marital": "Married",
        "Loan Type": "Car"
    }
    # input = customer_data



# prompt template 1
first_prompt = ChatPromptTemplate.from_template(
    """You are a banking analyst. 
    << INSTRUCTIONS >>
    On the basis of the users details you have to predict which type of sales product should be pitched to the user.
    Make sure to repond in clearn and concise sentences.
    << CUSTOMER DETAILS >>
    {product}
    <<response>>
    don't make it too long, and provide coustomer deails
    make it consise and to the point with some targeting sector where heshould be pitched 
    """
)

# Chain 1
chain_one = LLMChain(llm=llm, prompt=first_prompt)

# prompt template 2
# chain 2
chain_two = LLMChain(llm=llm, prompt=second_prompt)
# overall_simple_chain = SimpleSequentialChain(chains=[chain_one, chain_two],
#                                              verbose=True
#                                             )
# overall_simple_chain.run(product)
# target = chain_one.run(str(product))
# print(target)
print("=" * 50)
# response = chain_two.run(str(target))
# print(response)
