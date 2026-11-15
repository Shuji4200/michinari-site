# MICHINARI事業アプリのソース

- `index.html`：MICHINARI事業（本体）・部門アプリ7つ・公開デモの共通コード。
  先頭近くの `const APP_MODE="main";` を書き換えて各アプリを作る。
- `build_dept.py`：`index.html` から `dept/{ceo,cso,cmo,cpo,chro,cfo,clo,public}.html` を作る。
- このフォルダのページはClaude内でだけ動く（データの保存はclaude.aiのアプリ側）。ここで開いても空の画面になる。
- 公開デモ（`/dashboard/`）は `dept/public.html` をコピーしたもの。サンプルデータのみ。

作業のルールは、Claudeのプロジェクト「【株式会社MICHINARI】」のドキュメント
`claude/hp-cmo-link.md` を参照。
