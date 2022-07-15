import sys
from jetan.jet.data import JetData

def check_main():
    data = JetData.decode(sys.stdin.read())

    print(data.encode())

