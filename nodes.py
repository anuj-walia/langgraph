from dotenv import load_dotenv
from langgraph.prebuilt.tool_executor import ToolExecutor
# Import the renamed variable 'agent_tools'
from react import reactable_agent, agent_tools
from state import AgentState
from langchain_openai import ChatOpenAI # This import seems unused here, consider removing if not needed elsewhere in the file.
load_dotenv()

def run_agent_reasoning_engine(state: AgentState):
    # The reactable_agent invocation expects the full state dictionary.
    agent_outcome = reactable_agent.invoke(state)
    return {"agent_outcome": agent_outcome}

# Use the renamed variable 'agent_tools'
tool_executor = ToolExecutor(agent_tools)

def run_tool_executor(state: AgentState):
    # agent_outcome should contain an AgentAction or AgentFinish.
    # We expect an AgentAction here based on the graph flow.
    agent_action = state["agent_outcome"]
    # Ensure agent_action is not AgentFinish before proceeding if necessary,
    # although the graph logic should handle this.
    tool_outcome = tool_executor.invoke(agent_action)
    # intermediate_steps typically expects a list of tuples: (AgentAction, observation)
    return {"intermediate_steps": [(agent_action, str(tool_outcome))]}
