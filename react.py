from dotenv import load_dotenv
from langchain import hub
from langchain.agents import create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

prompt_template: PromptTemplate = hub.pull("hwchase17/react")
# print("hub_template==>", prompt_template) # Can be commented out if not needed


@tool
def triple(num: float) -> float:
    """Triple the input number.

    Args:
        num: The float number to be tripled
    Returns:
        float: The input number multiplied by 3
    """
    return num * 3


# Define the tools list (restore both tools)
agent_tools = [TavilySearchResults(max_results=1), triple]


# ---- Debugging Start ----
# You can remove or comment out this debug block once the issue is resolved
# print("\n--- Debugging agent_tools ---")
# print(f"agent_tools list object: {agent_tools}")
# if isinstance(agent_tools, list):
#     for i, item in enumerate(agent_tools):
#         item_type = type(item)
#         has_name = hasattr(item, 'name')
#         has_description = hasattr(item, 'description')
#         print(f"Item {i}: Type={item_type}, Has Name={has_name}, Has Description={has_description}")
#         if has_name:
#             print(f"  - Name: {getattr(item, 'name', 'N/A')}")
#         if has_description:
#             desc = getattr(item, 'description', 'N/A')
#             print(f"  - Description: {desc[:100] + '...' if len(desc) > 100 else desc}")
# else:
#     print(f"agent_tools is not a list, it is: {type(agent_tools)}")
# print("--- End Debugging ---\n")
# ---- Debugging End ----


llm = ChatOpenAI(model="gpt-4.1-nano-2025-04-14", temperature=0)

# Correct the argument order: llm, tools, prompt
reactable_agent = create_react_agent(llm, agent_tools, prompt_template)
