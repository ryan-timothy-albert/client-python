"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mistralai_azure.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional, TypedDict, Union
from typing_extensions import NotRequired


FIMCompletionRequestStopTypedDict = Union[str, List[str]]
r"""Stop generation if this token is detected. Or if one of these tokens is detected when providing an array"""


FIMCompletionRequestStop = Union[str, List[str]]
r"""Stop generation if this token is detected. Or if one of these tokens is detected when providing an array"""


class FIMCompletionRequestTypedDict(TypedDict):
    model: Nullable[str]
    r"""ID of the model to use. Only compatible for now with:
    - `codestral-2405`
    - `codestral-latest`
    """
    prompt: str
    r"""The text/code to complete."""
    temperature: NotRequired[float]
    r"""What sampling temperature to use, between 0.0 and 1.0. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or `top_p` but not both."""
    top_p: NotRequired[float]
    r"""Nucleus sampling, where the model considers the results of the tokens with `top_p` probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or `temperature` but not both."""
    max_tokens: NotRequired[Nullable[int]]
    r"""The maximum number of tokens to generate in the completion. The token count of your prompt plus `max_tokens` cannot exceed the model's context length."""
    min_tokens: NotRequired[Nullable[int]]
    r"""The minimum number of tokens to generate in the completion."""
    stream: NotRequired[bool]
    r"""Whether to stream back partial progress. If set, tokens will be sent as data-only server-side events as they become available, with the stream terminated by a data: [DONE] message. Otherwise, the server will hold the request open until the timeout or until completion, with the response containing the full result as JSON."""
    stop: NotRequired[FIMCompletionRequestStopTypedDict]
    r"""Stop generation if this token is detected. Or if one of these tokens is detected when providing an array"""
    random_seed: NotRequired[Nullable[int]]
    r"""The seed to use for random sampling. If set, different calls will generate deterministic results."""
    suffix: NotRequired[Nullable[str]]
    r"""Optional text/code that adds more context for the model. When given a `prompt` and a `suffix` the model will fill what is between them. When `suffix` is not provided, the model will simply execute completion starting with `prompt`."""
    

class FIMCompletionRequest(BaseModel):
    model: Nullable[str]
    r"""ID of the model to use. Only compatible for now with:
    - `codestral-2405`
    - `codestral-latest`
    """
    prompt: str
    r"""The text/code to complete."""
    temperature: Optional[float] = 0.7
    r"""What sampling temperature to use, between 0.0 and 1.0. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or `top_p` but not both."""
    top_p: Optional[float] = 1
    r"""Nucleus sampling, where the model considers the results of the tokens with `top_p` probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or `temperature` but not both."""
    max_tokens: OptionalNullable[int] = UNSET
    r"""The maximum number of tokens to generate in the completion. The token count of your prompt plus `max_tokens` cannot exceed the model's context length."""
    min_tokens: OptionalNullable[int] = UNSET
    r"""The minimum number of tokens to generate in the completion."""
    stream: Optional[bool] = False
    r"""Whether to stream back partial progress. If set, tokens will be sent as data-only server-side events as they become available, with the stream terminated by a data: [DONE] message. Otherwise, the server will hold the request open until the timeout or until completion, with the response containing the full result as JSON."""
    stop: Optional[FIMCompletionRequestStop] = None
    r"""Stop generation if this token is detected. Or if one of these tokens is detected when providing an array"""
    random_seed: OptionalNullable[int] = UNSET
    r"""The seed to use for random sampling. If set, different calls will generate deterministic results."""
    suffix: OptionalNullable[str] = UNSET
    r"""Optional text/code that adds more context for the model. When given a `prompt` and a `suffix` the model will fill what is between them. When `suffix` is not provided, the model will simply execute completion starting with `prompt`."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["temperature", "top_p", "max_tokens", "min_tokens", "stream", "stop", "random_seed", "suffix"]
        nullable_fields = ["model", "max_tokens", "min_tokens", "random_seed", "suffix"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        
