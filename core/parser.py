import json
from llm.client import ask_llm

SYSTEM_PROMPT = """
You are an assistant converting user commands into JSON actions.

Return ONLY valid JSON:

{
  "action": "",
  "target": "",
  "parameters": ""
}

Examples:
open chrome
-> {"action":"open_app","target":"chrome","parameters":""}

delete file test.txt
-> {"action":"delete_file","target":"test.txt","parameters":""}
"""

def parse_command(command: str):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": command}
    ]

    result = ask_llm(messages)
    try:
        return json.loads(result)

    except json.JSONDecodeError as e:
        print("Error parsing JSON:", e)
        return None
    
