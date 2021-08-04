# 没？
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer


def main():

    # データ読み込み
    train = pd.read_csv('data/train.txt', header=0, sep='\t', encoding='utf-8')
    valid = pd.read_csv('data/valid.txt', header=0, sep='\t', encoding='utf-8')
    test = pd.read_csv('data/test.txt', header=0, sep='\t', encoding='utf-8')
    # データを再結合
    df = pd.concat([train, valid, test], axis=0)
    df.reset_index(drop=True, inplace=True)

    # 前処理
    df['TITLE'] = df['TITLE'].map(lambda x: x.lower()) # 小文字に変換
    df['TITLE'] = df['TITLE'].map(lambda x: re.sub('[0-9]+', '0', x)) # 数字を0に統一
    print(df.head())

    # データ分割
    train_valid = df[:len(train) + len(valid)]
    test = df[len(train) + len(valid):]

    # 特徴量抽出
    vectorizer = TfidfVectorizer()
    X_train_valid = vectorizer.fit_transform(train_valid['TITLE'])
    X_test = vectorizer.transform(test['TITLE'])

    # ベクトルをデータフレームに変換
    X_train_valid = pd.DataFrame(X_train_valid.toarray(), columns=vectorizer.get_feature_names())
    X_train = X_train_valid[:len(train)]
    X_valid = X_train_valid[len(train):]
    X_test = pd.DataFrame(X_test.toarray(), columns=vectorizer.get_feature_names())

    # データを保存
    X_train.to_csv('data/train.feature.txt', sep='\t', index=None)
    X_valid.to_csv('data/valid.feature.txt', sep='\t', index=None)
    X_test.to_csv('data/test.feature.txt', sep='\t', index=None)

if __name__ == '__main__':
    main()
