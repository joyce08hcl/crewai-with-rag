from crewai import Agent
from llm import model
from textwrap import dedent
from tools import search_tool, code_tool, csv_tool


architect = Agent(
        role = "Architect",
        goal=dedent("""Based on the user input of flow charts, network architectures, mind maps etc. Write a detailed description on what are the different components, how they are connected, according to the best practices. Additionally use the tools for better and accurate information"""),
        verbose = True,
        allow_delegation=False,
        llm=model,
        backstory=dedent("""You are an expert architect that explains in detail the workflow of complex network architectures and flow charts"""),
        tools=[
            search_tool
        ],
    
)


coder = Agent(
        role = "Coder",
        goal = dedent("""You are a helpful AI assistant who generates D2 code for diagrams based on user input. Your task is to convert the user's natural language description of a diagram into valid D2 lang code. Additionally use the tools provided for better D2 lang code generation"""),
        verbose = True,
        allow_delegation=False,
        llm=model,
        backstory = dedent("""You are an expert coder that can write D2 lang code fron any description so that the code can be used by the user to generate diagrams."""),
        tools=[
            # git_tool,
            code_tool,
            csv_tool
      ],
)

validator = Agent(
        role = "Validator",
        goal = dedent("""Find any issues or errors, provide detailed feedback and suggestions for the code generated. If the code is correct, approve it."""),
        verbose = True,
        allow_delegation=False,
        llm=model,
        allow_code_execution=True,
        backstory = dedent("""You are a validator who reviews the D2 code generated for creating diagrams and executes it to check for errors. Your task is to check the code for correctness, completeness, and adherence to the D2 lang library standards."""),
        tools=[
        code_tool
        ]
)