from crewai import Crew

def crew_func(architect, coder, validator, task1, task2, task3):
    agent_crew = Crew(
        agents=[architect, coder, validator],
        tasks=[task1, task2, task3], 
        verbose=2,
        memory = True,
        embedder={
                "provider": "openai",

                "config":{

                        "api_key":"sk-1234",
                        "model": 'text-embedding-ada-002'
                }
        }
    )
    result = agent_crew.kickoff()
    tokens_count = agent_crew.usage_metrics

    print("-----------------------------")
    print(result)
    print("-----------------------------")
    print(tokens_count)
    return result