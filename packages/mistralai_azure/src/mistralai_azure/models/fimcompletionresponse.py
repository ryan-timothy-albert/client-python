"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .chatcompletionchoice import ChatCompletionChoice, ChatCompletionChoiceTypedDict
from .usageinfo import UsageInfo, UsageInfoTypedDict
from mistralai_azure.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class FIMCompletionResponseTypedDict(TypedDict):
    id: str
    object: str
    model: str
    usage: UsageInfoTypedDict
    created: NotRequired[int]
    choices: NotRequired[List[ChatCompletionChoiceTypedDict]]
    

class FIMCompletionResponse(BaseModel):
    id: str
    object: str
    model: str
    usage: UsageInfo
    created: Optional[int] = None
    choices: Optional[List[ChatCompletionChoice]] = None
    
