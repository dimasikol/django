from . import task1
import random
def context(count_elements:list):
    if isinstance(count_elements,dict):
        context1 = [random.choice([task1.Task1().write1(), task1.Task1().write2(), task1.Task1().write3()]) for _ in range(int(count_elements["1"]))]

        #context2 = [task1.Task2().write() for _ in range(int(count_elements["2"]))]
        #context3 = [task1.Task3().write() for _ in range(int(count_elements["3"]))]
        #context4 = [task1.Task4().write() for _ in range(int(count_elements["4"]))]
        #context5 = [task1.Task5().write() for _ in range(int(count_elements["5"]))]
        context6 = [task1.Task6().write() for _ in range(int(count_elements["6"]))]
        context7 = [task1.Task7().write() for _ in range(int(count_elements["7"]))]
        context8 = [task1.Task8().write() for _ in range(int(count_elements["8"]))]
        context10 = [random.choice([task1.Task10().write1()]) for _ in range(int(count_elements["10"]))]
    else:
        context1 = [random.choice([task1.Task1().write1(), task1.Task1().write2(), task1.Task1().write3()]) for _ in range(int(count_elements))]
        # context2 = [task1.Task2().write() for _ in range(int(count_elements["2"]))]
        # context3 = [task1.Task3().write() for _ in range(int(count_elements["3"]))]
        # context4 = [task1.Task4().write() for _ in range(int(count_elements["4"]))]
        # context5 = [task1.Task5().write() for _ in range(int(count_elements))]
        context6 = [task1.Task6().write() for _ in range(int(count_elements))]
        context7 = [task1.Task7().write() for _ in range(int(count_elements))]
        context8 = [task1.Task8().write() for _ in range(int(count_elements))]
        context10 = [random.choice([task1.Task10().write1()]) for _ in range(int(count_elements))]
    context = {"answer1": context1,"answer5": "1","answer6":context6, "answer7": context7, "answer8": context8,"answer10": context10}
    return context
