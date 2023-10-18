from src.LLM.LLM import fake_chat


def code_fix(code: str) -> str:

    content,id = fake_chat('msg_user', 'msg_text', 'system', 0)
    return content
