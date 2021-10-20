# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = brawery_from_dict(json.loads(json_string))

from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, TypeVar, Callable, Type, cast
import dateutil.parser
import json

import requests


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class BraweryElement:
    id: int
    name: str
    brewery_type: str
    address_2: None
    address_3: None
    city: str
    state: str
    county_province: None
    postal_code: str
    country: str
    longitude: str
    latitude: str
    phone: str
    website_url: str
    updated_at: datetime
    created_at: datetime

    @staticmethod
    def from_dict(obj: Any) -> 'BraweryElement':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        name = from_str(obj.get("name"))
        brewery_type = from_str(obj.get("brewery_type"))
        address_2 = from_none(obj.get("address_2"))
        address_3 = from_none(obj.get("address_3"))
        city = from_str(obj.get("city"))
        state = from_str(obj.get("state"))
        county_province = from_none(obj.get("county_province"))
        postal_code = from_str(obj.get("postal_code"))
        country = from_str(obj.get("country"))
        longitude = from_none(obj.get("longitude"))
        latitude = from_none(obj.get("latitude"))
        phone = from_none(obj.get("phone"))
        website_url = from_none(obj.get("website_url"))
        updated_at = from_datetime(obj.get("updated_at"))
        created_at = from_datetime(obj.get("created_at"))
        return BraweryElement(id, name, brewery_type, address_2, address_3, city, state, county_province, postal_code, country, longitude, latitude, phone, website_url, updated_at, created_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["name"] = from_str(self.name)
        result["brewery_type"] = from_str(self.brewery_type)
        result["address_2"] = from_none(self.address_2)
        result["address_3"] = from_none(self.address_3)
        result["city"] = from_str(self.city)
        result["state"] = from_str(self.state)
        result["county_province"] = from_none(self.county_province)
        result["postal_code"] = from_str(self.postal_code)
        result["country"] = from_str(self.country)
        result["longitude"] = from_none(self.longitude)
        result["latitude"] = from_none(self.latitude)
        result["phone"] = from_none(self.phone)
        result["website_url"] = from_none(self.website_url)
        result["updated_at"] = self.updated_at.isoformat()
        result["created_at"] = self.created_at.isoformat()
        return result


def brawery_from_dict(s: Any) -> List[BraweryElement]:
    return from_list(BraweryElement.from_dict, s)

def getBraweries() -> List[BraweryElement]:
    r = requests.get("https://api.openbrewerydb.org/breweries/")
   
    print(r.text)
    result = brawery_from_dict(json.loads(r.text))
    return result