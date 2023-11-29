# To get environment variables
import os

# Make the display a bit wider
from IPython.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))

# To split our transcript into pieces
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Our chat model. We'll use the default which is gpt-3.5-turbo
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain

# Prompt templates for dynamic values
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate, # I included this one so you know you'll have it but we won't be using it
    HumanMessagePromptTemplate
)

# To create our chat messages
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import config
import openai
openai.api_key = config.OPENAI_API_KEY

with open('oveall_conversation_sum.txt', 'r') as file:
    content = file.read()
text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size=2400, chunk_overlap=250)
texts = text_splitter.create_documents([content])
# Your api key should be an environment variable, or else put it here
# We are using a chat model in case you wanted to use gpt4
llm = ChatOpenAI(temperature=2)
# verbose=True will output the prompts being sent to the
# chain = load_summarize_chain(llm, chain_type="map_reduce", verbose=True)
# output = chain.run(texts)
template="""
You are a helpful assistant that helps RM(Relationship Manager at banks), to make a sale in future.
So suggest the interest of the customer based on the conversation.
Don't make up any information, but use the information you have.
respond only at max 3 interest in bullet form.
<<RESPONSE FORMAT>>
-bullet format
-one or two words
-3 interest at max
"""
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

human_template="{text}" # Simply just pass the text as a human message
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages(messages=[system_message_prompt, human_message_prompt])

chain = load_summarize_chain(llm,
                             chain_type="map_reduce",
                             map_prompt=chat_prompt
                            )

# Because we aren't specifying a combine prompt the default one will be used

output = chain.run({
                    "input_documents": texts,
                   })

print(output)