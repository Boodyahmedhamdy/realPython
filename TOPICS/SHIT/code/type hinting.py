from typing import List, Dict

# x: int = 33
# y: float = 324.5
# z: str = "ahmed"
# print(x, y)


def do_nothing(name: str = "name") -> None:
    print(name)


def add_numbers(a: int, b: int, c: int) -> int:
    return a + b + c


do_nothing()


complexList1: list[str] = []
complexList: List[List[int]] = []


BoodyType = Dict[str, int]
BoodyS = List[BoodyType]
def something(b: BoodyType) -> None:
    print(b)

def anotherThing(some: BoodyS):
    print(some)


something({"ahmed": 443})
anotherThing([
    {"ahemd": 344},
    {"hamdy": 21}
])





# word = add_numbers("ahemd", "ahssa", "koky").strip()
# print(word)
# print(add_numbers("ahemd", "ahssa", "koky"))

