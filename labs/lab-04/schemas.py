from pydantic import BaseModel, Field


class Flashcard(BaseModel):
    application: str = Field(
        description="1-2 sentence real-world scenario where this concept is used or required"
    )
    challenge: str = Field(
        description="A specific problem to solve in the application scenario"
    )
    answer: str = Field(
        description="Correct solution to the challenge with brief explanation. Expand all acronyms"
    )
    evidence: str = Field(
        description="Direct quote from source notes supporting the answer"
    )
    misconception: str = Field(
        description="A misconception that a student might make, written as a quote of what they might say"
    )
    correction: str = Field(
        description="Why this misconception is wrong, citing facts from the notes"
    )


class FlashcardResponse(BaseModel):
    flashcards: list[Flashcard] = Field(
        description="The generated flashcards. Empty if the notes are too thin to support any card"
    )
