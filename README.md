# MCPサーバーおよびクライアントプロジェクト

このプロジェクトは、マルチエージェント通信プロトコル（MCP）サーバーとその操作のためのクライアントを実装しています。文書化されたツールを介したGeminiCLIとの効果的な対話を重視した、デモンストレーションおよび開発環境として機能します。

## 機能
- **基本的な算術ツール:** 数学演算のための`multi`、`div`、`divmod`を提供します。
- **名前リソース:** シンプルな`name`リソースを公開します。
- **トークンカウントツール:** セッションごとのトークン消費を記録する`record_tokens`と、合計および詳細な使用状況を取得する`get_token_usage`を含みます。

## セットアップ

### 前提条件
- `uv`: 高速なPythonパッケージインストーラーおよび依存関係解決ツールです。公式の`uv`インストールガイドに従ってください。
- Python 3.13以降。

### インストール
プロジェクトのルートディレクトリに移動し、依存関係をインストールします。
```bash
uv install
```

## 使用方法

### MCPサーバーの実行
MCPサーバーは`uv`を使用してバックグラウンドで実行できます。
```bash
uv run python main.py &
```

### ツールとの対話（GeminiCLI経由）
サーバーが実行されたら、GeminiCLIを介して公開されたツールと直接対話できます。例：
- トークンを記録するには：
  ```
  foo.record_tokens session1 100
  ```
- トークン使用量を取得するには：
  ```
  foo.get_token_usage
  ```

### MCPクライアントCLIの実行
このプロジェクトにはコマンドラインクライアントも含まれています。`uv`を使用して実行できます。
```bash
PYTHONPATH=src uv run python -m mcp_client.cli <command> [args]
```
例：
```bash
PYTHONPATH=src uv run python -m mcp_client.cli record_tokens --session_id my_session --tokens 50
PYTHONPATH=src uv run python -m mcp_client.cli get_token_usage
```

## テスト

### すべてのテストの実行
すべての単体テストと統合テストを実行するには：
```bash
uv run pytest tests/
```

### リンティングと型チェック
コードの品質と型ヒントへの準拠を保証するには：
- **Ruff (リンティング):**
  ```bash
uv run ruff check tests/
  ```
- **MyPy (型チェック):**
  ```bash
uv run mypy tests/
  ```
- **Pyright (型チェック):**
  ```bash
uv run pyright tests/
  ```

## プロジェクト構造
- `src/`: `mcp_client`と`mcp_svr1`を含む主要なアプリケーションソースコードが含まれています。
- `tests/`: プロジェクトの自動テストが含まれています。
- `docs/`: プロジェクトのドキュメント。
- `main.py`: MCPサーバーの主要なエントリポイント。

## 規約
- **Docstringとコメント:** すべてのdocstringとコメントは日本語で記述されています。
- **GeminiCLIとの対話:** Docstringは、特に言語マッチングにおいて、GeminiCLIのツール選択にとって重要なヒントです。明確で簡潔であり、日本語で関連するキーワードが含まれていることを確認してください。
