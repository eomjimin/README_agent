from llama_index.core.agent.workflow import ReActAgent
from llama_index.core.agent.react.formatter import ReActChatFormatter
from model import llm
from tools.write_readme_tool import write_readme
from prompts import WRITE_AGENT_SYSTEM_PROMPT

formatter = ReActChatFormatter.from_defaults(
    context=WRITE_AGENT_SYSTEM_PROMPT
)


write_agent = ReActAgent(
    name="WriteAgent",
    description="노트를 기반으로 구조화 된 README.md를 작성한다. 언어는 한국어로, 각 섹션 제목 앞에 적절한 이모지를 포함해서 작성. 🚀",
    tools=[write_readme],
    system_prompt=WRITE_AGENT_SYSTEM_PROMPT,
    formatter=formatter,
    llm=llm,
    can_handoff_to=["ReviewAgent"],
    finish_tool_name="write_readme"
)

print(write_agent.formatter)
