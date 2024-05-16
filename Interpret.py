from enum import IntEnum, auto
from sys import stdin


class Operation(IntEnum):
    MoveLeft = auto()
    MoveRight = auto()
    Increase = auto()
    Decrease = auto()
    Output = auto()
    Input = auto()
    JumpIfZero = auto()
    Rewind = auto()


def Interpret(operations: list[Operation]) -> bytearray:
    # Initialize
    opindex = 0
    pointer = 0
    tape = bytearray(1000)
    output = bytearray()

    # Run
    while opindex < len(operations):
        match operations[opindex]:
            case Operation.MoveLeft:
                pointer -= 1
            case Operation.MoveRight:
                pointer += 1
            case Operation.Increase:
                tape[pointer] = (tape[pointer] + 1) % 256
            case Operation.Decrease:
                tape[pointer] = (tape[pointer] + 255) % 256
            case Operation.Output:
                output.append(tape[pointer])
            case Operation.Input:
                tape[pointer] = ord(stdin.read(1))
            case Operation.JumpIfZero:
                if tape[pointer] == 0:
                    flag = 1
                    while flag != 0:
                        opindex += 1
                        match operations[opindex]:
                            case Operation.JumpIfZero:
                                flag += 1
                            case Operation.Rewind:
                                flag -= 1
            case Operation.Rewind:
                flag = 1
                while flag != 0:
                    opindex -= 1
                    match operations[opindex]:
                        case Operation.JumpIfZero:
                            flag -= 1
                        case Operation.Rewind:
                            flag += 1
                continue
            case _:
                raise Exception("Invalid operation")

        opindex += 1

    return output


def Brainfucker(code: str) -> bytearray:
    # Compile
    operations: list[Operation] = []
    for char in code:
        match char:
            case "+":
                operations.append(Operation.Increase)
            case "-":
                operations.append(Operation.Decrease)
            case ">":
                operations.append(Operation.MoveRight)
            case "<":
                operations.append(Operation.MoveLeft)
            case ".":
                operations.append(Operation.Output)
            case ",":
                operations.append(Operation.Input)
            case "[":
                operations.append(Operation.JumpIfZero)
            case "]":
                operations.append(Operation.Rewind)
    # Run
    return Interpret(operations)


def Ook(code: str) -> bytearray:
    # Compile
    operations: list[Operation] = []
    code = "".join(filter(lambda char: char in ".?!", code))
    assert len(code) % 2 == 0, "Invalid Ook code"
    for i in range(0, len(code), 2):
        match code[i : i + 2]:
            case ".?":
                operations.append(Operation.MoveRight)
            case "?.":
                operations.append(Operation.MoveLeft)
            case "..":
                operations.append(Operation.Increase)
            case "!!":
                operations.append(Operation.Decrease)
            case "!.":
                operations.append(Operation.Output)
            case ".!":
                operations.append(Operation.Input)
            case "!?":
                operations.append(Operation.JumpIfZero)
            case "?!":
                operations.append(Operation.Rewind)
    # Run
    return Interpret(operations)


## Test

test = "++++++++[>++++++[>+++++++<-]<-]>>.[-]"
print(Brainfucker(test).decode())

test = """
+++++ +++++ [->++ +++++ +++<] >++.+ +++++ .<+++ [->-- -<]>- -.+++ +++.< ++++[ ->+++ +<]>+ +++.<
++++[ ->--- -<]>- ----- -.<++ +[->+ ++<]> ++.<+ +++[- >---- <]>.< +++++ [->++ +++<] >+.<+ ++[->
---<] >-.++ ++++. <++++ [->-- --<]> ----- -.<++ +[->+ ++<]> +++.+ ++.+. +++++ +++.< ++++[ ->---
-<]>- ----- --.++ +.+++ +.--- ----. <+++[ ->+++ <]>++ ++++. <+++[ ->--- <]>-- ----. <++++ [->++
++<]> ..--- -.<++ ++[-> ++++< ]>++. <
"""
print(Brainfucker(test).decode())

test = """
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook! Ook? Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook? Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook! Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook! Ook? Ook! Ook! Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook? Ook. Ook? Ook! Ook. Ook? Ook! Ook!
Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook? Ook. Ook? Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook? Ook. Ook? Ook! Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook. Ook.
Ook. Ook. Ook. Ook. Ook? Ook. Ook? Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook? Ook. Ook? Ook! Ook. Ook? Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook! Ook? Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook? Ook!
Ook. Ook? Ook. Ook. Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook?
Ook! Ook! Ook! Ook! Ook! Ook! Ook? Ook. Ook? Ook! Ook. Ook? Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook! Ook? Ook! Ook! Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook? Ook. Ook? Ook! Ook. Ook?
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook? Ook! Ook. Ook?
Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook. Ook. Ook! Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook? Ook. Ook? Ook! Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook.
Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook.
Ook? Ook. Ook? Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook.
Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook!
Ook? Ook. Ook? Ook! Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook.
Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook? Ook. Ook? Ook! Ook. Ook? Ook! Ook. Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook?
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook? Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook! Ook.
Ook? Ook.
"""
print(Ook(test).decode())
