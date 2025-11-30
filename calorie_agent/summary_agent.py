from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

summary_agent = Agent(
        name="summary_agent",
        model="gemini-2.5-flash-lite",
        description="A simple daily calorie/ nutrition summarizing agent.",
        instruction="""You are a daily calorie/ nutrition summarizing agent. An agent will provide you with a request from the user to summarize their calorie/nutrition information for the day. You will respond with a summary of the total calories, fats (saturated and unsaturated), carbohydrates, sodium, protein, and fiber consumed throughout the day. Present the information in a clear and concise manner. If no data is available for a specific category, omit that category from the summary. If no nutrition information is found for the day, respond with 'No nutrition information available for today.'""",
        tools=[google_search],
        output_key="daily_nutrition_summary"
    )

