from crewai import Crew

def crew_func(coder, task2):
    agent_crew = Crew(
        agents=[coder],
        tasks=[task2], 
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