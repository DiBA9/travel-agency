import os
import sys
import datetime
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.models import Base, AgentDetails, CrewDetails, TaskDetails, TripResults
from services.agents import (
    create_agent_record, 
    retrieve_agent_by_id, 
    retrieve_agent_by_role, 
    retrieve_all_agents, 
    update_agent_record, 
    delete_agent_record
)
from services.crews import (
    create_crew_record, 
    retrieve_crew_by_id, 
    retrieve_crew_by_name, 
    retrieve_all_crews, 
    update_crew_record, 
    delete_crew_record
)
from services.tasks import(
    create_task_record, 
    retrieve_task_by_id, 
    retrieve_task_by_name, 
    retrieve_all_tasks, 
    update_task_record, 
    delete_task_record    
)
from services.trips import(
    create_trip_record, 
    retrieve_trip_by_id, 
    retrieve_trip_by_origin, 
    retrieve_all_trips, 
    update_trip_record, 
    delete_trip_record    
)
from config import DATABASE_URL

# Set up the SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope='session')
def test_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope='module')
def cleanup_db(test_db):
    created_ids = {
        'agent': [],
        'crew': [],
        'task': [],
        'trip': []
    }
    yield created_ids
    # Cleanup logic for agents
    if created_ids['agent']:
        test_db.query(AgentDetails).filter(AgentDetails.id.in_(created_ids['agent'])).delete(synchronize_session=False)
        test_db.commit()
    # Cleanup logic for crews
    if created_ids['crew']:
        test_db.query(CrewDetails).filter(CrewDetails.id.in_(created_ids['crew'])).delete(synchronize_session=False)
        test_db.commit()
    # Cleanup logic for tasks
    if created_ids['task']:
        test_db.query(TaskDetails).filter(TaskDetails.id.in_(created_ids['task'])).delete(synchronize_session=False)
        test_db.commit()
    # Cleanup logic for trips
    if created_ids['trip']:
        test_db.query(TripResults).filter(TripResults.id.in_(created_ids['trip'])).delete(synchronize_session=False)
        test_db.commit()

# Helper function to add created IDs to cleanup list
def track_created_ids(created_ids, instance, model_type):
    created_ids[model_type].append(instance.id)

# Tests for AgentDetails
def test_create_agent_record(cleanup_db):
    role = 'Test Role'
    backstory = 'Test Backstory'
    goal = 'Test Goal'
    tools = 'Test Tools'
    llm_model_name = 'Test Model'
    llm_temperature = 0.5
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    created_agent = create_agent_record(role, backstory, goal, tools, llm_model_name, llm_temperature, created_at, updated_at)
    track_created_ids(cleanup_db, created_agent, 'agent')
    assert created_agent.role == role

def test_retrieve_agent_by_id(cleanup_db):
    agent_id = cleanup_db['agent'][0]  # Get the first (and only) created agent ID
    agent = retrieve_agent_by_id(agent_id)
    assert agent.role == 'Test Role'

def test_retrieve_agent_by_role(cleanup_db):
    agent = retrieve_agent_by_role('Test Role')
    assert agent.goal == 'Test Goal'

def test_retrieve_all_agents():
    agents = retrieve_all_agents()
    assert len(agents) > 0

def test_update_agent_record(cleanup_db):
    agent_id = cleanup_db['agent'][0]  # Get the first (and only) created agent ID
    agent_data = dict(
        role = 'Test Role',
        backstory = 'Updated Backstory',
        goal = 'Updated Goal',
        tools = 'Updated Tools',
        llm_model_name = 'Updated Model',
        llm_temperature = 0.7,
        updated_at = datetime.datetime.now()
    )
    updated_agent = update_agent_record(agent_id, agent_data)
    assert updated_agent.goal == agent_data.get('goal')

def test_delete_agent_record(cleanup_db):
    agent_id = cleanup_db['agent'][0]  # Get the first (and only) created agent ID
    delete_agent_record(agent_id)
    agent = retrieve_agent_by_id(agent_id)
    assert agent is None

# Tests for CrewDetails
def test_create_crew_record(cleanup_db):
    name = 'Test Crew'
    description = 'Test Description'
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    tasks = 'task1,task2'
    agents = 'agent1,agent2'
    process = None
    verbose = 'True'
    manager_llm = None
    function_calling_llm = None
    config = None
    max_rpm = None
    language = None
    language_file = None
    memory = None
    cache = None
    embedder = None
    full_output = None
    step_callback = None
    task_callback = None
    share_crew = None
    output_log_file = None
    created_crew = create_crew_record(name, description, created_at, updated_at, tasks, agents, 
        process, verbose, manager_llm, function_calling_llm, config, max_rpm, language, language_file,
        memory, cache, embedder, full_output, step_callback, task_callback, share_crew, output_log_file
    )
    track_created_ids(cleanup_db, created_crew, 'crew')
    assert created_crew.name == name

def test_retrieve_crew_by_id(cleanup_db):
    crew_id = cleanup_db['crew'][0]  # Get the first (and only) created crew ID
    crew = retrieve_crew_by_id(crew_id)
    assert crew.name == 'Test Crew'

