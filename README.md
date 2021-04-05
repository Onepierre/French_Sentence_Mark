# French Sentence Mark
This code takes a text written by someone in French, and gives 5 marks:
One for the ponctuation, one for orthographic errors, one for grammatical errors, one for rarity of the words used and one for swear words.
The code won't work for other language.
## Environnement
### Install requirements
The code have been tested for
```
python==3.7
wordfreq==2.4.2
pygrammalecte==1.3.0
pyspellchecker==0.6.2
numpy==1.17.0
```
These are the core requirements which can be separately installed or just do:
```
pip install -r requirements.txt
```
or
```
python3.7 -m pip install -r requirements.txt
```
### Prepare your data
You need to put the different texts you want to analyze in the data/input.txt file.
Each text must be separated by a //FIN// marker.
### Run main.py
with the following command :
```
python main.py 
```
or
```
python3.7 main.py
```
The output is the file output.csv in the folder data. Each line contains the 5 scores the corresponding text in input got.
main takkes one optionnal argument if you want to print the results in the cms. In this case use```
```
python main.py True
```
or
```
python3.7 main.py True

```

For any issue or question, don't hesitate to contact me at pierre.clarou@polytechnique.org.
