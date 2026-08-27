PYTHON ?= python
LATEXMK ?= latexmk
LATEX_FLAGS := -lualatex -interaction=nonstopmode -halt-on-error

.PHONY: all prepare compile audit check-log clean

all: compile audit

prepare:
	$(MAKE) -C .. figures tables
	$(PYTHON) scripts/translate_generated_tables.py

compile: prepare
	$(LATEXMK) $(LATEX_FLAGS) main-ja.tex
	$(MAKE) check-log
	@echo "JAPANESE LATEX COMPILE: PASS"

check-log:
	@! grep -Eqi 'LaTeX Warning: (Citation|Reference).*undefined|There were undefined (references|citations)|multiply defined|multiply-defined' main-ja.log || \
		(echo "JAPANESE REFERENCE/CITATION/LABEL GATE: FAIL"; exit 1)
	@echo "JAPANESE REFERENCE/CITATION/LABEL GATE: PASS"

audit: prepare
	$(PYTHON) scripts/audit_correspondence.py

clean:
	$(LATEXMK) -C main-ja.tex >/dev/null 2>&1 || true
	@rm -f tables/generated/*.tex
