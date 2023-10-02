prefix=report

$(prefix).pdf: $(prefix).tex $(prefix).bbl $(shell ls *.tex | grep -v $(prefix).tex)
	pdflatex $<
	pdflatex $<

$(prefix).bbl: $(prefix).tex $(prefix).bib $(shell ls *.tex | grep -v $(prefix).tex)
	pdflatex $<
	bibtex $(prefix)
