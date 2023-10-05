from pydantic import BaseModel


class Homework(BaseModel):
    id: int
    description: str
    subject_id: int
    subject_name: str
    created_at: str
    is_done: bool = False