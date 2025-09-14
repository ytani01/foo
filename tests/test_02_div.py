import pytest
from fastmcp import Client

@pytest.mark.asyncio
async def test_div():
    client = Client("main.py")
    async with client:
        result = await client.call_tool("div", {"a": 6, "b": 2})
        assert result.data.result == 3.0

@pytest.mark.asyncio
async def test_div_by_zero():
    client = Client("main.py")
    async with client:
        with pytest.raises(Exception) as e:
            await client.call_tool("div", {"a": 6, "b": 0})
        assert "Divisor cannot be zero." in str(e.value)
