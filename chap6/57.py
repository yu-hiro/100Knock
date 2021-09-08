import numpy as np
import pandas as pd
import pickle

def main():
    # データ,モデル読み込み
    X_train = pd.read_csv('data/train.feature.txt', header=0, sep='\t', encoding='utf-8')
    model = pickle.load(open('model.pkl', 'rb'))

    # 重みの高い特徴量,低い特徴量トップ10を確認
    features = X_train.columns.values
    index = [i for i in range(1, 11)]
    for c, coef in zip(model.classes_, model.coef_):
        print(f'【カテゴリ】{c}')
        best10 = pd.DataFrame(features[np.argsort(coef)[::-1][:10]], columns=['トップ10'], index=index).T
        worst10 = pd.DataFrame(features[np.argsort(coef)[:10]], columns=['ワースト10'], index=index).T
        print(pd.concat([best10, worst10], axis=0))
        print('\n')

if __name__ == '__main__':
    main()