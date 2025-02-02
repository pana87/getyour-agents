import sys
import logfire
import os
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from dotenv import load_dotenv

load_dotenv()
logfire.configure(send_to_logfire='if-token-present')

model = OpenAIModel(
    os.getenv("LLM_MODEL"),
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("OPEN_ROUTER_API_KEY"),
)
agent = Agent(
    model,
    system_prompt=(
      'Du bist ein CouchDB Agent. '
    )
)

while True:
    user_input = input("You: ")
    if user_input.lower() == 'q':
        sys.exit(0)

    result = agent.run_sync(user_input)
    print(f"AI: {result.data}")

