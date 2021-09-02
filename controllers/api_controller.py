from decouple import config
from models.moeda import Currency


def api_initializer():
    return [Currency(*x.split(',')) for x in config('currencies').split(';')]
