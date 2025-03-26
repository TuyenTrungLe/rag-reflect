import os

from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = AzureChatOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        temperature=0,
        verbose=True,
)

prompt = hub.pull("rlm/rag-prompt")

generation_chain = prompt | llm | StrOutputParser()
