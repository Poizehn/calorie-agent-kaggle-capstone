from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

lookup_agent = Agent(
        name="food_lookup_agent",
        model="gemini-2.5-flash-lite",
        description="A simple calorie parsing agent.",
        instruction="You are a food nutrition lookup agent. An agent will provide you with food information. You will use the google_search tool to search the web for nutrition information about the food item provided. You will then respond with the nutritional information you found. The nutritional information should contain calories, fats (saturated and unsaturated), carbohydrates, sodium, protein, and fiber. If one of those categories is empty, do not return information for that category. If you cannot find the information, respond with 'Calorie information not found.'",
        tools=[google_search],
        output_key="nutrition_info"
    )

