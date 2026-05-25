from pathlib import Path

import torch

from ..deal import microsoft
from .train import calc_preds, cardi

NN_DIR = Path(__file__).parent


coeffs = torch.load(NN_DIR / "coeffs.pt")


def deal_tensor(seed):
    t = torch.zeros(1, 52 * 52)
    deal = microsoft(seed)
    for i, card in enumerate(deal):
        t[0][i * 52 + cardi(card)] = 1
    return t


def is_easy_deal(seed):
    indep = deal_tensor(seed)
    return calc_preds(coeffs, indep).item() < 0.5


for i in range(500000, 500500):
    if is_easy_deal(i):
        print(i)
