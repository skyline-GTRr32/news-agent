import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

# Load environment variables from .env file
load_dotenv()

# --- ENVIRONMENT SETUP ---
if not os.environ.get("GOOGLE_API_KEY"):
    print("ERROR: GOOGLE_API_KEY not found in .env file.")
    exit()


# --- LLM CONFIGURATION (Final and Correct) ---
# NOTE: The model name has been corrected to 'gemini-pro'.
# 'gemini-2.5-flash' is not a valid model name and will cause an error.
gemini_llm = LLM(
    model="gemini/gemini-p2.5-ro",
    temperature=0.7,
    api_key=os.environ.get("GOOGLE_API_KEY")
)


# =====================================================================
# === AGENT DEFINITION (Technical Writer) ===
# =====================================================================

# --- Technical Writer Agent ---
writer_agent = Agent(
  role='Expert Technical Writer',
  goal='Create a comprehensive and professional README.md file and a short, engaging project description.',
  backstory="""You are a renowned technical writer with a talent for creating compelling
  documentation for software projects. You are an expert in Markdown and know how
  to structure a README file to be both informative and welcoming to new users
  and potential contributors.""",
  verbose=True,
  allow_delegation=False,
  llm=gemini_llm
)


# =====================================================================
# === TASK DEFINITION (Generate README) ===
# =====================================================================

# --- Get User Input for the Project ---
print("--- README and Description Generator ---")
project_idea = input("Please describe your project. What is its main purpose and features?\n> ")

if not project_idea:
    print("Project description cannot be empty. Exiting.")
    exit()

# --- README Generation Task ---
readme_task = Task(
  description=f"""
  Based on the following project idea, create two distinct pieces of content:
  1. A complete and professional README.md file using Markdown.
  2. A short, one-sentence project description suitable for a GitHub repository.

  The README.md file must be well-structured and include the following sections:
  - A catchy Project Title.
  - A 'Description' section that expands on the user's idea.
  - A 'Key Features' section with a bulleted list of 3-5 hypothetical features.
  - A 'Getting Started' section with placeholder instructions for 'Installation' and 'Usage'.
  - A brief, standard 'Contributing' section.

  Here is the user's project idea:
  ---
  {project_idea}
  ---

  Your final output must contain the full README.md content first, followed by a clear separator
  like '--- short project description ---', and then the one-sentence description.
  """,
  expected_output='The full Markdown content for the README.md file, a separator, and then the one-sentence project description.',
  agent=writer_agent,
  output_file="README.md" # The main output will be saved here
)


# =====================================================================
# === CREW DEFINITION AND KICKOFF ===
# =====================================================================

# Assemble the crew with our single agent and task
readme_crew = Crew(
  agents=[writer_agent],
  tasks=[readme_task],
  process=Process.sequential,
  verbose=True
)

print("\n🚀 The Documentation Crew is ready to work!")
result = readme_crew.kickoff()

print("\n\n########################")
print("✅ Mission Accomplished!")
print("########################\n")
print("The full output (including the short description) is saved in README.md")
print("\nHere is the generated content:")
print(result)