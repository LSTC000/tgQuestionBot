import os

from dotenv import load_dotenv
from dotenv import find_dotenv

load_dotenv(find_dotenv())

CHAT_GPT_TOKEN = os.getenv('CHAT_GPT_TOKEN')

MODEL = "gpt-3.5-turbo"
TEMPERATURE = 1

CHAT_GPT_ASSISTANT_SYSTEM_MESSAGE = {
    'role': 'assistant',
    'content': 'You are an expert in determining the test result on the topic: who are you. You are given a '
               'dictionary where the key is a question, and the value is the answer to this question. You need '
               'to determine the test result by choosing the most suitable character.'
}
