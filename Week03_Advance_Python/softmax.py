import torch


class Softmax(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        """
        Tính toán hàm softmax cho tensor 1 chiều x.

        Args:
          x: Tensor 1 chiều đầu vào.

        Returns:
          Tensor 1 chiều sau khi áp dụng hàm softmax.
        """
        c = x.max()
        exp_x = torch.exp(x - c)
        sum_exp_x = exp_x.sum()
        return exp_x / (sum_exp_x + 1e-5)


class Softmax_stable(torch.nn.Module):
    """
    Class để tính toán hàm softmax cho một tensor 1 chiều, xử lý trường hợp tràn số.
    """

    def __init__(self):
        super().__init__()

    def forward(self, x):
        """
        Tính toán hàm softmax cho tensor 1 chiều x, xử lý trường hợp tràn số.

        Args:
          x: Tensor 1 chiều đầu vào.

        Returns:
          Tensor 1 chiều sau khi áp dụng hàm softmax.
        """
        c = x.max()
        x = x - c
        exp_x = torch.exp(x)
        sum_exp_x = exp_x.max()
        exp_x /= sum_exp_x
        sum_exp_x = exp_x.sum()
        return exp_x / (sum_exp_x + 1e-5)


# Ví dụ sử dụng

data = torch.tensor([1, 2, 3])

softmax_model = Softmax()
softmax_output = softmax_model(data)
print(softmax_output)

softmax_stable_model = Softmax_stable()
softmax_stable_output = softmax_stable_model(data)
print(softmax_stable_output)
