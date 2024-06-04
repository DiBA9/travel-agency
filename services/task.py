from sqlalchemy.orm import Session
from database.models import TaskDetails, SessionLocal
from database.crud import create_task, get_task_by_id, get_all_tasks, update_task, delete_task

def create_task_record(name: str, description: str, agent: str, expected_output: str, tools: str,
                       async_execution: bool, context: str, config: dict, output_json: bool,
                       output_pydantic: bool, output_file: str, callback: str, human_input: bool) -> TaskDetails:
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
            created_at=str(datetime.datetime.now())
        )
        created_task = create_task(db, task_details)
        return created_task
    finally:
        db.close()

def retrieve_task_by_id(task_id: int) -> TaskDetails:
    db: Session = SessionLocal()
    try:
        task = get_task_by_id(db, task_id)
        return task
    finally:
        db.close()

def retrieve_task_by_name(db: Session, name: str) -> TaskDetails:
    return db.query(TaskDetails).filter(TaskDetails.name == name).first()

def retrieve_all_tasks() -> list:
    db: Session = SessionLocal()
    try:
        tasks = get_all_tasks(db)
        return tasks
    finally:
        db.close()

def update_task_record(task_id: int, task_data: dict) -> TaskDetails:
    db: Session = SessionLocal()
    try:
        updated_task = update_task(db, task_id, task_data)
        return updated_task
    finally:
        db.close()

def delete_task_record(task_id: int) -> None:
    db: Session = SessionLocal()
    try:
        delete_task(db, task_id)
    finally:
        db.close()
