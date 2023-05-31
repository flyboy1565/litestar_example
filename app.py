from dataclasses import dataclass
from datetime import date
from typing import Literal, Dict, Any, List, Union, Annotated
from litestar import Controller, Litestar, post, get
from litestar.params import Parameter
from pydantic import BaseModel


@dataclass
class BaseBallPlayer(BaseModel):
    name: Annotated[str, Parameter(query="name")]
    description: Annotated[str, Parameter(query="Description")]
    birth_date: Annotated[date, Parameter(query="birth_date")]
    throwing_hand: Annotated[
        Literal["right", "left", "both"], Parameter(query="Throwing")
    ]
    batting_hand: Annotated[
        Literal["right", "left", "both"], Parameter(query="Batting")
    ]


PLAYERS: List[BaseBallPlayer] = []


class BaseBallController(Controller):
    @post(path="/api/create")
    async def create(self, data: BaseBallPlayer) -> BaseBallPlayer:
        PLAYERS.append(data)
        return data

    @get(path="/api/players")
    async def get_all(self) -> List[BaseBallPlayer]:
        return PLAYERS

    @get(path="/api/players/{name:str}")
    async def get_one(self, name: str) -> Union[BaseBallPlayer, None]:
        for player in PLAYERS:
            if player.name == name:
                return player
        return None


app = Litestar(route_handlers=[BaseBallController])
