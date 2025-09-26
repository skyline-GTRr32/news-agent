import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool

# Load environment variables from .env file
load_dotenv()

# --- ENVIRONMENT SETUP ---
if not os.environ.get("GOOGLE_API_KEY") or not os.environ.get("SERPER_API_KEY"):
    print("ERROR: API keys not found in .env file.")
    exit()


# --- LLM CONFIGURATION (Final and Correct) ---
# Using your preferred generic LLM class with the most stable model name.
gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    temperature=0.7,
    api_key=os.environ.get("GOOGLE_API_KEY")
)


# --- TOOL INITIALIZATION ---
search_tool = SerperDevTool()


# =====================================================================
# === AGENT DEFINITION (Just One Agent) ===
# =====================================================================

# --- AI News Researcher Agent ---
researcher = Agent(
  role='Expert AI News Researcher',
  goal='Find and create a concise summary of the top 3 most recent and impactful AI news stories.',
  backstory="""You are an expert at sifting through AI news, identifying the most
  significant developments, and summarizing them clearly.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool],
  llm=gemini_llm
)


# =====================================================================
# === TASK DEFINITION (Just One Task) ===
# =====================================================================

# --- Research and Summarize Task ---
research_and_summarize_task = Task(
  description="""Search the web to find the top 3 most significant AI news stories from the
  past week. Then, write a concise summary report of what you found. The report
  should have a title and a paragraph for each of the three news stories.""",
  expected_output='A well-formatted summary report with a title and three paragraphs.',
  agent=researcher,
  output_file="single_agent_report.md" # The final output file
)


# =====================================================================
# === CREW DEFINITION AND KICKOFF ===
# =====================================================================

# Assemble the crew with our single agent and task
ai_report_crew = Crew(
  agents=[researcher],
  tasks=[research_and_summarize_task],
  process=Process.sequential,
  verbose=True
)

print("🚀 The Single-Agent Crew is ready to work!")
result = ai_report_crew.kickoff()

print("\n\n########################")
print("✅ Mission Accomplished!")
print("########################\n")
print("Here is the final report:")
print(result)
print("\nThe report has also been saved to 'single_agent_report.md'")
