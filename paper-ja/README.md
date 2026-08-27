# 日本語自習版 — Private Compatibility and the Stability of Standards Coalitions

このディレクトリは、英語版論文 `paper/` を正本（canonical source）として作成した、著者自身の理論確認・自習・査読対応準備のための**非公式日本語訳**です。投稿原稿ではなく、scientific priority は常に英語版にあります。

**不一致がある場合は、必ず英語版を正とします（In case of any discrepancy, the English version controls.）**

## 基準版

- canonical English base: `c98309c75740df459ba356852b895d2d7a748d84`
- 作成時点: 2026-08-27
- 英語版の数式、notation、parameter restriction、equation labels、theorem labels、citation keys、section orderを変更しない方針で対応しています。

## 構造

`main-ja.tex` は英語版 `paper/main.tex` と同じ入力順を持ちます。Section 1–11、および Appendix A/B/C/Fを1対1で対応させています。参考文献データは `paper/references.bib` を共有し、文献タイトル・著者名・journal名・citation keyは翻訳しません。

## ビルド

リポジトリrootから次を実行します。

```bash
make -C paper-ja all
```

`paper-ja/Makefile` はまずcanonical側のfigure/table生成を呼び出し、日本語版ではfigure PDFをそのまま再利用します。表については、canonical generated tableの数式・labelを保持したまま、既知の英語表示文字列だけを決定論的に日本語へ置換して `paper-ja/tables/generated/` に生成します。その後、LuaLaTeXで `main-ja.tex` をコンパイルします。

## 機械監査

```bash
make -C paper-ja audit
```

`paper-ja/scripts/audit_correspondence.py` は、英語版と日本語版から `\label{}`、citation keys、`\ref{}`/`\eqref{}`、section hierarchy、theorem-type environments、display mathematics、inline mathematicsを抽出し、canonical mathematical objectsの欠落・改変がないことを検査します。日本語の語順により本文中のcross-referenceやinline mathの位置が動き得るため、これらはexact multiplicityで比較し、labelsとcitationsはordered streamで一致を要求します。generated tablesについてもlabel・数式token・tabular構造を比較します。

## 用途と同期ルール

この日本語版は internal study version / unofficial Japanese translation / faithful study companion です。英語版に変更が入った場合は、日本語版を自動的に正しいとみなさず、必ずbase SHAを更新して構造監査と翻訳同期を再実施してください。

図内部の英語ラベルは、canonical figure generation logicを複製・改変しないため英語版generated PDFを再利用しています。本文中の図captionは日本語化しています。数値図はあくまでillustrationであり、証明ではないという英語版の位置付けを維持しています。
