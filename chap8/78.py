import torch
from torch.utils.data import TensorDataset, DataLoader
import time

# パラメータ
d_input = 300
d_output = 4
epochs = 20
batch_size = [1, 2, 4, 8, 16, 32, 64, 128]

# 単層ニューラルネットワーク
class Net(torch.nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__() # 基底クラスの初期化
        self.fc = torch.nn.Linear(input_size, output_size, bias=False)

    # ある層からの入力xを受け取り、次の層への出力を計算する
    def forward(self, x):
        x = self.fc(x)

        return x

# 損失を計算
def cal_loss(net, loader_data, criterion, device):
    net.eval()  # 推論モードに切り替える
    loss = 0.0

    for data, target in loader_data:
        data = data.to(device)  # GPUに送る
        target = target.to(device)  # GPUに送る
        output = net(data)
        loss += criterion(output, target)

    result = loss / len(loader_data)

    return result

# 正解率を計算
def cal_acc(net, loader_data, device):
    net.eval() # 推論モードに切り替える
    correct = 0

    for data, target in loader_data:
        data = data.to(device)  # GPUに送る
        target = target.to(device)  # GPUに送る
        output = net(data)

        pred = torch.argmax(output, dim=-1)
        correct += (pred == target).sum().item()

    total = len(loader_data.dataset)
    result = correct / total

    return result

# 学習
def train_net(ds_train, ds_valid, net, optimizer, criterion, batch, device):
    net.to(device) # GPUに送る

    # DataLoaderを作成
    loader_train = DataLoader(ds_train, batch_size=batch, shuffle=True)
    loader_valid = DataLoader(ds_valid, batch_size=len(ds_valid), shuffle=False)

    print(f'train start! (batch_size: {batch})')
    for epoch in range(epochs):
        # 開始時刻の記録
        start = time.time()

        net.train()  # 訓練モードに切り替える
        for data, target in loader_train:
            data = data.to(device) # GPUに送る
            target = target.to(device) # GPUに送る
            optimizer.zero_grad()
            output = net(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

        # 損失、正解率を計算
        train_loss = cal_loss(net, loader_train, criterion, device)
        train_accuracy = cal_acc(net, loader_train, device)
        valid_loss = cal_loss(net, loader_valid, criterion, device)
        valid_accuracy = cal_acc(net, loader_valid, device)

        # 終了時刻の記録
        end = time.time()

        # 結果を出力
        print(f'epoch: {epoch + 1:3}/{epochs}, train_loss: {train_loss:.3f}, train_accuracy: {train_accuracy:.3f}, valid_loss: {valid_loss:.3f}, valid_accuracy: {valid_accuracy:.3f},TIME: {end-start:.3f}sec')

    print(f'train finished! (batch_size: {batch})')

    return

def main():
    # GPUを指定
    device = torch.device('cuda')

    # データの読み込み
    X_train = torch.load('data/X_train70.pt')
    y_train = torch.load('data/y_train70.pt')
    X_valid = torch.load('data/X_valid70.pt')
    y_valid = torch.load('data/y_valid70.pt')

    # データセットの作成
    ds_train = TensorDataset(X_train, y_train)
    ds_valid = TensorDataset(X_valid, y_valid)

    # ニューラルネットワークの定義
    net = Net(d_input, d_output)
    optimizer = torch.optim.SGD(net.parameters(), lr=0.003)

    # クロスエントロピー損失の定義
    criterion = torch.nn.CrossEntropyLoss()

    # バッチサイズを変更しながら、処理時間を計測
    for batch in batch_size:
        train_net(ds_train, ds_valid, net, optimizer, criterion, batch, device)


if __name__ == '__main__':
    main()