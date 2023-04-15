"This problem was asked by Twitter."
"You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:"
"    record(order_id): adds the order_id to the log"
"    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N."
"You should be as efficient with time and space as possible."

class Log:

    def __init__(self, n) -> None:
        self.n = n
        self.nRecordsBuffer = [None]*n
        self.currentIndex = 0

    def record(self, orderId):
        self.nRecordsBuffer[self.currentIndex] = orderId
        self.currentIndex = (self.currentIndex + 1) % self.n

    def getLast(self, i):
        return self.nRecordsBuffer[self.currentIndex - i - 1]

newLog = Log(4)

newLog.record(0)
newLog.record(1)
newLog.record(2)
newLog.record(3)
newLog.record(4)
newLog.record(5)

print(newLog.nRecordsBuffer)
print(newLog.getLast(1))