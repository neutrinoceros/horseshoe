import sys

def get_script_args () :
    args = [a for a in  sys.argv]
    args.reverse(); args.pop(); args.reverse();
    return args

clearLastLine = lambda : sys.stdout.write("\033[F")
