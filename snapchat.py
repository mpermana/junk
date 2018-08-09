"""
input: list: [2, 1, 9, 7], target: 88 -> YES   because: (2+9)*(1+7) = 88
+ * ( )
- you can reorder numbers
- you should use all the numbers

given the list: [2, 1, 9, 7] -> what is the largest number you can make?
2+1 * 9*7
2*1 * 9*7

1 1 1 1 1 1
1+1+1+1+1+1
1+1+1*1+1+1

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT


# stack = [2 9 + 1 7 + *]
# stack = [2 9 * 1 7 * +]
# stack = [2 9 1 7 * + +]
# stack = [1 1 7 9 * + +]


# + + +
# + + *
# + * +
# + * *
# * + +
import itertools

def evaluate(operations):
    try:
        stack = []
        for operand in operations:
            if operand == '+':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1+op2)
            elif operand == '*':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1*op2)
            else:
                stack.append(operand)
        return stack[0]
    except:
        return None

current_max = 0
max_operations = None

def doit(input, target):
    global current_max
    global max_operations
    # of combinations = 2^(n-1)
    # + + +
    # + + *
    # * * * 8 of them
    # 0       000
    # 1       001
    # 2       010
    # 3       011
    # 4       100
    for operand in itertools.product('+*', repeat=3):
        for operations in itertools.permutations(input + list(operand)):
            result = evaluate(operations)
            current_max = max(current_max, result)
            if result == current_max:
                max_operations = operations
            #if result == target:
            #    print 'operations', operations


input = [2, 1, 9, 7]
target = 88
print doit(input, target)
print 'current_max', current_max, max_operations
