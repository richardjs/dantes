# Based off this Jeremy Howard tutorial:
# https://www.kaggle.com/code/jhoward/linear-model-and-neural-net-from-scratch

from random import random

import torch
import torch.nn.functional as F

from ..data import HARD_DEALS, EASY_DEALS
from ..deal import microsoft

hardc = len(HARD_DEALS)
easyc = len(EASY_DEALS)

# 0 means an easy game, 1 means a hard game
t_dep = torch.zeros(hardc + easyc)
t_dep[:hardc] = 1

# Trying 52*52 inputs--each space in the deal has a binary categorical
# variable for each card


def cardi(card):
    rank, suit = card
    return rank + 13 * suit


t_indep = torch.zeros((hardc + easyc), 52 * 52)
i = 0
for seed in HARD_DEALS + EASY_DEALS:
    deal = microsoft(seed)
    for j, card in enumerate(deal):
        t_indep[i][j * 52 + cardi(card)] = 1

    i += 1

n_coeff = t_indep.shape[1]


trn_split = []
val_split = []
for i in range(hardc + easyc):
    if random() < 0.2:
        val_split.append(i)
    else:
        trn_split.append(i)

trn_indep = t_indep[trn_split]
trn_dep = t_dep[trn_split]
val_indep = t_indep[val_split]
val_dep = t_dep[val_split]

# Convert to column vectors
trn_dep = trn_dep[:, None]
val_dep = val_dep[:, None]


def init_coeffs(n_hidden):
    layer1 = (torch.rand(n_coeff, n_hidden) - 0.5) / n_hidden
    layer2 = torch.rand(n_hidden, 1)
    const = torch.rand(1)[0]
    return (
        layer1.requires_grad_(),
        layer2.requires_grad_(),
        const.requires_grad_(),
    )


def calc_preds(coeffs, indeps):
    layer1, layer2, const = coeffs
    res = F.relu(indeps @ layer1)
    res = res @ layer2 + const
    return torch.sigmoid(res)


def calc_loss(coeffs, indeps, deps):
    return torch.abs(calc_preds(coeffs, indeps) - deps).mean()


def update_coeffs(coeffs, lr):
    for layer in coeffs:
        layer.sub_(layer.grad * lr)
        layer.grad.zero_()


def one_epoch(coeffs, lr):
    loss = calc_loss(coeffs, trn_indep, trn_dep)
    loss.backward()
    with torch.no_grad():
        update_coeffs(coeffs, lr)
    print(f"{loss:.3f}", end="; ")


def acc(coeffs):
    return (val_dep == (calc_preds(coeffs, val_indep) > 0.5)).float().mean()


def train_model(epochs=30, n_hidden=52, lr=0.3):
    coeffs = init_coeffs(n_hidden)

    best_acc = 0
    best_coeffs = None

    for i in range(epochs):
        print(i, end=":\t")
        one_epoch(coeffs, lr=lr)

        a = acc(coeffs).item()
        if a > best_acc:
            best_acc = a
            best_coeffs = (
                coeffs[0].detach().clone(),
                coeffs[1].detach().clone(),
                coeffs[2].detach().clone(),
            )

        print(f"{acc(coeffs):.3f}")

    return best_coeffs, best_acc


if __name__ == "__main__":
    coeffs, a = train_model(epochs=300)
    torch.save(coeffs, "coeffs.pt")
    print("best accuracy:", a)
