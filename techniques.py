"""
Comprehensive Demonstration of Python Obfuscation Techniques
"""
import asyncio
import sys

# ==========================================
# 1. NAMING & SCOPE
# ==========================================

# - Non-PEP8 naming
nAmE3_ = "snake_case or pep8 violation"


class class2:
  pass


# - Name mangling (double underscore prefix)
class MangledClass:

  def __init__(self):
    self.__secret = 42  # Mangled to _MangledClass__secret


# - Dunder abuse
class DunderAbuse:

  def __init__(self):
    self.__dict__["__getitem__"] = lambda self, k: 999


# - Homoglyphs (l, 1, I; O, 0)
O = 1
l = 1
I = 1

# - Shadowing built-ins functions
list = [1, 2, 3]  # Shadows built-in list()
str = "shadowed"  # Shadows built-in str()


def print(x):
    x             # Shadows built-in print()


# - Non-declaration of constants
radius = 3.14159  # Not in full caps


# - Type hints
def typed_func(x: OverflowError, y: GeneratorExit) -> ProcessLookupError:
  return float(x)


# - Overriding exceptions
class Exception:
  pass  # Shadows built-in Exception


# - Definition-time default argument evaluation
def default_eval(val=print("Evaluated at definition time")):
  pass


# - Global/ local scoping pollution
value = "global"


def scope_pollution():
    value = "local"
    print(value)
    globals()[value] = "local"

    def nested_scope():
        nonlocal value
        value = "global"


# - Star unpacking assignment
first, *_, last = [1, 2, 3, 4, 5]


# ==========================================
# 2. CONTROL FLOW
# ==========================================

# - Loop-else constructs (for-else, while-else)
for i in range(2):
  pass
else:
  loop_else_var = True

# - Redundant paths
if True:
  redundant_path = 1
else:
  redundant_path = 2

# - Control flow except abuse (StopIteration, IndexError)
try:
  [()[0]]
except IndexError:
  control_flow_caught = True

# - Exception abuse
z = 1

try:
  if z == 1:
    raise ValueError
  raise TypeError
except TypeError:
    pass
except ValueError:
  exception_abuse_var = "routed"

# - Nested/ single-line expressions
nested_expr = [[y * 2 for y in range(x) if y != 1] for x in range(5) if x % 2 == 0]


# - Context managers
class C:
    def __enter__(self):
        self._x = 1
        return self
    def __exit__(self, *args):
        self._x = 0


with C() as c:
    print(c._x)


# - Unclear recursion
def unclear_rec(n):
  return n * unclear_rec(n - 1) if n > 1 else 1


# - Recursion within parameters
def f(n, acc=[]):
    if n == 0:
        return acc
    acc.append(n)
    return f(n - 1, acc=acc)


# - Async-await interweaving
async def a(n):
    return await b(n - 1) + 1 if n else 1


async def b(n):
    await asyncio.sleep(0)

    return await a(n) * 2


print(asyncio.run(a(3)))


# - Property side effects
class PropertySideEffect:

  @property
  def prop(self):
    return 1

  @prop.setter
  def prop(self, val):
    global side_effect_triggered
    side_effect_triggered = val


# ==========================================
# 3. SYNTAX & FUNCTIONAL
# ==========================================

# - Curried lambdas
curried = lambda x: lambda y: x + y

# - Immediately invoked function expressions (IIFE)
iife_result = (lambda x: x * 2)(5)

# - Decorator factories
def dec_factory(multiplier):
  return lambda f: lambda x: f(x) * multiplier


# - Interception via decorators
def interceptor(f):
  def wrapper(x):
    print("Before")
    result = f(x + 1)
    print(result)
    print("After")
    return result
  return wrapper


# - Multiple decorators
@interceptor
@interceptor
def multi_dec(x):
  return x


multi_dec(3)

# - Walrus assignment
if (walrus_val := 10) > 5:
  pass


# - Generators/ yield from
def data():
    yield "Start"
    yield from [1, 2, 3]
    yield "End"

for item in data():
    print(item)


# - Custom exception logic
class CustomException(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw ${amount}. Current balance: ${balance}."
        )


# - Incorrect comparators (is vs ==)
x = 100 is 100  # Identity vs equality on integers
y = None == None


# - Redundant docstrings/ comments
def docstring_func():
  """This is a redundant docstring that does nothing."""
  pass  # This is a redundant comment


# Redundant lines
1
False
1==2
'a'

# - Incorrect newlines and indents
x= 1; y =   2;


z=3;

# - Comprehension side effects
[print(x) for x in range(2)]


# - Primitive operator overloading
class CustomInt(int):
  def __add__(self, other):
    return super().__sub__(other) # Plus acting as minus


# - F-string side effects
f_string = f"{(global_var_side := 99)}"

# - Chained comparison operators
chained_comp = 1 < 2 <= 3 > 1

# - Implicit string concatenation
implicit_str = "part1" "part2"

# - Slice assignment mutation
slice_lst = [1, 2, 3]
slice_lst[1:] = [9, 9]

# - Function aliasing
aliased_print = print
aliased_print("Hello World!")


# - Redundant inheritance
class RedundantInheritance(FileExistsError, BaseException):
    pass


# ==========================================
# 4. DATA MANIPULATION
# ==========================================

# - Bitwise operators
bitwise_res = 5 & 3 | 1 << 2

# - Boolean arithmetic
bool_arithmetic = (True + True) * 3

# - Negative logic
negative_logic = not not not True


# - Mutable default arguments (referencing)
def mutable_default(lst=[]):
  lst.append(1)
  return lst


# - Slicing function
slicing_func = slice(0, 5, 2)
sliced_data = "abcdef"[slicing_func]

# - String-ASCII manipulation
ascii_manip = "".join([chr(ord(c) + 1) for c in "abc"])

# - Base representation
base_repr = int("1010", 2)
hex_number = 0x1A6F

# - Format specifiers
format_spec = f"{42:04x}"

# - Floating point abuse
float_abuse = 0.1 + 0.2 == 0.3  # False due to precision
inf = float("inf")
nan = float("nan")  # NaN == or is NaN evaluates to false

# - Chained assignment
a = b = c = 100
p, q = 1, 2


# - Dictionary unpacking
def dictionary_unpacked(a, b):
    return a + b


dict_unpack = {**{"a": 1}, **{"b": 2}}
print(dictionary_unpacked(**dict_unpack))

# ==========================================
# 5. OTHERS
# ==========================================

# - Dynamic class construction
DynamicClass = type("DynamicClass", (object,), {"attr": 123, "f": f})


# - Arbitrary arguments
def arbitrary_args(*args, **kwargs):
  return len(args) + len(kwargs)


# - Stack frame inspection
def log_call():
    current = sys._getframe(0).f_code.co_name
    caller = sys._getframe(1).f_code.co_name

    print(f"[LOG] {caller}() called {current}()")


def process_data():
    log_call()
    print("Processing data...")


def save_data():
    log_call()
    print("Saving data...")

process_data()
save_data()

