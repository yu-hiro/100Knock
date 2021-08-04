import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import precision_score, recall_score, f1_score

# カテゴリとその予測確率を計算
def score_model(model, X):
  return [np.max(model.predict_proba(X), axis=1), model.predict(X)]

def main():
    # データ,モデル読み込み
    test = pd.read_csv('data/test.txt', header=0, sep='\t', encoding='utf-8')
    X_test = pd.read_csv('data/test.feature.txt', header=0, sep='\t', encoding='utf-8')
    model = pickle.load(open('model.pkl', 'rb'))

    # カテゴリとその予測確率を計算
    test_pred = score_model(model, X_test)

    y_true = test['CATEGORY']
    y_pred = test_pred[1]

    # 適合率を計測
    precision = precision_score(y_true, y_pred, average=None, labels=['b', 'e', 't', 'm'])
    precision_micro = precision_score(y_true, y_pred, average='micro')
    precision = np.append(precision, precision_micro)
    precision_macro = precision_score(y_true, y_pred, average='macro')
    precision = np.append(precision, precision_macro)

    # 再現率を計測
    recall = recall_score(y_true, y_pred, average=None, labels=['b', 'e', 't', 'm'])
    recall_micro = recall_score(y_true, y_pred, average='micro')
    recall = np.append(recall, recall_micro)
    recall_macro = recall_score(y_true, y_pred, average='macro')
    recall = np.append(recall, recall_macro)

    # F1スコアを計測
    f1 = f1_score(y_true, y_pred, average=None, labels=['b', 'e', 't', 'm'])
    f1_micro = f1_score(y_true, y_pred, average='micro')
    f1 = np.append(f1, f1_micro)
    f1_macro = f1_score(y_true, y_pred, average='macro')
    f1 = np.append(f1, f1_macro)

    # 計測結果をデータフレームに変換
    score = pd.DataFrame({'適合率': precision, '再現率': recall, 'F1スコア': f1},
                         index=['b', 'e', 't', 'm', 'マイクロ平均', 'マクロ平均'])
    print(score)

if __name__ == '__main__':
    main()