import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score

def score_model(model, X):
  return [np.max(model.predict_proba(X), axis=1), model.predict(X)]

def main():
    # データ,モデル読み込み
    train = pd.read_csv('data/train.txt', header=0, sep='\t', encoding='utf-8')
    test = pd.read_csv('data/test.txt', header=0, sep='\t', encoding='utf-8')
    X_train = pd.read_csv('data/train.feature.txt', header=0, sep='\t', encoding='utf-8')
    X_test = pd.read_csv('data/test.feature.txt', header=0, sep='\t', encoding='utf-8')
    model = pickle.load(open('model.pkl', 'rb'))

    # カテゴリとその予測確率を計算
    train_pred = score_model(model, X_train)
    test_pred = score_model(model, X_test)

    # 正解率を計測
    train_accuracy = accuracy_score(train['CATEGORY'], train_pred[1])
    print('正解率(学習):{:.3f}'.format(train_accuracy))
    test_accuracy = accuracy_score(test['CATEGORY'], test_pred[1])
    print('正解率(評価):{:.3f}'.format(test_accuracy))

if __name__ == '__main__':
    main()