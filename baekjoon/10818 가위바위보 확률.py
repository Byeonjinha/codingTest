from itertools import cycle
import random

class Player:
    types, max_p = ("가위" , "바위" , "보"), 1

    def __init__(self,*args):
        size = len(Player.types)
        assert len(args) == size and sum(args) == Player.max_p, "invalid syntax"
        self.ps, self.history,self.rates = args,[0] * size, [0] * size

    def put(self):
        return Player.types.index(random.choice([Player.types[i] for i, p in enumerate(self.ps) for __ in range(p)]))

    def set(self, i):
        self.history[i] +=1
        self.rates = [round(case/sum(self.history),3) for i, case in enumerate(self.history)]

    @classmethod
    def record(cls,h,a,r_h,r_a):
        h.set(r_h),a.set(r_a)
        print("{}: home={} away={}".format(cls.record.__name__,h,a))
    @classmethod
    def match(cls, h, a, r_ts=("win", "lose","draw")):
        h_p, a_p = h.put(), a.put()
        key = {1: 'h_win', -2:'h_win', -1:'h_lose', 2: 'h_lose', 0:'h_draw'}[h_p-a_p]
        r_h, r_a = {'h_win':(0, 1), 'h_lose':(1, 0), 'h_draw':(2, 2)}[key]
        print("{}:home={}({}) away={}({})".format(cls.match.__name__, cls.types[h_p], r_ts[r_h], cls.types[a_p], r_ts[r_a]))
        cls.record(h, a, r_h, r_a)

    @classmethod
    def win(cls, w, l, draw=False):
        w_cy, l_cy = cycle(w.ps), cycle(l.ps)
        if not draw:
            next(w_cy)
        return sum([next(w_cy)  *next(l_cy) for _ in cls.types]) / (cls.max_p ** 2)
    @classmethod
    def predict(cls, h,a):
        w, l , d = cls.win(h,a), cls.win(a,h), cls.win(h,a,draw=True)
        print("{}: home={} away={}".format(cls.predict.__name__,*((w,l,d),(l,w,d))))

    def __str__(self):
        return "{}".format(",".join([str(case[0])+"("+str(case[1])+")" for case in list(zip(self.history,self.rates))]))

home = Player(0.3, 0.3, 0.4)
away = Player(0.000001, 0, 0.999999)
ads=1
while ads > 0 :

    Player.predict(home, away)
    # Player.match(home, away)
    ads-=1