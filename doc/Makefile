
all: OpSipBook

PHONY: refresh

OpSipBook: OpSipBook.pdf

restapi: restapi.pdf

OpSipBook.pdf: main.tex authoring.tex api/contents.tex api/restapi.tex
	pdflatex -jobname=OpSipBook main

restapi.pdf: api/main.tex api/contents.tex api/restapi.tex
	pdflatex -jobname=restapi api/main

clean:
	rm -f *.pdf *.log *.aux *~

refresh: wiki/Installazione_di_Opsip46.html
	./html2latex wiki/Installazione_di_Opsip46.html

wiki/Installazione_di_Opsip46.html:
	wget http://track.sip2ser.net/projects/sip2ser/wiki/Installazione_di_Opsip46.txt -O wiki/Installazione_di_Opsip46.html
