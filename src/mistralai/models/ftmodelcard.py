"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .modelcapabilities import ModelCapabilities, ModelCapabilitiesTypedDict
from datetime import datetime
from mistralai.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Final, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class FTModelCardTypedDict(TypedDict):
    r"""Extra fields for fine-tuned models."""

    id: str
    capabilities: ModelCapabilitiesTypedDict
    job: str
    root: str
    object: NotRequired[str]
    created: NotRequired[int]
    owned_by: NotRequired[str]
    name: NotRequired[Nullable[str]]
    description: NotRequired[Nullable[str]]
    max_context_length: NotRequired[int]
    aliases: NotRequired[List[str]]
    deprecation: NotRequired[Nullable[datetime]]
    archived: NotRequired[bool]


class FTModelCard(BaseModel):
    r"""Extra fields for fine-tuned models."""

    id: str

    capabilities: ModelCapabilities

    job: str

    root: str

    object: Optional[str] = "model"

    created: Optional[int] = None

    owned_by: Optional[str] = "mistralai"

    name: OptionalNullable[str] = UNSET

    description: OptionalNullable[str] = UNSET

    max_context_length: Optional[int] = 32768

    aliases: Optional[List[str]] = None

    deprecation: OptionalNullable[datetime] = UNSET

    # fmt: off
    TYPE: Annotated[Final[Optional[str]], pydantic.Field(alias="type")] = "fine-tuned" # type: ignore
    # fmt: on

    archived: Optional[bool] = False

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "object",
            "created",
            "owned_by",
            "name",
            "description",
            "max_context_length",
            "aliases",
            "deprecation",
            "type",
            "archived",
        ]
        nullable_fields = ["name", "description", "deprecation"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m