import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import optuna

# データ読み込み
train = pd.read_csv('data/train.txt', header=0, sep='\t', encoding='utf-8')
valid = pd.read_csv('data/valid.txt', header=0, sep='\t', encoding='utf-8')
test = pd.read_csv('data/test.txt', header=0, sep='\t', encoding='utf-8')
X_train = pd.read_csv('data/train.feature.txt', header=0, sep='\t', encoding='utf-8')
X_valid = pd.read_csv('data/valid.feature.txt', header=0, sep='\t', encoding='utf-8')
X_test = pd.read_csv('data/test.feature.txt', header=0, sep='\t', encoding='utf-8')

def score_model(model, X):
  return [np.max(model.predict_proba(X), axis=1), model.predict(X)]

# 最適化対象を指定
def objective(trial):
    # チューニング対象パラメータのセット
    l1_ratio = trial.suggest_uniform('l1_ratio', 0, 1)
    C = trial.suggest_loguniform('C', 1e-4, 1e4)

    # モデルの学習
    model = LogisticRegression(random_state=42, max_iter=10000, l1_ratio=l1_ratio, C=C)
    model.fit(X_train, train['CATEGORY'])

    # 予測値の取得
    valid_pred = score_model(model, X_valid)

    # 正解率の算出
    valid_accuracy = accuracy_score(valid['CATEGORY'], valid_pred[1])
    return valid_accuracy

def main():
    # 最適化
    study = optuna.create_study(direction='maximize')
    study.optimize(objective, timeout=3600)
    trial = study.best_trial
    print('パラメータ:')
    for key, value in trial.params.items():
        print('    {}: {}'.format(key, value))

    # パラメータの設定
    l1_ratio = trial.params['l1_ratio']
    #l1_ratio = 0.21665687910675627
    C = trial.params['C']
    #C = 335.6753938719889

    # モデルの学習
    model = LogisticRegression(random_state=42, max_iter=10000, l1_ratio=l1_ratio, C=C)
    model.fit(X_train, train['CATEGORY'])

    # カテゴリとその予測確率を計算
    train_pred = score_model(model, X_train)
    valid_pred = score_model(model, X_valid)
    test_pred = score_model(model, X_test)

    # 正解率を計測
    train_accuracy = accuracy_score(train['CATEGORY'], train_pred[1])
    print('正解率(学習):{:.3f}'.format(train_accuracy))
    valid_accuracy = accuracy_score(valid['CATEGORY'], valid_pred[1])
    print('正解率(検証):{:.3f}'.format(valid_accuracy))
    test_accuracy = accuracy_score(test['CATEGORY'], test_pred[1])
    print('正解率(評価):{:.3f}'.format(test_accuracy))

if __name__ == '__main__':
    main()