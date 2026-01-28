import json
from datetime import datetime
from pathlib import Path
from typing import Dict,List,Optional


def generate_conversation_id()->str:
    #Unique id generated based on timestamp
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def format_timestamp(timestamp:Optional[str]=None)->str:
    if timestamp is  None:
        timestamp=datetime.now().isoformat()

    dt=datetime.fromisoformat(timestamp)
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def truncate_text(text:str,max_length=50) -> str:
    if len(text)<=max_length:
        return text
    return text[:max_length-3] + "..."

def save_json(data:Dict,filepath:Path) -> None:
    with open(filepath, 'w' , encoding='utf-8') as f:
        json.dump(data,f,indent=2,ensure_ascii=False)

def load_json(filepath: Path) -> Dict:
    """Load JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def list_conversation_files(conversations_dir: Path) -> List[Path]:
    """List all conversation JSON files."""
    return sorted(conversations_dir.glob("*.json"), reverse=True)


