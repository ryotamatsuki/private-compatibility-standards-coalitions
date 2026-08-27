PYTHON ?= python
LATEXMK ?= latexmk
LATEX_FLAGS := -pdf -interaction=nonstopmode -halt-on-error

.PHONY: all verify verify-symbolic verify-welfare verify-numeric figures tables tables-check paper check-paper-log clean

all: verify figures tables tables-check paper

verify-symbolic:
	$(PYTHON) code/verify_symbolic.py

verify-welfare:
	$(PYTHON) code/verify_welfare_inequalities.py

verify-numeric:
	$(PYTHON) code/verify_numeric.py

verify: verify-symbolic verify-welfare verify-numeric

figures:
	$(PYTHON) code/make_figures.py
	@test -s paper/figures/generated/figure_01_timing.pdf
	@test -s paper/figures/generated/figure_02_selective_erosion.pdf
	@test -s paper/figures/generated/figure_03_f_regions.pdf

tables:
	$(PYTHON) code/make_tables.py
	@test -s paper/tables/generated/table_cournot_blocks.tex
	@test -s paper/tables/generated/table_thresholds.tex
	@test -s paper/tables/generated/table_stability_regions.tex

# Syntax-check generated table fragments independently of the full manuscript.
tables-check: tables
	@mkdir -p build/table-check
	@printf '%s\n' \
		'\documentclass{article}' \
		'\usepackage{booktabs}' \
		'\usepackage{graphicx}' \
		'\begin{document}' \
		'\input{../../paper/tables/generated/table_cournot_blocks}' \
		'\input{../../paper/tables/generated/table_thresholds}' \
		'\input{../../paper/tables/generated/table_stability_regions}' \
		'\end{document}' > build/table-check/table_check.tex
	@cd build/table-check && $(LATEXMK) $(LATEX_FLAGS) -bibtex- table_check.tex
	@echo "TABLE LATEX CHECK: PASS"

paper:
	@cd paper && if grep -RqsE '\\cite[a-zA-Z*]*\{' sections appendix main.tex && grep -qsE '^[[:space:]]*@' references.bib; then \
		$(LATEXMK) $(LATEX_FLAGS) main.tex; \
	else \
		$(LATEXMK) $(LATEX_FLAGS) -bibtex- main.tex; \
	fi
	@$(MAKE) check-paper-log
	@echo "LATEX COMPILE: PASS"

check-paper-log:
	@! grep -Eqi 'LaTeX Warning: (Citation|Reference).*undefined|There were undefined (references|citations)|multiply defined|multiply-defined' paper/main.log || \
		(echo "LATEX REFERENCE/CITATION/LABEL GATE: FAIL"; exit 1)
	@echo "LATEX REFERENCE/CITATION/LABEL GATE: PASS"

clean:
	@cd paper && $(LATEXMK) -C main.tex >/dev/null 2>&1 || true
	@rm -f paper/figures/generated/*.pdf
	@rm -f paper/tables/generated/*.tex
	@rm -rf build
