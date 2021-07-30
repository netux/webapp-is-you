from __future__ import annotations

import datetime
from typing import Iterable, TYPE_CHECKING, Any, Coroutine, Optional

import discord
from discord.ext import commands
from PIL import Image

if TYPE_CHECKING:
    from .cogs.render import Renderer
    from .cogs.variants import VariantHandlers

class Context(commands.Context):
    async def error(self, msg: str) -> discord.Message: ...
    async def send(self, content: str="", embed: Optional[discord.Embed] = None, **kwargs) -> discord.Message: ...

class DataAccess:
    bot: Bot
    def __init__(self, bot: Bot) -> None:...
    def load_letters(self) -> None:...
    def tile_data(self, tile: str) -> dict | None:...
    def tile_datas(self) -> Iterable[tuple[str, dict]]:...
    def level_tile_data(self, tile: str) -> dict | None:...
    def plate(self, direction: int | None, wobble: int) -> tuple[Image.Image, tuple[int, int]]:...
    def letter_width(self, char: str, mode: str, *, greater_than: int) -> int:...
    def letter_sprite(self, char: str, mode: str, width: int, wobble: int, *, seed: int) -> Image.Image:...

class Bot(commands.Bot):
    get: DataAccess
    cogs: list[str]
    embed_color: discord.Color
    webhook_id: int
    prefixes: list[str]
    exit_code: int
    loading: bool
    started: datetime.datetime
    renderer: Renderer
    handlers: VariantHandlers
    def __init__(self, *args, cogs: list[str], embed_color: discord.Color, webhook_id: int, prefixes: list[str], exit_code: int = 0, **kwargs):...
    async def get_context(self, message: discord.Message) -> Coroutine[Any, Any, Context]:...
    def get_tile(self, tile: str) -> dict | None:...
