from typing import Protocol


class UseCaseProtocol(Protocol):
    async def execute(self, *args, **kwargs):
        ...
