# michaelpeterswa
# fiftyfifty.py

import argparse
import random
import time
import argparse

def gen_random_list(length):
    random.seed(time.time())
    results = []
    for i in range(length):
        curr = random.random()
        if curr < 0.5:
            results.append(0)
        else:
            results.append(1)
    
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("first_team")
    parser.add_argument("second_team")
    parser.add_argument("N", help="rounds of random numbers",
                        type=int)
    args = parser.parse_args()

    results = gen_random_list(args.N)
    final = sum(results)/len(results)

    if final < 0.5:
        print(f'Winner is {args.first_team} ({final})')
    else:
        print(f'Winner is {args.second_team} ({final})')
