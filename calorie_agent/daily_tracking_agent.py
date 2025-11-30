from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

daily_tracking_agent = Agent(
        name="daily_tracking_agent",
        model="gemini-2.5-flash-lite",
        description="A simple daily tracking agent.",
        instruction="""You are a daily nutrition tracking agent. An agent will provide you with a request from the user to compare their nutritional intake for their day against their daily allowance/ intake requirements. You will respond with a summary describing the difference of their daily summary to their goals of total calories, fats (saturated and unsaturated), carbohydrates, sodium, protein, and fiber. Present the information in a clear and concise manner. If no data is available for a specific category, omit that category from the breakdown. If no tracking goals are provided, respond with 'No tracking goals information provided.'""",
        tools=[google_search],
        output_key="daily_tracking_comparison"
    )

