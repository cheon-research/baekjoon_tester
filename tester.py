import os
from subprocess import Popen, PIPE, STDOUT

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input', '-I', type=str, default="input.txt")
parser.add_argument('--solution', '-S', type=str, default="solution.py")
args = parser.parse_args()


# solution file open
if os.path.isfile(args.solution):
    p = Popen(["python", args.solution], stdin=PIPE, stdout=PIPE, stderr=STDOUT, encoding="utf-8")
else:
    raise FileNotFoundError(f"No such file or directory: '{args.solution}'")

# input data file open
if os.path.isfile(args.input):
    with open(args.input, "r") as f:
        inputs = f.readlines()
        # check "\n" in last line
        if "\n" not in inputs[-1]:
            inputs[-1] += "\n"
        inputs = "".join(inputs)
else:
    raise FileNotFoundError(f"No such file or directory: '{args.input}'")

print("### INPUT ###")
print(inputs)

print("### OUTPUT ###")
outputs = p.communicate(input=inputs)[0] # (stdout, stderr)
print(outputs)
