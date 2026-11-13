import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient


async def main() -> None:
    model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        api_key=os.environ["OPENAI_API_KEY"],
    )
    agent = AssistantAgent(
        name="hr_assistant",
        model_client=model_client,
        system_message="You are an HR assistant.",
    )
    try:
        await Console(
            agent.run_stream(
                task="Write a 5-line job description for a Junior Python Developer."
            )
        )
    finally:
        await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
