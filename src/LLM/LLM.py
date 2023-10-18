import json
import logging as log
import requests

from flask import jsonify

from src.LLM import config

_log = log.getLogger(__name__)


def chat(msg_user: str, msg_text: str, system='', conv_id=None):
    new_conv_id = None
    msg_content = None

    _log.info('Begin chat: %s', msg_text)

    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'engine': 'gpt-35-turbo-0301',
        'temperature': 0,
        'maxTokens': 1000,
        'topP': 0,
        'system': system,
        'message': {
            'user': msg_user,
            'text': msg_text
        }
    }
    chat_url = f'{config.llm_server}/api/chat/{conv_id}' if conv_id is not None else f'{config.llm_server}/api/chat'
    resp = requests.post(chat_url, headers=headers, json=payload)
    if resp.status_code == 200:
        resp_json = resp.json()
        new_conv_id = resp_json['id']
        msg_content = resp_json['content']
        _log.info('Chat reply: %s', msg_content)
    else:
        _log.error('Fail to chat with field_mapping: %r', resp)

    _log.info('End chat: %s', msg_text)
    return msg_content, new_conv_id


def fake_chat(msg_user: str, msg_text: str, system='', conv_id=None):
    new_conv_id = None
    msg_content = None

    _log.info('Begin chat: %s', msg_text)

    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'engine': 'gpt-35-turbo-0301',
        'temperature': 0,
        'maxTokens': 1000,
        'topP': 0,
        'system': system,
        'message': {
            'user': msg_user,
            'text': msg_text
        }
    }
    chat_url = f'{config.llm_server}/api/chat/{conv_id}' if conv_id is not None else f'{config.llm_server}/api/chat'
    resp = {
        'id': 'this is the fake conversation id',
        'content': 'this is the fake conversation content'
    }
    new_conv_id = resp['id']
    msg_content = resp['content']
    _log.info('Chat reply: %s', msg_content)
    _log.info('End chat: %s', msg_text)
    return msg_content, new_conv_id
