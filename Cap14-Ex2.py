import time

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

def main(sz):
    import random
    rng = random.Random()   # Instantiate a generator

    bd = list(range(sz))     # Generate the initial permutation
    num_found = 0
    tries = 0
    t0 = time.clock()
    while num_found < 1:
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd):
           t1 = time.clock()
           print("Found solution {0} in {1} tries and {2:.4f} seconds".format(bd, tries,t1-t0))
           tries = 0
           num_found += 1

    return t1 - t0

sz = 4
t = main(sz)
while t < 60:
    sz +=1
    t = main(sz)

print("The maximum size puzzle that we can solve in under a minuto is {0}. It's took {1}"
      .format(sz,t))