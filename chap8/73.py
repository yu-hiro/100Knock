import torch

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

def main():
    # 学習データの読み込み
    X_train = torch.load('data/X_train70.pt')
    y_train = torch.load('data/y_train70.pt')

    # ニューラルネットワークの定義
    net = Net(d_input, d_output)
    optimizer = torch.optim.SGD([net.fc.weight], lr=0.003)

    # クロスエントロピー損失の定義
    criterion = torch.nn.CrossEntropyLoss()

    # 学習
    for epoch in range(epochs):
        net.train() # 訓練モードに切り替える
        for i in range(X_train.shape[0]):
            optimizer.zero_grad()
            loss = criterion(net(X_train[:i]), y_train[:i])
            loss.backward()
            optimizer.step()

        print(f'epoch: {epoch + 1:3}/{epochs}, loss: {loss.data}')

    print(net.fc.weight)


if __name__ == '__main__':
    main()