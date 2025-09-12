![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Scenario-Based Python Interview Questions & Answers

## Q1. Print audit: suppress newline & compose a status line
**Scenario:** You need to print a progress line like `Processed: 45%` that updates in-place without adding new lines.

**Answer:** Use `end='\r'` and optional flush.
```python
import time

for i in range(0, 101, 5):
    print(f"Processed: {i:3d}%", end="\r", flush=True)
    time.sleep(0.01)
print()  # final newline
```

## Q2. Commenting strategy in a shared script
**Scenario:** A team script has unclear sections. Add a docstring to explain module purpose and single-line comments to clarify tricky logic.

**Answer:** Combine module docstring + inline comments.
```python
"""ETL utility: reads CSV, cleans rows, writes JSON summary."""
def clean_row(row):
    # Normalize empty strings to None for downstream JSON serialization
    return [v if v.strip() else None for v in row]
```

## Q3. Datatype coercion during CSV ingestion
**Scenario:** A CSV column `quantity` may contain `'12'`, `'12.0'`, or `''`. Convert to `int` if possible else `None`.

**Answer:** Try conversions in order, handle exceptions.
```python
def to_int_or_none(s: str):
    s = s.strip()
    if not s:
        return None
    try:
        return int(s)
    except ValueError:
        try:
            f = float(s)
            return int(f) if f.is_integer() else None
        except ValueError:
            return None
```

## Q4. Complex numbers for signal processing stub
**Scenario:** You store FFT results as complex numbers and need magnitude and phase arrays.

**Answer:** Use `abs()` and `cmath.phase`.
```python
import cmath

def mag_phase(samples):
    return [abs(z) for z in samples], [cmath.phase(z) for z in samples]
```

## Q5. Variables and shadowing in nested scopes
**Scenario:** A nested function accidentally masks an outer variable. Demonstrate the fix using `nonlocal`.

**Answer:** Use `nonlocal` to modify enclosing scope variable.
```python
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c = counter()
assert [c(), c(), c()] == [1, 2, 3]
```

## Q6. Operators: safe division with graceful fallback
**Scenario:** Divide `a/b` but return `0` if `b==0` without exceptions leaking.

**Answer:** Leverage conditional or try/except.
```python
def safe_div(a, b):
    return a / b if b != 0 else 0
```

## Q7. Strings: masking sensitive tokens
**Scenario:** Replace all but the last 4 characters of an API token with `*`.

**Answer:** Use slicing and multiplication.
```python
def mask(token: str) -> str:
    keep = 4
    return "*" * max(0, len(token) - keep) + token[-keep:]
```

## Q8. Strings: align tabular console output
**Scenario:** Print a neat two-column table (name left-aligned width 12, count right-aligned width 5).

**Answer:** Use format specs.
```python
def print_row(name, count):
    print(f"{name:<12}{count:>5d}")

for n, c in [("Apples",12),("Bananas",3),("Cherries",140)]:
    print_row(n, c)
```

## Q9. Lists: stable in-place partition by predicate
**Scenario:** Move all falsy values to the end of a list while preserving relative order of truthy and falsy groups.

**Answer:** Rebuild in place from two list comps.
```python
def stable_partition_inplace(seq):
    trues = [x for x in seq if x]
    falses = [x for x in seq if not x]
    seq[:] = trues + falses
```

## Q10. Lists: chunk an iterable into fixed-size batches
**Scenario:** Process a long list in batches of 100.

**Answer:** Slice stepping.
```python
def batched(lst, size=100):
    for i in range(0, len(lst), size):
        yield lst[i:i+size]
```

## Q11. Sets: remove duplicates while keeping first occurrence
**Scenario:** Deduplicate but preserve order.

**Answer:** Track a `seen` set.
```python
def dedupe(seq):
    seen, out = set(), []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out
```

## Q12. Sets: compute symmetric difference across many sets
**Scenario:** Given many role sets, find users present in an odd number of roles.

**Answer:** Reduce with XOR-like symmetric difference.
```python
from functools import reduce
def odd_membership(*sets):
    return reduce(lambda a, b: a ^ b, sets)
```

## Q13. Tuples: robust unpacking with tail capture
**Scenario:** Parse `first, *middle, last` names safely.

**Answer:** Starred unpacking.
```python
def split_names(parts):
    first, *middle, last = parts
    return first, middle, last
```

## Q14. Tuples: return multiple results from a validator
**Scenario:** Validate a line and return `(ok, reason)` with reason `None` if ok.

**Answer:** Idiomatic tuple returns.
```python
def validate(line: str):
    if not line.strip():
        return False, "blank"
    if line.count(",") < 2:
        return False, "missing fields"
    return True, None
```

## Q15. Dicts: invert mapping with collision handling
**Scenario:** Invert `{user:id}` to `{id:[users...]}`.

**Answer:** Use `dict.setdefault`.
```python
def invert_multi(d):
    out = {}
    for k, v in d.items():
        out.setdefault(v, []).append(k)
    return out
```

## Q16. Dicts: merge with rule “prefer non-None, else other”
**Scenario:** Merge profile shards preferring non-`None` values.

**Answer:** Walk union of keys.
```python
def merge_pref_non_none(a, b):
    keys = set(a) | set(b)
    return {k: (a.get(k) if a.get(k) is not None else b.get(k))
            for k in keys}
```

## Q17. Conversions: rows (list of tuples) → dict-of-lists
**Scenario:** Convert `[("a",1),("b",2),("a",3)]` into `{"a":[1,3],"b":[2]}`.

**Answer:** Grouping.
```python
def group_pairs(pairs):
    out = {}
    for k,v in pairs:
        out.setdefault(k, []).append(v)
    return out
```

## Q18. Conditionals: nested rules for pricing
**Scenario:** Apply tiered discounts based on amount and customer type.

**Answer:** Clear guard-clauses beat deep nesting.
```python
def price(amount, customer):
    if amount <= 0:
        return 0
    if customer == "VIP":
        return amount * (0.85 if amount >= 1000 else 0.9)
    if customer == "STD":
        return amount * (0.95 if amount >= 500 else 1.0)
    return amount
```

## Q19. Loops: break/else to detect search miss
**Scenario:** Search a list; print “not found” once if no match.

**Answer:** Use `for ... else`.
```python
def find_first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n
    else:
        return None
```

## Q20. Functions: safe mutability patterns
**Scenario:** Default parameter should not reuse the same list across calls.

**Answer:** Use `None` sentinel.
```python
def append_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

## Q21. Functions: implement simple memoization without decorators
**Scenario:** Cache expensive results keyed by arg.

**Answer:** Keep closure dict.
```python
def memoize(func):
    cache = {}
    def wrapper(x):
        if x in cache: return cache[x]
        cache[x] = func(x)
        return cache[x]
    return wrapper
```

## Q22. Exceptions: classify and continue processing
**Scenario:** Read many lines; skip malformed ones but collect reasons.

**Answer:** Catch specific exceptions; store diagnostics.
```python
def parse_ints(lines):
    bad = []
    out = []
    for i, line in enumerate(lines, 1):
        try:
            out.append(int(line.strip()))
        except ValueError as e:
            bad.append((i, str(e)))
    return out, bad
```

## Q23. Exception `else`/`finally`: write file only if compute succeeds
**Scenario:** Only write output if the computation had no exceptions; always close resources.

**Answer:** Use `else` to guard the write.
```python
def compute_and_write(path):
    try:
        result = 1/1  # placeholder
    except ZeroDivisionError:
        return False
    else:
        with open(path, "w") as f:
            f.write(str(result))
        return True
    finally:
        pass  # cleanup hooks if needed
```

## Q24. OOP: encapsulate validation in constructor
**Scenario:** Create `User(email)` that validates on creation; stringifying shows masked email.

**Answer:** Combine `__init__` + `__str__`.
```python
class User:
    def __init__(self, email: str):
        if "@" not in email:
            raise ValueError("invalid email")
        self._email = email

    def __str__(self):
        name, dom = self._email.split("@", 1)
        mask = name[0] + "*"*(len(name)-2) + name[-1] if len(name) > 2 else name
        return f"{mask}@{dom}"

u = User("alice@example.com"); print(str(u))
```

## Q25. OOP Inheritance: extend behavior with `super()`
**Scenario:** `TimedFileWriter` should log write durations but otherwise behave like `FileWriter`.

**Answer:** Call `super()` then add timing.
```python
import time, os

class FileWriter:
    def write(self, path, text):
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

class TimedFileWriter(FileWriter):
    def write(self, path, text):
        start = time.perf_counter()
        super().write(path, text)
        elapsed = (time.perf_counter() - start)*1000
        print(f"Wrote {os.path.basename(path)} in {elapsed:.2f} ms")
```

## Q26. Dunder methods: custom container with `len`, `in`, indexing
**Scenario:** Build a read-only settings view backed by a dict.

**Answer:** Implement `__len__`, `__contains__`, `__getitem__`, `__iter__`.
```python
class SettingsView:
    def __init__(self, d): self._d = dict(d)
    def __len__(self): return len(self._d)
    def __contains__(self, k): return k in self._d
    def __getitem__(self, k): return self._d[k]
    def __iter__(self): return iter(self._d)
```

## Q27. Dunder `__add__`: vector add with type safety
**Scenario:** Support `v1 + v2`; raise for mismatched sizes.

**Answer:** Check length and type.
```python
class Vec:
    def __init__(self, xs): self.xs = tuple(xs)
    def __add__(self, other):
        if not isinstance(other, Vec) or len(other.xs) != len(self.xs):
            return NotImplemented
        return Vec(a+b for a,b in zip(self.xs, other.xs))
    def __repr__(self): return f"Vec{self.xs}"
```

## Q28. Packages: expose only public API via `__all__`
**Scenario:** Your package has helpers you don’t want to export.

**Answer:** Define `__all__` in `__init__.py`.
```python
# mypkg/__init__.py
from .core import run
__all__ = ["run"]
```

## Q29. Executable module: support `python -m mypkg.tool`
**Scenario:** Provide a command entry via module execution.

**Answer:** Use `if __name__ == "__main__":`.
```python
# mypkg/tool.py
def main():
    print("Tool running")
if __name__ == "__main__":
    main()
```

## Q30. CSV: robust reading with dialect sniffing and headers
**Scenario:** Unknown delimiter; need dict rows.

**Answer:** Use `csv.Sniffer` + `DictReader`.
```python
import csv

def read_unknown_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        sample = f.read(2048)
        f.seek(0)
        dialect = csv.Sniffer().sniff(sample)
        reader = csv.DictReader(f, dialect=dialect)
        return list(reader)
```

## Q31. CSV: write only selected columns and custom header order
**Scenario:** Keep columns `["id","name","score"]` in that order.

**Answer:** Use `DictWriter` with `fieldnames`.
```python
import csv

def write_subset(rows, path):
    fields = ["id","name","score"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})
