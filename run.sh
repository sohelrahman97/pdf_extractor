cd 'source'
cp *.pdf '../'
cd '..'
python3 -W "ignore" pdf_extract.py
chmod +w *.pdf
mv *.pdf 'legacy'
mv *.txt 'output'
