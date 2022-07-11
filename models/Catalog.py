from typing import List
from pydantic import BaseModel


class Category(BaseModel):
    id: int
    title: str

    def __hash__(self):
        return hash((self.id, self.title))

    def __eq__(self, other):
        return self.id == self.id


class Label(BaseModel):
    id: int

    def __eq__(self, other):
        return self.id == self.id

class Attribute(BaseModel):
    labels: List[Label]
    id: int
    title: str


class Product(BaseModel):
    id: int
    title: str
    price: int
    categories: List[Category]
    labels: List[int]


class Catalog(BaseModel):
    products: List[Product]
    attributes: List[Attribute]



