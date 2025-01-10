import torch


def test_cuda():
    print("torch.cuda.is_available:", torch.cuda.is_available())


if __name__ == "__main__":
    test_cuda()
