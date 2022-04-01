# LawTech-visualization
Generate pdfs of the text with the highlighting controlled by the json files

## How to use
1. install fpdf if you don't have it yet
```
pip install fpdf
```
2. clone this repository
```
git clone git@github.com:Glanfaloth/LawTech-visualization.git
```
3. place the data folder inside
```
    .
    ├── visualization.py
    ├── data
    │   ├── 1_0_0.json
    │   ├── 1_0_1.json
    │   ├── 1_1_0.json
    │   ├── 1_1_1.json
    │   └── ...
    └── ...
```
4. run the script
```
python3 visualization.py
```
5. pdf files will be generated automatically
