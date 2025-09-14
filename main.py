from mcp.server.fastmcp import FastMCP
from dataclasses import dataclass

@dataclass
class DivmodResult:
    quotient: int
    remainder: int

from typing import List, Dict




mcp = FastMCP("foo")

@mcp.tool()
def multi(a: int, b:int) -> int:
    """掛け算の結果を返す。"""
    return a * b


@mcp.tool()
def div(a: int, b: int) -> float:
    """割り算の結果を返す。"""
    if b == 0:
        raise ValueError("Divisor cannot be zero.")
    return a / b

@mcp.tool()
def divmod(dividend: int, divisor: int) -> DivmodResult:
    """2つの数値の商と剰余を計算します。

    Args:
        dividend: 割られる数。
        divisor: 割る数。
    """
    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")
    quotient = dividend // divisor
    remainder = dividend % divisor
    return DivmodResult(quotient=quotient, remainder=remainder)

@mcp.tool()
def get_name() -> str:
    """'name'リソースの値を返します。"""
    return name()

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

@mcp.tool()
def clear_token_log() -> str:
    """トークン消費ログをクリアする。"""
    global token_log
    token_log = []
    return "トークンログをクリアしました。"



@mcp.resource("server://name")
def name() -> str:
    """Returns My name."""
    return "谷林"


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
