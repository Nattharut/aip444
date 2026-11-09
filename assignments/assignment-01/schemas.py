from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


# extra="forbid" emits additionalProperties: false, which strict json_schema
# structured outputs require on every object.
class Finding(BaseModel):
    model_config = ConfigDict(extra="forbid")

    path: str = Field(
        description="File path relative to the repository root, exactly as given in the input or a tool result"
    )
    line: int = Field(
        description="1-based line number in the file (the new version of the file for a diff). Use the line where the problem is, not the start of the function"
    )
    severity: Literal["critical", "warning", "info"] = Field(
        description="critical: exploitable or breaks at runtime. warning: likely bug or real maintenance cost. info: minor improvement"
    )
    category: str = Field(
        description="One lowercase word or hyphenated phrase, e.g. secrets, injection, naming, unused-import"
    )
    description: str = Field(
        description="What is wrong and why it matters, in 1-3 sentences. Name the exact identifier or value"
    )
    suggestion: str = Field(
        description="The concrete fix, in one or two sentences or a short code snippet"
    )
    evidence: str = Field(
        description="The exact source line the finding is about, copied character for character from the input or a tool result, without its line-number prefix"
    )


class ReviewResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    findings: list[Finding] = Field(
        description="Every issue found. Empty if the code has no issues in your area"
    )
