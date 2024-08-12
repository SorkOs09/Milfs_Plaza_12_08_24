init -99 python:
    class MyRandom(object):
        """docstring for MyRandom"""
        def __init__(self, x0, x1):
            self.arr = []
            self.x0  = x0
            self.x1  = x1+1
            self.set_list()
        def set_list(self):
            self.arr = []
            for i in xrange(self.x0, self.x1):
                for j in xrange(renpy.random.randint(1, 4)):
                    self.arr.append(i)
        
        def get_n(self):
            rtrn = renpy.random.choice(self.arr)
            if rtrn in self.arr:
                self.arr.remove(rtrn)
            if not len(self.arr):
                self.set_list()
            
            return rtrn
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
