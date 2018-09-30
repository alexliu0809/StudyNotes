from itertools import product
import psutil
import os
import string
#tokens_as_list = [["c","b","a"],["c","b","a"],["c","b","a"],["c","b","a"],["c","b","a"],["c","b","a"],["c","b","a"],["c","b","a"],["c","b","a"]]
#for string in product(*tokens_as_list):
    #process = psutil.Process(os.getpid())
    #print(process.memory_info().rss)
    #print(string)

class Iter():

    def __init__(self):

        self.tokens_as_list = [
        list(string.ascii_letters),
        list(string.ascii_uppercase),
        list(string.ascii_lowercase),
        list(string.ascii_letters),
        list(string.hexdigits)
        ]

        total = 1
        for val in self.tokens_as_list:

            total *= len(val)

        #print(total)
        #print(product(*self.tokens_as_list))
        
        a = list("".join(string) for string in product(*self.tokens_as_list))
        process = psutil.Process(os.getpid())
        print(process.memory_info().rss)
        print(a[0]) #aAaa0
        print(a[-1])
        #2630791168

        """

        #15212544
        #('a', 'A', 'a', 'a', '0')
        for val in product(*self.tokens_as_list):
            print(val)
            process = psutil.Process(os.getpid())
            print(process.memory_info().rss)
            break
        """
        

    def __iter__(self):
        current = 0
        while current <= 10:
            yield from product(*self.tokens_as_list) 
            current += 1


it = Iter()
#counter = 0
#for val in it:
    #counter += 1
    #print(val)
