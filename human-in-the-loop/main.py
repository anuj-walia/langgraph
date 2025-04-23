from typing import TypedDict
from langgraph.graph import StateGraph,END
from langgraph.checkpoint.memory import MemorySaver

class State(TypedDict):
    input: str
    user_feedback: str


def step1(state: State):
    print(f"Step 1: --> state ==> {state['input']}")

def human_feedback(state: State):
    print(f"human step: --> state ==> {state['input']}")


def step3(state: State):
    print(f"step3 --> state ==>: {state['input']}")

builder=StateGraph(State)
builder.add_node("step1",step1)
builder.add_node("human_feedback",human_feedback)
builder.add_node("step3",step3)
builder.add_edge("step1","human_feedback")
builder.add_edge("human_feedback","step3")
builder.add_edge("step3",END)
builder.set_entry_point("step1")
memory=MemorySaver()
app=builder.compile(checkpointer=memory,interrupt_before=["human_feedback"])

app.get_graph().draw_png(output_file_path="human_in_the_loop.png")

if __name__=="__main__":
    #run th graph with human in the loop interruption
    app.invoke(input={"input":"Hello LangGraph"})
    app.next_step()