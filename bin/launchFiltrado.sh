

for file in $1/*
do
    # echo $file

    if [ -f $file ] && [ ${file: -4} == ".org" ]; then
	echo $file
	export infile=$file
	name="$(basename $file)"
	export outfile="$(dirname $file)/exports/${name%.*}.html"
	$1/bin/toHtml.el

	FICHERO_A_FILTRAR=$outfile
	FICHERO_TRAS_FILTRAR="${name%.*}.html"
	python $1/bin/filtro.py $FICHERO_A_FILTRAR
	rm $FICHERO_A_FILTRAR
	#rm "$(echo $FICHERO_A_FILTRAR)~"
	#git add $FICHERO_TRAS_FILTRAR
    fi
done
