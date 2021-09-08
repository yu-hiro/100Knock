import pandas as pd
from gensim.models import KeyedVectors
import string
import torch

# 50で作成したデータ (columns=['TITLE','CATEGORY'], sep='\t', index=None)
train50 = 'data/train.txt'
valid50 = 'data/valid.txt'
test50 = 'data/test.txt'

# 7章で用いた単語ベクトル
word_vec7 = 'data/GoogleNews-vectors-negative300.bin.gz'

def transform_word_vec(text, model):
    # 記号をスペースに置換し、スペースで区切ってリスト化
    table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    words = text.translate(table).split()
    # 1語ずつベクトル化
    vec = [model[word] for word in words if word in model]

    # 見出しに含まれる単語のベクトルの平均を返す
    return torch.tensor(sum(vec) / len(vec))

def main():
    # 50で作成したデータの読み込み
    train = pd.read_csv(train50, header=0, sep='\t', encoding='utf-8')
    valid = pd.read_csv(valid50, header=0, sep='\t', encoding='utf-8')
    test = pd.read_csv(test50, header=0, sep='\t', encoding='utf-8')
    # 単語ベクトルの読み込み
    model = KeyedVectors.load_word2vec_format(word_vec7, binary=True)

    # 特徴量行列を作成
    X_train = torch.stack([transform_word_vec(text, model) for text in train['TITLE']])
    X_valid = torch.stack([transform_word_vec(text, model) for text in valid['TITLE']])
    X_test = torch.stack([transform_word_vec(text, model) for text in test['TITLE']])
    # ラベルベクトルを作成
    category = {'b': 0, 't': 1, 'e': 2, 'm': 3}
    y_train = torch.tensor(train['CATEGORY'].map(lambda x: category[x]).values)
    y_valid = torch.tensor(valid['CATEGORY'].map(lambda x: category[x]).values)
    y_test = torch.tensor(test['CATEGORY'].map(lambda x: category[x]).values)

    # 作成した行列・ベクトルを保存
    torch.save(X_train, 'data/X_train70.pt')
    torch.save(X_valid, 'data/X_valid70.pt')
    torch.save(X_test, 'data/X_test70.pt')
    torch.save(y_train, 'data/y_train70.pt')
    torch.save(y_valid, 'data/y_valid70.pt')
    torch.save(y_test, 'data/y_test70.pt')


if __name__ == '__main__':
    main()