from dotenv import dotenv_values
from langchain.chat_models import init_chat_model

config = dotenv_values(".env")

print(config["model"])

llm=init_chat_model(config["model"]
    , api_key=config["apikey"]
    ,verbose=True
    ,base_url="https://api.cerebras.ai/v1"
)
risposta= llm.invoke("Chi è Elon Musk? Rispondi brevemente!")

print(type(risposta))
print(risposta)
print(risposta.content)