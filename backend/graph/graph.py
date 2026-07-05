from langgraph.graph import StateGraph, END
from backend.graph.state import RecommendationState
from backend.graph.nodes import (
    profile_analyzer,
    retriever,
    recommendation_generator,
    validator,
)


def build_recommendation_graph():
    graph = StateGraph(RecommendationState)

    graph.add_node("profile_analyzer", profile_analyzer)
    graph.add_node("retriever", retriever)
    graph.add_node("recommendation_generator", recommendation_generator)
    graph.add_node("validator", validator)

    graph.set_entry_point("profile_analyzer")
    graph.add_edge("profile_analyzer", "retriever")
    graph.add_edge("retriever", "recommendation_generator")
    graph.add_edge("recommendation_generator", "validator")
    graph.add_edge("validator", END)

    return graph.compile()


recommendation_graph = build_recommendation_graph()