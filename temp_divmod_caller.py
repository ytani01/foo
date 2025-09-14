import asyncio
from fastmcp import Client

async def call_divmod():
    client = Client("main.py")
    async with client:
        result = await client.call_tool("divmod", {"dividend": 10, "divisor": 3})
        print(f"Quotient: {result.data.quotient}")
        print(f"Remainder: {result.data.remainder}")

if __name__ == "__main__":
    asyncio.run(call_divmod())