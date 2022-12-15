from pydantic import BaseModel, Field

class StationSchema(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=3, max_length=50)
    active: bool = Field(...)
    claimable: bool = Field(...)

class TicketSchema(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=50)
    price: float = Field(..., gt=0)
    date: str = Field(..., min_length=3, max_length=50)
    arrival_station: StationSchema = Field(...)
    departure_station: StationSchema = Field(...)
    arrival_date_time: str = Field(..., min_length=3, max_length=50)
    departure_date_time: str = Field(..., min_length=3, max_length=50)
    has_placements: bool = Field(...)
    commercial_number: str = Field(..., min_length=3, max_length=50)
