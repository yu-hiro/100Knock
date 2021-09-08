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
    X_test = torch.load('data/X_test70.pt')
    y_train = torch.load('data/y_train70.pt')
    y_test = torch.load('data/y_test70.pt')

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

    # 正解率を計算する
    train_accuracy = cal_acc(net, X_train, y_train)
    test_accuracy = cal_acc(net, X_test, y_test)
    print('正解率(学習):{:.3f}'.format(train_accuracy))
    print('正解率(評価):{:.3f}'.format(test_accuracy))

if __name__ == '__main__':
    main()