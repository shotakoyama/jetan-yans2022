import json
from .corr import Corr

def decode_corr(corr):
    corr = corr.strip()
    corr = json.loads(corr)
    corr = Corr.decode(corr)
    return corr