```

## Q32. Datetime: normalize mixed input timezones to UTC timestamps
**Scenario:** Inputs are naive local timestamps or explicit ISO strings; normalize to epoch seconds (assume naive == local machine time).

**Answer:** Use `datetime`/`timezone`.
```python
from datetime import datetime, timezone

def to_epoch_seconds(ts: str):
    try:
        dt = datetime.fromisoformat(ts)
    except ValueError:
        dt = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
    if dt.tzinfo is None:
        dt = dt.astimezone()  # assume local
    return int(dt.astimezone(timezone.utc).timestamp())
```

## Q33. Datetime: humanize durations (minutes, seconds)
**Scenario:** Convert seconds to `MM:SS`.

**Answer:** Divmod.
```python
def mm_ss(total_secs: int) -> str:
    m, s = divmod(total_secs, 60)
    return f"{m:02d}:{s:02d}"
```

## Q34. File I/O: stream large file and compute rolling hash
**Scenario:** Compute SHA256 for a multi-GB file.

**Answer:** Read in chunks.
```python
import hashlib

def sha256_file(path, chunk=1<<20):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(chunk), b""):
            h.update(block)
    return h.hexdigest()
```

## Q35. File I/O: safely write to file with atomic replace
**Scenario:** Prevent partial writes on crash.

**Answer:** Write temp file then `replace`.
```python
import os, tempfile

def atomic_write(path, data: str):
    d = os.path.dirname(path) or "."
    fd, tmp = tempfile.mkstemp(dir=d, prefix=".tmp_")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(data)
        os.replace(tmp, path)
    except Exception:
        try: os.remove(tmp)
        except OSError: pass
        raise
```

## Q36. JSON: validate shape and coerce types
**Scenario:** Incoming JSON must contain `id:int`, `name:str`, optional `tags:list[str]`.

**Answer:** Manual checks.
```python
def validate(payload: dict):
    if not isinstance(payload.get("id"), int):
        raise ValueError("id must be int")
    name = payload.get("name")
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name required")
    tags = payload.get("tags", [])
    if not isinstance(tags, list) or not all(isinstance(t, str) for t in tags):
        raise ValueError("tags must be list[str]")
    return {"id": payload["id"], "name": name.strip(), "tags": tags}
```

## Q37. JSON: pretty-print and stable key ordering
**Scenario:** Commit JSON outputs with deterministic diffs.

**Answer:** `sort_keys=True`, `indent=2`.
```python
import json
def dump_pretty(obj) -> str:
    return json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False)
```

## Q38. Lambda: multi-key sort on list of dicts
**Scenario:** Sort by `-score` then `name`.

**Answer:** Use tuple key; negative for desc numeric.
```python
rows = [{"name":"Bob","score":9},{"name":"Ann","score":9},{"name":"Cara","score":8}]
rows.sort(key=lambda r: (-r["score"], r["name"]))
```

## Q39. Logging: structured context for a request
**Scenario:** Log all entries with a request ID prefix.

**Answer:** Create a logger adapter or use `%` argument.
```python
import logging
logger = logging.getLogger("app")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

def log_request(req_id, msg):
    logger.info("[req:%s] %s", req_id, msg)
```

## Q40. Logging: separate error log file
**Scenario:** Info to stdout, errors to file.

**Answer:** Configure two handlers.
```python
import logging, sys

logger = logging.getLogger("svc")
logger.setLevel(logging.DEBUG)

h_console = logging.StreamHandler(sys.stdout)
h_console.setLevel(logging.INFO)

h_file = logging.FileHandler("errors.log")
h_file.setLevel(logging.ERROR)

fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
h_console.setFormatter(fmt); h_file.setFormatter(fmt)
logger.addHandler(h_console); logger.addHandler(h_file)
```

## Q41. Argparse: CLI that reads a CSV and prints total rows
**Scenario:** Build `python tool.py --path data.csv`.

**Answer:** Use `argparse`.
```python
import argparse, csv

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--path", required=True)
    args = p.parse_args()
    with open(args.path, newline="") as f:
        count = sum(1 for _ in csv.reader(f))
    print(count)

if __name__ == "__main__":
    main()
```

## Q42. Argparse: flag with default and mutually exclusive options
**Scenario:** Allow `--verbose` or `--quiet`, not both.

**Answer:** Use mutually exclusive group.
```python
import argparse

p = argparse.ArgumentParser()
g = p.add_mutually_exclusive_group()
g.add_argument("--verbose", action="store_true")
g.add_argument("--quiet", action="store_true")
opts = p.parse_args()
```

## Q43. XML: parse config and update a node value
**Scenario:** Change `<timeout>` to `30` seconds.

**Answer:** Use `xml.etree.ElementTree`.
```python
import xml.etree.ElementTree as ET

def set_timeout(path, value="30"):
    tree = ET.parse(path)
    root = tree.getroot()
    node = root.find(".//timeout")
    if node is None:
        node = ET.SubElement(root, "timeout")
    node.text = value
    tree.write(path, encoding="utf-8", xml_declaration=True)
```

## Q44. XML: read attributes safely
**Scenario:** Extract `host` and `port` attributes; default port 80.

**Answer:** Use `.get()` with default.
```python
def read_endpoint(elem):
    return elem.get("host"), int(elem.get("port", "80"))
```

## Q45. Email: compose a simple text email (no send)
**Scenario:** Create an RFC-compliant message string for inspection/storage.

**Answer:** Use `email.message.EmailMessage`.
```python
from email.message import EmailMessage
from email.utils import formatdate

def make_mail(frm, to, subject, body):
    m = EmailMessage()
    m["From"] = frm
    m["To"] = to
    m["Subject"] = subject
    m["Date"] = formatdate(localtime=True)
    m.set_content(body)
    return m.as_string()
```

## Q46. Input: robust menu with validation loop
**Scenario:** Keep asking until user gives 1–3.

**Answer:** Loop with `try/except`.
```python
def prompt_choice():
    while True:
        s = input("Choose 1..3: ").strip()
        if s.isdigit() and 1 <= int(s) <= 3:
            return int(s)
        print("Invalid choice.")
```

## Q47. End-to-end mini ETL (CSV → cleanse → JSON)
**Scenario:** Read CSV, trim whitespace, drop blank rows, output pretty JSON.

**Answer:** Combine `csv` and `json`.
```python
import csv, json

def csv_to_clean_json(csv_path, json_path):
    rows = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            r2 = {k: (v.strip() if isinstance(v, str) else v) for k,v in r.items()}
            if any(r2.values()):  # skip entirely blank
                rows.append(r2)
    with open(json_path, "w", encoding="utf-8") as out:
        json.dump(rows, out, indent=2, ensure_ascii=False)
```

## Q48. Rolling window average without third-party libs
**Scenario:** Compute 3-point moving average for a list.

**Answer:** Slide and average.
```python
def moving_avg(xs, k=3):
    if k <= 0: raise ValueError
    out = []
    s = sum(xs[:k])
    out.append(s/k)
    for i in range(k, len(xs)):
        s += xs[i] - xs[i-k]
        out.append(s/k)
    return out
```

## Q49. Validate balanced brackets
**Scenario:** Determine if string has balanced `()[]{}`.

**Answer:** Use stack.
```python
def balanced(s):
    pairs = {')':'(',']':'[','}':'{'}
    st = []
    for ch in s:
        if ch in "([{": st.append(ch)
        elif ch in ")]}":
            if not st or st.pop() != pairs[ch]: return False
    return not st
```

## Q50. Find first non-repeating character in string
**Scenario:** Return index of first unique char else `-1`.

**Answer:** Two-pass count then scan.
```python
def first_unique(s):
    from collections import Counter
    c = Counter(s)
    for i,ch in enumerate(s):
        if c[ch] == 1: return i
    return -1
```

## Q51. Map-reduce style word count with only built-ins
**Scenario:** Count words across many files.

**Answer:** Walk files and aggregate.
```python
import os
from collections import Counter

