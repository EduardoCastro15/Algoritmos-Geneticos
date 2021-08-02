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

    def sinFunction(self, L):
        aux = 0
        for i in L:
            aux = math.sin(i)
            self.L3.append(aux)

        return self.L3

    def sin2Function(self, L):
        aux = 0
        for i in L:
            aux = pow(math.sin(i), 2)
            self.L3.append(aux)

        return self.L3

    def cosFunction(self, L):
        aux = 0
        for i in L:
            aux = math.cos(i)
            self.L3.append(aux)

        return self.L3

    def cos2Function(self, L):
        aux = 0
        for i in L:
            aux = pow(math.cos(i), 2)
            self.L3.append(aux)

        return self.L3 
    
    def fitFunction(self, L):
        aux = 0
        for x in L:
            aux = eval(self.fitFunc.get())
            self.L3.append(aux)
        
        return self.L3

    def binData(self, r, q1):
        self.r = int(r)
        self.q1 = int(q1)
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
        
        self.info1 = messagebox.showinfo('Binary Data', self.L1)

        for i in self.L1:
            self.valInt = int(i, 2)
            self.L.append(self.valInt)
        
        self.info1 = messagebox.showinfo('Binary Int Representation Data', self.L)

        #plt.plot(self.sinFunction(self.L), 'c--v')
        self.quickSort(self.L,0,len(self.L)-1)
        #plt.plot(self.sinFunction(self.L), 'g--^')

        #plt.figure(1)
        self.info2 = messagebox.showinfo('Binary Sorted Data', self.L1)
        self.info2 = messagebox.showinfo('Binary Sorted Int Representation Data', self.L)

        return self.L

    def grayData(self, r, q):
        self.r = int(r)
        self.q1 = int(q)
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
            
        # print('Binary', self.L1)
        # print('Gray code', self.L)
        self.info1 = messagebox.showinfo('Binary Data', self.L1)

        for i in self.L1:
            self.valInt = int(i, 2)
            self.L2.append(self.valInt)
        
        self.info1 = messagebox.showinfo('Binary Int Representation Data', self.L2)

        self.L1.clear()
            
        for i in self.L:
            self.valInt = int(i, 2)
            self.L1.append(self.valInt)
            
        #plt.plot(self.L1, 'r--d')

        self.quickSort(self.L1,0,len(self.L1)-1)
        self.info2 = messagebox.showinfo('Gray Code Data', self.L)
        self.info2 = messagebox.showinfo('Gray Code Int Representation Data', self.L1)

        return self.L1
            
        #plt.title('Gray Code Data')
        #plt.plot(self.L1, 'b--o')
        #plt.show()

    def realData(self, r, q):
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
            plt.plot(i, '--v')
            self.quickSort(i, 0, len(i)-1)
            plt.plot(i, '--^')

        self.info2 = messagebox.showinfo('Ordered Real Data', self.listToString4Real(self.L1))

        # plt.title('Real Data')
        # plt.show()

        return self.L1
        #print('L1', self.L1)

    def intData(self, r, q):
        self.r = int(r)
        self.q1 = int(q)
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
            plt.plot(i, '--v')
            self.quickSort(i, 0, len(i)-1)
            plt.plot(i, '--^')

        self.info2 = messagebox.showinfo('Ordered Int Data', self.listToString4Real(self.L1))

        return self.L1
        # plt.title('Int Data')
        # plt.show()

    def go(self):
        if(self.binValue.get()==1)&(self.grayValue.get()==0)&(self.intValue.get()==0)&(self.realValue.get()==0):
            self.L4 = self.fitFunction(self.binData(self.ran.get(), self.q.get()))
            self.info2 = messagebox.showinfo(('Ordered Binary User Function Data'), self.L4)
            plt.plot(self.L4, 'r--o')
            plt.title('Binary User Fitness Function')
            plt.show()

        elif(self.grayValue.get()==1)&(self.binValue.get()==0)&(self.intValue.get()==0)&(self.realValue.get()==0):
            self.L4 = self.fitFunction(self.grayData(self.ran.get(), self.q.get()))
            self.info2 = messagebox.showinfo(('Ordered Gray User Function Data'), self.L4)
            plt.plot(self.L4, 'r--o')
            plt.title('Gray User Fitness Function')
            plt.show()

        elif(self.realValue.get()==1)&(self.binValue.get()==0)&(self.intValue.get()==0)&(self.grayValue.get()==0):
            self.L4 = self.realData(self.ran.get(), self.q.get())

            for i in self.L4:
                self.L5.append(self.fitFunction(i))
                plt.plot(self.fitFunction(i), '--o')
            
            self.info1 = messagebox.showinfo(('Ordered Real User Function Data'), self.L5)

            plt.grid()
            plt.title('Real User Fitness Function')
            plt.show()

        elif(self.intValue.get()==1)&(self.binValue.get()==0)&(self.grayValue.get()==0)&(self.realValue.get()==0):
            self.L4 = self.intData(self.ran.get(), self.q.get())

            for i in self.L4:
                self.L5.append(self.fitFunction(i))
                plt.plot(self.fitFunction(i), '--o')
            
            self.info1 = messagebox.showinfo(('Ordered Int User Function Data'), self.L5)

            plt.grid()
            plt.title('Int User Fitness Function ')
            plt.show()

        else:
            self.info1 = messagebox.showerror('Fatal Error!', 'You can only select one type of data!')

    def sinBF(self):
        if(self.binValue.get()==1)&(self.grayValue.get()==0)&(self.intValue.get()==0)&(self.realValue.get()==0):
            self.L4 = self.sinFunction(self.binData(self.ran.get(), self.q.get()))
            self.info1 = messagebox.showinfo('Unordered Binary sin(x) Data', self.L4)
            plt.plot(self.L4, 'r--d')
            self.quickSort(self.L4,0,len(self.L4)-1)
            self.info2 = messagebox.showinfo('Ordered Binary sin(x) Data', self.L4)
            plt.plot(self.L4, 'b--o')
            plt.title('Binary sin(x) Fitness Function')
            plt.legend(('Unordered Binary sin(x)', 'Ordered Binary sin(x)'), prop = {'size': 10}, loc='upper left')
            plt.show()

        elif(self.grayValue.get()==1)&(self.binValue.get()==0)&(self.intValue.get()==0)&(self.realValue.get()==0):
            self.L4 = self.sinFunction(self.grayData(self.ran.get(), self.q.get()))
            self.info1 = messagebox.showinfo('Unordered Gray sin(x) Data', self.L4)
            plt.plot(self.L4, 'r--d')
            self.quickSort(self.L4,0,len(self.L4)-1)
            self.info2 = messagebox.showinfo('Ordered Gray sin(x) Data', self.L4)
            plt.plot(self.L4, 'b--o')
            plt.title('Gray sin(x) Fitness Function')
            plt.legend(('Unordered Gray sin(x)', 'Ordered Gray sin(x)'), prop = {'size': 10}, loc='upper left')
            plt.show()

        elif(self.realValue.get()==1)&(self.binValue.get()==0)&(self.intValue.get()==0)&(self.grayValue.get()==0):
            self.L4 = self.realData(self.ran.get(), self.q.get())

            for i in self.L4:
                self.L5.append(self.sinFunction(i))
                plt.plot(self.sinFunction(i), '--o')
            
            self.info1 = messagebox.showinfo(('Ordered Real sin(x) Data'), self.L5)
            
            plt.grid()
            plt.title('Real sin(x) Fitness Function ')
            #plt.legend(('Unordered Int sin(x)', 'Ordered Int sin(x)'), prop = {'size': 10}, loc='upper left')
            plt.show()

        elif(self.intValue.get()==1)&(self.binValue.get()==0)&(self.grayValue.get()==0)&(self.realValue.get()==0):
            self.L4 = self.intData(self.ran.get(), self.q.get())

            for i in self.L4:
                self.L5.append(self.sinFunction(i))
                plt.plot(self.sinFunction(i), '--o')
            
            self.info1 = messagebox.showinfo(('Ordered Int sin(x) Data'), self.L5)
            
            plt.grid()
            plt.title('Int sin(x) Fitness Function ')
            #plt.legend(('Unordered Int sin(x)', 'Ordered Int sin(x)'), prop = {'size': 10}, loc='upper left')
            plt.show()

        else:
            self.info1 = messagebox.showerror('Fatal Error!', 'You can only select one type of data!')

    def sin2BF(self):
        if(self.binValue.get()==1)&(self.grayValue.get()==0)&(self.intValue.get()==0)&(self.realValue.get()==0):
            self.L4 = self.sin2Function(self.binData(self.ran.get(), self.q.get()))
            self.info1 = messagebox.showinfo('Unordered Binary sin^2(x) Data', self.L4)
            plt.plot(self.L4, 'r--d')
            self.quickSort(self.L4,0,len(self.L4)-1)
            self.info2 = messagebox.showinfo('Ordered Binary sin^2(x) Data', self.L4)
            plt.plot(self.L4, 'b--o')
            plt.title('Binary sin^2(x) Fitness Function')
            plt.legend(('Unordered Binary sin^2(x)', 'Ordered Binary sin^2(x)'), prop = {'size': 10}, loc='upper left')
            plt.show()

        elif(self.grayValue.get()==1)&(self.binValue.get()==0)&(self.intValue.get()==0)&(self.realValue.get()==0):
            self.L4 = self.sin2Function(self.grayData(self.ran.get(), self.q.get()))
            self.info1 = messagebox.showinfo('Unordered Gray sin^2(x) Data', self.L4)
            plt.plot(self.L4, 'r--d')
            self.quickSort(self.L4,0,len(self.L4)-1)
            self.info2 = messagebox.showinfo('Ordered Gray sin^2(x) Data', self.L4)
            plt.plot(self.L4, 'b--o')
            plt.title('Gray sin^2(x) Fitness Function')
            plt.legend(('Unordered Gray sin^2(x)', 'Ordered Gray sin^2(x)'), prop = {'size': 10}, loc='upper left')
            plt.show()

        elif(self.realValue.get()==1)&(self.binValue.get()==0)&(self.intValue.get()==0)&(self.grayValue.get()==0):
            self.L4 = self.realData(self.ran.get(), self.q.get())

            for i in self.L4:
                self.L5.append(self.sin2Function(i))
                plt.plot(self.sin2Function(i), '--o')
            
            self.info1 = messagebox.showinfo(('Ordered Real sin^2(x) Data'), self.L5)
            
            plt.grid()
            plt.title('Real sin^2(x) Fitness Function ')
            #plt.legend(('Unordered Int sin(x)', 'Ordered Int sin(x)'), prop = {'size': 10}, loc='upper left')
            plt.show()

        elif(self.intValue.get()==1)&(self.binValue.get()==0)&(self.grayValue.get()==0)&(self.realValue.get()==0):
            self.L4 = self.intData(self.ran.get(), self.q.get())

            for i in self.L4:
                self.L5.append(self.sin2Function(i))
                plt.plot(self.sin2Function(i), '--o')
            
            self.info1 = messagebox.showinfo(('Ordered Int sin^2(x) Data'), self.L5)
            
            plt.grid()
            plt.title('Int sin^2(x) Fitness Function ')
            #plt.legend(('Unordered Int sin(x)', 'Ordered Int sin(x)'), prop = {'size': 10}, loc='upper left')
            plt.show()

        else:
            self.info1 = messagebox.showerror('Fatal Error!', 'You can only select one type of data!')

    def cosBF(self):
        if(self.binValue.get()==1)&(self.grayValue.get()==0)&(self.intValue.get()==0)&(self.realValue.get()==0):
            self.L4 = self.cosFunction(self.binData(self.ran.get(), self.q.get()))
            self.info1 = messagebox.showinfo('Unordered Binary cos(x) Data', self.L4)
            plt.plot(self.L4, 'r--d')
            self.quickSort(self.L4,0,len(self.L4)-1)
            self.info2 = messagebox.showinfo('Ordered Binary cos(x) Data', self.L4)
            plt.plot(self.L4, 'b--o')
            plt.title('Binary cos(x) Fitness Function')
            plt.legend(('Unordered Binary cos(x)', 'Ordered Binary cos(x)'), prop = {'size': 10}, loc='upper left')
            plt.show()

        elif(self.grayValue.get()==1)&(self.binValue.get()==0)&(self.intValue.get()==0)&(self.realValue.get()==0):
            self.L4 = self.cosFunction(self.grayData(self.ran.get(), self.q.get()))
            self.info1 = messagebox.showinfo('Unordered Gray cos(x) Data', self.L4)
            plt.plot(self.L4, 'r--d')
            self.quickSort(self.L4,0,len(self.L4)-1)
            self.info2 = messagebox.showinfo('Ordered Gray cos(x) Data', self.L4)
            plt.plot(self.L4, 'b--o')
            plt.title('Gray cos(x) Fitness Function')
            plt.legend(('Unordered Gray sin(x)', 'Ordered Gray cos(x)'), prop = {'size': 10}, loc='upper left')
            plt.show()

        elif(self.realValue.get()==1)&(self.binValue.get()==0)&(self.intValue.get()==0)&(self.grayValue.get()==0):
            self.L4 = self.realData(self.ran.get(), self.q.get())

            for i in self.L4:
                self.L5.append(self.cosFunction(i))
                plt.plot(self.cosFunction(i), '--o')
            
            self.info1 = messagebox.showinfo(('Ordered Real cos(x) Data'), self.L5)
            
            plt.grid()
            plt.title('Real cos(x) Fitness Function ')
            #plt.legend(('Unordered Int sin(x)', 'Ordered Int sin(x)'), prop = {'size': 10}, loc='upper left')
            plt.show()

        elif(self.intValue.get()==1)&(self.binValue.get()==0)&(self.grayValue.get()==0)&(self.realValue.get()==0):
            self.intData(self.ran.get(), self.q.get())
            self.L4 = self.intData(self.ran.get(), self.q.get())

            for i in self.L4:
                self.L5.append(self.cosFunction(i))
                plt.plot(self.cosFunction(i), '--o')
            
            self.info1 = messagebox.showinfo(('Ordered Int cos(x) Data'), self.L5)
            
            plt.grid()
            plt.title('Int cos(x) Fitness Function ')
            #plt.legend(('Unordered Int sin(x)', 'Ordered Int sin(x)'), prop = {'size': 10}, loc='upper left')
            plt.show()

        else:
            self.info1 = messagebox.showerror('Fatal Error!', 'You can only select one type of data!')

    def cos2BF(self):
        if(self.binValue.get()==1)&(self.grayValue.get()==0)&(self.intValue.get()==0)&(self.realValue.get()==0):
            self.L4 = self.cos2Function(self.binData(self.ran.get(), self.q.get()))
            self.info1 = messagebox.showinfo('Unordered Binary cos^2(x) Data', self.L4)
            plt.plot(self.L4, 'r--d')
            self.quickSort(self.L4,0,len(self.L4)-1)
            self.info2 = messagebox.showinfo('Ordered Binary cos^2(x) Data', self.L4)
            plt.plot(self.L4, 'b--o')
            plt.title('Binary cos^2(x) Fitness Function')
            plt.legend(('Unordered Binary cos^2(x)', 'Ordered Binary cos^2(x)'), prop = {'size': 10}, loc='upper left')
            plt.show()

        elif(self.grayValue.get()==1)&(self.binValue.get()==0)&(self.intValue.get()==0)&(self.realValue.get()==0):
            self.L4 = self.cos2Function(self.grayData(self.ran.get(), self.q.get()))
            self.info1 = messagebox.showinfo('Unordered Gray cos^2(x) Data', self.L4)
            plt.plot(self.L4, 'r--d')
            self.quickSort(self.L4,0,len(self.L4)-1)
            self.info2 = messagebox.showinfo('Ordered Gray cos^2(x) Data', self.L4)
            plt.plot(self.L4, 'b--o')
            plt.title('Gray cos^2(x) Fitness Function')
            plt.legend(('Unordered Gray cos^2(x)', 'Ordered Gray cos^2(x)'), prop = {'size': 10}, loc='upper left')
            plt.show()

        elif(self.realValue.get()==1)&(self.binValue.get()==0)&(self.intValue.get()==0)&(self.grayValue.get()==0):
            self.L4 = self.realData(self.ran.get(), self.q.get())

            for i in self.L4:
                self.L5.append(self.cos2Function(i))
                plt.plot(self.cos2Function(i), '--o')
            
            self.info1 = messagebox.showinfo(('Ordered Real cos^2(x) Data'), self.L5)
            
            plt.grid()
            plt.title('Real cos^2(x) Fitness Function ')
            #plt.legend(('Unordered Int sin(x)', 'Ordered Int sin(x)'), prop = {'size': 10}, loc='upper left')
            plt.show()

        elif(self.intValue.get()==1)&(self.binValue.get()==0)&(self.grayValue.get()==0)&(self.realValue.get()==0):
            self.intData(self.ran.get(), self.q.get())
            self.L4 = self.intData(self.ran.get(), self.q.get())

            for i in self.L4:
                self.L5.append(self.cos2Function(i))
                plt.plot(self.cos2Function(i), '--o')
            
            self.info1 = messagebox.showinfo(('Ordered Int cos^2(x) Data'), self.L5)
            
            plt.grid()
            plt.title('Int cos^2(x) Fitness Function ')
            #plt.legend(('Unordered Int sin(x)', 'Ordered Int sin(x)'), prop = {'size': 10}, loc='upper left')
            plt.show()

        else:
            self.info1 = messagebox.showerror('Fatal Error!', 'You can only select one type of data!')

                
    def __init__(self):
        self.root = Tk()
        self.root.title('Fitness Function Implementation')
        #self.root.iconbitmap('pythonIcon.ico')
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
        self.lblFunction = Label(self.frame, text='Select defined fitness function below...')
        self.lblFunction.grid(row=0, column=1, sticky='N')
        self.sinButton = Button(self.frame, text='sin(x)', command = lambda: self.sinBF())
        self.sinButton.grid(row=1, column=1, sticky='N')
        self.sin2Button = Button(self.frame, text='sin^2(x)', command = lambda: self.sin2BF())
        self.sin2Button.grid(row=2, column=1, sticky='N')
        self.cosButton = Button(self.frame, text='cos(x)', command = lambda: self.cosBF())
        self.cosButton.grid(row=3, column=1, sticky='N')
        self.cos2Button = Button(self.frame, text='cos^2(x)', command = lambda: self.cos2BF())
        self.cos2Button.grid(row=4, column=1, sticky='N')
        self.lblFunction2 = Label(self.frame, text='Or you can introduce your own function in Python syntax')
        self.lblFunction2.grid(row=5, column=1, sticky='N')
        self.fitFunc = Entry(self.frame)
        self.fitFunc.grid(row=6, column=1, sticky='N')
        self.b1 = Button(self.frame, text = 'Go!', command = lambda: self.go())
        self.b1.grid(row=7, column=1, pady=5)
        self.b2 = Button(self.frame, text = 'Exit', command = self.root.destroy)
        self.b2.grid(row=8, column=1, pady=5)
        self.L = []
        self.L1 = []
        self.L2 = []
        self.L3 = []
        self.L4 = []
        self.L5 = []
        self.root.mainloop()

gui = GUI()