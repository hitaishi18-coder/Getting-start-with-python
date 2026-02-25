from pydantic import BaseModel , computed_field, field_validator, Field


class Booking(BaseModel):
    user_id : int
    room_id : int

    nights : int = Field(... , ge=1)
    rate_per_night: float = Field(..., gt=0)
    discount : float = Field(0, ge=0)


    @field_validator("discount")
    def discount_not_too_large(cls, v):
        if v > 50 :
            raise ValueError("Discount cannot exceed 50%")
        return v 
    
    @computed_field
    @property
    def total_amount(self)-> float:
        return self.nights * self.rate_per_night
    
    @computed_field
    @property
    def tax(self) -> float:
        return self.total_amount * 0.18
    

    @computed_field
    @property
    def grand_total(self) -> float:
        discounted = self.total_amount * (1 - self.discount / 100)
        return discounted + self.tax
    
booking = Booking(
    user_id=1,
    room_id=2,
    nights=2,
    rate_per_night=200,
    discount=20
)

print(booking.grand_total)

print(booking.model_dump())