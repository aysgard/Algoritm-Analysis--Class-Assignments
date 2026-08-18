
### Q1

"""
Algorithm Alice:
    // Alice has picked three distinct integers
    List = [a, b, c]

    // Shuffle List randomly
    random.shuffle(list)

    // Place the integers onto Stack S:
    S = Stack()
    S.push(List[0])
    S.push(List[1])
    S.push(List[2])

    // choose x
    x = S.pop()
    IF S.peek() > x:
        x  = S.pop()

"""
"""
Since an element can be accessed only from the end, called the top, of a stack, 
we choose x via returning the last added, i.e, top item and remove it from the stack.
Now S.peek() is the integer previously placed at the middle .

Let's call the maximum value of these integers M.

Since the three integers are placed in the stack in random order, 
M is equally likely to be in any of the three positions (Top, Middle, Bottom). 
The probability of M being in any specific position is 1/3.

Looking at these three cases:

Case1: M is at the top.
Then x is assigned M immediately.
The comparison S.peek() > x = M false.
Hence x is remains M.

Case2: M is in the middle.
x is assigned the top value, which is not M.
The comparison S.peek() > x checks if M > Top, which is true.
Then x is updated to S.pop(), which is M.

Case3: M is at the bottom.
x is assigned to the top value, which is not M again.
The comparison S.peek() > x checks if Middle > Top.
Then x is updated to the second largest integer between the middle and the top.
Since there is no loop, x will not be assigned to the max value M.
It results is failure.

Therefore the algorith succeeds in Case1 and Case2.
Probability of Success := P = P(Case1) + P(Case2) = 1/3 + 1/3 = 2/3 

"""