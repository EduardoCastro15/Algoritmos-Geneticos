import random
from tkinter import *
from tkinter import Checkbutton, Entry, messagebox

import matplotlib.pyplot as plt
from sympy import *
from sympy.combinatorics.graycode import bin_to_gray
import math
import cmath

class GUI():
    def partition(self, arr, low, high): 
        i = (low-1)         # index of smaller element 
        pivot = arr[high]     # pivot 
    
        for j in range(low , high): 
    
            # If current element is smaller than the pivot 
            if   arr[j] < pivot: 
            
                # increment index of smaller element 
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
    
        arr[i+1],arr[high] = arr[high],arr[i+1]

        return (i+1)

    def quickSort(self, arr,low,high): 
        if low < high: 
    
            # pi is partitioning index, arr[p] is now 
            # at right place 
            pi = self.partition(arr,low,high) 
    
            # Separately sort elements before 
            # partition and after partition 
            self.quickSort(arr, low, pi-1) 
            self.quickSort(arr, pi+1, high) 
    
    # Driver code to test above
    def listToString(self, s):
        str1 = ''
        for ele in s:
            str1 += str(ele)

        return str1

    def listToString4Real(self, s):
        str1 = ''
        for ele in s:
            str1 += str(ele)+', '

        return str1

    def cuentaBits(self, n):
        aux = 0
        while n>0:
            n = n>>1
            aux+=1
        
        return aux

    def go(self):

        if(self.binValue.get()==1)&(self.grayValue.get()==0)&(self.intValue.get()==0)&(self.realValue.get()==0):
            self.r = int(self.ran.get())
            self.q1 = int(self.q.get())

            self.r = self.cuentaBits(self.r)
            #print(self.r)
            for _ in range(self.q1):
                for _ in range(self.r):
                    if(random.random()>0.5):
                        self.L.append(1)
                    else:
                        self.L.append(0)
                self.L1.append(self.listToString(self.L))
                self.L.clear()

            for i in self.L1:
                self.valInt = int(i, 2)
                self.L.append(self.valInt)
            #print(self.L1)

            #self.info = messagebox.showinfo('Generated numbers', self.listToString(str(self.L)))
            plt.plot(self.L, 'r--d')
            
            self.quickSort(self.L,0,len(self.L)-1)

            #self.info1 = messagebox.showinfo('Sorted generated numbers', self.listToString(str(self.L)))
            self.info2 = messagebox.showinfo('Binary', self.L1)
            plt.plot(self.L, 'b--o')
            plt.title('Binary Data')
            plt.show()

        elif(self.grayValue.get()==1)&(self.binValue.get()==0)&(self.intValue.get()==0)&(self.realValue.get()==0):
            self.r = int(self.ran.get())
            self.q1 = int(self.q.get())

            self.r = self.cuentaBits(self.r)
            #print(self.r)
            for _ in range(self.q1):
                for _ in range(self.r):
                    if(random.random()>0.5):
                        self.L.append(1)
                    else:
                        self.L.append(0)
                self.L1.append(self.listToString(self.L))
                self.L.clear()
            
            for i in self.L1:
                self.valGray = bin_to_gray(i)
                self.L.append(self.valGray)
            
            print('Binary', self.L1)
            print('Gray code', self.L)
            self.info1 = messagebox.showinfo('Binary Data', self.L1)
            self.L1.clear()
            
            for i in self.L:
                self.valInt = int(i, 2)
                self.L1.append(self.valInt)
            
            plt.plot(self.L1, 'r--d')

            self.quickSort(self.L1,0,len(self.L1)-1)
            self.info2 = messagebox.showinfo('Gray Code Data', self.L)
            
            plt.title('Gray Code Data')
            plt.plot(self.L1, 'b--o')
            plt.show()

        elif(self.realValue.get()==1)&(self.binValue.get()==0)&(self.intValue.get()==0)&(self.grayValue.get()==0):
            self.r1 = float(self.ran.get())
            self.r = 100*self.r1
            self.q1 = int(self.q.get())
            #print(self.r)
            self.r = math.log2(self.r)

            #print(self.r)

            if(self.r-int(self.r))>5:
                self.r = int(self.r)+1
            else:
                self.r = int(self.r)
            
            #print(self.r)

            for _ in range(self.q1):
                for _ in range(self.r):
                    self.L.append(round(random.uniform(0, self.r1), 2))
                    self.L2 = self.L.copy()
                self.L1.append(self.L2)
                #print('L',self.L)
                self.L.clear()
            
            self.info1 = messagebox.showinfo('Unordered Real Data', self.listToString4Real(self.L1)) 
            
            for i in self.L1:
                plt.plot(i, '--o')
                self.quickSort(i, 0, len(i)-1)
                plt.plot(i, '--d')

            self.info2 = messagebox.showinfo('Ordered Real Data', self.listToString4Real(self.L1))

            plt.title('Real Data')
            plt.show()

            #print('L1', self.L1)    

        elif(self.intValue.get()==1)&(self.binValue.get()==0)&(self.grayValue.get()==0)&(self.realValue.get()==0):
            self.r = int(self.ran.get())
            self.q1 = int(self.q.get())
            self.r1 = self.r

            self.r = self.cuentaBits(self.r)
            #print(self.r)
            for _ in range(self.q1):
                for _ in range(self.r):
                    self.L.append(random.randint(0, self.r1))
                    self.L2 = self.L.copy()
                self.L1.append(self.L2)
                #print('L',self.L)
                self.L.clear()
            
            #print(self.L1)
            self.info1 = messagebox.showinfo('Unordered Int Data', self.listToString4Real(self.L1))

            for i in self.L1:
                plt.plot(i, '--o')
                self.quickSort(i, 0, len(i)-1)
                plt.plot(i, '--d')

            self.info2 = messagebox.showinfo('Ordered Int Data', self.listToString4Real(self.L1))

            plt.title('Int Data')
            plt.show()

        else:
            self.info1 = messagebox.showerror('Fatal Error!', 'You can only select one type of data!')
                
    def __init__(self):
        self.root = Tk()
        self.root.title('Plotting Data')
        self.root.iconbitmap('pythonIcon.ico')
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bd=20)
        self.lblRange = Label(self.frame, text = 'Insert the limit range of random numbers!')
        self.lblRange.grid(row=0, column=0, sticky='N')
        self.ran = Entry(self.frame)
        self.ran.grid(row=1, column=0, sticky='N')
        self.lblQuantity = Label(self.frame, text = 'Insert how many random numbers you want!')
        self.lblQuantity.grid(row=2, column=0, sticky='N')
        self.q = Entry(self.frame)
        self.q.grid(row=3, column=0, sticky='N')
        self.lblDataType = Label(self.frame, text="Select data type you want to show!")
        self.lblDataType.grid(row=4, column=0, sticky='N')
        self.intValue = BooleanVar()
        self.intButton = Checkbutton(self.frame, text='Int', var = self.intValue)
        self.intButton.grid(row=5, column=0, sticky='W')
        self.binValue = BooleanVar()
        self.binButton = Checkbutton(self.frame, text='Binary', var = self.binValue)
        self.binButton.grid(row=6, column=0, sticky='W')
        self.realValue = BooleanVar()
        self.realButton = Checkbutton(self.frame, text='Real', var = self.realValue)
        self.realButton.grid(row=7, column=0, sticky='W')
        self.grayValue = BooleanVar()
        self.grayButton = Checkbutton(self.frame, text='Gray Code', var = self.grayValue)
        self.grayButton.grid(row=8, column=0, sticky='W')
        self.b1 = Button(self.frame, text = 'Go!', command = lambda: self.go())
        self.b1.grid(row=9, column=0, pady=5)
        self.b2 = Button(self.frame, text = 'Exit', command = self.root.destroy)
        self.b2.grid(row=10, column=0, pady=5)
        self.L = []
        self.L1 = []
        self.L2 = []
        self.root.mainloop()

gui = GUI()