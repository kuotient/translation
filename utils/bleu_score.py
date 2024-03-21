from nltk.translate.bleu_score import sentence_bleu,SmoothingFunction
from nltk.tokenize import word_tokenize
from utils.tokenizer import tokenize


def simple_score(text1, text2, lang="en"):
    if lang == "ko":
        reference = tokenize(text1)
        candidate = tokenize(text2)
    elif lang == "en":
        reference = word_tokenize(text1.lower())
        candidate = word_tokenize(text2.lower())
        
    print('reference', reference)
    print('candidate', candidate)
    # base = sentence_bleu([reference], reference)
    score = sentence_bleu([reference], candidate, smoothing_function=SmoothingFunction().method2)
    return score


if __name__ == "__main__":
    lang = input('lang(en,ko)>')
    while True:
        ref = input("ref: ")
        cand = input("cand: ")
        print('score',simple_score(ref, cand, lang))
