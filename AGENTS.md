# AGENTS.md — Repository Constitution

## Purpose

The purpose of this repository is not to discover additional model extensions. Its purpose is to convert the Stage-8 frozen theoretical core into a rigorous, reproducible, journal-ready manuscript.

The first-submission target is the *International Journal of Industrial Organization* (IJIO). Journal fit must never be achieved by changing mathematics, assumptions, or results without an explicit theory-repair stage.

The paper's identity is:

\[
\boxed{
\text{Private compatibility}
\rightarrow
\text{selective erosion of regional coalition rents}
\rightarrow
\text{government preference reversal}
\rightarrow
\text{multilateral strict blocking}
}
\]

The central mathematical mechanism is:

\[
\boxed{
\mathscr E_i-\mathscr D_i
\longrightarrow
-\mathscr D_i
}
\]

All work in this repository must strengthen the derivation, exposition, verification, interpretation, or literature positioning of this mechanism. It must not add results merely to make the model appear broader.

## Governing Documents and Source Hierarchy

Read these documents before modifying theory or manuscript content:

1. [`docs/CANONICAL_MODEL.md`](docs/CANONICAL_MODEL.md) — mathematical source of truth.
2. [`docs/THEOREM_LEDGER.md`](docs/THEOREM_LEDGER.md) — status and dependency of all results.
3. Stage 8 final audit.
4. Stage 7.5 outputs.
5. Stage 1–7 outputs.
6. Original undergraduate thesis.

[`docs/LITERATURE_POSITIONING.md`](docs/LITERATURE_POSITIONING.md) governs novelty claims and literature positioning.

A newer document is **not automatically mathematically correct**. If a canonical expression appears inconsistent with primitives, recompute from primitives. Do not silently repair the canonical theory and continue.

If an inconsistency is found, stop and report:

`THEORY INCONSISTENCY DETECTED`

with:

- problematic expression;
- primitive derivation;
- expected expression;
- actual expression;
- affected theorem(s).

No manuscript work may proceed until the inconsistency is explicitly resolved.

## Freeze Rules

Without an explicit post-Stage-8 theory-repair decision, do **not** add or substitute any of the following:

- new parameter;
- fourth country or full \(n\)-country model;
- heterogeneous firms;
- Bertrand competition;
- continuous interoperability;
- installed base;
- dynamics;
- innovation;
- security externalities;
- lobbying;
- standards-essential patents (SEP);
- transfers;
- empirical calibration;
- endogenous market size;
- alternative government objective;
- alternative coalition concept;
- alternative demand system.

This prohibition also applies to changes proposed as “robustness checks.” If a potentially useful extension is identified, record it only as:

`PROPOSED EXTENSION — NOT IMPLEMENTED`

Do not implement it in the canonical manuscript branch.

## Claim Discipline

Do not make broad priority claims such as:

> We are the first to combine governments and firm standard decisions.

> We are the first to show that compliance costs affect harmonization incentives.

> We are the first to show regional standards can block multilateral harmonization.

> We are the first to introduce fixed costs into standards competition.

> No previous paper considers private compatibility.

The default central novelty claim is:

> Private compatibility can destabilize an exclusionary formal standards coalition because firms can selectively circumvent the coalition's exclusionary benefits without providing reciprocal compatibility to coalition members.

A more mechanism-oriented formulation is:

> We identify a selective-erosion mechanism through which private compatibility choices can reverse governments' ranking between regional and multilateral standardization.

Any stronger claim requires explicit literature verification and an update to `docs/LITERATURE_POSITIONING.md` before it enters the manuscript.

## Mathematical Verification Rule

Every material expression intended for the paper must pass all three checks:

1. primitive derivation;
2. symbolic verification;
3. numerical sanity check.

Numerical evidence is never a substitute for proof.

When the verification pipeline is added in the next stage, SymPy/Python output and the LaTeX expression must agree exactly before the relevant section may advance.

## LaTeX Workflow Rule

Full-paper writing must use the following workflow:

\[
\boxed{
\text{one section}
\rightarrow
\text{save}
\rightarrow
\text{integrate}
\rightarrow
\text{compile whole manuscript}
\rightarrow
\text{audit}
}
\]

Do not generate the full manuscript in one pass.

At the completion of every section:

1. save the section as a `.tex` file;
2. integrate it into `main.tex` with `\input{}` or the repository's approved equivalent;
3. compile the whole manuscript;
4. require compilation errors = 0;
5. require undefined references = 0;
6. require undefined citations = 0;
7. require duplicate labels = 0;
8. audit notation against `docs/CANONICAL_MODEL.md`;
9. audit formulas against the verification scripts;
10. audit compliance with the freeze rules.

If any gate fails, do not proceed to the next section.

## Figure and Table Rule

Future numerical figures must be generated reproducibly from canonical formulas using Python. Do not manually type numerical values into figures.

Before creating a figure, state its purpose in one sentence. Each figure must be classified as one of:

- general theorem visualization;
- conceptual illustration;
- numerical illustration.

Record the formula or data source used to generate it. Numerical illustrations must never be presented as proofs.

Every figure and table retained in the paper must be explicitly referenced in the text. Delete unreferenced figures and tables.

## Literature Rule

Use the following source priority for citations:

1. original article;
2. publisher version;
3. author manuscript;
4. NBER, CEPR, or another official working-paper source.

Do not finalize citations from blogs, summary sites, or AI-generated bibliographies alone. Do not invent references, bibliographic metadata, DOIs, volumes, issues, pages, or publication years.

If a work is still a working paper as of the verified 2026 source, cite it as a working paper.

Use `docs/LITERATURE_POSITIONING.md` as the claim-control document. It is not a substitute for bibliographic verification.

## Coalition and Notation Discipline

- Use \(\rho\) for formal partitions. Do not use \(P\) for the formal partition because \(P\) is a Cournot profit block.
- Distinguish the profit block \(D\) from the reciprocal disadvantage \(\mathscr D_i\).
- Do not reintroduce the old incorrect IS welfare formula except when explicitly labelled as a historical error.
- Do not claim a unique \(SU_{12}\) in the symmetric Main Model.
- Do not make \(\delta\) a required Main-Model parameter.
- Do not state that network effects are necessary for the general selective-erosion mechanism.
- Do not restore the old SW-equilibrium proposition as a valid result.

## Stop Conditions

Stop manuscript work immediately if any of the following is detected:

- contradiction in a Stage-8 canonical formula;
- Main Theorem becomes tautological;
- disappearance of the claimed open parameter region;
- private-adoption equilibrium inconsistency;
- coalition-stability proof failure;
- reintroduction of the old welfare error;
- inability to verify the identity of a material citation or source.

The required status is then:

\[
\boxed{
\text{MANUSCRIPT HOLD — THEORY REPAIR REQUIRED}
}
\]

Do not work around the problem by adding a new mechanism or parameter.

## Current Repository Phase

Current phase: **repository governance and canonical-theory freeze**.

Manuscript prose, LaTeX scaffold, figures, and verification code are deliberately outside this phase.

The next authorized phase is: **modular LaTeX manuscript scaffold and reproducible verification pipeline**.
