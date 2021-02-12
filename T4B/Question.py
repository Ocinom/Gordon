class qn():

    def __init__(self, q: str, y=None, n=None):
        self.q = q
        self.y = y
        self.n = n

    def __str__(self):
        return self.q

    def add_query(self, nq, yq):
        self.n = nq
        self.y = yq

def start(cur):
    while isinstance(cur, qn):
        print(cur, end = '\t')
        resp = input("(y/n): ")
        if resp.lower().startswith('y'):
            cur = cur.y
        else:
            cur = cur.n
    print(cur)