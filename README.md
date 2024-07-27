# pdf_extractor

pdf_extractor is a project that automates text extraction from a document that contains work schedule

## Under the hood

This is a very simple python program, so it is very lightweight. Two main python libraries have been used:

* <u>Pandas</u>: a software library written for the Python programming language for data manipulation and analysis. 
* <u>Tabula</u>: tabula-py is a simple Python wrapper of tabula-java, which can read table of PDF. 

## Running the code

### Using main program directly
You can use the program directly using:
  ```sh
python pdf_extract.py
  ```

### Using script to automate data extraction
Make the script executable:
  ```sh
chmod +x run.sh
  ```
Run the script:  
  ```sh
./run.sh
  ```

Script will be run. It will obtain PDF file from specified location, store it locally, extract the desired data, and clean up the program directory.

## Tailoring to your needs
You can go into the code and input the location which you want pdf_extractor to obtain the raw data from.

## Documentation
* https://tabula-py.readthedocs.io/en/latest/
* https://pandas.pydata.org/docs/

