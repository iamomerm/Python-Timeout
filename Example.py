import time
from timeout import Timeout

# Void - Timed Out
def endless_greet(firstname, lastname):
    while True:
        print('Hello', firstname, lastname)
        time.sleep(1)

# Int
def multiply(num1, num2):
    return num1 * num2

status = Timeout.timeout(endless_greet, 5)('John', 'Smith')
if not status:
    print('Function Call Has Timed Out!')

status = Timeout.timeout(multiply, 5)(2, 3)
if status is False:
    print('Function Call Has Timed Out!')
else:
    print(status)
