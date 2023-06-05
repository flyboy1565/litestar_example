from dataclasses import dataclass
from datetime import date
from typing import Annotated, List, Literal, Union

import uvicorn
from litestar import Controller, Litestar, get, post
from litestar.enums import RequestEncodingType
from litestar.params import Body, Parameter


@dataclass
class BaseBallPlayer:
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
    async def create(
        self,
        data: BaseBallPlayer = Body(
            title="OAuth2Login", media_type=RequestEncodingType.URL_ENCODED
        ),
    ) -> BaseBallPlayer:
        print(data)
        PLAYERS.append(data)
        return data

    @get(path="/api/players")
    async def get_all(self) -> List[BaseBallPlayer]:
        return PLAYERS

    @get(path="/api/players/{name:str}")
    async def get_one(self, name: str) -> Union[BaseBallPlayer, None]:
        for player in PLAYERS:
            print(player)
            if player.name == name:
                print("found")
                return player
        return None


app = Litestar(route_handlers=[BaseBallController])
