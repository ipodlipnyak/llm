from flask import Flask, request, jsonify
import os
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex

index_name = "test_index"

def initialize_index():
    if not os.path.exists(index_name):
        documents = SimpleDirectoryReader("./data").load_data()
        index = GPTSimpleVectorIndex.from_documents(documents)
        index.save_to_disk(index_name)


app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "payload": "are you lost"
    })


@app.route("/query", methods=["GET"])
def query_index():
    payload = "No text found, please include a ?text=blah parameter in the URL"
    status = 400

    index = GPTSimpleVectorIndex.load_from_disk(index_name)
    query_text = request.args.get("text", None)
    if query_text:
        payload = index.query(query_text)
        status = 200

    response = ({ "payload": payload }, status)
    return response



if __name__ == "__main__":
    initialize_index()
    app.run(host="0.0.0.0", port=5602)
