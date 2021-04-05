import re
import numpy as np
from wordfreq import word_frequency
from pygrammalecte import grammalecte_text
from pygrammalecte import GrammalecteGrammarMessage

# Get ponctuation score


def get_ponctuation_score(text):
  # Just check if there exists ponctuation
  if re.search(r"[;,.]", text):
    return 1
  return 0

# Get orthographoc score


def get_orthographic_score(full_text, splitted_sentence):
  error_count = 0
  for message in grammalecte_text(full_text):
      #Only detect orthographic errors
      if not isinstance(message, GrammalecteGrammarMessage):
        error_count += 1
  score_ortho = 1-error_count/len(splitted_sentence)
  return score_ortho

# Get grammatical score


def get_grammatical_score(brut_text, splitted_sentence):
  error_count = 0
  for message in grammalecte_text(brut_text):
      #Only detect grammar errors
      if isinstance(message, GrammalecteGrammarMessage):
        error_count += 1
  score_gramm = 1-error_count/len(splitted_sentence)
  return score_gramm

# Get rare words score
# We find the less used word in the sentence


def get_wordrarity_score(splitted_sentence):
  max_freq = word_frequency('est', 'fr')
  freq_m = []
  for word in splitted_sentence:
    freq_m.append(word_frequency(word, 'fr'))
  freq = min(freq_m)
  score_vocab = 1 - freq/max_freq
  return score_vocab

# Get vulgarity score


def get_badword_score(splitted_sentence, SW):
  count_swear = np.sum([splitted_sentence.count(word) for word in SW])
  score_swear = 1 - count_swear/len(splitted_sentence)
  return score_swear
