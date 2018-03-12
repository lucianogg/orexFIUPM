NOMBRE_PAGINA=$1 # Sin lo de .HTML
FICHERO_A_FILTRAR="$1.html"
FICHERO_TRAS_FILTRAR="$1-filtered.html"

python ../filtro/filtro.py $FICHERO_A_FILTRAR
rm $FICHERO_A_FILTRAR
git add $FICHERO_TRAS_FILTRAR
