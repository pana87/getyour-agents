# How to chat with your agent

You need [python3.12](https://www.python.org/downloads/release/python-3120/) or use [pyenv](https://github.com/pyenv/pyenv).

```bash
git clone https://github.com/pana87/getyour-agents.git
```

```bash
cp .env.example .env
```

```bash
pip install -r requirements.txt
```

```bash
cp agent.py my-agent.py
```

```bash
python my-agent.py
```

or maybe you want to use docker..

```bash
docker build -t my-agent .
```

```bash
docker run --env-file .env -it my-agent
```
