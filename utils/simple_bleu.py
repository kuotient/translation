from nltk.translate.bleu_score import sentence_bleu,SmoothingFunction
from nltk.tokenize import word_tokenize
from utils.tokenizer import tokenize
import re

def is_korean(text):
    for char in text:
        if '가' <= char <= '힣':
            return True
    return False

def simple_score(text1, text2):
    text1 = re.sub("\n", " ", text1)
    text2 = re.sub("\n", " ", text2)
    if is_korean(text1):
        reference = tokenize(text1)
        candidate = tokenize(text2)
    else:
        reference = word_tokenize(text1.lower())
        candidate = word_tokenize(text2.lower())
    # base = sentence_bleu([reference], reference)
    score = sentence_bleu([reference], candidate, smoothing_function=SmoothingFunction().method2)
    return score


if __name__ == "__main__":
    lang = input('lang(en,ko)>')
    while True:
        ref = input("ref: ")
        cand = input("cand: ")
        print('score',simple_score(ref, cand, lang))
