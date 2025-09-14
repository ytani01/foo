import pytest
from fastmcp import Client

@pytest.mark.asyncio
async def test_multi():
    client = Client("main.py")
    async with client:
        result = await client.call_tool("multi", {"a": 2, "b": 3})
        assert result.data.result == 6
