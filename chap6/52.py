import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

def main():
    # データ読み込み
    train = pd.read_csv('data/train.txt', header=0, sep='\t', encoding='utf-8')
    X_train = pd.read_csv('data/train.feature.txt', header=0, sep='\t', encoding='utf-8')

    # モデルの学習
    model = LogisticRegression(random_state=42, max_iter=10000)
    model.fit(X_train, train['CATEGORY'])

    # モデルを保存
    pickle.dump(model, open('model.pkl', 'wb'))

if __name__ == '__main__':
    main()