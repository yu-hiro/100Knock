import pandas as pd
from sklearn.model_selection import train_test_split

r_filepath = 'data/newsCorpora.csv'


def main():
    # 2.情報源（publisher）が”Reuters”, “Huffington Post”, “Businessweek”, “Contactmusic.com”, “Daily Mail”の事例（記事）のみを抽出する．
    # 読み込み
    df = pd.read_csv(r_filepath, names=['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'],
                     header=None, sep='\t', encoding='utf-8')
    pubs = ['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail']
    df = df[df['PUBLISHER'].isin(pubs)]

    # 3.抽出された事例をランダムに並び替える．
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    print(df.head())

    # 4.データ分割
    train, test = train_test_split(df, test_size=0.2, random_state=42, stratify=df['CATEGORY'])
    valid, test = train_test_split(test, test_size=0.5, random_state=42, stratify=test['CATEGORY'])
    # データを保存
    train.to_csv('data/train.txt', columns=['TITLE','CATEGORY'], sep='\t', index=None)
    valid.to_csv('data/valid.txt', columns=['TITLE','CATEGORY'], sep='\t', index=None)
    test.to_csv('data/test.txt', columns=['TITLE','CATEGORY'], sep='\t', index=None)

    # 各カテゴリの事例数を出力
    print('train ---- ', train.shape)
    print(train['CATEGORY'].value_counts())
    print('valid ---- ', valid.shape)
    print(valid['CATEGORY'].value_counts())
    print('test ----', test.shape)
    print(test['CATEGORY'].value_counts())


if __name__ == '__main__':
    main()