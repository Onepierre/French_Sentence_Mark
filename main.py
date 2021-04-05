import csv
import sys

from scorer import *


def purify_sentence(sentence):
  #Replace ponctuation by whitespaces
  sentence = sentence.replace(',', '').replace(
      '.', ' ').replace('?', ' ').replace('!', ' ')

  #Remove multiple whitespace
  sentence = re.sub('\s+', ' ', sentence)

  #Remove the whitespace at the beginning
  if sentence[0] == " ":
    sentence = sentence[1:]
  #Remove the whitespace at the end
  if sentence =='':
    return sentence
  if sentence[-1] == " ":
    sentence = sentence[:-1]
  return sentence


def load_bad_words():
  #Load the badwords
  SW = []
  with open("data/swearwords.txt", "r") as f:
    for x in f:
      SW.append(x[:-1])
  return SW

def main(printing = False):
  scores = []
  with open('data/input.txt',"r") as f:
    brut_text = f.read()
  SW = load_bad_words()

  list_of_texts = brut_text.split("//FIN//")
  for text in list_of_texts:
    score = [0, 0, 0, 0, 0]
    score[0] = get_ponctuation_score(text)
    #ponct/ortho/gramm/rare/swear
    sentences_brut = text.split(".")
    sentences = []

    for sent in sentences_brut:
      sent = re.sub('\s+', ' ', sent)
      if not (sent == '' or sent == ' '):
        sentences.append(sent)

    for sentence in sentences:
      sent_pur = purify_sentence(sentence)
      splitted_sentence = re.split(r"[;,'.\s]\s*", sent_pur)
      score[1] += get_orthographic_score(sent_pur, splitted_sentence)
      score[2] += get_grammatical_score(sent_pur, splitted_sentence)
      score[3] += get_wordrarity_score(splitted_sentence)
      score[4] += get_badword_score(splitted_sentence, SW)
    score[1] /= len(sentences)
    score[2] /= len(sentences)
    score[3] /= len(sentences)
    score[4] /= len(sentences)
    if printing:
      print(text)
      print(score)
    scores.append(score)
  with open("data/output.csv","w") as f:
    spamwriter = csv.writer(f, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for s in scores:
      spamwriter.writerow(s)
    

if __name__ == "__main__":
    # execute only if run as a script
    if len(sys.argv) > 1:
      main(sys.argv[1])
    else:
      main()
