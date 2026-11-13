# MICHINARI事業（GitHub公開版＝育成のみ）

GitHub Pages 用の研修アプリです。リポジトリ `michinari-site` の `academy/` フォルダに置くと、
`https://shuji4200.github.io/michinari-site/academy/` で開けます。

- `index.html` … アプリ本体（スマホ対応・タップ操作）
- `content/curriculum.json` … ステージとレッスンの中身。ここを書き換えると内容が更新されます
  - `status`: `"draft"`＝準備中 / `"published"`＝公開
  - `sections[].body`: 「- 」で箇条書き、「**太字**」、「> 」で強調ボックス、空行で段落
- 進捗はブラウザごとに保存（ログイン不要）
- 検索エンジンには載らない設定（noindex）。ただしURLを知っている人は誰でも見られます
- 顧客管理（CRM）はGitHub版には入っていません（顧客情報を公開しないため）。claude.ai版でのみ使えます