def wordcount(paths):
    total = Counter()
    for p in paths:
        with open(p, encoding="utf-8") as f:
            total.update(f.read().split())
    return total
```

## Q52. Binary file detect: is file likely text?
**Scenario:** Decide if bytes are mostly printable ASCII/UTF-8.

**Answer:** Heuristic on sample bytes.
```python
import string

def is_text(path, sample=2048):
    with open(path, "rb") as f:
        b = f.read(sample)
    if b.startswith(b"\xef\xbb\xbf"):  # UTF-8 BOM
        b = b[3:]
    printable = set(bytes(string.printable, "ascii"))
    ratio = sum(ch in printable for ch in b) / max(len(b), 1)
    return ratio > 0.9
```

## Q53. Command tool: grep-like substring finder
**Scenario:** CLI to print lines containing a substring (case-insensitive option).

**Answer:** `argparse`, iterate file.
```python
import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument("pattern")
    p.add_argument("path")
    p.add_argument("-i","--ignore-case", action="store_true")
    a = p.parse_args()
    pat = a.pattern.lower() if a.ignore_case else a.pattern
    with open(a.path, encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            hay = line.lower() if a.ignore_case else line
            if pat in hay:
                print(f"{i:6d}: {line.rstrip()}")

if __name__ == "__main__":
    main()
```

## Q54. Safe eval alternative for simple arithmetic
**Scenario:** Evaluate `2+3*4` input from user without `eval`.

**Answer:** Use `ast` parse and whitelist nodes.
```python
import ast, operator

OPS = {
    ast.Add: operator.add, ast.Sub: operator.sub,
    ast.Mult: operator.mul, ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv, ast.Mod: operator.mod,
    ast.Pow: operator.pow, ast.USub: operator.neg,
}

def safe_arith(expr: str):
    def eval_(node):
        if isinstance(node, ast.Num): return node.n
        if isinstance(node, ast.UnaryOp) and type(node.op) in OPS:
            return OPS[type(node.op)](eval_(node.operand))
        if isinstance(node, ast.BinOp) and type(node.op) in OPS:
            return OPS[type(node.op)](eval_(node.left), eval_(node.right))
        raise ValueError("unsupported")
    tree = ast.parse(expr, mode="eval")
    return eval_(tree.body)
```

## Q55. Retry wrapper for flaky function with exponential backoff
**Scenario:** Retry a function up to 3 times on specific exceptions.

**Answer:** Use `time.sleep` and exception filter.
```python
import time

def retry(func, attempts=3, exc=Exception, base=0.1):
    for i in range(attempts):
        try:
            return func()
        except exc:
            if i == attempts - 1:
                raise
            time.sleep(base * (2 ** i))
```

## Q56. Timed LRU cache without `functools.lru_cache`
**Scenario:** Cache values for N seconds using dict.

**Answer:** Store (value, expiry) tuples.
```python
import time

def ttl_cache(ttl=5):
    store = {}
    def decorator(fn):
        def wrapper(x):
            now = time.time()
            val = store.get(x)
            if val and val[1] > now:
                return val[0]
            res = fn(x)
            store[x] = (res, now + ttl)
            return res
        return wrapper
    return decorator
```

## Q57. Rate limiter: allow K calls per T seconds
**Scenario:** Prevent too-frequent calls.

**Answer:** Keep timestamps queue.
```python
import time, collections

def rate_limiter(k=5, interval=1.0):
    calls = collections.deque()
    def allow():
        now = time.time()
        while calls and now - calls[0] > interval:
            calls.popleft()
        if len(calls) < k:
            calls.append(now)
            return True
        return False
    return allow
```

## Q58. Context manager: temporary directory change
**Scenario:** Run code within a different CWD and restore after.

**Answer:** Implement `__enter__/__exit__`.
```python
import os

class chdir:
    def __init__(self, path): self.path = path
    def __enter__(self):
        self.prev = os.getcwd()
        os.chdir(self.path)
    def __exit__(self, *exc):
        os.chdir(self.prev)
```

## Q59. Context manager: suppress specific exceptions
**Scenario:** Ignore `FileNotFoundError` only.

**Answer:** `contextlib.suppress`.
```python
from contextlib import suppress
with suppress(FileNotFoundError):
    open("maybe.txt").read()
```

## Q60. Iterator: file line window generator
**Scenario:** Yield overlapping windows of N lines.

**Answer:** Use deque.
```python
from collections import deque

def line_windows(path, n=3):
    buf = deque(maxlen=n)
    with open(path, encoding="utf-8") as f:
        for line in f:
            buf.append(line.rstrip("\n"))
            if len(buf) == n:
                yield tuple(buf)
```

## Q61. Generator: tail -f like follower
**Scenario:** Follow a file as it grows.

**Answer:** Poll and yield new lines.
```python
import time

def follow(path):
    with open(path, "r") as f:
        f.seek(0, 2)  # end
        while True:
            line = f.readline()
            if line:
                yield line.rstrip("\n")
            else:
                time.sleep(0.2)
```

## Q62. CLI: csv dedupe keyed by column
**Scenario:** Remove duplicate rows by `id`, keep first.

**Answer:** Track ids; write out.
```python
import argparse, csv

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--in", dest="inp", required=True)
    p.add_argument("--out", dest="out", required=True)
    p.add_argument("--key", required=True)
    a = p.parse_args()

    seen = set()
    with open(a.inp, newline="", encoding="utf-8") as fi, \
         open(a.out, "w", newline="", encoding="utf-8") as fo:
        r = csv.DictReader(fi)
        w = csv.DictWriter(fo, fieldnames=r.fieldnames)
        w.writeheader()
        for row in r:
            k = row.get(a.key)
            if k not in seen:
                seen.add(k)
                w.writerow(row)

if __name__ == "__main__":
    main()
```

## Q63. Email: build multipart (text + attachment)
**Scenario:** Create an email with a small text attachment; no sending.

**Answer:** Use `EmailMessage`.
```python
from email.message import EmailMessage

def with_attachment():
    m = EmailMessage()
    m["From"] = "a@example.com"
    m["To"] = "b@example.com"
    m["Subject"] = "Report"
    m.set_content("See attached report.")
    m.add_attachment(b"hello,world\n", maintype="text", subtype="plain", filename="report.txt")
    return m.as_string()
```

## Q64. XML: transform elements into dicts
**Scenario:** Convert `<user id="1"><name>A</name></user>` to `{"id":"1","name":"A"}`.

**Answer:** ElementTree traversal.
```python
import xml.etree.ElementTree as ET

def user_to_dict(elem):
    out = dict(elem.attrib)
    for child in elem:
        out[child.tag] = child.text
    return out
```

## Q65. Exceptions: escalating after partial cleanup
**Scenario:** Close files, then re-raise the original error.

**Answer:** `finally` with bare `raise` inside `except`.
```python
def process(path):
    f = None
    try:
        f = open(path)
        return f.read()
    except Exception:
        if f: f.close()
        raise
```

## Q66. Strings: normalize whitespace and collapse multiples
**Scenario:** Convert messy input to single-spaced text.

**Answer:** Split and join.
```python
def normalize_spaces(s):
    return " ".join(s.split())
```

## Q67. Lists: stable sort by multiple keys with missing values
**Scenario:** Sort by last name then first name; missing values last.

**Answer:** Use tuple keys with `or`.
```python
def sort_people(rows):
    rows.sort(key=lambda r: ((r.get("last") or "zzz"), (r.get("first") or "zzz")))
```

## Q68. Sets: compute Jaccard similarity
**Scenario:** Compare two documents by unique word overlap.

**Answer:** |A∩B| / |A∪B|.
```python
def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a or b else 1.0
```

## Q69. Tuples: Named result for readability
**Scenario:** Return stats `(min, max, avg)` with field access by name.

**Answer:** Use `collections.namedtuple`.
```python
from collections import namedtuple

Stats = namedtuple("Stats", "min max avg")
def stats(xs):
    return Stats(min(xs), max(xs), sum(xs)/len(xs))
```

## Q70. Dicts: LRU-like eviction by insertion order
**Scenario:** Keep only last N inserted keys (3.7+ dicts are ordered).

**Answer:** Pop oldest when over capacity.
```python
def put(cache: dict, k, v, cap=100):
    cache[k] = v
    while len(cache) > cap:
        cache.pop(next(iter(cache)))
```

## Q71. Conversions: parse `key=value` lines to dict
**Scenario:** Read simple config file.

**Answer:** Split on first `=`.
```python
def parse_kv(lines):
    out = {}
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"): continue
        k, _, v = line.partition("=")
        out[k.strip()] = v.strip()
    return out
```

## Q72. Conditionals: tri-state boolean from string
**Scenario:** Map `"yes"|"no"|""` → `True|False|None`.

**Answer:** Case-insensitive mapping.
```python
def parse_bool(s: str | None):
    if not s: return None
    s = s.strip().lower()
    if s in {"y","yes","true","1"}: return True
    if s in {"n","no","false","0"}: return False
    return None
```

## Q73. Loops: paginate a generator
**Scenario:** Yield pages of N items from a big generator.

**Answer:** Accumulate until full.
```python
def paginate(gen, size):
    page = []
    for item in gen:
        page.append(item)
        if len(page) == size:
            yield page
            page = []
    if page:
        yield page
```

## Q74. Functions: compose two callables
**Scenario:** Build `g∘f`.

**Answer:** Return a wrapper.
```python
def compose(f, g):
    return lambda x: g(f(x))
```

## Q75. Exceptions: retry only on selected messages
**Scenario:** Retry if message contains “temporarily”.

**Answer:** Inspect `str(e)`.
```python
def retry_on_message(fn, times=3):
    for i in range(times):
        try:
            return fn()
        except Exception as e:
            if "temporarily" not in str(e) or i == times-1:
                raise
```

## Q76. OOP: iterable data source class
**Scenario:** `for row in DataSource(path)` should yield parsed rows.

**Answer:** Implement `__iter__`.
```python
class DataSource:
    def __init__(self, path): self.path = path
    def __iter__(self):
        with open(self.path, encoding="utf-8") as f:
            for line in f:
                yield line.rstrip("\n").split(",")
```

## Q77. OOP: singleton via module-level instance (simple)
**Scenario:** Provide a config registry singleton without metaclasses.

**Answer:** Expose one instance.
```python
class Registry:
    def __init__(self): self._d = {}
    def get(self,k,default=None): return self._d.get(k, default)
    def set(self,k,v): self._d[k]=v

registry = Registry()  # import and use this instance
```

## Q78. Modules: import from sibling package using absolute import
**Scenario:** Project layout enforces absolute imports.

**Answer:** `from pkg.module import thing`.
```python
# app/controllers/user.py
from app.services.auth import login
```

## Q79. Logging + exceptions: capture stack trace with message
**Scenario:** On failure, log with stacktrace and continue.

**Answer:** `logger.exception`.
```python
import logging
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def do_work():
    try:
        1/0
    except Exception:
        log.exception("Work failed but continuing...")
```

# Scenario-Based Python Interview Questions & Answers (Extended, Standard Library Only)

## Q80. End-to-end: validate CSV, summarize, and write XML report
**Scenario:** Read `sales.csv` (`id,amount,date`), skip bad rows, compute total amount per date, write an XML like:
```xml
<report>
  <day date="2025-09-12" total="123.45"/>
</report>
```

**Answer:** Combine `csv`, `datetime`, and `xml.etree.ElementTree`.
```python
import csv, xml.etree.ElementTree as ET
from datetime import datetime
from collections import defaultdict

def build_report(csv_path, xml_path):
    totals = defaultdict(float)
    with open(csv_path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            try:
                amt = float(row["amount"])
                dt = datetime.fromisoformat(row["date"]).date().isoformat()
                totals[dt] += amt
            except (KeyError, ValueError):
                continue

    root = ET.Element("report")
    for day, total in sorted(totals.items()):
        ET.SubElement(root, "day", date=day, total=f"{total:.2f}")

    ET.ElementTree(root).write(xml_path, encoding="utf-8", xml_declaration=True)
```

## Q81. Robust `input()` workflow with defaults and retries
**Scenario:** CLI utility prompts for a port. If the user presses Enter, default to `8080`. Retry on invalid input; allow three attempts then exit politely.

**Answer:** Loop with counter and `isdigit()` checks.
```python
def prompt_port(default=8080, tries=3):
    for attempt in range(tries):
        s = input(f"Port [{default}]: ").strip()
        if not s:
            return default
        if s.isdigit() and 1 <= int(s) <= 65535:
            return int(s)
        print("Invalid port (1-65535).")
    raise SystemExit("Too many invalid attempts.")
```

## Q82. File IO: safe append with file locking (cross-platform light approach)
**Scenario:** Multiple processes append lines to the same log. Use a minimal advisory lock strategy on POSIX; on Windows, fall back to best effort.

**Answer:** Use `fcntl` if available, else plain append.
```python
import os, sys

def append_line(path, line):
    if os.name == "posix":
        import fcntl
        with open(path, "a", encoding="utf-8") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            try:
                f.write(line + "\n")
            finally:
                fcntl.flock(f, fcntl.LOCK_UN)
    else:
        with open(path, "a", encoding="utf-8") as f:
            f.write(line + "\n")
```

## Q83. Strings: CSV line sanitizer without using `csv` module
**Scenario:** You must sanitize a single CSV line by escaping embedded quotes and wrapping fields that contain commas or quotes.

**Answer:** Implement RFC-style quoting.
```python
def csv_escape(fields):
    out = []
    for f in fields:
        needs_quote = (',' in f) or ('"' in f) or ("\n" in f)
        g = f.replace('"', '""')
        out.append(f'"{g}"' if needs_quote else g)
    return ",".join(out)
```

## Q84. Operators: custom sort with “priority bucket” items first
**Scenario:** Sort product codes so that codes starting with `VIP-` appear first, then the rest alphabetically.

**Answer:** Supply a tuple key.
```python
def sort_codes(codes):
    return sorted(codes, key=lambda c: (0 if c.startswith("VIP-") else 1, c))
```

## Q85. Lists: in-place remove duplicates keeping last occurrence
**Scenario:** Given `["a","b","a","c","b"]` ⇒ `["a","c","b"]` (keep last positions).

**Answer:** Walk backward; track seen; rebuild slice.
```python
def dedupe_keep_last(xs):
    seen = set()
    out = []
    for x in reversed(xs):
        if x not in seen:
            seen.add(x)
            out.append(x)
    xs[:] = reversed(out)
```

## Q86. Sets: fast membership gate for high-volume stream
**Scenario:** You repeatedly check if user IDs are in a denylist. Show why a `set` beats a `list` and implement the check.

**Answer:** Use O(1) average lookup with `set`.
```python
def gate(user_id, deny: set):
    return user_id not in deny
```

## Q87. Tuples & immutability: cache keys for expensive function
**Scenario:** Build a cache key from multiple parameters including lists. Make the key hashable.

**Answer:** Convert nested lists to tuples.
```python
def keyify(*args):
    def freeze(x):
        if isinstance(x, list): return tuple(map(freeze, x))
        if isinstance(x, dict): return tuple(sorted((k, freeze(v)) for k,v in x.items()))
        return x
    return tuple(map(freeze, args))
```

## Q88. Dicts: diff two configuration maps
**Scenario:** Produce three dicts: `added`, `removed`, and `changed` (where value differs).

**Answer:** Compare key sets and values.
```python
def diff_dicts(a, b):
    ka, kb = set(a), set(b)
    added   = {k: b[k] for k in kb - ka}
    removed = {k: a[k] for k in ka - kb}
    changed = {k: (a[k], b[k]) for k in ka & kb if a[k] != b[k]}
    return added, removed, changed
```

## Q89. Conversions: pivot a list of dict rows to dict of lists (columns)
**Scenario:** Convert `rows=[{"x":1,"y":2},{"x":3,"y":4}]` ⇒ `{"x":[1,3],"y":[2,4]}`.

**Answer:** Initialize lists per column.
```python
def pivot(rows):
    cols = {}
    for r in rows:
        for k, v in r.items():
            cols.setdefault(k, []).append(v)
    return cols
```

## Q90. Conditionals: readable rule engine using lookup tables
**Scenario:** Compute shipping fee by `(country, weight_kg)` brackets without many `if/elif`.

**Answer:** Nested dict and range lookup.
```python
RATES = {
    "IN": [(1, 50), (5, 120), (float("inf"), 200)],
    "US": [(1, 70), (5, 150), (float("inf"), 250)],
}
def shipping(country, weight):
    for limit, price in RATES.get(country, RATES["US"]):
        if weight <= limit:
            return price
    return 0
```

## Q91. Loops: bounded retry with `for-else` + `break`
**Scenario:** Try pinging a host up to 5 times; report failure if all attempts fail.

**Answer:** Use `for ... else`.
```python
def ping_sim(tries=5):
    for _ in range(tries):
        if do_ping():
            print("up"); break
    else:
        print("down")
# placeholder
def do_ping(): return False
```

## Q92. Functions: pure function vs side effects in data cleaners
**Scenario:** Implement both a pure cleaner (returns new list) and an in-place cleaner; explain tradeoffs.

**Answer:** Provide two variants.
```python
def clean_new(xs):  # pure
    return [x.strip() for x in xs]

def clean_inplace(xs):  # mutates
    for i, x in enumerate(xs):
        xs[i] = x.strip()
```

## Q93. Exceptions: domain-specific error hierarchy
**Scenario:** Create custom exceptions `ConfigError` and `MissingKey` (subclass) and show targeted handling.

**Answer:** Subclass `Exception`.
```python
class ConfigError(Exception): pass
class MissingKey(ConfigError): pass

def read_required(d, key):
    if key not in d: raise MissingKey(f"missing {key}")
    return d[key]
```

## Q94. OOP: encapsulate resource lifecycle with context manager
**Scenario:** A `Session` opens a file and ensures closure even on errors using `with`.

**Answer:** Implement `__enter__`/`__exit__`.
```python
class Session:
    def __init__(self, path): self.path = path; self.f = None
    def __enter__(self):
        self.f = open(self.path, "w", encoding="utf-8"); return self.f
    def __exit__(self, exc_type, exc, tb):
        if self.f: self.f.close()
        return False
```

## Q95. OOP Inheritance: cooperative multiple inheritance
**Scenario:** Ensure both mixins’ `__init__` run correctly.

**Answer:** Use `super()` in all classes.
```python
class A:
    def __init__(self, *a, **k): super().__init__(*a, **k); self.a=True
class B:
    def __init__(self, *a, **k): super().__init__(*a, **k); self.b=True
class C(A, B):
    def __init__(self): super().__init__()
```

## Q96. Dunder `__repr__`: debug-friendly representation
**Scenario:** Implement a concise `__repr__` for an order object that includes ID and item count.

**Answer:** Return unambiguous string.
```python
class Order:
    def __init__(self, oid, items): self.oid=oid; self.items=list(items)
    def __repr__(self): return f"Order(oid={self.oid!r}, items={len(self.items)})"
```

## Q97. Modules: split utilities across files and re-export API
**Scenario:** Have `utils/strings.py` and `utils/files.py`, expose a flat API on import `from utils import slugify, read_text`.

**Answer:** Re-export in `__init__.py`.
```python
# utils/__init__.py
from .strings import slugify
from .files import read_text
__all__ = ["slugify", "read_text"]
```

## Q98. Modules: demonstrate `if __name__ == "__main__"` testing block
**Scenario:** Add quick smoke tests runnable only when the file is executed directly.

**Answer:** Guard under main.
```python
def add(a,b): return a+b

if __name__ == "__main__":
    assert add(2,3) == 5
    print("OK")
```

## Q99. CSV: tolerant numeric parser with blanks and currency symbols
**Scenario:** Parse values like `" $1,234.50 "` → `1234.50` or `None` if not numeric.

**Answer:** Clean then convert.
```python
def parse_money(s):
    if s is None: return None
    s = s.strip().replace(",", "").replace("$", "")
    if not s: return None
    try: return float(s)
    except ValueError: return None
```

## Q100. Datetime: bucket timestamps into hourly windows
**Scenario:** Given ISO strings, group counts by hour `YYYY-MM-DD HH:00`.

**Answer:** Round down minutes/seconds.
```python
from datetime import datetime

def hourly_buckets(iso_ts):
    buckets = {}
    for ts in iso_ts:
        dt = datetime.fromisoformat(ts)
        hour = dt.replace(minute=0, second=0, microsecond=0)
        buckets[hour] = buckets.get(hour, 0) + 1
    return buckets
```

## Q101. File IO: read a huge file and report top 10 most common lines
**Scenario:** Memory is limited; avoid loading everything at once.

**Answer:** Count incrementally.
```python
from collections import Counter

def top_lines(path, n=10):
    c = Counter()
    with open(path, encoding="utf-8") as f:
        for line in f:
            c[line.rstrip("\n")] += 1
    return c.most_common(n)
```

## Q102. JSON: streaming writer that writes one JSON per line (JSONL)
**Scenario:** Append events so each line is a JSON object for easy processing.

**Answer:** Use `json.dumps` per line.
```python
import json
def write_jsonl(path, records):
    with open(path, "a", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
```

## Q103. Lambda: conditional expression inside comprehension
**Scenario:** Transform negatives to zero while keeping positives.

**Answer:** Use inline conditional.
```python
def clamp_nonneg(xs):
    return [x if x >= 0 else 0 for x in xs]
```

## Q104. Logging: per-module logger hierarchy
**Scenario:** Child modules should inherit level/handlers from a package logger.

**Answer:** Get loggers by name.
```python
import logging
logging.basicConfig(level=logging.INFO)
pkg_logger = logging.getLogger("mypkg")
child_logger = logging.getLogger("mypkg.sub.mod")
child_logger.info("inherits handlers")
```

## Q105. Argparse: subcommands (`init`, `run`) with different options
**Scenario:** `tool init --path P` and `tool run --threads N`.

**Answer:** Use subparsers.
```python
import argparse

p = argparse.ArgumentParser("tool")
subs = p.add_subparsers(dest="cmd", required=True)

sp_init = subs.add_parser("init")
sp_init.add_argument("--path", required=True)

sp_run = subs.add_parser("run")
sp_run.add_argument("--threads", type=int, default=1)

args = p.parse_args()
```

## Q106. XML: pretty-print output with indentation
**Scenario:** ElementTree writes compact XML; indent for readability.

**Answer:** Implement recursive indenter.
```python
import xml.etree.ElementTree as ET

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for e in elem:
            indent(e, level+1)
        if not e.tail or not e.tail.strip():
            e.tail = i
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i
```

## Q107. Email: parse a raw email and extract subject + sender
**Scenario:** Given a raw RFC 5322 message string, parse headers and get payload.

**Answer:** Use `email.parser`.
```python
from email import message_from_string

def parse_raw(raw):
    msg = message_from_string(raw)
    return msg.get("Subject"), msg.get("From"), msg.get_payload()
```

## Q108. `input()`: hidden password prompt without echo
**Scenario:** Ask for a password without showing typed characters.

**Answer:** Use `getpass`.
```python
import getpass
pwd = getpass.getpass("Password: ")
```

## Q109. Exceptions: wrap unknown errors with context without losing traceback
**Scenario:** Add context string and preserve original traceback.

**Answer:** Use `raise ... from e`.
```python
def load_json_safe(s):
    import json
    try:
        return json.loads(s)
    except Exception as e:
        raise ValueError("Invalid JSON payload") from e
```

## Q110. OOP: enforce read-only attribute via `@property` no setter
**Scenario:** `Order.total` is computed and must not be set externally.

**Answer:** Provide only getter.
```python
class Order:
    def __init__(self, items): self.items = list(items)
    @property
    def total(self): return sum(price*qty for price, qty in self.items)
```

## Q111. Dunder `__eq__`/`__hash__` consistency
**Scenario:** Make `User(id)` comparable by id and usable as a dict key.

**Answer:** Define both.
```python
class User:
    def __init__(self, uid): self.uid = uid
    def __eq__(self, other): return isinstance(other, User) and self.uid == other.uid
    def __hash__(self): return hash(self.uid)
```

## Q112. Modules: load a Python file from a path at runtime
**Scenario:** Simple plug-in system: import a module by file path.

**Answer:** Use `importlib.util`.
```python
import importlib.util, sys

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod
```

## Q113. CSV: compute column stats (min/max/avg) with missing values
**Scenario:** Skip blanks, tolerate invalid cells.

**Answer:** Aggregate safely.
```python
def stats_csv(path, col):
    n = s = mn = mx = None, 0.0, None, None
    n = 0
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            try:
                v = float(row[col])
            except (KeyError, ValueError, TypeError):
                continue
            s += v; n += 1
            mn = v if mn is None else min(mn, v)
            mx = v if mx is None else max(mx, v)
    return {"count": n, "min": mn, "max": mx, "avg": (s/n if n else None)}
```

## Q114. Datetime: compute next business day skipping weekends
**Scenario:** If date is Fri or weekend, return next Monday.

**Answer:** Adjust by weekday index.
```python
from datetime import date, timedelta

def next_business_day(d: date):
    wd = d.weekday()  # Mon=0..Sun=6
    if wd >= 4:
        return d + timedelta(days=7 - wd)
    return d + timedelta(days=1)
```

## Q115. File IO: detect and convert file encoding to UTF-8 (basic heuristic)
**Scenario:** Treat files as UTF-8 if possible, else fallback to Latin-1.

**Answer:** Try/except decode.
```python
def read_text_best_effort(path):
    try:
        return open(path, encoding="utf-8").read()
    except UnicodeDecodeError:
        return open(path, encoding="latin-1").read()
```

## Q116. JSON: merge two JSON objects deeply
**Scenario:** Recursively merge nested dicts; lists concatenate; scalars from `b` override `a`.

**Answer:** Recursive function.
```python
def deep_merge(a, b):
    if isinstance(a, dict) and isinstance(b, dict):
        out = dict(a)
        for k, v in b.items():
            out[k] = deep_merge(a.get(k), v) if k in a else v
        return out
    if isinstance(a, list) and isinstance(b, list):
        return a + b
    return b
```

## Q117. Lambda: key function for natural sort (`x2` before `x10`)
**Scenario:** Sort strings containing numbers in human order.

**Answer:** Split into digit/non-digit chunks.
```python
import re
def naturalsort_key(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.findall(r"\d+|\D+", s)]
```

## Q118. Logging: JSON-like structured log line without external libs
**Scenario:** Emit one-line JSON fields for ingestion.

**Answer:** Use `json.dumps` in formatter.
```python
import logging, json, sys

class JSONFormatter(logging.Formatter):
    def format(self, record):
        obj = {"lvl": record.levelname, "msg": record.getMessage(), "name": record.name}
        return json.dumps(obj, ensure_ascii=False)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JSONFormatter())
log = logging.getLogger("svc"); log.setLevel(logging.INFO); log.addHandler(handler)
log.info("started")
```

## Q119. Argparse: environment variable defaults
**Scenario:** If `--host` not supplied, default from `APP_HOST` env or `127.0.0.1`.

**Answer:** Read `os.environ`.
```python
import argparse, os

p = argparse.ArgumentParser()
p.add_argument("--host", default=os.environ.get("APP_HOST", "127.0.0.1"))
args = p.parse_args()
```

## Q120. XML: schema-less validation by tag/attribute presence
**Scenario:** Ensure each `<user>` has `id` and `<name>` child; collect errors.

**Answer:** Walk tree and record issues.
```python
import xml.etree.ElementTree as ET

def validate_users_xml(path):
    errors = []
    root = ET.parse(path).getroot()
    for u in root.findall(".//user"):
        if "id" not in u.attrib:
            errors.append("user missing id")
        if u.find("name") is None:
            errors.append(f"user {u.get('id','?')} missing <name>")
    return errors
```
# Scenario-Based Python Interview Questions & Answers — Extended (Lengthier Tasks, Stdlib Only)

> Continuing from Q120. Longer, real-interview scenarios. No third-party libraries. Only topics in your README (core language, OOP, modules, and stdlib items like csv, datetime, file I/O, json, lambda, logging, argparse, xml, email, input).  
> All code fences are prefixed so they won’t render in your UI.

## Q121. Build a **mini template engine** for emails
**Scenario:** Marketing wants to send emails using templates like:  
`"Hello {{ name }}, your order {{ order_id }} ships on {{ date:%Y-%m-%d }}."`  
Rules:  
- `{{ var }}` inserts value from a dict.  
- `{{ var:%FORMAT }}` applies `datetime.strftime` if the value is a `datetime`.  
- Unknown keys should raise a clear error.  
- No third-party libs.  

**Answer:** Tokenize with regex, resolve placeholders, handle `strftime` if a format suffix exists.

```python
import re
from datetime import datetime

TOKEN = re.compile(r"\{\{\s*([a-zA-Z_]\w*)(?::%([^}]+))?\s*\}\}")

def render(template: str, ctx: dict) -> str:
    def sub(m: re.Match):
        key = m.group(1)
        fmt = m.group(2)
        if key not in ctx:
            raise KeyError(f"Missing key: {key}")
        val = ctx[key]
        if fmt:
            if not isinstance(val, datetime):
                raise TypeError(f"Key {key} requires datetime for format %{fmt}")
            return val.strftime("%" + fmt)
        return str(val)
    return TOKEN.sub(sub, template)

# Example
# print(render("Hello {{ name }}, ship {{ date:%Y-%m-%d }}", {"name":"A", "date":datetime.now()}))
```

## Q122. **CSV Schema Validator & Normalizer** with configurable rules
**Scenario:** Data team supplies a YAML/JSON spec (assume JSON for stdlib) describing columns with types (`int`, `float`, `str`), required flags, and default values if missing. Build a validator that:  
- Reads CSV rows as dicts  
- Coerces types (empty → default if provided, else error for required)  
- Reports row-level errors and writes a “cleaned” CSV  

**Answer:** Encode schema, coerce, collect errors.

```python
import csv, json

def coerce(value, typ):
    if value is None or value == "":
        return None
    if typ == "int":
        return int(value)
    if typ == "float":
        return float(value)
    if typ == "str":
        return str(value)
    raise ValueError(f"Unknown type {typ}")

def validate_and_clean(csv_in, csv_out, spec_json):
    spec = json.loads(spec_json)  # {"columns":[{"name":"id","type":"int","required":True,"default":null}, ...]}
    cols = [c["name"] for c in spec["columns"]]
    rules = {c["name"]: c for c in spec["columns"]}
    errors = []

    with open(csv_in, newline="", encoding="utf-8") as fi, \
         open(csv_out, "w", newline="", encoding="utf-8") as fo:
        r = csv.DictReader(fi)
        w = csv.DictWriter(fo, fieldnames=cols)
        w.writeheader()
        for i, row in enumerate(r, 2):
            clean = {}
            row_ok = True
            for name in cols:
                rule = rules[name]
                val = row.get(name, "")
                if val == "" and rule.get("default") is not None:
                    val = rule["default"]
                try:
                    clean[name] = coerce(val, rule["type"])
                    if rule.get("required") and (clean[name] is None or clean[name] == ""):
                        raise ValueError("required missing")
                except Exception as e:
                    row_ok = False
                    errors.append((i, name, str(e), val))
                    break
            if row_ok:
                # write normalized strings for CSV
                w.writerow({k: ("" if v is None else v) for k, v in clean.items()})
    return errors
```

## Q123. **Join two CSVs** (left join) without pandas
**Scenario:** Given `orders.csv` (order_id, user_id, amount) and `users.csv` (user_id, name), output `orders_enriched.csv` with `name` added. If user missing, put `UNKNOWN`.  

**Answer:** Build an index dict for `users`, stream through orders.

```python
import csv

def left_join_orders_users(orders_path, users_path, out_path):
    users = {}
    with open(users_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            users[row["user_id"]] = row.get("name","")

    with open(orders_path, newline="", encoding="utf-8") as fi, \
         open(out_path, "w", newline="", encoding="utf-8") as fo:
        r = csv.DictReader(fi)
        fn = r.fieldnames + ["name"]
        w = csv.DictWriter(fo, fieldnames=fn)
        w.writeheader()
        for row in r:
            uid = row.get("user_id")
            row["name"] = users.get(uid, "UNKNOWN")
            w.writerow(row)
```

## Q124. **Command-line ToDo Manager** (JSON-backed, `argparse`)
**Scenario:** Build `todo.py` that supports:  
- `add --text "Buy milk"`  
- `list` (show pending with IDs)  
- `done --id 3` (mark as done with timestamp)  
Data persists to `todo.json`.  

**Answer:** CLI with subcommands, JSON read/write, timestamps.

```python
import argparse, json, os
from datetime import datetime

STORE = "todo.json"

def load():
    if not os.path.exists(STORE): return []
    with open(STORE, encoding="utf-8") as f:
        return json.load(f)

def save(items):
    with open(STORE, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

def add(text):
    items = load()
    items.append({"id": (items[-1]["id"]+1 if items else 1),
                  "text": text, "done": False, "done_at": None})
    save(items)

def mark_done(iid):
    items = load()
    for it in items:
        if it["id"] == iid and not it["done"]:
            it["done"] = True
            it["done_at"] = datetime.now().isoformat(timespec="seconds")
            break
    save(items)

def list_items():
    for it in load():
        flag = "✓" if it["done"] else " "
        print(f"[{flag}] {it['id']:3d}  {it['text']}  {it['done_at'] or ''}")

def main():
    p = argparse.ArgumentParser("todo")
    sp = p.add_subparsers(dest="cmd", required=True)
    a = sp.add_parser("add"); a.add_argument("--text", required=True)
    l = sp.add_parser("list")
    d = sp.add_parser("done"); d.add_argument("--id", type=int, required=True)
    args = p.parse_args()
    if args.cmd == "add": add(args.text)
    elif args.cmd == "list": list_items()
    else: mark_done(args.id)

if __name__ == "__main__":
    main()
```

## Q125. **Transactional File Writes** with rollback on error
**Scenario:** You must update two files. If writing the second fails, revert the first to its original content to maintain consistency.  

**Answer:** Read originals, write temps, replace both; on failure, roll back.

```python
import os, tempfile, shutil

def write_atomic_pair(path1, data1, path2, data2):
    d1, d2 = os.path.dirname(path1) or ".", os.path.dirname(path2) or "."
    fd1, tmp1 = tempfile.mkstemp(dir=d1, prefix=".tmp_")
    fd2, tmp2 = tempfile.mkstemp(dir=d2, prefix=".tmp_")
    try:
        with os.fdopen(fd1, "w", encoding="utf-8") as f1: f1.write(data1)
        with os.fdopen(fd2, "w", encoding="utf-8") as f2: f2.write(data2)
        # both temps written, now replace originals atomically
        os.replace(tmp1, path1)
        os.replace(tmp2, path2)
    except Exception:
        # best-effort cleanup
        for t in (tmp1, tmp2):
            try: os.remove(t)
            except OSError: pass
        raise
```

## Q126. **Job Scheduler** using `heapq` (priority queue)
**Scenario:** Implement an in-process scheduler that schedules callables at given datetimes. Supports `schedule(fn, when)` and `run_pending(now)` that executes due jobs in timestamp order.  

**Answer:** Use min-heap keyed by epoch time.

```python
import heapq, time
from datetime import datetime, timezone

class Scheduler:
    def __init__(self): self.q = []  # (epoch, seq, fn)
    def schedule(self, fn, when: datetime):
        epoch = when.replace(tzinfo=when.tzinfo or timezone.utc).timestamp()
        heapq.heappush(self.q, (epoch, len(self.q), fn))
    def run_pending(self, now=None):
        now = now or time.time()
        while self.q and self.q[0][0] <= now:
            _, _, fn = heapq.heappop(self.q)
            fn()

# Example
# s = Scheduler(); s.schedule(lambda: print("run"), datetime.now(timezone.utc)); s.run_pending()
```

## Q127. **Topological Sort** for module build order
**Scenario:** Given module dependencies as `{mod: [deps...]}`, produce a build order or detect cycles.  

**Answer:** DFS with temporary marks to detect cycles.

```python
def topo_sort(graph: dict[str, list[str]]):
    visited, temp, out = set(), set(), []

    def visit(n):
        if n in visited: return
        if n in temp: raise ValueError("Cycle detected")
        temp.add(n)
        for m in graph.get(n, []):
            visit(m)
        temp.remove(n)
        visited.add(n)
        out.append(n)

    for k in graph:
        visit(k)
    return out  # reverse postorder
```

## Q128. **Finite State Machine** for simple token validator
**Scenario:** Validate identifiers that must start with a letter or `_`, followed by letters, digits, or `_`, and cannot end with `_`.  

**Answer:** Explicit states and transitions.

```python
import string
ALPHA = set(string.ascii_letters + "_")
ALNUMU = set(string.ascii_letters + string.digits + "_")

def valid_ident(s):
    if not s or s[0] not in ALPHA: return False
    for ch in s[1:]:
        if ch not in ALNUMU: return False
    return s[-1] != "_"
```

## Q129. **Mini Query Language Parser** using `ast`-like evaluation
**Scenario:** Filter list of dicts with expressions like `score > 90 and passed == True`. Support ops: `==`, `!=`, `<`, `<=`, `>`, `>=`, `and`, `or`, `not`, parentheses.  

**Answer:** Tokenize + recursive descent parser → eval against a record.

```python
import re, operator

OPS = {"==":operator.eq,"!=":operator.ne,"<":operator.lt,"<=":operator.le,">":operator.gt,">=":operator.ge}
TOK = re.compile(r"\s*(\(|\)|==|!=|<=|>=|<|>|and|or|not|True|False|[A-Za-z_]\w*|\d+)\s*")

def tokenize(s): return [t for t in TOK.findall(s)]

def parse(tokens):
    pos = 0
    def peek(): return tokens[pos] if pos < len(tokens) else None
    def eat(t=None):
        nonlocal pos
        tok = peek()
        if t and tok != t: raise SyntaxError(f"expected {t}")
        pos += 1; return tok

    def atom():
        tok = peek()
        if tok == "(":
            eat("("); e = expr(); eat(")"); return e
        if tok in ("True","False"):
            eat(); return ("const", tok == "True")
        if tok and tok.isdigit():
            eat(); return ("const", int(tok))
        if tok and re.match(r"[A-Za-z_]\w*", tok):
            eat(); return ("var", tok)
        raise SyntaxError("bad token")

    def notexpr():
        if peek() == "not":
            eat("not"); return ("not", notexpr())
        return comp()

    def comp():
        left = atom()
        tok = peek()
        if tok in OPS:
            op = eat(); right = atom()
            return ("binop", op, left, right)
        return left

    def andexpr():
        left = notexpr()
        while peek() == "and":
            eat("and"); left = ("and", left, notexpr())
        return left

    def expr():
        left = andexpr()
        while peek() == "or":
            eat("or"); left = ("or", left, andexpr())
        return left

    tree = expr()
    if pos != len(tokens): raise SyntaxError("extra tokens")
    return tree

def eval_ast(node, row):
    t = node[0]
    if t == "const": return node[1]
    if t == "var":   return row.get(node[1])
    if t == "not":   return not eval_ast(node[1], row)
    if t == "and":   return eval_ast(node[1], row) and eval_ast(node[2], row)
    if t == "or":    return eval_ast(node[1], row) or  eval_ast(node[2], row)
    if t == "binop":
        _, op, l, r = node
        return OPS[op](eval_ast(l, row), eval_ast(r, row))
    raise ValueError("bad node")
```

## Q130. **Rolling Log Rotation** with `logging.handlers`
**Scenario:** Implement rotating logs: max file 1MB, keep 3 backups, log format with ISO timestamps and module names.  

**Answer:** Configure `RotatingFileHandler`.

```python
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(path="app.log"):
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)
    h = RotatingFileHandler(path, maxBytes=1_000_000, backupCount=3)
    fmt = logging.Formatter("%(asctime)s %(name)s %(levelname)s - %(message)s")
    h.setFormatter(fmt)
    logger.addHandler(h)
    return logger
```

## Q131. **Backup & Restore Utility** (tar-like directory copier)
**Scenario:** Copy a directory tree to a backup location and produce a manifest JSON with file sizes & SHA256. Also support restore mode that compares hashes and copies missing/different files back.  

**Answer:** Walk tree, hash files, JSON manifest.

```python
import os, json, hashlib, shutil

def sha256_path(p, chunk=1<<20):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(chunk), b""):
            h.update(b)
    return h.hexdigest()

def snapshot(root):
    manifest = {}
    for base, _, files in os.walk(root):
        for fn in files:
            path = os.path.join(base, fn)
            rel = os.path.relpath(path, root)
            manifest[rel] = {"size": os.path.getsize(path), "sha256": sha256_path(path)}
    return manifest

def backup(src, dst, manifest_path):
    if not os.path.exists(dst): os.makedirs(dst)
    man = snapshot(src)
    with open(manifest_path, "w") as f: json.dump(man, f, indent=2)
    for rel in man:
        s = os.path.join(src, rel); d = os.path.join(dst, rel)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        shutil.copy2(s, d)

def restore(dst, src, manifest_path):
    man = json.load(open(manifest_path))
    for rel, meta in man.items():
        s = os.path.join(src, rel); d = os.path.join(dst, rel)
        if not os.path.exists(d) or sha256_path(d) != meta["sha256"]:
            os.makedirs(os.path.dirname(d), exist_ok=True)
            shutil.copy2(s, d)
```

## Q132. **Email Digest Generator** (no send) aggregating CSV activity
**Scenario:** Generate a plaintext “daily digest” from `activity.csv` with columns `user, action, ts`. Group by user; sort entries by time. Create an `EmailMessage` (string) body.  

**Answer:** Parse CSV, group/sort, compose message.

```python
import csv
from collections import defaultdict
from email.message import EmailMessage
from datetime import datetime

def digest(csv_path):
    by_user = defaultdict(list)
    with open(csv_path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            by_user[r["user"]].append((r["action"], r["ts"]))
    lines = []
    for user, items in sorted(by_user.items()):
        items.sort(key=lambda x: datetime.fromisoformat(x[1]))
        lines.append(f"User: {user}")
        for action, ts in items:
            lines.append(f"  - {ts}  {action}")
        lines.append("")
    body = "\n".join(lines)
    msg = EmailMessage()
    msg["Subject"] = "Daily Activity Digest"
    msg.set_content(body)
    return msg.as_string()
```

## Q133. **Regex-based Log Parser** into structured JSONL
**Scenario:** Parse lines like `2025-09-12T08:33:12Z INFO module - message text` into JSON fields (`ts, level, module, msg`). Write JSONL.  

**Answer:** Regex capture groups, `json.dumps` per line.

```python
import re, json

PAT = re.compile(r"^(\S+) (\S+) (\S+) - (.*)$")

def logs_to_jsonl(path_in, path_out):
    with open(path_in, encoding="utf-8") as fi, open(path_out, "w", encoding="utf-8") as fo:
        for line in fi:
            m = PAT.match(line.rstrip("\n"))
            if not m: continue
            ts, level, module, msg = m.groups()
            fo.write(json.dumps({"ts": ts, "level": level, "module": module, "msg": msg}) + "\n")
```

## Q134. **CSV Windowed Aggregations** (sum over trailing N rows per group)
**Scenario:** Given transactions with `user, amount`, compute for each row the sum of the last 3 amounts for that *user*, including current row.  

**Answer:** Maintain per-user deque and rolling sums.

```python
import csv
from collections import deque

def window_sum_by_user(in_path, out_path, k=3):
    state = {}  # user -> (deque, running_sum)
    with open(in_path, newline="", encoding="utf-8") as fi, \
         open(out_path, "w", newline="", encoding="utf-8") as fo:
        r = csv.DictReader(fi)
        w = csv.DictWriter(fo, fieldnames=r.fieldnames + ["sum_last_k"])
        w.writeheader()
        for row in r:
            u = row["user"]; amt = float(row["amount"])
            dq, total = state.get(u, (deque(), 0.0))
            dq.append(amt); total += amt
            if len(dq) > k:
                total -= dq.popleft()
            state[u] = (dq, total)
            row["sum_last_k"] = f"{total:.2f}"
            w.writerow(row)
```

## Q135. **Inventory Reconciliation** with discrepancy report
**Scenario:** Two CSVs: `expected.csv` and `actual.csv` with `sku, qty`. Report: `missing` (in expected not actual), `extra` (in actual not expected), `mismatch` (present in both but different qty).  

**Answer:** Build dicts and compare.

```python
import csv

def load_kv(path):
    d = {}
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            d[r["sku"]] = int(r["qty"])
    return d

def reconcile(expected, actual):
    exp, act = load_kv(expected), load_kv(actual)
    missing = {k: exp[k] for k in exp.keys() - act.keys()}
    extra   = {k: act[k] for k in act.keys() - exp.keys()}
    mismatch = {k: (exp[k], act[k]) for k in exp.keys() & act.keys() if exp[k] != act[k]}
    return missing, extra, mismatch
```

## Q136. **Text Indexer** (inverted index) with search query
**Scenario:** Index a set of text files into `term -> set(file)` (case-insensitive, alphanum tokens). Provide `search("cat AND dog")`, `search("cat OR dog")`, `search("cat NOT dog")`.  

**Answer:** Build inverted index; parse Boolean operators.

```python
import os, re
from collections import defaultdict

WORD = re.compile(r"[A-Za-z0-9]+")

class Index:
    def __init__(self): self.inv = defaultdict(set)
    def add_file(self, path):
        text = open(path, encoding="utf-8").read().lower()
        for w in WORD.findall(text):
            self.inv[w].add(path)

    def search(self, query):
        tokens = query.lower().split()
        if "and" in tokens:
            a, _, b = tokens
            return self.inv.get(a,set()) & self.inv.get(b,set())
        if "or" in tokens:
            a, _, b = tokens
            return self.inv.get(a,set()) | self.inv.get(b,set())
        if "not" in tokens:
            a, _, b = tokens
            return self.inv.get(a,set()) - self.inv.get(b,set())
        return self.inv.get(tokens[0], set())
```

## Q137. **CSV → XML Converter** with mapping and attribute support
**Scenario:** Map CSV columns to XML attributes and child elements. Example output:
```xml
<users>
  <user id="1"><name>Alice</name><age>30</age></user>
</users>
```

**Answer:** Build tree with ElementTree.

```python
import csv, xml.etree.ElementTree as ET

def csv_to_xml(csv_path, xml_path):
    root = ET.Element("users")
    with open(csv_path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            u = ET.SubElement(root, "user", id=r["id"])
            ET.SubElement(u, "name").text = r.get("name", "")
            ET.SubElement(u, "age").text = r.get("age", "")
    ET.ElementTree(root).write(xml_path, encoding="utf-8", xml_declaration=True)
```

## Q138. **Stats Pipeline** with median & percentile (no numpy)
**Scenario:** Given a list of numbers, compute median and p95.  

**Answer:** Sort and compute indexes.

```python
def median(xs):
    xs = sorted(xs)
    n = len(xs)
    mid = n // 2
    return (xs[mid-1] + xs[mid]) / 2 if n % 2 == 0 else xs[mid]

def percentile(xs, p):
    xs = sorted(xs)
    k = (len(xs)-1) * (p/100)
    f = int(k)
    c = min(f+1, len(xs)-1)
    if f == c: return xs[f]
    return xs[f] + (xs[c]-xs[f]) * (k - f)
```

## Q139. **CSV Duplicate Finder** by multi-column key with report
**Scenario:** Given columns `["first","last","dob"]` define duplicates. Report groups with row numbers.  

**Answer:** Accumulate dictionary of key→rows.

```python
import csv
from collections import defaultdict

def find_dupes(path, key_cols):
    groups = defaultdict(list)
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for i, row in enumerate(r, 2):
            key = tuple(row[k] for k in key_cols)
            groups[key].append(i)
    return {k:v for k,v in groups.items() if len(v) > 1}
```

## Q140. **Mini Markdown to Text** converter (very limited)
**Scenario:** Support bold `**x**`, italics `_x_`, inline code `` `code` ``, and strip headings `#`.  

**Answer:** Regex replaces.

```python
import re

def md_to_text(s):
    s = re.sub(r"^#+\s*", "", s, flags=re.MULTILINE)      # headings
    s = re.sub(r"\*\*(.*?)\*\*", r"\1", s)                # bold
    s = re.sub(r"_(.*?)_", r"\1", s)                      # italics
    s = re.sub(r"`([^`]+)`", r"\1", s)                    # code
    return s
```

## Q141. **Path Normalizer & Deduplicator** for import paths
**Scenario:** Given a list of absolute/relative paths with `..`, `.`, and duplicates, return canonical absolute unique paths (no symlink resolution).  

**Answer:** Use `os.path.abspath` + `normpath`, store in set.

```python
import os

def normalize_paths(paths):
    norm = {os.path.abspath(os.path.normpath(p)) for p in paths}
    return sorted(norm)
```

## Q142. **Interactive Prompt** with command history (in-memory)
**Scenario:** Build a simple REPL for arithmetic expressions using the safe evaluator from earlier (Q54). Support `history` command to print past inputs.  

**Answer:** Loop, handle special commands, store history.

```python
def repl():
    hist = []
    while True:
        s = input("calc> ").strip()
        if s in {"exit","quit"}: break
        if s == "history":
            for i, h in enumerate(hist, 1): print(f"{i}: {h}")
            continue
        try:
            hist.append(s)
            print(safe_arith(s))  # from Q54
        except Exception as e:
            print("ERR:", e)
# repl()
```

## Q143. **User Config Loader** with environment overrides
**Scenario:** Load `config.json`, then overlay any environment variables with prefix `APP_` onto matching keys (case-insensitive).  

**Answer:** Normalize keys; overlay.

```python
import json, os

def load_config(path):
    cfg = json.load(open(path, encoding="utf-8"))
    # create case-insensitive key map
    lower_map = {k.lower(): k for k in cfg.keys()}
    for k, v in os.environ.items():
        if not k.startswith("APP_"): continue
        key = k[4:].lower()
        if key in lower_map:
            cfg[lower_map[key]] = v
    return cfg
```

## Q144. **File Differ** (line-by-line) with unified diff output
**Scenario:** Implement a small diff that aligns lines and prints context +/- markers (very simplified).  

**Answer:** Use `difflib.unified_diff` (stdlib).

```python
import difflib

def udiff(path_a, path_b):
    a = open(path_a, encoding="utf-8").read().splitlines()
    b = open(path_b, encoding="utf-8").read().splitlines()
    return "\n".join(difflib.unified_diff(a, b, fromfile=path_a, tofile=path_b))
```

## Q145. **Rate-limited Logger Adapter** (don’t spam)
**Scenario:** Only log identical messages once per 10 seconds; increment a suppressed counter otherwise, then print a summary when allowed again.  

**Answer:** Track last timestamp and count per message.

```python
import logging, time

class RateLimitedLogger:
    def __init__(self, logger=None, window=10.0):
        self.log = logger or logging.getLogger("rate")
        self.win = window
        self.state = {}  # msg -> (last_ts, suppressed)

    def info(self, msg):
        now = time.time()
        last, sup = self.state.get(msg, (0, 0))
        if now - last >= self.win:
            if sup:
                self.log.info("%s (suppressed %d similar msgs)", msg, sup)
            else:
                self.log.info(msg)
            self.state[msg] = (now, 0)
        else:
            self.state[msg] = (last, sup + 1)
```

## Q146. **Chunked File Downloader Simulator** (no network)
**Scenario:** Simulate reading a large local file in chunks and writing to a destination with progress callback. Useful for teaching chunked IO patterns.  

**Answer:** Loop with `read` and emit percentage.

```python
import os

def copy_chunked(src, dst, chunk=1<<20, on_progress=None):
    size = os.path.getsize(src)
    done = 0
    with open(src, "rb") as fi, open(dst, "wb") as fo:
        while True:
            b = fi.read(chunk)
            if not b: break
            fo.write(b)
            done += len(b)
            if on_progress:
                on_progress(done / size if size else 1.0)
```

## Q147. **Table Formatter** with column width detection and wrapping
**Scenario:** Given rows (list of dicts), print a table that wraps long cell contents to fit `max_width`.  

**Answer:** Compute col widths, wrap via `textwrap`.

```python
import textwrap

def print_table(rows, max_width=30):
    if not rows: return
    cols = list(rows[0].keys())
    widths = {c: min(max(len(str(r.get(c,""))) for r in rows), max_width) for c in cols}
    sep = " | "
    print(sep.join(c.ljust(widths[c]) for c in cols))
    print("-+-".join("-"*widths[c] for c in cols))
    for r in rows:
        lines = []
        for c in cols:
            cell = str(r.get(c,""))
            lines.append(textwrap.wrap(cell, widths[c]) or [""])
        for i in range(max(len(x) for x in lines)):
            print(sep.join((lines[j][i] if i < len(lines[j]) else "").ljust(widths[cols[j]]) for j in range(len(cols))))
```

## Q148. **Simple HTTP Log Analyzer** (no network) for common format
**Scenario:** Given Apache/Nginx common log format lines in a file, compute hits per status code and top 5 IPs.  

**Answer:** Regex parse, `Counter`.

```python
import re
from collections import Counter

LOG = re.compile(r'^(\S+) \S+ \S+ \[[^\]]+\] "\S+ \S+ \S+" (\d{3}) \S+')

def analyze(path):
    by_ip = Counter()
    by_status = Counter()
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = LOG.match(line)
            if not m: continue
            ip, status = m.groups()
            by_ip[ip] += 1
            by_status[status] += 1
    return by_status, by_ip.most_common(5)
```

## Q149. **INI-like Config Parser** (subset) without `configparser`
**Scenario:** Parse a minimal INI with `[section]`, `key=value` lines, `#` comments. Return nested dict.  

**Answer:** Manual parsing.

```python
def parse_ini(lines):
    cfg = {}; cur = None
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#"): continue
        if line.startswith("[") and line.endswith("]"):
            cur = line[1:-1].strip()
            cfg[cur] = {}
        else:
            k, _, v = line.partition("=")
            if cur is None: raise ValueError("key outside section")
            cfg[cur][k.strip()] = v.strip()
    return cfg
```

## Q150. **Docstring Extractor** for a package
**Scenario:** Walk a package directory, import each `.py` module safely, and extract module-level, class, and function docstrings into a JSON report. Avoid executing top-level code with side effects—just import (note: imports might run top-level).  

**Answer:** Use `importlib` and `inspect`. (In real systems, use caution or AST parsing.)

```python
import os, sys, json, inspect, importlib.util

def load_module_from_path(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

def extract_docstrings(pkg_dir):
    report = {}
    for root, _, files in os.walk(pkg_dir):
        for f in files:
            if not f.endswith(".py"): continue
            path = os.path.join(root, f)
            name = os.path.relpath(path, pkg_dir).replace(os.sep, ".")[:-3]
            mod = load_module_from_path(name, path)
            info = {"__doc__": inspect.getdoc(mod), "classes": {}, "functions": {}}
            for n, obj in inspect.getmembers(mod):
                if inspect.isclass(obj):
                    info["classes"][n] = inspect.getdoc(obj)
                elif inspect.isfunction(obj):
                    info["functions"][n] = inspect.getdoc(obj)
            report[name] = info
    return json.dumps(report, indent=2, ensure_ascii=False)
```

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
