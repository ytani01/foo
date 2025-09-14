import asyncio
from fastmcp import Client

async def main():
    client = Client("main.py")
    async with client:
        result = await client.read_resource("server://name")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())