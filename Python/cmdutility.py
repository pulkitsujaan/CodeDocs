import argparse
import sys

def calc(args):
    # if(args.o=='add' and (args.a==56 and args.b==9) or (args.b==56 and args.a==9) ):
    #     return "LOL"
    # elif(args.o=='multi' and (args.a==45 and args.b==3) or (args.b==45 and args.a==3) ):
    #     return "LOL"
    # elif(args.o=='div' and (args.a==56 and args.b==6) or (args.b==56 and args.a==6) ):
    #     return "LOL"
    # elif args.o == 'add':#use this line to use faulty calculator
    if args.o == 'add':#comment this line if you want to use faulty calculator
        return args.a + args.b
    elif args.o == 'sub':
        return args.a - args.b
    elif args.o == 'multi':
        return args.a * args.b
    elif args.o == 'div':
        return args.a / args.b
    else:
        return "Something went wrong..."
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--a',type=int,default=0,help="Enter first number...This is a Utility for calculating numbers...")

    parser.add_argument('--b',type=int,default=0,help="Enter Second number...This is a Utility for calculating numbers...")
    
    parser.add_argument('--o',type=str,default="add",help="Enter operation...This is a Utility for calculating numbers...")

    args=parser.parse_args()
    sys.stdout.write(str(calc(args)))
if __name__=="__main__":
    main()