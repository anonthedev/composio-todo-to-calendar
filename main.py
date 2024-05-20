import os
import dotenv
import zoneinfo
from datetime import datetime
from crewai import Agent, Task
from langchain_openai import ChatOpenAI
from composio_crewai import ComposioToolset, App

dotenv.load_dotenv()
llm = ChatOpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], model_name="gpt-4-turbo-preview")

composio_tool_set = ComposioToolset(apps=[App.GOOGLECALENDAR])

date = datetime.today().strftime('%Y-%m-%d')

timezone = datetime.now().astimezone().tzinfo
print(timezone)

todo = '''
    1PM - 3PM -> Code,
    5PM - 7PM -> Meeting,
    9AM - 12AM -> Learn soemthing
    8PM - 10PM -> Game
'''

def run_crew():
    gcal_agent = Agent(role='Google Calendar Agent',
                       goal="""You take action on Google Calendar using Google Calendar APIs""",
                       backstory="""You are AI agent that is responsible for taking actions on 
                                    Google Calendar on users behalf. You need to take action on 
                                    Calendar using Google Calendar APIs. Use Correct tools to run 
                                    apis from the given tool-set""",
                       verbose=True,
                       tools=composio_tool_set,
                       llm=llm)
    task = Task(
        description=f"book slots according to {todo}. Label them with the work provided to be done in that time period. Schedule it for today. Today's date is {date} (it's in YYYY-MM-DD format) and make the timezone be {timezone}.",
        agent=gcal_agent,
        expected_output="if free slot is found"
    )
    task.execute()
    return "Crew run initiated", 200

run_crew()