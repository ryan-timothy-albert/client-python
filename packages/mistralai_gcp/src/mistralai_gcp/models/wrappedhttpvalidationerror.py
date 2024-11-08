"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httpvalidationerror import HTTPValidationError
from mistralai_gcp import utils
from mistralai_gcp.types import BaseModel, OptionalNullable, UNSET
from typing import Optional


class WrappedHTTPValidationErrorData(BaseModel):
    object: Optional[str] = None

    message: Optional[HTTPValidationError] = None

    type: Optional[str] = None

    param: OptionalNullable[str] = UNSET

    code: OptionalNullable[str] = UNSET


class WrappedHTTPValidationError(Exception):
    data: WrappedHTTPValidationErrorData

    def __init__(self, data: WrappedHTTPValidationErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, WrappedHTTPValidationErrorData)
