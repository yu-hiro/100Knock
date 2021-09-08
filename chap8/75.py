import torch
import matplotlib.pyplot as plt
import numpy as np

# パラメータ
d_input = 300
d_output = 4
epochs = 20

# 単層ニューラルネットワーク
class Net(torch.nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__() # 基底クラスの初期化
        self.fc = torch.nn.Linear(input_size, output_size, bias=False)

    # ある層からの入力xを受け取り、次の層への出力を計算する
    def forward(self, x):
        x = self.fc(x)

        return x

# 正解率を計算
def cal_acc(net, X, y):
    net.eval() # 推論モードに切り替える
    total = 0
    correct = 0
    with torch.no_grad():
        for i in range(X.shape[0]):
            pred = torch.argmax(net(X[i]), dim=-1)
            total += 1
            if pred == y[i]:
                correct += 1
    result = correct / total

    return result

def main():
    # データの読み込み
    X_train = torch.load('data/X_train70.pt')
    X_valid = torch.load('data/X_valid70.pt')
    y_train = torch.load('data/y_train70.pt')
    y_valid = torch.load('data/y_valid70.pt')

    # ニューラルネットワークの定義
    net = Net(d_input, d_output)
    optimizer = torch.optim.SGD([net.fc.weight], lr=0.003)

    # クロスエントロピー損失の定義
    criterion = torch.nn.CrossEntropyLoss()

    # 学習
    log_train = []
    log_valid = []
    for epoch in range(epochs):
        net.train()  # 訓練モードに切り替える
        for i in range(X_train.shape[0]):
            optimizer.zero_grad()
            loss = criterion(net(X_train[:i]), y_train[:i])
            loss.backward()
            optimizer.step()

        # 損失、正解率を計算
        train_loss = criterion(net(X_train), y_train)
        valid_loss = criterion(net(X_valid), y_valid)
        train_accuracy = cal_acc(net, X_train, y_train)
        valid_accuracy = cal_acc(net, X_valid, y_valid)
        # ログを取得する
        log_train.append([train_loss, train_accuracy])
        log_valid.append([valid_loss, valid_accuracy])

    # グラフにプロット
    fig, axes = plt.subplots(1, 2)
    axes[0].plot(np.array(log_train).T[0], label='train')
    axes[0].plot(np.array(log_valid).T[0], label='valid')
    axes[0].set_xlabel('epoch')
    axes[0].set_ylabel('loss')
    axes[1].plot(np.array(log_train).T[1], label='train')
    axes[1].plot(np.array(log_valid).T[1], label='valid')
    axes[1].set_xlabel('epoch')
    axes[1].set_ylabel('accuracy')
    # plt.show()  # 表示する場合
    plt.savefig('75_fig.png') # 画像保存する場合


if __name__ == '__main__':
    main()