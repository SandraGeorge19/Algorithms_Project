
import random
import time
import sys
import matplotlib.pyplot as plt
import numpy as np
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from insertionSort import insertionSort
from mergeSort import mergeSort
from heapSort import heapSort


class Compare:
    def __init__(self):
        # Dictionary being used when testing sort for 1 algorithm
        self.FuncName = {
            'Bubble': bubbleSort,
            'Selection': selectionSort,
            'Insertion': insertionSort,
            'Merge': mergeSort,
            'Heap': heapSort,

        }

        # For type DataSet
        self.data_type = {
            1: "",
            2: "_sorted",
            3: "_reverse"
        }

        self.inputSize = 1000
        self.dataSet = 1

        # Taking average given no of dataset , Default value : 3
        # For generating avg on more number of dataset , execute dataset_generator.py
        # before compare.py
        self.Num_Of_Case = 3

    # Function for calculating average time taken by each sorting algorithm
    def calculateAvg(self, func, execTime):
        sortingName = self.FuncName[func]
        timeElapsed = 0
        for i in range(1, self.Num_Of_Case + 1):
            fileName = "DataSet/dataSet" + str(i) + self.data_type.get(self.dataSet) + ".txt"
            inputFile = open(fileName, "r")
            arr = np.loadtxt(inputFile, dtype=int, max_rows=self.inputSize)
            inputFile.close()
            startTime = time.time()
            if arr.size == 1:
                list1 = []
                list1.append(arr[()])
                arr = list1
            sortingName(arr, 0, len(arr) - 1)
            timeElapsed = timeElapsed + time.time() - startTime

        timeElapsed = (timeElapsed / self.Num_Of_Case) * 1000
        execTime.append(timeElapsed)
        print('Time elapsed in Execution of ' + func + ' : ' + str(timeElapsed) + ' milli seconds')

    def main(self):
        print("Average of exection time taken for :", self.Num_Of_Case, " DataSet")
        print("Select Sorting Algorithm to test :")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Heap Sort")
        print("6. All Sorting Algorithms")

        func = []
        while len(func) == 0:
            algorithm = int(input("Enter the Algorithm number :"))
            if algorithm == 6:
                func = [item for item in range(1, 7)]
                break
            if (algorithm >= 1 or algorithm <= 5):
                func.append(algorithm)
                break
            print("Please Enter valid Input")

        print("\nSelect Type of Data Set for sorting :")
        print("1. Random/Unsorted Input")
        print("2. Sorted Input")
        print("3. Reversely Sorted Input")

        self.dataSet = int(input("how do you want the inputs to be:"))

        # Input Size
        size = [5000, 6000, 7000, 8000, 9000, 10000]

        # List to store execution time of each sorting algorithm
        bubble = []
        select = []
        insert = []
        merge = []
        heap = []

        for num in size:
            self.inputSize = num
            print("\n For input size of :" + str(num))
            for algo in func:
                if algo == 1:
                    self.calculateAvg('Bubble', bubble)
                elif algo == 2:
                    self.calculateAvg('Selection', select)
                elif algo == 3:
                    self.calculateAvg('Insertion', insert)
                elif algo == 4:
                    self.calculateAvg('Merge', merge)
                elif algo == 5:
                    self.calculateAvg('Heap', heap)

        # For Ploting Graph
        if algorithm == 1:
            plt.plot(size, bubble, label="Bubble Sort")
        elif algorithm == 2:
            plt.plot(size, select, label="Selection Sort")
        elif algorithm == 3:
            plt.plot(size, insert, label="Insertion Sort")
        elif algorithm == 4:
            plt.plot(size, merge, label="Merge Sort")
        elif algorithm == 5:
            plt.plot(size, heap, label="Heap Sort")
        elif algorithm == 6:
            plt.plot(size, bubble, label="Bubble Sort")
            plt.plot(size, select, label="Selection Sort")
            plt.plot(size, insert, label="Insertion Sort")
            plt.plot(size, merge, label="Merge Sort")
            plt.plot(size, heap, label="Heap Sort")


        plt.xlabel('Input Size')
        plt.ylabel('Execution time in milliseconds')
        plt.title('Graph comparing Sorting Algorithms !')
        plt.legend()
        plt.savefig('graph' + self.data_type.get(self.dataSet) + '.png')
        print("Check graph" + self.data_type.get(self.dataSet) + '.png' + " for saved graph")
        print("Displaying plotted graph")
        plt.show()


sys.setrecursionlimit(10 ** 6)
compare = Compare()
compare.main()