def test_retrieve_crew_by_name(cleanup_db):
    crew = retrieve_crew_by_name('Test Crew')
    assert crew.description == 'Test Description'

def test_retrieve_all_crews():
    crews = retrieve_all_crews()
    assert len(crews) > 0

def test_update_crew_record(cleanup_db):
    crew_id = cleanup_db['crew'][0]  # Get the first (and only) created crew ID
    crew_data = dict(name = 'Updated Crew',
        description = 'Updated Description',
        created_at = datetime.datetime.now(),
        updated_at = datetime.datetime.now(),
        tasks = 'task3,task4',
        agents = 'agent3,agent4',
        process = None,
        verbose = 'True',
        manager_llm = None,
        function_calling_llm = None,
        config = None,
        max_rpm = None,
        language = None,
        language_file = None,
        memory = None,
        cache = None,
        embedder = None,
        full_output = None,
        step_callback = None,
        task_callback = None,
        share_crew = None,
        output_log_file = None
    )
    updated_crew = update_crew_record(crew_id, crew_data)
    assert updated_crew.description == crew_data.get('description')

def test_delete_crew_record(cleanup_db):
    crew_id = cleanup_db['crew'][0]  # Get the first (and only) created crew ID
    delete_crew_record(crew_id)
    crew = retrieve_crew_by_id(crew_id)
    assert crew is None

# Tests for TaskDetails
def test_create_task_record(cleanup_db):
    name = 'Test Task'
    description = 'Test Description'
    agent = 'agent1'
    expected_output = 'What good looks like.'
    tools = 'tool1,tool2'
    async_execution = False
    context = None
    config = None
    output_json = None
    output_pydantic = False
    output_file = None
    callback = None
    human_input = False
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    created_task = create_task_record(name, description, agent, expected_output, tools, async_execution, context,
        config, output_json, output_pydantic, output_file, callback, human_input, created_at, updated_at
    )
    track_created_ids(cleanup_db, created_task, 'task')
    assert created_task.name == name

def test_retrieve_task_by_id(cleanup_db):
    task_id = cleanup_db['task'][0]  # Get the first (and only) created task ID
    task = retrieve_task_by_id(task_id)
    assert task.name == 'Test Task'

def test_retrieve_task_by_name(cleanup_db):
    task = retrieve_task_by_name('Test Task')
    assert task.description == 'Test Description'

def test_retrieve_all_tasks():
    tasks = retrieve_all_tasks()
    assert len(tasks) > 0

def test_update_task_record(cleanup_db):
    task_id = cleanup_db['task'][0]  # Get the first (and only) created task ID
    task_data = dict(name = 'Updated Task',
        description = 'Updated Description',
        agent = 'agent2',
        expected_output = 'What updated good looks like.',
        tools = 'tool3,tool4',
        async_execution = None,
        context = None,
        output_json = None,
        output_pydantic = None,
        output_file = None,
        callback = None,
        human_input = False,
        created_at = datetime.datetime.now(),
        updated_at = datetime.datetime.now()
    )
    updated_task = update_task_record(task_id, task_data)
    assert updated_task.description == task_data.get('description')

def test_delete_task_record(cleanup_db):
    task_id = cleanup_db['task'][0]  # Get the first (and only) created task ID
    delete_task_record(task_id)
    task = retrieve_task_by_id(task_id)
    assert task is None

# Tests for Tripetails
def test_create_trip_record(cleanup_db):
    origin = 'Test Origin'
    cities = 'Test City'
    travel_dates = '2025/06/01,2025/07/01'
    interests = 'Test Interest'
    result = 'Test Result'
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    created_trip = create_trip_record(origin, cities, travel_dates, 
        interests, result, created_at, updated_at
    )
    track_created_ids(cleanup_db, created_trip, 'trip')
    assert created_trip.origin == origin

def test_retrieve_trip_by_id(cleanup_db):
    trip_id = cleanup_db['trip'][0]  # Get the first (and only) created trip ID
    trip = retrieve_trip_by_id(trip_id)
    assert trip.origin == 'Test Origin'

def test_retrieve_trip_by_origin(cleanup_db):
    trip = retrieve_trip_by_origin('Test Origin')
    assert trip.interests == 'Test Interest'

def test_retrieve_all_trips():
    trips = retrieve_all_trips()
    assert len(trips) > 0

def test_update_trip_record(cleanup_db):
    trip_id = cleanup_db['trip'][0]  # Get the first (and only) created trip ID
    trip_data = dict(
        origin = 'Test Origin',
        cities = 'Test City',
        travel_dates = '2025/06/01,2025/07/01',
        interests = 'Test Interests',
        result = 'Test Result',
        created_at = datetime.datetime.now(),
        updated_at = datetime.datetime.now()
    )
    updated_trip = update_trip_record(trip_id, trip_data)
    assert updated_trip.interests == trip_data.get('interests')

def test_delete_trip_record(cleanup_db):
    trip_id = cleanup_db['trip'][0]  # Get the first (and only) created trip ID
    delete_trip_record(trip_id)
    trip = retrieve_trip_by_id(trip_id)
    assert trip is None