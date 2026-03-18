import argparse as ap

par = ap.ArgumentParser(description="just type one of them or both and see what's going to happen, created by:theRA - github:https://github.com/usserhub")

par.add_argument("NAMO", help="Just your Name and that's it")
par.add_argument("--hello", action=("store_true"), help="ever wanted to be hellowed")
par.add_argument("--greet", action=("store_true"), help="ever wanted to be greetted")


ar = par.parse_args()

if ar.hello and ar.greet:
    print(f"hello MR.{ar.NAMO} and welcome")
elif ar.hello:
    print(f"hello Mr.{ar.NAMO} but you're not welcomed")
elif ar.greet:
    print(f"No Hello to to you mr.{ar.NAMO} just com inside")
else:
    print(f"hey!! mr.{ar.NAMO} GET OUT!!!")