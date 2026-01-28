import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv

class Config:
    ##API KEYS CONFIGURATIONS
    ANTHROPIC_API_KEY=os.getenv("ANTHROPIC_API_KEY")
    DEFAULT_MODEL=os.getenv("DEFAULT_MODEL", "claude-sonnet-4-20250514")
    DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", "0.7"))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "4096")))

    #PATH
    BASE_DIR=Path(__file__).parent.parent
    DATA_DIR=BASE_DIR/"data"
    CONVERSATION_DIR=DATA_DIR/"conversations"

    #ENSURE DIRECTORIES
    CONVERSATION_DIR.mkdir(parents=True, exsist_OK=True)


    @classmethod

    def validate(cls):
        if not cls.ANTHROPIC_API_KEY:
            raise ValueError ("Anthropic api key not found" \
            "Please set it in your env files")

        if not cls.ANTHROPIC_API_KEY.startswith("sk-ant")
            raise ValueError(
                "Invalid ANTHROPIC_API_KEY format. "
                "It should start with 'sk-ant-'"
            )

# Validate on import
Config.validate()
