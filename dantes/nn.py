# Based off this Jeremy Howard tutorial:
# https://www.kaggle.com/code/jhoward/linear-model-and-neural-net-from-scratch

from random import random

import torch

from .data import HARD_DEALS, EASY_DEALS
from .deal import microsoft

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


t_indep = torch.zeros((hardc + easyc), 52 * 52, dtype=torch.bool)
i = 0
for seed in HARD_DEALS + EASY_DEALS:
    deal = microsoft(seed)
    for j, card in enumerate(deal):
        t_indep[i][j * 52 + cardi(card)] = 1

    i += 1

n_coeff = t_indep.shape[1]


trn_split = []
val_split = []
for i in range(hardc+easyc):
    if random() < .2:
        val_split.append(i)
    else:
        trn_split.append(i)

trn_indep = t_indep[trn_split]
trn_dep = t_dep[trn_split]
val_indep = t_indep[val_split]
val_dep = t_dep[val_split]

def init_coeffs():
    return (torch.rand(n_coeff) - 0.5).requires_grad_()

def calc_preds(coeffs, indeps):
    return torch.sigmoid((indeps * coeffs).sum(axis=1))

def calc_loss(coeffs, indeps, deps):
    return torch.abs(calc_preds(coeffs, indeps) - deps).mean()

def one_epoch(coeffs, lr):
    loss = calc_loss(coeffs, trn_indep, trn_dep)
    loss.backward()
    with torch.no_grad():
        coeffs.sub_(coeffs.grad * lr)
        coeffs.grad.zero_()
    print(f"{loss:.3f}", end="; ")

def acc(coeffs):
    return (val_dep == (calc_preds(coeffs, val_indep) > 0.5)).float().mean()

def train_model(epochs=30, lr=0.1):
    coeffs = torch.rand(n_coeff) - 0.5
    coeffs.requires_grad_()

    for _ in range(epochs):
        one_epoch(coeffs, lr=lr)
        torch.save(coeffs, "coeffs.pt")
        print(f"{acc(coeffs):.3f}")

    return coeffs

coeffs = train_model(epochs=10000)
