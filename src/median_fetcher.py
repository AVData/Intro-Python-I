# Catalog what we already konw
# define what median means
# the middle element of al the lements once they're sorted
# figure out how to calcualte it
# how doe we deal with an even number of numbers
# when should we handle the sorting

class MedianFetcher:
    def __init__(self):
        # define all the attributes on 'self'
        # self.median = None
        self.numbers = []

    # Insert the value n into our class
    def insert(self, n):
        # where do store n?
        # maybe we store it in self.median?
        # what happens when we insert more values?
        self.numbers.append(n)
        self.numbers.sort() # sorts the list in-place

    def get_median(self):
        if len(self.numbers) == 0:
            return None
        # figure out if the length of the numbers list is odd or even
        mid = len(self.numbers) // 2
        if len(self.numbers) % 2 == 1:
            # if it's odd, then we can just pick the middle numbers
            # if it's even, get the average of the two middle numbers
            # take the length, devite it by 2
            return self.numbers[mid]
        else:
            # if it's even, get the average o the two middle numbers
            # grab the element right before the mide element
            return (self.numbers[mid-1] + self.numbers[mid]) / 2


medianFetcher = MedianFetcher()
print(medianFetcher.get_median())
medianFetcher.insert(5)
print(medianFetcher.get_median())
medianFetcher.insert(10)
print(medianFetcher.get_median())
medianFetcher.insert(100)
print(medianFetcher.get_median())
