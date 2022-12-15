from pydantic import BaseModel


class WordDetails(BaseModel):
    line_no: int
    char_no: int
    remaining_chars: int
    word: str


class LineDetails(BaseModel):
    line_no: int
    char_length: int
    text: str
