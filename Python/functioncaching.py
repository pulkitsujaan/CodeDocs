"""function caching"""
# function caching is very important to save time in the execution of a program
from functools import lru_cache
import time
def main():
    valcache=int(input("How many values you want to cache?\n"))
    @lru_cache(maxsize=valcache)
    def func1(n):
        time.sleep(n)
        return n
    print("Run from now")
    func1(3)
    print("done....calling again")
    func1(2)
    print("Now done")
    func1(3)
    func1(6)
    func1(6)
    print("Finaled")

if __name__=="__main__":
    main()