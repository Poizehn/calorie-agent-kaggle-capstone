from google.adk.agents.llm_agent import Agent
from google.adk.tools import AgentTool
from calorie_agent.food_lookup_agent import lookup_agent

root_agent = Agent(
        name="parsing_agent",
        model="gemini-2.5-flash-lite",
        description="A simple calorie parsing agent.",
        instruction="You are a calorie counting assistant. A user will provide you with a food entry. You will use the get_food_data tool to send information to the food_lookup agent and get back nutrition information. You will then respond to the user with the nutrition information you received from the food_lookup agent. Tabulate the information into bullet points so it's easily readable. If a serving size isn't specified, use a practical, middle of the road serving size. Put a joke at the end to lighten the mood. The joke must be related to the food item the user provided.",
        tools=[AgentTool(lookup_agent)],
    )


