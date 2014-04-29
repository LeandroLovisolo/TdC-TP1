.PHONY: all clean informe.pdf graficos graficos-altopalermo graficos-mcdonalds graficos-starbucks

all: informe.pdf

clean:
	rm -f informe.pdf tex/*.pdf tex/*.aux tex/*.log tex/*.toc

informe.pdf: tex/informe.tex tex/*.jpg tex/*.png
	cd tex; pdflatex -interaction=nonstopmode -halt-on-error informe.tex && \
	        pdflatex -interaction=nonstopmode -halt-on-error informe.tex
	cp tex/informe.pdf .

graficos: graficos-altopalermo graficos-mcdonalds graficos-starbucks

graficos-altopalermo:
	./entropia.py source < data/altopalermo.txt > tmp.txt
	./histograma tmp.txt altopalermo-source
	./entropia.py destination < data/altopalermo.txt > tmp.txt
	./histograma tmp.txt altopalermo-destination
	rm tmp.txt

graficos-mcdonalds:
	./entropia.py source < data/mcdonalds.txt > tmp.txt
	./histograma tmp.txt mcdonalds-source
	./entropia.py destination < data/mcdonalds.txt > tmp.txt
	./histograma tmp.txt mcdonalds-destination
	rm tmp.txt

graficos-starbucks:
	./entropia.py source < data/starbucks.txt > tmp.txt
	./histograma tmp.txt starbucks-source
	./entropia.py destination < data/starbucks.txt > tmp.txt
	./histograma tmp.txt starbucks-destination
	rm tmp.txt