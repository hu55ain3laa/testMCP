# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AttendanceCreateResponse"]


class AttendanceCreateResponse(BaseModel):
    response_mesage: Optional[str] = FieldInfo(alias="responseMesage", default=None)
    """number of entries created."""
