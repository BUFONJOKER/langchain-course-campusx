from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template='''
    Role: You are a ai research paper assistant.
    Task: Summarize the {research_paper} research paper.
    Constraint: explain the research paper with more {paper_style} way.

    Expected Output:
    1 - core idea of the research paper
    2 - problems it solves
    3 - real world applications
    ''', input_variables=["research_paper", "paper_style"]
)

template.save("prompt_template.json")