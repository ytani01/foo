import pytest
from fastmcp import Client
from fastmcp.exceptions import ToolError

@pytest.mark.asyncio
async def test_divmod_positive_numbers():
    client = Client("main.py")
    async with client:
        result = await client.call_tool("divmod", {"dividend": 10, "divisor": 3})
        assert result.data.quotient == 3
        assert result.data.remainder == 1

@pytest.mark.asyncio
async def test_divmod_negative_dividend():
    client = Client("main.py")
    async with client:
        result = await client.call_tool("divmod", {"dividend": -10, "divisor": 3})
        assert result.data.quotient == -4
        assert result.data.remainder == 2

@pytest.mark.asyncio
async def test_divmod_negative_divisor():
    client = Client("main.py")
    async with client:
        result = await client.call_tool("divmod", {"dividend": 10, "divisor": -3})
        assert result.data.quotient == -4
        assert result.data.remainder == -2

@pytest.mark.asyncio
async def test_divmod_division_by_zero():
    client = Client("main.py")
    async with client:
        with pytest.raises(ToolError, match="Divisor cannot be zero."):
            await client.call_tool("divmod", {"dividend": 10, "divisor": 0})
