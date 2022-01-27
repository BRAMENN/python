# Copyright (c) 2022 Tulir Asokan
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from typing import Any, AsyncContextManager
from sqlite3 import Row

from asyncpg import Record
import asyncpg

from mautrix.util.logging import TraceLogger

from . import aiosqlite

class LoggingConnection:
    scheme: str
    wrapped: aiosqlite.TxnConnection | asyncpg.Connection
    log: TraceLogger
    def __init__(
        self, scheme: str, wrapped: aiosqlite.TxnConnection | asyncpg.Connection, log: TraceLogger
    ) -> None: ...
    async def transaction(self) -> AsyncContextManager[None]: ...
    async def execute(self, query: str, *args: Any, timeout: float | None = None) -> str: ...
    async def executemany(self, query: str, *args: Any, timeout: float | None = None) -> str: ...
    async def fetch(
        self, query: str, *args: Any, timeout: float | None = None
    ) -> list[Row | Record]: ...
    async def fetchval(
        self, query: str, *args: Any, column: int = 0, timeout: float | None = None
    ) -> Any: ...
    async def fetchrow(
        self, query: str, *args: Any, timeout: float | None = None
    ) -> Row | Record: ...
    async def copy_records_to_table(
        self,
        table_name: str,
        *,
        records: list[tuple[Any, ...]],
        columns: tuple[str, ...] | list[str],
        schema_name: str | None = None,
        timeout: float | None = None,
    ) -> None: ...