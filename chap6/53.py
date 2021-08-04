import numpy as np
import pandas as pd
import pickle

def score_model(model, X):
  return [np.max(model.predict_proba(X), axis=1), model.predict(X)]

def main():
    # データ,モデル読み込み
    X_train = pd.read_csv('data/train.feature.txt', header=0, sep='\t', encoding='utf-8')
    X_test = pd.read_csv('data/test.feature.txt', header=0, sep='\t', encoding='utf-8')
    model = pickle.load(open('model.pkl', 'rb'))

    # カテゴリとその予測確率を計算
    train_pred = score_model(model, X_train)
    test_pred = score_model(model, X_test)

    # 結果
    print('学習', train_pred)
    print('評価', test_pred)

if __name__ == '__main__':
    main()