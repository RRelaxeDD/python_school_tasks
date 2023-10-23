class SiteChecker:

    def __init__(self, func):
        print("> class SiteChecker method __init__ launched")
        self.func = func
    
    def __call__(self):
        print(f"> checking before start {self.func.__name__}")
        self.func()
        print("> Checking safe turn off")

@SiteChecker
def site():
    print("site working")

if __name__ == "__main__":
    print(">> site started")
    site()
    print(">> site shutted down")
