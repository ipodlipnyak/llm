Containerized api ready to use as a microservice in your private network.

### Docker

Copy `docker.env.example` into `docker.env` and fill `OPEN_API_KEY` variabel with [your value](https://platform.openai.com/account/api-keys).

``` bash
cp docker.env.example docker.env
```

Start it and route other apps to it.

``` bash
docker compose up -d
```

There is no authorisation guards. And indexes just dumps as `test_index.json` file.

### Poetry

Other way around would be to start project inside python venv.

``` bash
export OPEN_API_KEY=yourOpenaiaApiKey
poetry run python3 main.py
```

## You should look into those projects

- [LLaMa Index](https://gpt-index.readthedocs.io/en/latest/index.html) - awesome llm framework
- [LLaMa-python](https://abetlen.github.io/llama-cpp-python/) - good start to try llm with python
- [Hugging Face](https://huggingface.co/)
