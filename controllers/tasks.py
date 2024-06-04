from crewai import Task
from textwrap import dedent
from database.models import SessionLocal, TaskDetails
from services.task import retrieve_task_by_name
from services.tool import load_tool

class TaskBase:
    def tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

#### Travel
class TravelTasks(TaskBase):
    def __init__(self):
        self.db = SessionLocal()

    def get_task(self, task_name, agent, **kwargs):
        # Fetch task details from the database
        task_details = retrieve_task_by_name(self.db, task_name)
        if not task_details:
            raise ValueError(f"Task '{task_name}' not found in the database.")

        # Include tip_section in the kwargs
        kwargs['tip_section'] = self.tip_section()

        # Construct the task description with provided parameters
        description = dedent(task_details.description.format(**kwargs))

        # Load tools as callable objects
        tools = [load_tool(tool.strip()) for tool in task_details.tools.split(',')]

        # Create and return the Task object
        return Task(
            name=task_details.name,
            description=description,
            agent=agent,
            expected_output=task_details.expected_output,
            tools=tools,
            async_execution=task_details.async_execution,
            context=task_details.context.split(',') if task_details.context else [],
            config=task_details.config,
            output_json=task_details.output_json,
            output_pydantic=task_details.output_pydantic,
            output_file=task_details.output_file,
            callback=task_details.callback,
            human_input=task_details.human_input,
        )

    def __del__(self):
        self.db.close()

# Example of another task class inheriting from TaskBase
class AnotherTaskClass(TaskBase):
    def __init__(self):
        self.db = SessionLocal()

    def get_another_task(self, task_name, agent, **kwargs):
        # Fetch task details from the database
        task_details = retrieve_task_by_name(self.db, task_name)
        if not task_details:
            raise ValueError(f"Task '{task_name}' not found in the database.")

        # Include tip_section in the kwargs
        kwargs['tip_section'] = self.tip_section()

        # Construct the task description with provided parameters
        description = dedent(task_details.description.format(**kwargs))

        # Create and return the Task object
        return Task(
            name=task_details.name,
            description=description,
            agent=agent,
            expected_output=task_details.expected_output,
            tools=[tool.strip() for tool in task_details.tools.split(',')],
            async_execution=task_details.async_execution,
            context=task_details.context.split(',') if task_details.context else [],
            config=task_details.config,
            output_json=task_details.output_json,
            output_pydantic=task_details.output_pydantic,
            output_file=task_details.output_file,
            callback=task_details.callback,
            human_input=task_details.human_input,
        )

    def __del__(self):
        self.db.close()
