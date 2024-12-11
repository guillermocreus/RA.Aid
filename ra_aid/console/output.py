from typing import Any, Dict
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from langchain_core.messages import AIMessage

# Import shared console instance
from .formatting import console

def print_agent_output(chunk: Dict[str, Any]) -> None:
    """Print only the agent's message content, not tool calls.
    
    Args:
        chunk: A dictionary containing agent or tool messages
    """
    if 'agent' in chunk and 'messages' in chunk['agent']:
        messages = chunk['agent']['messages']
        for msg in messages:
            if isinstance(msg, AIMessage):
                # Handle text content
                if isinstance(msg.content, list):
                    for content in msg.content:
                        if content['type'] == 'text':
                            console.print(Panel(Markdown(content['text']), title="🤖 Assistant"))
                else:
                    console.print(Panel(Markdown(msg.content), title="🤖 Assistant"))