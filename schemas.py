from pydantic import BaseModel,condecimal
from typing import Annotated #it is used to validate the data and 
class productCreate(BaseModel):
    category: str
    department:str 
    name:str
    brand:str
    model:str
    price:Annotated[float,condecimal(max_digits=10,decimal_places=2)]

class productResponse(productCreate):
    id: int

    model_config = {
        "from_attributes": True
    }