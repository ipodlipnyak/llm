Containerized api ready to use as a microservice in your private network.

Copy `docker.env.example` into `docker.env` and fill `OPEN_API_KEY` variabel with your value.

``` bash
cp docker.env.example docker.env
```

Start it and route other apps to it.

``` bash
docker compose up -d
```

There is no authorisation guards. And indexes just dumps as json file.

## You should look into this projects

- [LLaMa-python](https://abetlen.github.io/llama-cpp-python/) - good start to try llm
- [LLaMa Index](https://gpt-index.readthedocs.io/en/latest/index.html) - awesome llm framework

