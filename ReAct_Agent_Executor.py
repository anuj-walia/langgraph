from dotenv import load_dotenv
load_dotenv()

from langchain_core.agents import AgentFinish
from langgraph.graph import END, StateGraph


from nodes import run_agent_reasoning_engine, run_tool_executor
from state import AgentState
from langchain_core.runnables.graph import MermaidDrawMethod


AGENT_REASON="agent_reason"
ACT="act"

def should_continue(data):
    if isinstance(data["agent_outcome"],AgentFinish):
        return END
    return ACT

flow=StateGraph(AgentState)
flow.add_node(AGENT_REASON,run_agent_reasoning_engine)
flow.add_node(ACT,run_tool_executor)
flow.set_entry_point(AGENT_REASON)
flow.add_conditional_edges(AGENT_REASON,should_continue)
flow.add_edge(ACT,AGENT_REASON)
app=flow.compile()
app.get_graph().print_ascii()
print(app.get_graph().draw_mermaid())
# app.get_graph().draw_mermaid_png(
#     output_file_path="./React_Agent_Executor_Mermaid.png",
#     # draw_method=MermaidDrawMethod.PYPPETEER
# )
#
# app.get_graph().draw_png(output_file_path="./React_Agent_Executor.png")
if __name__=="__main__":
    print("Hello LangGraph")
    res = app.invoke(
        input={
            "input": "I am male 40 year s of age. What is the weather in brampton, Ontario tomorrow ? Suggest me what to wear based on weather. ",
        }
    )
    print(res["agent_outcome"].return_values["output"])