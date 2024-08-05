from crewai import Crew
from agents import architect, coder, validator
from tasks import task1, task2, task3

crew = Crew(
    agents=[architect, coder, validator],
    tasks=[task1, task2, task3], 
    verbose=2,
)