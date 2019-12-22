import json
import config as cfg

def gross_earn(hours):
    hours = int(hours)
    gross_income = hours * cfg.hourly_rate
    return gross_income


def net_income(hours):

    income = gross_earn(hours)
    sup_rate = 0.095
    tax_rate = cfg.tax_rate
    supann = income * cfg.super_rate
    # CAlculation removes tax and super annuation
    gross = income - supann

    tax = gross * cfg.tax_rate

    net = gross - tax

    return net
