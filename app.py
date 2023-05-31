from datetime import date
from typing import Literal, Dict, Any, List, Union
from litestar import Controller, Litestar, post, get


class BaseBallPlayer:
    name: str
    description: str
    birth_date: date
    throwing_hand: Literal["right", "left", "both"]
    batting_hand: Literal["right", "left", "both"]


PLAYERS: List[BaseBallPlayer]


class BaseBallController(Controller):
    @post(path="/api/create")
    async def create(self, data: BaseBallPlayer) -> Dict[str, Any]:
        PLAYERS.append(data)
        return data

    @get(path="/api/players")
    async def get_all(self) -> List[BaseBallPlayer]:
        return List[BaseBallPlayer]

    @get(path="/api/players/{name:str}")
    async def get_one(self, name: str) -> Union[BaseBallPlayer, None]:
        for player in PLAYERS:
            if player.name == name:
                return player
        return None


app = Litestar(route_handlers=[BaseBallController])
