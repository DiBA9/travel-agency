import os
import sys
import pytest
import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base, AgentDetails, CrewDetails, TaskDetails, TripResults
from database.crud import *

# Create a new in-memory database for testing
@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()

# # Tests for AgentDetails
def test_create_agent(test_db):
    agent_details = AgentDetails(
        role='Test Agent',
        backstory='A test backstory',
        goal='A test goal',
        tools='tool1,tool2',
        llm_model_name='test_model',
        llm_temperature=0.7
    )
    created_agent = create_agent(test_db, agent_details)
    assert created_agent.role == 'Test Agent'

def test_read_agent_by_id(test_db):
    agent = read_agent_by_id(test_db, 1)
    assert agent is not None
    assert agent.role == 'Test Agent'

def test_read_agent_by_role(test_db):
    agent = read_agent_by_role(test_db, 'Test Agent')
    assert agent is not None
    assert agent.role == 'Test Agent'

def test_read_all_agents(test_db):
    agents = read_all_agents(test_db)
    assert len(agents) > 0

def test_update_agent(test_db):
    update_data = {
        'goal': 'An updated test goal'
    }
    updated_agent = update_agent(test_db, 1, update_data)
    assert updated_agent.goal == 'An updated test goal'

def test_delete_agent(test_db):
    delete_agent(test_db, 1)
    agent = read_agent_by_id(test_db, 1)
    assert agent is None

# Tests for CrewDetails
def test_create_crew(test_db):
    crew_details = CrewDetails(
        name='Test Crew',
        description='A test crew',
        created_at=datetime.datetime(2023, 1, 1),
        updated_at=datetime.datetime(2023, 1, 1),
        tasks='task1,task2',
        agents='agent1,agent2',
        process='test_process',
        verbose='test_verbose',
        manager_llm='test_manager_llm',
        function_calling_llm='test_function_calling_llm',
        config={},
        max_rpm=100,
        language='English',
        language_file='path/to/language/file',
        memory='test_memory',
        cache='test_cache',
        embedder='test_embedder',
        full_output='test_full_output',
        step_callback='test_step_callback',
        task_callback='test_task_callback',
        share_crew='test_share_crew',
        output_log_file='path/to/output/log/file'
    )
    created_crew = create_crew(test_db, crew_details)
    assert created_crew.name == 'Test Crew'

def test_read_crew_by_id(test_db):
    crew = read_crew_by_id(test_db, 1)
    assert crew is not None
    assert crew.name == 'Test Crew'

def test_read_crew_by_name(test_db):
    crew = read_crew_by_name(test_db, 'Test Crew')
    assert crew is not None
    assert crew.name == 'Test Crew'

def test_read_all_crews(test_db):
    crews = read_all_crews(test_db)
    assert len(crews) > 0

def test_update_crew(test_db):
    update_data = {
        'description': 'An updated test crew'
    }
    updated_crew = update_crew(test_db, 1, update_data)
    assert updated_crew.description == 'An updated test crew'

def test_delete_crew(test_db):
    delete_crew(test_db, 1)
    crew = read_crew_by_id(test_db, 1)
    assert crew is None

# Tests for TaskDetails
def test_create_task(test_db):
    task_details = TaskDetails(
        name='Test Task',
        description='A test task',
        agent='Test Agent',
        expected_output='Test output',
        tools='tool1,tool2',
        async_execution=False,
        context='context1,context2',
        config={},
        output_json=False,
        output_pydantic=False,
        output_file='path/to/output/file',
        callback='test_callback',
        human_input=False,
        created_at=datetime.datetime(2023, 1, 1),
        updated_at=datetime.datetime(2023, 1, 1)
    )
    created_task = create_task(test_db, task_details)
    assert created_task.name == 'Test Task'

def test_read_task_by_id(test_db):
    task = read_task_by_id(test_db, 1)
    assert task is not None
    assert task.name == 'Test Task'

def test_read_task_by_name(test_db):
    task = read_task_by_name(test_db, 'Test Task')
    assert task is not None
    assert task.name == 'Test Task'

def test_read_all_tasks(test_db):
    tasks = read_all_tasks(test_db)
    assert len(tasks) > 0

def test_update_task(test_db):
    update_data = {
        'description': 'An updated test task'
    }
    updated_task = update_task(test_db, 1, update_data)
    assert updated_task.description == 'An updated test task'

def test_delete_task(test_db):
    delete_task(test_db, 1)
    task = read_task_by_id(test_db, 1)
    assert task is None

# Tests for TripResults
def test_create_trip_results(test_db):
    trip_results = TripResults(
        origin='Test Origin',
        cities='City1,City2',
        travel_dates='2023-01-01 to 2023-01-10',
        interests='Interest1,Interest2',
        result='Test result'
    )
    created_trip_results = create_trip_results(test_db, trip_results)
    assert created_trip_results.origin == 'Test Origin'

def test_read_trip_results_by_id(test_db):
    trip_results = read_trip_results_by_id(test_db, 1)
    assert trip_results is not None
    assert trip_results.origin == 'Test Origin'

def test_read_trip_results_by_origin(test_db):
    trip_results = read_trip_results_by_origin(test_db, 'Test Origin')
    assert trip_results is not None
    assert trip_results.origin == 'Test Origin'

def test_read_all_trip_results(test_db):
    trip_results = read_all_trip_results(test_db)
    assert len(trip_results) > 0

def test_update_trip_results(test_db):
    update_data = {
        'result': 'An updated test result'
    }
    updated_trip_results = update_trip_results(test_db, 1, update_data)
    assert updated_trip_results.result == 'An updated test result'

def test_delete_trip_results(test_db):
    delete_trip_results(test_db, 1)
    trip_results = read_trip_results_by_id(test_db, 1)
    assert trip_results is None