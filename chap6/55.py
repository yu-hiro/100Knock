import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import confusion_matrix

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

    # 混同行列の作成(学習データ)
    train_cm = confusion_matrix(train['CATEGORY'], train_pred[1])
    print('学習')
    print(train_cm)

    # 混同行列の作成(評価データ)
    test_cm = confusion_matrix(test['CATEGORY'], test_pred[1])
    print('評価')
    print(test_cm)


if __name__ == '__main__':
    main()