import os,sys
import pandas as pd
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from sklearn.preprocessing import LabelEncoder

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


def main():
    # detect device
    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "mps"
        if torch.backends.mps.is_available()
        else "cpu"
    )
    print(f"Using {device} device")

    # init the model
    model = NeuralNetwork().to(device=device)
    print(model)

    # load the data
    data = pd.read_csv("labeled_features/PAAC_PCP.csv")
    X = data.drop(["Labels"],axis=1).values
    y = data["Labels"].values

    # encode string labels to numerical ones
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # convert the data to PyTorch tensors
    X_tensor = torch.tensor(X, dtype=torch.float32)
    y_tensor = torch.tensor(y_encoded, dtype=torch.long)

    print(f"Features:\n{X_tensor}")
    print(f"Labels:\n{y_tensor}")

    # == DATA IS PREPARED -- time to build model training code ==
    logits = model(X)

if __name__ == "__main__":
    main()
    sys.exit()