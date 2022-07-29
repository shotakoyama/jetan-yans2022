import sys
from jetan.jet.data import JetData

def head_main(n):
    data = JetData.decode(sys.stdin.read())
    data = JetData(data[:n])
    print(data.encode())

