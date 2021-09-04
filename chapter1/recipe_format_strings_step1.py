import datetime
import delorean
from decimal import Decimal


# input data
data = [
    (1000, 10),
    (2000, 17),
    (2500, 170),
    (2500, -170),
]

print("REVENUE | PROFIT | PERCENT")
TEMPLATE = "{revenue:>7,} | {profit:>6} | {percent:>7.2%}"

for revenue, profit in data:
    row = TEMPLATE.format(revenue=revenue, profit=profit, percent=profit / revenue)
    print(row)


INPUT_TEXT = """
AFTER THE CLOSE OF THE SECOND QUARTER, OUR COMPANY, CASTAÑACORP
HAS ACHIEVED A GROWTH IN THE REVENUE OF 7.47%. THIS IS IN LINE
WITH THE OBJECTIVES FOR THE YEAR. THE MAIN DRIVER OF THE SALES HAS
BEEN
THE NEW PACKAGE DESIGNED UNDER THE SUPERVISION OF OUR MARKETING
DEPARTMENT.
OUR EXPENSES HAS BEEN CONTAINED, INCREASING ONLY BY 0.7%, THOUGH THE
BOARD
CONSIDERS IT NEEDS TO BE FURTHER REDUCED. THE EVALUATION IS
SATISFACTORY
AND THE FORECAST FOR THE NEXT QUARTER IS OPTIMISTIC. THE BOARD
EXPECTS
AN INCREASE IN PROFIT OF AT LEAST 2 MILLION DOLLARS.
"""

words = INPUT_TEXT.split()
redacted = [''.join(w for w in word) for word in words]
ascii_text = [word.encode("ascii", errors="replace").decode("ascii") for word in redacted]
newlines = [word + "\n" if word.endswith(".") else word for word in ascii_text]
LINE_SIZE = 80
lines = []
line = ""
for word in newlines:
    if line.endswith('\n') or len(line) + len(word) + 1 > LINE_SIZE:
        lines.append(line)
        line = ""
    line = f"{line} {word}"

lines = [line.title() for line in lines]
result = "\n".join(lines)
print(result)

log = '[2018-05-05T11:07:12.267897] - SALE - PRODUCT: 1345 - PRICE: $09.99'
# divide_it = log.split(" - ")
# print(divide_it)
#
# timestamp_string, _, product_string, price_string = divide_it
# timestamp = delorean.parse(timestamp_string.strip('[]'))
# product_id = int(product_string.split(':')[-1])
# print(product_id)
#
# price = Decimal(price_string.split("$")[-1])
# print(price)
#
# print(timestamp, product_id, price)


class PriceLog(object):
    def __init__(self, timestamp, product_id, price):
        self.timestamp = timestamp
        self.product_id = product_id
        self.price = price

    def __repr__(self):
        return f"PriceLog {self.timestamp}, {self.product_id}, {self.price}"

    @classmethod
    def parse(cls, text_log):
        """
        Parse from a text log with the format
        [<Timestamp>] - SALE - PRODUCT: <product id> - PRICE: $<price>
        to a PriceLog object.
        """
        divide_it = text_log.split(" - ")
        tmp_string, _, product_string, price_string, = divide_it
        timestamp = delorean.parse(tmp_string.strip("[]"))
        product_id = int(product_string.split(":")[-1])
        price = Decimal(price_string.split("$")[-1])

        return cls(timestamp=timestamp, product_id=product_id, price=price)


new_data = PriceLog.parse(log)
print(f"New data: {new_data}")
