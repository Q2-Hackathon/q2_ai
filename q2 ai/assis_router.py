
from langchain.chains.router import MultiPromptChain
from openai import OpenAI
from langchain.chains.router.llm_router import LLMRouterChain,RouterOutputParser
from langchain.prompts import PromptTemplate
from langchain.chains import LLMMathChain, LLMChain
import os
from langchain.memory import ChatMessageHistory
base_dir = os.path.dirname(os.path.abspath(__file__))

import langchain
import openai
from langchain.chains import LLMMathChain, LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ChatMessageHistory
from langchain.prompts import (
    ChatPromptTemplate,
)
import playsound
import subprocess

# from langchain.callbacks.stdout import StdOutCallbackHandler
# from langchain.chains import

import config
import openai
openai.api_key = config.OPENAI_API_KEY

llm_model = "gpt-3.5-turbo"
history = ChatMessageHistory()

# import playsound
from pathlib import Path

counter = 0
# speech_file_path = Path(__file__).parent/f"speech_{counter}.mp3"
client = OpenAI()
def make_speech(text):
    global counter
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    speech_file_path = base_dir + "\speech_0.mp3"
    # speech_file_path = Path(__file__).parent / f"speech_{counter}.mp3"
    response.stream_to_file(speech_file_path)
    # return_code = subprocess.call(["afpaly", speech_file_path])
    # playsound.playsound(speech_file_path)
    counter += 1


make_payment_template = """You are a banking assistant for makeing transaction.
<< USER INPUT & CHAT HISTORY>>
{input}

<< INSTRUCTIONS >>
""
If user is asking to make transaction then get these informations - 
    Sender: Get the Senders Name
    Amount: how much money to send
""

<< RESPONSE FORMAT >>
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


account_details_template = """You are a very good in giving the users account details. \
<< USER DETAILS >>
User Namw: Shashank Srivasrava
ACCOUNT NUMBER: 123456789
ACCOUNT TYPE: SAVING
ACCOUNT BALANCE: 1000000
DATE OF BIRTH: 01/01/2000
ADDRESS: 123, ABC, XYZ, 123456
PHONE NUMBER: 1234567890
EMAIL: example@q2.com
INVESTMENT: 100000
LOAN: 100000

<< INSTRUCTIONS >>
Response in clear and descriptive manner.
Asking for any other way you can help the user.

<< USER INPUT >>
{input}"""

history_template = """You are a very good historian. \
You have an excellent knowledge of and understanding of people,\
events and contexts from a range of historical periods. \
You have the ability to think, reflect, debate, discuss and \
evaluate the past. You have a respect for historical evidence\
and the ability to make use of it to support your explanations \
and judgements.

Here is a question:
{input}"""


general_template = """You are very good at giving financial advice. \
You have a good knowledge of financial markets, \
financial products and the financial services industry. \
You have the ability to explain complex information \

<< USER INPUT >>
{input}"""
prompt_infos = [
    {
        "name": "make payment",
        "description": "For making payment transactions",
        "prompt_template": make_payment_template
    },
    {
        "name": "my acount details",
        "description": "Good for answering questions about your account",
        "prompt_template": account_details_template
    },
    {
        "name": "general",
        "description": "Good for answering general banking questions",
        "prompt_template": general_template
    }
]


llm = ChatOpenAI(temperature=0.5, model=llm_model)

destination_chains = {}
for p_info in prompt_infos:
    name = p_info["name"]
    prompt_template = p_info["prompt_template"]
    prompt = ChatPromptTemplate.from_template(template=prompt_template)
    chain = LLMChain(llm=llm, prompt=prompt)
    destination_chains[name] = chain

destinations = [f"{p['name']}: {p['description']}" for p in prompt_infos]
destinations_str = "\n".join(destinations)
# here we can crete a default prompt template
default_prompt = ChatPromptTemplate.from_template("{input}")
default_chain = LLMChain(llm=llm, prompt=default_prompt)

MULTI_PROMPT_ROUTER_TEMPLATE = """Given a raw text input to a \
language model select the model prompt best suited for the input. \
You will be given the names of the available prompts and a \
description of what the prompt is best suited for. \
You may also revise the original input if you think that revising\
it will ultimately lead to a better response from the language model.

<< FORMATTING >>
Return a markdown code snippet with a JSON object formatted to look like:
```json
{{{{
    "destination": string \ name of the prompt to use or "DEFAULT"
    "next_inputs": string \ a potentially modified version of the original input
}}}}
```

REMEMBER: "destination" MUST be one of the candidate prompt \
names specified below OR it can be "DEFAULT" if the input is not\
well suited for any of the candidate prompts.
REMEMBER: "next_inputs" can just be the original input \
if you don't think any modifications are needed.

<< CANDIDATE PROMPTS >>
{destinations}

<< INPUT >>
{{input}}

<< OUTPUT (remember to include the ```json)>>"""
def fun():
    print("Enter your query")
    user_query = input()
    router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(
        destinations=destinations_str
    )
    router_prompt = PromptTemplate(
        template=router_template,
        input_variables=["input"],
        output_parser=RouterOutputParser(),
    )

    router_chain = LLMRouterChain.from_llm(llm, router_prompt)

    chain = MultiPromptChain(router_chain=router_chain,
                             destination_chains=destination_chains,
                             default_chain=default_chain, verbose=True
                            )
    # response = chain.run("Make a payment of $100 to John Doe")
    response = chain.run("/Chat History: " + str(history.messages) + "User input : " + user_query)
    history.add_ai_message(response + user_query)
    make_speech(response)
    print(history)

    print(response)
    print("=" * 50)
    fun()

fun()
# make_speech("HEello world")
# speech_file_path = "D:/Hackathins/speech_0.mp3"
# # response.stream_to_file(speech_file_path)
# # return_code = subprocess.call(["afpaly", speech_file_path])
# playsound.playsound(speech_file_path)
# counter += 1