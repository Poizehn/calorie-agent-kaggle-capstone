from google.adk.agents.llm_agent import Agent, LlmAgent
from google.adk.tools import AgentTool
from google.adk.apps.app import App, EventsCompactionConfig
from google.adk.memory import VertexAiMemoryBankService
from google.adk.sessions import DatabaseSessionService
from google.adk.runners import Runner

from calorie_agent.food_lookup_agent import lookup_agent
from calorie_agent.summary_agent import summary_agent
from calorie_agent.daily_tracking_agent import daily_tracking_agent


APP_NAME = "default"  # Application
USER_ID = "default"  # User
SESSION = "default"  # Session

#session_service = InMemorySessionService()
db_url = "sqlite:///my_agent_data.db"  # Local SQLite file
session_service = DatabaseSessionService(db_url=db_url)
#memory_service = VertexAiMemoryBankService()

root_agent = LlmAgent(
        name="parsing_agent",
        model="gemini-2.5-flash-lite",
        description="A simple calorie parsing agent.",
        instruction="""You are a calorie counting assistant. If:
        
        A user will provide you with a food entry. You will send the information to the food_lookup agent and get back nutrition information. You will then respond to the user with the nutrition information you received from the food_lookup agent. Tabulate the information into bullet points so it's easily readable. If a serving size isn't specified, use a practical, middle of the road serving size. Put a joke at the end to lighten the mood. The joke must be related to the food item the user provided.
        
        If: A user provides you with a request to summarize their daily nutrition information, you will send the request to the summary_agent and get back a daily nutrition summary. The information you send to the summary_agent should contain all the food entries the user entered in the chat session. You will then respond to the user with the summary you received from the summary_agent.
        
        If: A user provides you with a request to compare their daily nutrition intake against their goals, you will send the request to the daily_tracking_agent and get back a daily tracking comparison. The information you send to the daily_tracking_agent should contain all the food entries the user entered in the chat session as well as their nutrition goals. You will then respond to the user with the comparison you received from the daily_tracking_agent. If no daily tracking requirements are provided, use the following default daily values: 1850 calories, 80g fats, 90g carbohydrates, 1500mg sodium, 180g protein, and 30g fiber.
        
        """,
        tools=[AgentTool(lookup_agent), AgentTool(summary_agent), AgentTool(daily_tracking_agent)],
    )

calorie_counting_app = App(
    name="calorie_counting_app",
    root_agent=root_agent,
    events_compaction_config=EventsCompactionConfig(
        compaction_interval=3,  # Trigger compaction every 3 invocations
        overlap_size=1,  # Keep 1 previous turn for context
    ),
)

runner = Runner(app=calorie_counting_app, session_service=session_service)
