"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mistralai.types import BaseModel
from mistralai.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class FilesAPIRoutesDownloadFileRequestTypedDict(TypedDict):
    file_id: str


class FilesAPIRoutesDownloadFileRequest(BaseModel):
    file_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]