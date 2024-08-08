from crewai import Agent, Task, Crew, Process
from parallel_crew import crew1, crew2, crew3, crew4
import concurrent.futures

def kickoff_crew(crew, inputs):
    return crew.kickoff(inputs=inputs)

def process_question(question):
    
    architecture_type = question
    inputs = {'architecture_type': architecture_type}

    # Using ThreadPoolExecutor to run crews in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(kickoff_crew, crew1, inputs)
        future2 = executor.submit(kickoff_crew, crew2, inputs)
        future3 = executor.submit(kickoff_crew, crew3, inputs)

        result1 = future1.result()
        result2 = future2.result()
        result3 = future3.result()

    text = f"The Network architecture for the {architecture_type} is {result1} and the security assessment is {result2} and the CI/CD pipelines are {result3}"
    
    
    inputs = {
        'architecture_type': architecture_type,
        'text': text
    }

    result = crew4.kickoff(inputs=inputs)
    tokens_count = crew4.usage_metrics


    print("-----------------------------")
    print(result)
    print("-----------------------------")
    print(tokens_count)

    context = result

    inputs = {
        "question": f"{question}",
        "Context_js": f"{context}"
    }
    print("\n\n\n\n\n\nQuestion\n\n\n\n\n\n", inputs["question"])
    print("\n\n\n\n\n\nContext\n\n\n\\n\n\n\n",inputs["Context_js"])

    ques = inputs["question"]
    context = inputs["Context_js"]
    return ques, context

# question = """Design an architecture for a real-time data processing pipeline using Apache Kafka, Spark, and Elasticsearch."""
# process_question(question)