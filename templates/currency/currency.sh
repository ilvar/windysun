rm idr-indonesian-rupiah
rm *.txt
wget  http://www.xe.com/currency/idr-indonesian-rupiah
grep -w IDRUSD11 idr-indonesian-rupiah > IDRUSD11
grep -w IDREUR12 idr-indonesian-rupiah > IDREUR12
html2text -o idr2usd.txt -ascii -nobs IDRUSD11
html2text -o idr2eur.txt -ascii -nobs IDREUR12
rm IDR*
awk '{print substr($0,1,4)}' idr2usd.txt > usd.txt
awk '{print substr($0,1,5)}' idr2eur.txt > eur.txt
rm idr*