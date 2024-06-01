from textwrap import dedent
from services.agent import create_agent_record, retrieve_agent_by_role, update_agent_tools
from database.models import init_db

# Initialize the database
init_db()

# Create an agent
# created_agent = create_agent_record(
#     role="Local Tour Guide",
#     backstory="""
#         I am a knowledgeable local guide with extensive information about the city, it's attractions and customs.
#     """,
#     goal="""
#         Provide the best insights about a selected city.
#     """,
#     tools="SearchTools.search_internet",
#     llm_model_name="gpt-3.5-turbo",
#     llm_temperature=7
# )

# Update the tools for the created agent
# updated_agent = update_agent_tools("Expert Travel Agent", "SearchTools.search_internet,CalculatorTools.calculate")

# Retrieve the agent to confirm it was saved correctly
retrieved_agent = retrieve_agent_by_role("Expert Travel Agent")

# # Confirm the agent details
# print("Created Agent:")
# print(f"Role: {created_agent.role}")
# print(f"Backstory: {created_agent.backstory}")
# print(f"Goal: {created_agent.goal}")
# print(f"Tools: {created_agent.tools}")
# print(f"LLM Model Name: {created_agent.llm_model_name}")
# print(f"LLM Temperature: {created_agent.llm_temperature}")

print("\nRetrieved Agent:")
print(f"Role: {retrieved_agent.role}")
print(f"Backstory: {retrieved_agent.backstory}")
print(f"Goal: {retrieved_agent.goal}")
print(f"Tools: {retrieved_agent.tools}")
print(f"LLM Model Name: {retrieved_agent.llm_model_name}")
print(f"LLM Temperature: {retrieved_agent.llm_temperature}")