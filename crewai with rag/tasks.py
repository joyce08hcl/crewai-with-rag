from crewai import Task
from textwrap import dedent
from config import documentation


def tasks_func(user_input, diagram_language, d2_examples, architect, coder, validator):

    task1 = Task(
        description=dedent(f"""
            1. Write a detailed description of the following architecture so that the coder can easily write code based on your description: {user_input}
            2. Additionally use the tools to write accurate and detailed description of the user query and information about all possible related components and how they are connected. 
            3. if you are going to use Search tool replace the search positional argument: to 'search_query'
            4. Write your final description of the user input based on all the data collected.
        """),
        expected_output="Detailed description of cloud architecture or flow diagram of the user input",
        agent=architect,
    )

    task2 = Task(
        description=dedent(f"""
        1. Based on the detailed description of the flow chart or network architecture, write correct {diagram_language} code of the description.
        2. Additionally use the below documentation to write accurate {diagram_language} code and enhance the code with different shapes, connectors, icons, colors etc.
        4. Write your final {diagram_language} code based on all the data collected.
        Documentation:{documentation}
        5. Based on the details, use subgraph to denote related components if applicable. Generate the code for an elaborate diagram based on the description.
        6. Refer to the following examples and the final structure and syntax of the {diagram_language} code generated should follow the examples and the data collected from the tools. Include each and every component provided in the description.
            {d2_examples}
        """),
        expected_output=f"{diagram_language} code corresponding to the {user_input}, accurately representing the flowchart or network architecture. The final answer should have the same structure as the provided examples",
        agent=coder,
        context=[task1],
    )

    task3 = Task(
        description=dedent(f"""
        1. Based on the code generated validate if the code is correct and syntactically accurate for {diagram_language}.
        2. If yes approve the code otherwise provide relevant corrections.
        3. All the important components should be named properly and the relationship between these components should also be well illustrated.
        4. Additionally use the tools to check whether the generated code is correct and has no errors including syntax, structure etc.
        5. if you are going to use Code Docs content tool replace the search positional argument: to 'search_query'
        6. Provide your final answer whether  any changes has to be made in the code generated or not based on all the data collected.
        7. The final answer should be in the format ```(the final answer)```.
        """),
        expected_output="Details on whether the code generated is valid or not. Specify the reason too. Final answer should be the correct diagram language code.",
        agent=validator,
        context=[task2],
    )
    return task1, task2, task3
