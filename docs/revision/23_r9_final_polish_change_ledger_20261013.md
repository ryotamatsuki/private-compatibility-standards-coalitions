# R9 final polish — change ledger (2026-10-13)

基準: PR33 の `e828684594479b674b9b1538ae0bc4a19a00b681`。
改稿 branch: `revision/r9-jict-astra-final-polish`、
[PR34](https://github.com/ryotamatsuki/private-compatibility-standards-coalitions/pull/34/files)。
以下の本文抜粋は old → new。全行の原文/改稿文は PR diff と提出ZIP同梱の
`r9_final_source_changes.patch` で追跡できる。更新理由は各項目に記録する。

## 変更の分類

**認証済みの economic primitives、定理の実質的結論、不等式、厳密witness、
元の証明・検証コード・Leanには変更なし。**

数式の追加は同じ厚生差の成分表示と既存の頑健性結果の proof bridge / exact certificate。
Proposition1 の等号の説明を正確にしたが、順位・誘因の元不等式は変えていない。
この区別を「純粋な英文修正のみ」と偽らない。
新しいモデル・経済学的新定理・正のdの連合安定性結果は追加していない。

## 本文

| ファイル・箇所 | 原文 | 改稿 | 理由・分類 |
|---|---|---|---|
| `short_01_introduction.tex`, §1 誘因 | “A lower residual per-unit cost can reverse the preference, strengthen the incentive without reversal, or leave the incentive weaker than before.” | “Depending on the residual cost, private adaptation can reverse the preference, strengthen the incentive without reversal, or weaken it relative to no adoption.” | dを下げると単調に悪化するという誤読を避け、固定dの効果とno-adoption比較を区別。意味の明確化。 |
| 同、closest literature | Gandal/Shy・Takaradaを政府認識/consumption externalitiesのテーマとして簡潔に列挙 | conversion costs/strong networkのGandal/Shy結果、local/transboundary externalitiesのTakarada core結果を明示し、post-formal-partition firm investmentと継続利得を比較 | primary evidenceに沿った定理・均衡対象の位置付け。自称“first”は追加しない。 |
| 同、plural agreement | “Kawabata and Takarada … examines”; “Buccella et al. … studies”; “Parenti and Vannoorenberghe … links” | “examine”; “study”; “link” | 主語・動詞の一致、英文のみ。 |
| 同、working paper | “An unpublished working paper … (… 2024; revised 2026)” | “A working paper … (… 2024)” | 確認可能なNBER版のみを記述。未確認の改訂時点を削除。 |
| `short_02_model.tex`, singleton rule | singleton g=0という式とモデル設定のみ | “The singleton rule treats network benefits as gains from interoperability across producers: a proprietary product alone generates none. It does not model a proprietary installed base. This assumption materially affects government rankings …” | 経済的意味・重要性・S1での失敗を明示。仮定自体は不変。 |
| `short_04_incentives.tex`, R直後 | “The term R(d,v) is not imposed as an erosion parameter. …” | R = [K_R−K_I] + [2(A_R−P)] の正確なCS/国内利潤表示と、残余costによる保護・域外国市場Dの残存を説明 | 新しい主張ではない。非自明な代数と経済的解釈の橋渡し。 |
| 同、eq.(15) | align中の間隔/行区切りが読みづらい | A_R/B_Rの行とK_Rの行を分離 | 数式内容不変、LaTeX表示。 |
| 同、Proposition1 equalities | “The equalities … are indifference boundaries.” | “At R(d,v)=D, the member is indifferent between SU and IS after adoption. At R(d,v)=E, adoption leaves its relative IS incentive unchanged.” | 等号が意味する二つの異なる比較を厳密に記述。理論の不等式は不変。 |
| 同、Table1 | 生成tableが本文途中、等号一行がBoundary/Indifference | 本文は正確にTable1を参照。tableはReferences後、R=DとR=Eを別行 | 追跡性・公開提出形式。元のtable generatorは不変、short builderだけでoverride。 |
| 同、Figure1 | 短縮 figure 名、長いcaption、floatがproofを中断する可能性 | Fig1.pdf/EPS、残余rentと二閾値、線種、c/v、3領域、numerical illustrationで採用equilibrium certificateではないと明記。[H]でproof後に配置 | 数値・解析対象は不変、reader verificationと配置。 |
| `short_05_stability_scope.tex` | “Proof and exhaustive five-partition blocking check.”という非formal見出しから表・説明 | `begin{proof}` … 同じfinite-deviation table … strict/weak/asymmetryの説明 … `end{proof}` | 偏差分類→表→網羅性→補足G→終点の流れを正式な証明として明示。長いoptional proof headingは12ptでoverflowしたため使わない。 |
| `short_06_discussion.tex` | “national fiscal or political incentive”; “pre-registered …” | “national-welfare incentive”; “pre-specified …” | 政府目的はCS+国内利潤であり、fiscal目的や未確認の事前登録を示唆しない。 |
| `main.tex`, disclosure/SI pointer | supplement各部とreplicationについて一般的説明 | Online Resource1、Eのequilibrium/sign proofs、Gのfive-partition ledger、同梱R2–R9/独立matrix/selected Leanを正確に案内 | 本文と配布物の一致。Lean whole-paper証明を主張しない。 |
| `main.tex`, format | elsarticle [review] (1.5 spacing)、18頁 | [12pt,review] +1-inch geometry +setspace、frontmatter reset後もtrue double spacing、baseline log gate、19頁 | 公開JICT double-spacing要件への是正。証明を削除して頁数を調整しない。 |

## 補足 A–G

元の `paper/appendix/app_a…app_f…tex` は一行も変更していない。
39頁版の元main/sections/bibliography/preambleも不変。

| short-only生成/追加箇所 | 旧状態 → 新状態 | 理由 |
|---|---|---|
| A–Fの本文参照 | full版の節/補題名 → short版§2/3/4/5の対応するheading/式 | リンク先が実在する節への限定的置換。元原稿は不変。 |
| B, N_MS | 長い一行のpolynomial → 同じpolynomialをdisplay rowsに分割 | overfullで数式が読めない状態を解消。係数・項の並びは不変。 |
| D | inherited alignの単一control-space → 正しいLaTeX row break | q_A/q_S/T_W/T_A^R/F*が別行に表示される。原式は不変。 |
| 補足paths/preamble | 長いtexttt code path → breakable path、emergencystretch1em | 記号・参照先を変えずに余白へのはみ出しを防ぐ。 |
| E.1 | “full fixed-c root characterization is certified by … code” | Phi/N、positive denominator、U(c)、L1/L2、coefficient signs、Sturm recurrence、Q(c) isolating interval、Descartes、excluded endpoints | 旧認証結果を読者が追える数学的対象と判定手順に接続。 |
| E.2/E.3 | “transformed-domain exact sign certificate … proves Phi_S1<0” | FOC、全quantities/profit/CS/Phi、K≥11/16、triangular transform、Bernstein変換と18 rational coefficients、境界でのstrict sign | codeを動かさず証明対象と理由を把握できるようにする。別証明ルートを追加。 |
| E.4 | demand matrixと“exact R5 sign certificates establish …”のみ | C_G diagonal/singleton定義、four configurations、正定値/内点、Cournot/price FOCを別々に導出、均衡式・利潤、welfare targets、正分母、explicit/compact polynomial、全zero indicesとminimum証明表 | 同じ負の頑健性主張への短い厳密証明。Cournot利潤をBertrandに流用しない。 |
| E.5 | Lean FV5 とR6の一般的参照 | FV5はconditional blocking predicateのみ、Gのfull payoff ledger、d=0 scopeを明記 | 形式検証の範囲を過大に説明しない。 |
| G | 既存short_supplement_blocking.tex | unchanged | 既存の全partition proof ledgerを保持。新しい定理不要。 |

Eの旧全文はbase commitの元Appendix E、改稿全文は
`paper/jict_short/short_supplement_robustness.tex` とその生成
`app_e_robustness.tex` で対比できる。追加proofは必要な橋渡しに限定した。

## ビルド・検証・提出物

- `build_jict_short.py`: short-only E override、fresh SI copy（aux cacheを引き継がない）、
  spacing/log gate、boundary-table override、separate identified-source build/current cover date、
  Fig1EPS、ESM1、expanded anonymous replication、manifest更新。
  元の39頁JICT builder・original replication builderは変更しない。
- `make_jict_short_figure.py`: legend fontsize 9→10 のみ。数値・式・frozen full figureは不変。
- `check_jict_short_independent.py`: 新規の別 evaluator。旧チェックをimportしない。
  原始条件のmarket matrix、全firm normal form、witnessの全coalitions、
  exact Bernsteinとprinted S1 array一致を検証。
- `audit_jict_short_package.py`: 新規の提出ファイル検査。Gitでprotected files差分なしを確認、
  source ZIP empty-directory再compile、PDF text一致、embedded fonts、recursive anonymity、
  spacing、identified separation、exact change patch、review bundle作成。
- Short Preview CI: 実際の新replication ZIPからindependent checker/全R2–R9/make verifyを実行。
  元のPaper CIのR2–R9/Lean/39頁原稿・旧提出物監査は不変。
- ローカル接続断対応のtemporary read-only byte exportは最終物を回収した後にCIから削除する。
  GitHub資格情報・環境変数は出力しない。PRを自動mergeする処理はない。
- `jict_short_identified_source.zip` は著者情報を含む別source ZIP。
  reviewer/SIのanonymous ZIPへtitle/coverを混入しない。
- 修正後19頁 / SI22頁。修正前18頁との比較では1.5→double spacingの変更を必ず併記する。

全変更はPR差分で review 可能である。著者によるPR承認があるまで merge せず、
投稿システムにも書き込まない。
