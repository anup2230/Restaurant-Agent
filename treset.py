from fastapi import Response
import os
import vocode
from vocode.streaming.telephony.hosted.inbound_call_server import InboundCallServer
from vocode.streaming.models.agent import ChatGPTAgentConfig
from vocode.streaming.agent.chat_gpt_agent import ChatGPTAgent
from vocode.streaming.models.agent import EchoAgentConfig
from vocode.streaming.models.message import BaseMessage
from vocode.streaming.models.telephony import TwilioConfig

vocode.api_key = "ce4e08a06a670d590af69d82a022f4f6"

vocode.setenv(
    OPENAI_API_KEY="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",
    DEEPGRAM_API_KEY="2831b98dff178ebfd92537c96c369ba008d0dc44",
    AZURE_SPEECH_KEY="95226e3c78304389ba09455f7e9b9b81",
    AZURE_SPEECH_REGION="eastus",
)



agent_config=EchoAgentConfig(initial_message=BaseMessage(text="hello!"))

agent=ChatGPTAgent(
            ChatGPTAgentConfig(
                initial_message=BaseMessage(text="Hello!"),
                prompt_preamble="Have a pleasant conversation about life",
            )
)
