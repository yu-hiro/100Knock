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
    y_train = torch.load('data/y_train70.pt')

    # ニューラルネットワークの定義
    net = Net(d_input, d_output)

    # クロスエントロピー損失の定義
    criterion = torch.nn.CrossEntropyLoss()

    # クロスエントロピー損失と、重み行列に対する勾配を計算
    net.zero_grad()  # 勾配を初期化
    l_1 = criterion(net(X_train[:1]), y_train[:1])
    l_1.backward()
    grad_1 = net.fc.weight.grad
    print(l_1)
    print(grad_1)

    net.zero_grad()  # 勾配を初期化
    l = criterion(net(X_train[:4]), y_train[:4])
    l.backward()
    grad = net.fc.weight.grad
    print(l)
    print(grad)


if __name__ == '__main__':
    main()