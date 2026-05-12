# Google Chat Enter Disable

Google Chat（Web版）で Enter キーによる即時送信を無効化し、すべて改行として扱う Chrome 拡張機能です。送信は **送信ボタンのクリックのみ** に限定されます。

## 動作

| キー操作 | 標準のGoogle Chat | 本拡張機能あり |
|---|---|---|
| `Enter` 単独 | 送信 | **改行** |
| `Shift + Enter` | 改行 | **改行** |
| `Ctrl + Enter` / `⌘ + Enter` | 改行 | **改行** |
| 送信ボタンのクリック | 送信 | **送信** |

日本語入力中（IME変換確定）の Enter は横取りしないため、変換確定が誤って改行になることはありません。

## 対応サイト

- `https://chat.google.com/*` — Google Chat 独立版
- `https://mail.google.com/*` — Gmail 内の Chat 統合

メインのメッセージ入力欄、スレッド返信欄、メッセージ編集欄を含む、チャット内のすべての入力欄（`<textarea>` および `contenteditable="true"`）に作用します。

## インストール手順

1. このリポジトリ（または配布されたフォルダ）を任意の場所に配置する。解凍した場合、解凍後のフォルダは削除しないこと。
2. Chrome で `chrome://extensions` を開く。
3. 右上の **デベロッパーモード** を ON にする。
4. **パッケージ化されていない拡張機能を読み込む** をクリック。
5. このフォルダ（`manifest.json` がある階層）を選択する。
6. 拡張機能一覧に **Google Chat Enter Disable** が表示され、有効になっていることを確認する。
7. Google Chat（または Gmail）のタブを開き直す。

## アンインストール

`chrome://extensions` から本拡張機能を削除してください。

## 注意事項

- 会社の Chrome に拡張機能のインストール制限がかかっている場合、Workspace 管理者の許可が必要になることがあります。
- Chrome 起動時に「デベロッパーモードの拡張機能を実行しています」という警告が出る場合がありますが、動作には影響しません。
- 一時的に無効化したい場合は、`chrome://extensions` から本拡張機能のトグルを OFF にしてください。

## プライバシー

- 外部サーバーとの通信は一切行いません。
- メッセージ内容の保存・送信は行いません。
- ストレージへのデータ保存も行いません。

## ファイル構成

```
gchat-enter-disable-extension/
├── manifest.json   # Manifest V3 設定
├── content.js      # キー入力ハンドラ
├── icons/          # 拡張機能アイコン (16/32/48/128 px)
├── scripts/
│   └── generate_icons.py   # アイコン再生成スクリプト（任意）
└── README.md
```

## バージョン

1.0.0
