class MathDojo:
    def __init__(self):
        self.result= 0

    def add(self, num, *nums):
        sum = 0
        total = 0
        for x in nums:
            sum += x
            total = sum + num
        self.result = self.result + total
        return self

    def subtract(self, num, *nums):
        sum = 0
        total = 0
        for x in nums:
            sum -= x
            total = sum - num
        self.result = self.result + total
        return self

md = MathDojo()
x = md.add(2,5,7,7).subtract(1,2,3).result
print(x)