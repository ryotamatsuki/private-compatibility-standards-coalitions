from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "paper" / "tables" / "generated"
DST = ROOT / "paper-ja" / "tables" / "generated"

REPLACEMENTS = {
    "Cournot building blocks. The table reports the equilibrium quantities, firm-profit blocks, and consumer-surplus blocks for the four product-market configurations used throughout the analysis.": "Cournot均衡の構成ブロック。本表は、分析全体で用いる4つの生産物市場構成について、均衡数量、企業利益ブロック、消費者余剰ブロックを示す。",
    "Market configuration & Firm type & Quantity & Profit & CS block": "市場構成 & 企業類型 & 数量 & 利益 & CSブロック",
    "Complete compatibility": "完全互換",
    "Compatible firm": "互換企業",
    "SU member market": "SU加盟国市場",
    "Bloc firm": "ブロック企業",
    "Excluded outsider": "排除された域外企業",
    "SU outsider market": "SU域外国市場",
    "Native outsider": "域外国の自国企業",
    "Separate standards (SW)": "各国別標準 (SW)",
    "Native firm": "自国企業",
    "Foreign firm": "外国企業",
    "Private-adoption incentives and thresholds. The table reports the operating-profit gains associated with adopting an additional formal standard and the resulting fixed-cost thresholds in the symmetric Main Model.": "私的採用の誘因と閾値。本表は、追加的な正式標準の採用に伴う営業利益増分と、対称的Main Modelにおける固定費用閾値を示す。",
    "Decision & Rival adoption state & Operating-profit gain & Fixed-cost threshold": "意思決定 & ライバルの採用状態 & 営業利益増分 & 固定費用閾値",
    "SU outsider: adopt bloc standard": "SU域外企業：ブロック標準を採用",
    "SU member: adopt outsider standard": "SU加盟企業：域外標準を採用",
    "Other member has not adopted": "他の加盟企業は未採用",
    "Other member has adopted": "他の加盟企業は採用済み",
    "SW foreign firm: adopt target standard": "SW外国企業：対象国標準を採用",
    "Rival foreign firm has not adopted": "ライバル外国企業は未採用",
    "Rival foreign firm has adopted": "ライバル外国企業は採用済み",
    "Relevant no-adoption lower boundary": "関連する非採用領域の下限",
    "SW unilateral or any post-rival adoption": "SW単独採用またはライバル採用後の採用",
    "Headline formal-stability regions in the symmetric Main Model for $(c,v)\\in\\Omega_0$. The table reports the private-adoption continuation state and the strict-blocking stable set.": "$(c,v)\\in\\Omega_0$ における対称的Main Modelの主要な正式制度安定領域。本表は、私的採用の継続状態と厳格ブロッキングの安定集合を示す。",
    "Fixed-cost region & Private-adoption continuation & Stable formal partitions": "固定費用領域 & 私的採用の継続状態 & 安定な正式分割",
    "Outside the headline theorem": "主要定理の対象外",
    "Not characterized here": "ここでは特徴付けない",
    "Outsider-only bypass in each SU; no SW adoption": "各SUで域外企業のみ迂回；SWでは採用なし",
    "No SU or SW private adoption": "SU・SWとも私的採用なし",
}


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    names = ["table_cournot_blocks.tex", "table_thresholds.tex", "table_stability_regions.tex"]
    for name in names:
        text = (SRC / name).read_text(encoding="utf-8")
        for en, ja in REPLACEMENTS.items():
            text = text.replace(en, ja)
        (DST / name).write_text(text, encoding="utf-8")
        print(f"generated paper-ja/tables/generated/{name}")


if __name__ == "__main__":
    main()
