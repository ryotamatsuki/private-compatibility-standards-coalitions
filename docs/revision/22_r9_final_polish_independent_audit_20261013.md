# R9 JICT short edition — final independent audit (2026-10-13)

対象: *Private Compatibility and Government Incentives for Standards Harmonization*。
基準原稿は PR #33 統合後の `revision/research-track`、コミット
`e828684594479b674b9b1538ae0bc4a19a00b681`。
作業・提出物は PR [#34](https://github.com/ryotamatsuki/private-compatibility-standards-coalitions/pull/34)
の `revision/r9-jict-astra-final-polish` に限定する。マージ・投稿は行っていない。

この監査は既存 Stage 11/13/14 の判定を引き継がず、原稿の原始条件から
市場・企業行動・政府厚生・連合偏差を再構成した AI による監査である。
外部の人間による独立査読を実施したとは主張しない。

## 判定

| 評価軸 | 判定 | 具体的根拠・適用範囲 |
|---|---|---|
| 経済学的貢献 | **CONDITIONAL GO** | §1、§4.2–4.4、§6。同じ原始条件で厳密な企業採用と正の残余費用下の政府選好反転が共存することが、単なる厚生差の恒等式を超える知見。限定的な診断・応用理論として投稿価値がある。一般的な互換性定理、普遍的政策勧告としての GO ではない。 |
| 数学的正確性 | **PASS** | §2–5、SI A–G。R(d,v) と両厚生差を別実装で再導出。正確な有理数 witness、全企業行動・全連合偏差を再最適化。E.3/E.4 の領域全体の符号を有理 Bernstein 証明で独立確認。認証済み命題を覆す反例なし。 |
| 証明の検証可能性 | **PASS** | §4 の余剰・国内利潤分解、§5 の正式 proof と網羅表、SI E.1–E.5 の対象関数・分母・領域・端点・判定方法、G の全偏差台帳。コードを読まずに何を証明するか理解できる。 |
| 文章・構成の可読性 | **PASS** | §1 の問・最接近研究・限界、§2 の singleton-zero の意味、§4 の恒等式直後の直観、§5 の証明終点、§6 の適用限界。全頁の図表・数式・参照を目視した。 |
| 先行研究との位置付け | **PASS** | §1 と下記の primary-source 照合。問、均衡対象、既存の定理・結果の相違を明示。「初めて」の主張なし。Ding の全証明や文献全体の網羅性は認証対象外。 |
| JICT 投稿技術要件 | **UNVERIFIED** | 公開規定に対するファイル事前検査は PASS。本文は実際の 12pt double spacing で 19頁、SI は22頁。匿名性・flat TeX ZIP・参考文献・組込フォント・別著者頁・EPS を確認。live portal の項目、アップロード後の合成 PDF、著者の最終申告は未検証であり、Stage 14 の完全な投稿 freeze は出さない。 |

CONDITIONAL GO の条件は、現在の限定的な貢献・適用範囲の記述を維持すること。
新モデルや未証明の一般化・実証分析を追加する要求ではない。採択見込みの保証でもない。
核心の数学的誤りは検出していないため、Stage 4/5 への理論差戻しは不要。
ただし「18頁 = double-spaced」という以前の技術判定は取り消し、書式を修正して
Stage 13/14 のファイル検査をやり直した。

## 使用した最新ワークフロー

最新版 main を開始時と最終反映前の双方で確認した:
`81c37dd95fc93d918138ba9d0da86541d3cc1067`。
stable v2.9 は `338677e9566e6bf63a455de81da4ac47153b4e69`。
以下は main の内容を精読した（v2.10 と呼び替えない）。

- [GOVERNANCE.md](https://github.com/ryotamatsuki/research-paper-workflow/blob/81c37dd95fc93d918138ba9d0da86541d3cc1067/GOVERNANCE.md)
- [THEORY_PAPER_RESEARCH_PIPELINE.md](https://github.com/ryotamatsuki/research-paper-workflow/blob/81c37dd95fc93d918138ba9d0da86541d3cc1067/THEORY_PAPER_RESEARCH_PIPELINE.md)
- [REVIEWER_VERIFIABILITY_CHECKLIST.md](https://github.com/ryotamatsuki/research-paper-workflow/blob/81c37dd95fc93d918138ba9d0da86541d3cc1067/checklists/REVIEWER_VERIFIABILITY_CHECKLIST.md)
- [EXPOSITION_STREAMLINING_CHECKLIST.md](https://github.com/ryotamatsuki/research-paper-workflow/blob/81c37dd95fc93d918138ba9d0da86541d3cc1067/checklists/EXPOSITION_STREAMLINING_CHECKLIST.md)
- [FIGURE_TABLE_CHECKLIST.md](https://github.com/ryotamatsuki/research-paper-workflow/blob/81c37dd95fc93d918138ba9d0da86541d3cc1067/checklists/FIGURE_TABLE_CHECKLIST.md)
- [ECONOMIC_CONTRIBUTION_COMPLETENESS_CHECKLIST.md](https://github.com/ryotamatsuki/research-paper-workflow/blob/81c37dd95fc93d918138ba9d0da86541d3cc1067/checklists/ECONOMIC_CONTRIBUTION_COMPLETENESS_CHECKLIST.md)

main に統合された未リリースの「既存結論の反転・成立境界・一般化」とフロンティア照合も適用した。
異なる政府目的を置くだけでは貢献にならず、最接近研究を知る編集者に残る経済学的知見を
説明できるかを別に評価した。また、正しさ・再現性・査読者検証可能性を分離した。

## 本文の命題を順番に監査

| 箇所 | 原始条件と結論 | 独立再構成・証明判定 |
|---|---|---|
| §2, eqs. (1)–(4) | 三国、分断市場、線形単位需要、互換性グループ、singleton-zero、内点領域 | 需要行列と own-output derivative から Cournot を解き直し、数量・operating profit・CS が一致。A は内点と一意性を区別。 |
| §3, eqs. (5)–(7) | F の厳密区間による outsider-only 採用と SW 無採用 | 必要条件とは呼んでいない。C/D への参照は対応する。witness では全 normal form に対する strict dominance を確認し、混合均衡の選択問題も回避。 |
| §4.1–4.2, eqs. (8)–(19) | pre-gap = E−D、post-gap = −D+R(d,v) | member-market CS と国内企業の二市場利潤を別々に計算し R を再導出。域外国市場の C は未適応なので D が残る。R の分母は正、d 微分は正。 |
| Proposition 1, eq. (20) | E>D>0 の条件付き三領域 | 恒等式から必要十分な比較を示す短い証明。R=D は post-adoption の順位無差別、R=E は「誘因の変化がゼロ」。両者を同一の indifference と呼ぶ曖昧さを解消。根は d≥0 上で一意だが、経済的範囲は d≤c に切り詰める。 |
| Proposition 2, eqs. (21)–(23) | 0<lambda<1 の非空開集合の存在 | (c,v,lambda,F)=(1/10,6/25,1/2,9/100)、d=1/20 を厳密再計算。pre=2408509/295731200>0、post=−1341/184832<0。全 firm actions の厳密比較から、その witness の近傍が成立。全パラメータでの一意性・グローバル安定性を主張しない。 |
| Theorem 1, eqs. (24)–(26) | d=0、Omega_0、五つの partition、指定 blocking rule | proof 内の網羅表が誘導 partition と利得比較を接続。G の7非空連合による列挙と一致。対称 high-F の弱い block と、intermediate-F の厳密優越を区別。正の d へ拡張していない。 |

短縮本文には named Proposition が2個、Theorem が1個あり、形式だけを揃えるための
新しい Lemma/Corollary は追加しなかった。Theorem 1 は証明表を proof 内に置くことが
適切であり、表の前に偏差の分類、後に relabeling と weak blocking・局所的非対称性の
論理を置き、証明の終点を明示した。式・厳密不等式・仮定・witness 自体は変更していない。

## Appendix E: コード参照で終わらない証明経路

| 主張・箇所 | 原始条件 → 均衡 → 対象 → 正負判定 → 範囲 → 結論 |
|---|---|
| E.1 canonical network | §2 の Cournot blocks → Phi=K_M+2A+C−K_I−3P → N=32(1−v)^2(2−3v)^2 Phi。分母正。v=0 の負の式を明示。固定 c では v=U(c)t/(1+t)、L_1/L_2 の係数符号と Q(c) の唯一の根を Sturm/Descartes で検査。c=1/9 と excluded upper endpoint を扱う。初期 SU 優位の成立境界を得る。 |
| E.2 sign method | bivariate power-to-Bernstein の正確な係数変換を記載。重みの非負性・和が1という恒等式から符号を証明。zero indices と active weights によって v=0 での strictness も説明。 |
| E.3 singleton benefits | 全 nonempty group の network rule → 二つの Cournot FOC → 四数量、profit=(1−v)q²、CS → Phi_S1 → 正分母 M_1 と Q_1。canonical triangular domain を (x,y) へ写し、18個の有理 Bernstein 係数を全文表示。Q_1>0 から Phi_S1<0。K≥11/16、内点と端点を説明。 |
| E.4 differentiated Cournot | gamma=1/2 と C_G の diagonal/singleton 定義 → M 正定値 → 数量 FOC と q=(M+diag M_ii)^−1(1−r) → profit=M_ii q²、quadratic CS → explicit N_C/E_C と正分母 → 厳密係数証明で Phi/E<0、D>0。全0<c<1/3, 0≤v<1/4。 |
| E.4 differentiated Bertrand | 同じ primitives から direct demand D=M^−1 → 価格 FOC と別の価格均衡 → explicit output/profit=q²/D_ii → Phi/E/D → D_+>0、Q_Phi/Q_E/Q_D の正確な数学的定義と Bernstein 証明。Cournot の利潤式を流用しない。 |
| E.4 political implication | Phi<0 は採用前から IS 選好。full bypass 後は −D<0、relative-IS-incentive change=E<0。固定有理点の adoption witness は別の存在証明。両 competition mode で私的採用が成立しても、地域選好からの反転という政治結果は失敗する。 |
| E.5 blocking boundary | 対称性の等号が strict/weak を分離する。asymmetry bridge とGを参照。Lean FV5 は payoff を仮定した論理部分だけ。 |

E.1 の検査対象は displayed blocks から定義された N と、その明示された L_1/L_2 の係数である。
Sturm recurrence、rational endpoints、試験点、根の隔離区間を記載し、
「何の root isolation なのか」をコード依存にしなかった。
E.3/E.4 の証明は数値グリッドではなく exact rational polynomial certificates である。
E.4 の長い係数展開は掲載せず、対象多項式の定義、係数変換、全 zero-index set、
最小正係数を掲載した。独立 JSON は全係数を含む。

この Appendix E は short-edition-only override であり、元の A–F のファイルは変更していない。
元の E の結論を修正したのではなく、同じ結論への証明を読める形に再提示した。

## 独立検証の独立性と限界

追加 evaluator:
`code/revision/check_jict_short_independent.py`。

入力は原稿の需要・cost・compatibility rule、国別厚生、partition/deviation rule。
`canonical.py` や R2–R9 module を import していない。
既存 R4/R5 code はこの監査の先行する読解段階で見ている。このため完全な blind review
とは呼ばない。独立性は別 evaluator、原始条件からの行列再導出、別証明ルートにある。

- Canonical R と政府厚生差を新しい market-matrix routine から再構成。
- 全5 partitions の全 firm strategy profiles（SU は8、SW は64）を再最適化。
  任意の unilateral change（追加二標準の採用を含む）を比較し、witness で strict dominance を確認。
- Canonical symmetric/asymmetric d=0 witnesses で、5 partitions ×7 nonempty coalitions を
  strict と weak/Pareto の双方で独立列挙。
- S1 の全 triangular domain には、旧 R4 の検査法とは別の Bernstein certificate を新たに構成。
- Differentiated Cournot/Bertrand を別々の FOC で再導出し、原稿定義の多項式を生成。
  Bernstein coefficients の正確な符号・degree・zeros・minimum を確認し、
  逆に basis から元の polynomial を再構成して変換ミスを排除。
- E.3 の印刷された18係数も、再導出した配列と照合。
- 実際に配布する匿名 replication ZIP から再実行し、certificate JSON が byte-identical と確認するCI。
  同ZIPのR2–R9も実行する。

この検証だけで全パラメータの coalition stability を証明したとはしない。
領域上の定理は原稿の解析証明・元の exact-domain audits と合わせて評価し、
有限 witness の再構成は別の反例探索・導出照合として扱う。

## Lean と数学的認証の範囲

`formal/r7/` は変更していない。GitHub Paper CI の fresh execution で
`lake env lean R7Formal.lean` を実行する。初回PR CI
[38328420209](https://github.com/ryotamatsuki/private-compatibility-standards-coalitions/actions/runs/38328420209)
では FV1–FV5 と `R7 FORMAL VERIFICATION: PASS` を確認。
使用 axioms は propext, Classical.choice, Quot.sound のみ。

| Lean result | 認証する部分 | 認証しない部分 |
|---|---|---|
| FV1 | zero-network gap の代数的負符号 | 需要・厚生式自体の経済的導出 |
| FV2 | specified R の d に関する単調性 | Cournot から R を得る段階 |
| FV3/FV4 | assumed D/E/R に基づく post-gap・選好効果 | firm adoption equilibrium 全体 |
| FV5 | equality を含む payoff comparison の strict/weak blocking 区別 | coalition payoff・全partition偏差ゲーム |
| 対象外 | — | E.3/E.4 の matrix equilibrium/Bernstein、論文全体の自動形式化 |

Lean がローカルにインストールされているとは報告しない。実行・ログの認証主体は
GitHub CI であり、最新コミットの結果は PR Checks と紐付けて読む。

## 三つの判定を混同しない

| 対象 | 証明の正しさ | 計算の再現可能性 | 査読者の検証可能性 |
|---|---|---|---|
| 中心結果 | PASS: 原始条件からの再導出、exact witness、既存exact監査・解析証明 | PASS: 元監査と独立 evaluator、source ZIP | PASS: §2/4、C/Dの参照、CS/国内利潤の橋渡し |
| Appendix E | PASS: positive denominators、exact sign certificates、別 derivation | PASS: R4/R5、独立 Bernstein、配布 ZIP から同一 JSON | PASS: E.1–E.4が対象・方法・範囲・経済的結論を記載 |
| Stability | PASS: finite deviation rule、G、strict/weak 区別 | PASS: R6/R7/R9と別 evaluator の witness enumeration | PASS: §5 proof + G全偏差台帳 |

## 先行研究の照合と残る弱点

| 研究 | 確認した結果・均衡対象 | 本稿との実質的差分 |
|---|---|---|
| Gandal & Shy (2001) | conversion costs が standardization unions を支え、strong network effects は mutual recognition を促すという政府政策・厚生結果 | formal partition 選択後に企業が fixed setup と残余 marginal cost を負担する one-way adaptation を内生化し、同じ SU の continuation value を変える。彼らの theorem の一般化・同一 primitives での反証とは呼ばない。 |
| Takarada et al. (2020) | consumption externalities と national treatment の下で regional/multilateral core。local/transboundary の区別と fixed-cost extension | consumption standard の選択ではなく compatibility adoption の firm subgame を government ranking と接続。core/stability の既知の発想自体を新規性としない。 |
| Innocenti & Menicucci (2021) | 価格競争前の企業の compatibility choices、対称性・品質差下の企業均衡 | 国別厚生による正式制度の比較が対象。政府を足すだけでなく、post-agreement adaptation による継続利得変化を計算する。 |
| Ding et al. (2022) | private two-sided platforms の partial compatibility と coalition-proof outcomes | firm/platform coalition と government standards coalition は異なる。本稿の full-bypass stability は応用であり、一般的 coalition-proof compatibility theorem として売らない。 |
| Schmidt & Steingress (2022) | heterogeneity、costly standards adoption、scale/selection、trade effects | adoption/trade response から、home CS と national producer rents が government agreement ranking にどう入るかを解く。実証推定・heterogeneity を包含しない。 |

Primary evidence（公開URL）:
[Gandal/Shy author-university record](https://cris.tau.ac.il/en/publications/standardization-policy-and-international-trade/);
[Takarada full publisher text](https://onlinelibrary.wiley.com/doi/10.1111/jpet.12425);
[Innocenti/Menicucci full discussion paper](https://www.crctr224.de/research/discussion-papers/archive/dp278/@@download/file/CRCTR224_2021_278.pdf);
[Ding publisher record](https://www.sciencedirect.com/science/article/pii/S0264999322002322);
[Schmidt/Steingress author-hosted full article and appendix](https://juliaschmidtecon.github.io/No_double_standards_article_appendix.pdf).
Ding の publisher full-text access は制限があり、全証明の照合を行ったとはしない。
Gandal/Shy についても、公開著者記録の結果と書誌を確認した範囲を超える全文認証はしない。
Maggi/Mrazova は [NBER WP33318](https://www.nber.org/papers/w33318) の確認できる2024年 working-paper versionとして本文で扱い、
検証できない revised-2026 表記を削除した。未確認の「初めて」は一切追加しない。

§4 の三領域は恒等式からの elementary consequence であり、単独では強い貢献にならない。
残る貢献は R の equilibrium derivation、同一 primitives の strict adoption + strict reversal、
および政治結果と私的採用の portability を分離する sharp failure evidence の組合せである。
singleton-zero 仮定は実質的に重要であり、モデル選択の fragility は残る。
三国・線形・一国一企業・binary adoption・no transfers も制約である。
政策適用には setup costs、残余 cost、network benefits、home rents、reciprocity の測定が要る。
実証的な介入効果、global first best、positive-d stability は主張していない。

## Stage 11 / 13 / 14 と提出パッケージ

- Stage 11: PASS。原稿から reconstruction し、正しさと reader verifiability を独立評価。
  特に旧 Appendix E の「コードが保証する」記述を proof bridge で埋めた。
- Stage 13: PASS。contribution completeness、English、proof flow、cross-reference、figure/table、
  全頁の PDF inspection を実施。proof を削ってページ数を合わせていない。
- Stage 14: 公開ルールに対するファイル preflight PASS、live portal を含む総合判定は UNVERIFIED。
  本依頼は投稿操作を禁止しているので portal login/upload は行わない。Stage 15 は対象外。

JICT 公開規定と scope:
[submission guidelines](https://link.springer.com/journal/10842/submission-guidelines),
[aims and scope](https://link.springer.com/journal/10842/aims-and-scope),
[editorial board](https://link.springer.com/journal/10842/editorial-board)。
通常20頁未満の double-spaced 原稿、hard maximum40頁を区別する。
公開規定確認日は2026-10-13。

| 項目 | 結果 |
|---|---|
| 改稿前短縮版 | 18頁。ただし elsarticle review の1.5 spacing。 |
| 改稿後短縮版 | 19頁、12pt、1-inch margins、本文 baseline約24ptの true double spacing。 |
| 元の長稿 | 39頁。元ソースと既存 A–F・検証・Lean を保持。書式を揃えた圧縮率の比較とはしない。 |
| 補足 | 22頁、匿名 Online Resource1、A–G。 |
| Abstract / keywords | 約188 whitespace words、6 keywords、JEL有り。 |
| 参考文献・数式・図表・参照 | undefined reference/citation、duplicate labelなし。Table1境界が本文と一致。Fig1は数値illustrationと明示。 |
| 編集可能 source ZIP | main/SI はflat/self-contained。空ディレクトリで再compileし、shipped PDFと正規化textが一致。identified sourceは別ZIP。 |
| 匿名化 | reviewer PDFs、metadata、main/SI source ZIP、replication のnested ZIPまで検査。identified title/coverを分離。 |
| 複製可能性 | 新しい short replication archive にR2–R9、Lean、独立checker、exact JSON、actual short source ZIPを同梱。旧builderは変更なし。 |
| 視覚 | local main1–19、SI1–22、title/cover全頁確認。最終SIの未変更19頁は以前の画像とpixel-identical、変更1/2/15を再閲覧。図・表・多項式・頁境界に欠落なし。 |
| CI | PR [Checks](https://github.com/ryotamatsuki/private-compatibility-standards-coalitions/pull/34/checks) に各headの Paper CI と Short Preview。初回head862d7e9の4run全success。最終headの結果はChecksを正とし、初回successだけで代用しない。 |

本環境では harmless な小さい overfull 警告（本文約2.6pt、継承したSI Fの約1pt）が残ったが、
該当表示にclipping/重なりはない。大きな proof heading のoverflowとN_MS/Appendix Dの
壊れたalignはshort-only presentationで解消した。

ローカル最終表示確認後に実行環境がオフラインになった。
最終反映・source ZIP clean-room/配布ZIP監査は新しい GitHub CI にも移した。
この運用障害を数学的成功の根拠にしたり、未実行検査を PASS と扱ったりしない。
machine evidence は `r9_final_package_qa.json`、`independent-certificates.json`、
原文・改稿文の全差分は `r9_final_source_changes.patch` と PR Files changed に残る。

## 懐疑的編集者への独立評価

39頁版の長所は導出と監査の完全な保管である。ただし JICT の読者が中心の問いと
限界を判断するには本文が長い。最終19頁版は企業採用、政府順位、full-bypass stability の
論理を保ち、機械的な詳細は補足に移し、その補足の証明対象を明確にした。

投稿する価値はある。民間相互運用性が進むことと、政府が国際標準化を選ぶことを分離し、
企業の厳密な最適行動が実際に起きる同じ primitives において政府の順位が反転する点、
その政治効果が合理的な代替需要・network 仮定では消える点を同時に理解させるからである。
これは standards/competition/trade の接点にある限定的 applied-theory contributionである。

一方、編集者が generality、制度の実証的裏付け、既存compatibility理論を超える大きな
理論的新規性を求めるなら desk rejection は合理的に起こり得る。負の robustness は
この懸念をなくさない。最終稿の価値は適用限界を隠さず経済的メカニズムを検証できることにあり、
英文校閲や19頁化だけが科学的貢献を作ったわけではない。
