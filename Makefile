.PHONY: all clean informe.pdf graficos graficos-altopalermo graficos-mcdonalds graficos-starbucks estadisticas

all: informe.pdf

clean:
	rm -f informe.pdf tex/*.pdf tex/*.aux tex/*.log tex/*.toc

informe.pdf: tex/informe.tex tex/*.jpg tex/*.png
	cd tex; pdflatex -interaction=nonstopmode -halt-on-error informe.tex && \
	        pdflatex -interaction=nonstopmode -halt-on-error informe.tex
	cp tex/informe.pdf .

graficos: graficos-altopalermo graficos-mcdonalds graficos-starbucks

graficos-altopalermo:
	./informacion source 10 < data/altopalermo.txt > tmp.txt
	./graficar_informacion tmp.txt altopalermo-source
	./informacion destination 10 < data/altopalermo.txt > tmp.txt
	./graficar_informacion tmp.txt altopalermo-destination
	rm tmp.txt

graficos-mcdonalds:
	./informacion source 10 < data/mcdonalds.txt > tmp.txt
	./graficar_informacion tmp.txt mcdonalds-source
	./informacion destination 10 < data/mcdonalds.txt > tmp.txt
	./graficar_informacion tmp.txt mcdonalds-destination
	rm tmp.txt

graficos-starbucks:
	./informacion source 10 < data/starbucks.txt > tmp.txt
	./graficar_informacion tmp.txt starbucks-source
	./informacion destination 10 < data/starbucks.txt > tmp.txt
	./graficar_informacion tmp.txt starbucks-destination
	rm tmp.txt

estadisticas:
	./estadisticas > tex/estadisticas.tex