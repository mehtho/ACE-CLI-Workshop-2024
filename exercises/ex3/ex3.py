import os

name = os.getenv("MY_NAME")
bad = os.getenv("BAD_VAR")

if name:
    print("Remove 'bad_var'" if bad else name + ' has completed ex3')
else:
    print("The 'my_name' environment variable is not set.")
