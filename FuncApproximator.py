# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 08:24:21 2025

@author: miles
"""

import random  
import winsound
from copy import deepcopy as Copy
add = lambda list1, list2: [n1 + n2 for n1, n2 in zip(list1, list2)]
mul = lambda list1, list2: [n1 * n2 for n1, n2 in zip(list1, list2)]
def rand(list1:list[int], Range:list[int]) -> list[int]:
    list1[random.randint(0, len(list1)-1)] = (round(random.uniform(Range[0], Range[1]), 1) if random.choice([True, False]) == True else -round(random.uniform(Range[0], Range[1]), 1))
    return list1
ReLU = lambda list1 :list(map(lambda a : max(0, a), list1))
class Network:
    def __init__(self, size:tuple[int]) -> None:
        self.lens, self.total_len = size, len(size)
        self.biases = []
        self.weights = []
        for n in size:
            self.biases.append([0 for _ in range(n)])
        for index, n in enumerate(size[:-1]): 
            self.weights.append(([[1 for _ in range(n*size[index + 1])]]))
    def Evaluate(self, Inputs:list[int]) -> int:
        assert len(Inputs) == 1
        layers = [add(Inputs, self.biases[0])]
        for num in range(1, self.total_len):
            prev_layer = layers[num - 1]
            my_biases = self.biases[num]
            my_weights = self.weights[num - 1]
            my_len = self.lens[num]
            layers.append(ReLU(add(my_biases, list(map(lambda index : sum(mul(prev_layer, my_weights[index])), [0]*my_len)))))
        return layers[len(layers) - 1][0]
    def Randomize(self) -> None:
        for _ in range(2):
            weights, biases = random.choice([self.weights[0], self.weights[1], self.weights[2], self.weights[3]]), random.choice([self.biases[0], self.biases[1], self.biases[2], self.biases[3], self.biases[4]])
            if biases is self.biases[0]:
                self.biases[0] = rand(self.biases[0], PARAMS['Bias Range'])
            elif biases is self.biases[1]:
                self.biases[1] = rand(self.biases[1], PARAMS['Bias Range'])
            elif biases is self.biases[2]:
                self.biases[2] = rand(self.biases[2], PARAMS['Bias Range'])
            elif biases is self.biases[3]:
                self.biases[3] = rand(self.biases[3], PARAMS['Bias Range'])
            elif biases is self.biases[4]:
                self.biases[4] = rand(self.biases[4], PARAMS['Bias Range'])
            if weights is self.weights[0]:
                self.weights[0] = [rand(n, PARAMS['Weight Range']) for index, n in enumerate(self.weights[0])]
            elif weights is self.weights[1]:
                self.weights[2] = [rand(n, PARAMS['Weight Range']) for index, n in enumerate(self.weights[1])]
            elif weights is self.weights[2]:
                self.weights[2] = [rand(n, PARAMS['Weight Range']) for index, n in enumerate(self.weights[2])]
            elif weights is self.weights[3]:
                self.weights[3] = [rand(n, PARAMS['Weight Range']) for index, n in enumerate(self.weights[3])]
PARAMS = {
    'Weight Range' : [0.1, 0.7],
    'Bias Range' : [0.1, 1.5],
    'Network Size' : (1, 20, 15, 10, 1),
    'Do Softmax' : False,
    'Error Limit' : 0.5,
    'Testing loop' : 5,
    'Input Range' : (-5, 5)
    }
def func(x:int) -> int:
    return x*2


def Main():
    best = Network(PARAMS['Network Size'])
    best_difnum = 100
    while True:
        op = input("FuncApproximator_V2.0 >> ")
        if op == 'Train':
            while True:
                new = Copy(best)
                new.Randomize()
                difs = []
                for n in range(PARAMS['Testing loop']):
                    num = random.randint(PARAMS['Input Range'][0], PARAMS['Input Range'][1])
                    difs.append(abs(func(num) - new.Evaluate([num])))
                    total_dif = sum(difs)
                if total_dif < best_difnum:
                    print(f'New Best {total_dif}')
                    best = Copy(new)
                    best_difnum = total_dif
                if total_dif < PARAMS['Error Limit']:
                    print("Testing")
                    for index in range(5):
                        num = random.randint(PARAMS['Input Range'][0]-5, PARAMS['Input Range'][1]+5)
                        if abs(best.Evaluate([num]) - func(num)) >= PARAMS['Error Limit']:
                            break # break means it failed the test
                    else: # if it didn't fail
                        print('Done') 
                        winsound.Beep(1500, 700)
                        break
                    print(f"Testing Failed on Test Number : {index}")
                    
        elif op == 'Test':
            print("\nEnter Numbers to Test\nEnter 'Stop' to End\n")
            while True: 
                num = (input("FuncApproximator_V1.0 Testing >> "))
                if num == 'Stop':
                    break
                num = int(num)
                print(f"func({num}) = {func(num)}, Result = {best.Evaluate([num])}")
        elif op == "Stop":
            break
        elif op == "New Error Limit":
            PARAMS["Error Limit"] = float(input("   Enter new Error Limit >> ")),
        else:
            print('Invalididated Command')

if __name__ == '__main__':
    Main()
