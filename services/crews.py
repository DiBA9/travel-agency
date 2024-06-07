from typing import List
from sqlalchemy.orm import Session
from database.models import SessionLocal, CrewDetails
from database.crud import (
    create_crew,
    retrieve_crew_by_id,
    retrieve_crew_by_name,
    retrieve_all_crews,
    update_crew,
    delete_crew
)

def create_crew_record(name: str, description: str, created_at: str, updated_at: str, tasks: str, agents: str, 
                       process: str, verbose: str, manager_llm: str, function_calling_llm: str, config: dict, 
                       max_rpm: int, language: str, language_file: str, memory: str, cache: str, embedder: str, 
                       full_output: str, step_callback: str, task_callback: str, share_crew: str, 
                       output_log_file: str) -> CrewDetails:
    db: Session = SessionLocal()
    try:
        crew_details = CrewDetails(
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            tasks=tasks,
            agents=agents,
            process=process,
            verbose=verbose,
            manager_llm=manager_llm,
            function_calling_llm=function_calling_llm,
            config=config,
            max_rpm=max_rpm,
            language=language,
            language_file=language_file,
            memory=memory,
            cache=cache,
            embedder=embedder,
            full_output=full_output,
            step_callback=step_callback,
            task_callback=task_callback,
            share_crew=share_crew,
            output_log_file=output_log_file
        )
        return create_crew(db, crew_details)
    finally:
        db.close()

def retrieve_crew_by_id(crew_id: int) -> CrewDetails:
    db: Session = SessionLocal()
    try:
        return retrieve_crew_by_id(db, crew_id)
    finally:
        db.close()

def retrieve_crew_by_name(name: str) -> CrewDetails:
    db: Session = SessionLocal()
    try:
        return retrieve_crew_by_name(db, name)
    finally:
        db.close()

def retrieve_all_crew_records() -> List[CrewDetails]:
    db: Session = SessionLocal()
    try:
        return retrieve_all_crews(db)
    finally:
        db.close()

def update_crew_record(crew_id: int, crew_data: dict) -> CrewDetails:
    db: Session = SessionLocal()
    try:
        return update_crew(db, crew_id, crew_data)
    finally:
        db.close()

def delete_crew_record(crew_id: int) -> None:
    db: Session = SessionLocal()
    try:
        delete_crew(db, crew_id)
    finally:
        db.close()

