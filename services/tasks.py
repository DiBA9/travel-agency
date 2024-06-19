from typing import List
from sqlalchemy.orm import Session
from database.models import SessionLocal, TaskDetails
from database.crud import (
    create_task,
    read_task_by_id,
    read_task_by_name,
    read_all_tasks,
    update_task,
    delete_task
)

def create_task_record(name: str, description: str, agent: str, expected_output: str, tools: str, 
                       async_execution: bool, context: str, config: dict, output_json: bool, 
                       output_pydantic: bool, output_file: str, callback: str, human_input: bool, 
                       created_at: str, updated_at: str) -> TaskDetails:
    db: Session = SessionLocal()
    try:
        task_details = TaskDetails(
            name=name,
            description=description,
            agent=agent,
            expected_output=expected_output,
            tools=tools,
            async_execution=async_execution,
            context=context,
            config=config,
            output_json=output_json,
            output_pydantic=output_pydantic,
            output_file=output_file,
            callback=callback,
            human_input=human_input,
            created_at=created_at,
            updated_at=updated_at
        )
        return create_task(db, task_details)
    finally:
        db.close()

def retrieve_task_by_id(task_id: int) -> TaskDetails:
    db: Session = SessionLocal()
    try:
        return read_task_by_id(db, task_id)
    finally:
        db.close()

def retrieve_task_by_name(name: str) -> TaskDetails:
    db: Session = SessionLocal()
    try:
        return read_task_by_name(db, name)
    finally:
        db.close()

def retrieve_all_tasks() -> List[TaskDetails]:
    db: Session = SessionLocal()
    try:
        return read_all_tasks(db)
    finally:
        db.close()

def update_task_record(task_id: int, task_data: dict) -> TaskDetails:
    db: Session = SessionLocal()
    try:
        return update_task(db, task_id, task_data)
    finally:
        db.close()

def delete_task_record(task_id: int) -> None:
    db: Session = SessionLocal()
    try:
        delete_task(db, task_id)
    finally:
        db.close()

