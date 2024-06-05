from crewai import Task
from textwrap import dedent
from database.models import SessionLocal, TaskDetails
from services.task import (
    retrieve_task_by_id, 
    retrieve_task_by_name, 
    retrieve_all_tasks, 
    create_task_record, 
    update_task_record, 
    delete_task_record
)
from controllers.tools import load_tool

class TaskBase:
    def tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

class TravelTasks(TaskBase):
    def __init__(self):
        self.db = SessionLocal()

    def get_task_by_name(self, task_name, agent, **kwargs):
        task_details = retrieve_task_by_name(task_name)
        if not task_details:
            raise ValueError(f"Task '{task_name}' not found in the database.")
        
        kwargs['tip_section'] = self.tip_section()
        description = dedent(task_details.description.format(**kwargs))
        tools = [load_tool(tool.strip()) for tool in task_details.tools.split(',')]

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
        task_details = retrieve_task_by_id(task_name)
        if not task_details:
            raise ValueError(f"Task '{task_name}' not found in the database.")
        
        kwargs['tip_section'] = self.tip_section()
        description = dedent(task_details.description.format(**kwargs))
        tools = [load_tool(tool.strip()) for tool in task_details.tools.split(',')]

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
