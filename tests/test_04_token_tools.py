import pytest
from fastmcp import Client

import json # Import json
from typing import Any # Import Any

@pytest.mark.asyncio
async def test_record_and_get_token_usage():
    client = Client("main.py")
    async with client:
        # Clear the token_log before each test to ensure a clean state
        await client.call_tool("clear_token_log", {})

        # Test record_tokens
        response1 = await client.call_tool("record_tokens", {"session_id": "test_session_1", "tokens": 100})
        assert response1.data.result == "Session test_session_1 記録: 100 tokens"

        response2 = await client.call_tool("record_tokens", {"session_id": "test_session_1", "tokens": 50})
        assert response2.data.result == "Session test_session_1 記録: 50 tokens"

        response3 = await client.call_tool("record_tokens", {"session_id": "test_session_2", "tokens": 200})
        assert response3.data.result == "Session test_session_2 記録: 200 tokens"

        # Test get_token_usage
        response_usage = await client.call_tool("get_token_usage", {})
        
        # Use Any for type hint and perform runtime check
        content_item: Any = response_usage.content[0]
        # Ensure it's a TextContent and has a text attribute
        assert hasattr(content_item, 'text') and isinstance(content_item.text, str)
        
        parsed_data = json.loads(content_item.text)

        assert parsed_data["total_tokens"] == 350
        assert len(parsed_data["details"]) == 3
        assert {"session": "test_session_1", "tokens": 100} in parsed_data["details"]
        assert {"session": "test_session_1", "tokens": 50} in parsed_data["details"]
        assert {"session": "test_session_2", "tokens": 200} in parsed_data["details"]

@pytest.mark.asyncio
async def test_get_token_usage_empty():
    client = Client("main.py")
    async with client:
        # Clear the token_log before each test to ensure a clean state
        await client.call_tool("clear_token_log", {})

        response_usage = await client.call_tool("get_token_usage", {})
        
        # Use Any for type hint and perform runtime check
        content_item: Any = response_usage.content[0]
        # Ensure it's a TextContent and has a text attribute
        assert hasattr(content_item, 'text') and isinstance(content_item.text, str)
        
        parsed_data = json.loads(content_item.text)

        assert parsed_data["total_tokens"] == 0
        assert len(parsed_data["details"]) == 0