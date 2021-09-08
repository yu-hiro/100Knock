import torch

# パラメータ
d_input = 300
d_output = 4

# 単層ニューラルネットワーク
class Net(torch.nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__() # 基底クラスの初期化
        self.fc = torch.nn.Linear(input_size, output_size, bias=False)

    # ある層からの入力xを受け取り、次の層への出力を計算する
    def forward(self, x):
        x = self.fc(x)

        return x

def main():
    # 学習データの読み込み
    X_train = torch.load('data/X_train70.pt')

    # ニューラルネットワークの定義
    net = Net(d_input, d_output)

    # 行列の積を計算
    y_hat_1 = torch.softmax(net(X_train[:1]), dim=1)
    Y_hat = torch.softmax(net(X_train[:4]), dim=1)

    # 結果を表示
    print(y_hat_1)
    print(Y_hat)


if __name__ == '__main__':
    main()