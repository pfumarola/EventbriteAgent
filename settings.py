from pydantic import BaseModel
from cat.mad_hatter.decorators import plugin

class EventbriteAgentSettings(BaseModel):
    token: str

@plugin
def settings_model():
    return EventbriteAgentSettings