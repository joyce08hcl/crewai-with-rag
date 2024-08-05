from crewai_tools import CodeDocsSearchTool, CSVSearchTool
from langchain_community.tools import DuckDuckGoSearchResults
from langchain.agents import Tool


search = DuckDuckGoSearchResults()

search_tool = Tool(
  name="Search tool",
  func=search.run,
  description="Useful for search-based queries",
)

code_tool = CodeDocsSearchTool(docs_url='https://d2lang.com/tour/')

csv_tool = CSVSearchTool(csv='/home/jovyan/crewai with rag/d2lang_data.csv')

