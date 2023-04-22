from flask import Flask, request
import os
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex

index_name = 'test_index'

def initialize_index():
    if not os.path.exists(index_name):
        documents = SimpleDirectoryReader("./data").load_data()
        index = GPTSimpleVectorIndex.from_documents(documents)
        index.save_to_disk(index_name)


app = Flask(__name__)


@app.route("/")
def home():
    return "are you lost?"


@app.route("/query", methods=["GET"])
def query_index():
    index = GPTSimpleVectorIndex.load_from_disk(index_name)
    query_text = request.args.get("text", None)
    if query_text is None:
        return "No text found, please include a ?text=blah parameter in the URL", 400
    response = index.query(query_text)
    return str(response), 200


if __name__ == "__main__":
    initialize_index()
    app.run(host="0.0.0.0", port=5602)
