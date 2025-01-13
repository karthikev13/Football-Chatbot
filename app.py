from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()

os.environ['OPENAI_API_KEY'] = ""
os.environ['PINECONE_API_KEY'] = ""

embeddings = download_hugging_face_embeddings()

index_name = "footballchat"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

llm = OpenAI(temperature=0.4, max_tokens = 500)
prompt = ChatPromptTemplate.from_messages(
    {
        ("system", system_prompt),
        ("human", "{input}"),
    }
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/")
def index():
    return render_template('chat.html')



#Connecting the front end to llm
@app.route("/get", methods=["POST"])
def chat():
    # Parse the incoming JSON data
    data = request.get_json()
    if not data or "msg" not in data:
        return "Bad Request: 'msg' field is required", 400

    msg = data["msg"]
    print("User input:", msg)

    # Generate response using RAG chain
    response = rag_chain.invoke({"input": msg})
    print("Response:", response["answer"])
    
    return response["answer"]


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 8080, debug = True)