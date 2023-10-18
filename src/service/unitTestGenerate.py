from src.LLM.LLM import fake_chat


def unit_test_generate(code: str) -> str:

    content,id = fake_chat('msg_user', 'msg_text', 'system', 0)
    return content
