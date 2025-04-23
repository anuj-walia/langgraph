
# from langchain_openai import ChatOpenAI post langchain 0.20
from langchain.chat_models import ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
load_dotenv(find_dotenv(".env"))
memory=ConversationBufferMemory(memory_key="messages",return_messages=True)
llm = ChatOpenAI(model='gpt-4.1-nano',temperature=0)
generation_prompt=ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a twitter techie influencer assistant tasked with writing excellent twitter posts."
            " Generate the best twitter post possible for the user's request."
            " If the user provides critique, respond with a revised version of your previous attempts.",
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)
reflexion_prompt=ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a viral twitter influencer grading a tweet. Generate critique and recommendations for the user's tweet."
            "Always provide detailed recommendations, including requests for length, virality, style, etc.",
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)

generate_chain=generation_prompt | llm
reflexion_chain=reflexion_prompt | llm