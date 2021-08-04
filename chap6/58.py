import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# カテゴリとその予測確率を計算
def score_model(model, X):
  return [np.max(model.predict_proba(X), axis=1), model.predict(X)]

def main():

    result_58 = []
    for C in np.logspace(-5, 4, 10, base=10):
        # データ読み込み
        train = pd.read_csv('data/train.txt', header=0, sep='\t', encoding='utf-8')
        X_train = pd.read_csv('data/train.feature.txt', header=0, sep='\t', encoding='utf-8')
        valid = pd.read_csv('data/valid.txt', header=0, sep='\t', encoding='utf-8')
        X_valid = pd.read_csv('data/valid.feature.txt', header=0, sep='\t', encoding='utf-8')
        test = pd.read_csv('data/test.txt', header=0, sep='\t', encoding='utf-8')
        X_test = pd.read_csv('data/test.feature.txt', header=0, sep='\t', encoding='utf-8')

        # モデルの学習
        model = LogisticRegression(random_state=42, max_iter=10000)
        model.fit(X_train, train['CATEGORY'])

        # カテゴリとその予測確率を計算
        train_pred = score_model(model, X_train)
        valid_pred = score_model(model, X_valid)
        test_pred = score_model(model, X_test)

        # 正解率を計測
        train_accuracy = accuracy_score(train['CATEGORY'], train_pred[1])
        valid_accuracy = accuracy_score(valid['CATEGORY'], valid_pred[1])
        test_accuracy = accuracy_score(test['CATEGORY'], test_pred[1])

        # 計測結果
        result_58.append([C, train_accuracy, valid_accuracy, test_accuracy])

    # グラフ化
    result = np.array(result_58).T
    plt.plot(result[0], result[1], label='train')
    plt.plot(result[0], result[2], label='valid')
    plt.plot(result[0], result[3], label='test')
    plt.ylim(0, 1.1)
    plt.ylabel('Accuracy')
    plt.xscale('log')
    plt.xlabel('C')
    plt.legend()
    # plt.show()
    plt.savefig('58_fig.png') # 画像保存する場合

if __name__ == '__main__':
    main()
