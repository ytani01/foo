from fastmcp import FastMCP
from typing import List, Dict

mcp = FastMCP("Token Counter Server")

# トークン消費ログを保持するリスト
token_log: List[Dict] = []

@mcp.tool()
def record_tokens(session_id: str, tokens: int) -> str:
    """セッションごとの消費トークンを記録する"""
    token_log.append({"session": session_id, "tokens": tokens})
    return f"Session {session_id} 記録: {tokens} tokens"

@mcp.tool()
def get_token_usage() -> dict:
    """セッションごとのトークン消費一覧・合計を返す"""
    total = sum(e["tokens"] for e in token_log)
    return {"total_tokens": total, "details": token_log}

if __name__ == "__main__":
    mcp.run(transport="stdio")  # GeminiCLIなどと標準入出力経由で連携
