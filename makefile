.PHONY: all clean informe.pdf

all: informe.pdf

clean:
	rm -f informe.pdf tex/*.pdf tex/*.aux tex/*.log tex/*.toc

informe.pdf: tex/informe.tex tex/*.jpg tex/*.png
	cd tex; pdflatex -interaction=nonstopmode -halt-on-error informe.tex && \
	        pdflatex -interaction=nonstopmode -halt-on-error informe.tex
	cp tex/informe.pdf .