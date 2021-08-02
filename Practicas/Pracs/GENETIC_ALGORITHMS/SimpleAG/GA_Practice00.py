import matplotlib.pyplot as plt
import random
from tkinter import * 
from tkinter import Entry
from tkinter import messagebox

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
            str1 += ele

        return str1

    def go(self):
        self.r = int(self.ran.get())
        self.q1 = int(self.q.get())

        for _ in range(self.q1):
            self.value = random.randint(0, self.r)
            self.L.append(self.value)
            self.generated = self.listToString(str(self.L))
        
        self.info = messagebox.showinfo('Generated numbers', self.generated)
        plt.plot(self.L, 'r--d')
        self.n = len(self.L)
        self.quickSort(self.L,0,self.n-1)

        for i in self.L:
            self.val_bin = format(i, 'b')
            self.L1.append(self.val_bin)
            self.generated1 = self.listToString(str(self.L1))

        self.info1 = messagebox.showinfo('Sorted generated numbers', self.listToString(str(self.L)))
        self.info2 = messagebox.showinfo('Sorted generated numbers in binary format', self.generated1)
        plt.plot(self.L, 'b--o')
        plt.show()

    def __init__(self):
        self.root = Tk()
        self.root.title('Data Sort')
        self.root.iconbitmap('pythonIcon.ico')
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bd=20)
        self.random = random.seed(0)
        self.lblRange = Label(self.frame, text = 'Please, insert the limit range of random numbers!')
        self.lblRange.grid(row=0, column=0, sticky='N')
        self.ran = Entry(self.frame)
        self.ran.grid(row=1, column=0, sticky='N')
        self.lblQuantity = Label(self.frame, text = 'Please, insert how many random numbers you want!')
        self.lblQuantity.grid(row=2, column=0, sticky='N')
        self.q = Entry(self.frame)
        self.q.grid(row=3, column=0, sticky='N')
        self.L = []
        self.L1 = []
        self.b1 = Button(self.frame, text = 'Go!', command = lambda: self.go())
        self.b1.grid(row=4, column=0, pady=5)
        self.b2 = Button(self.frame, text = 'Exit', command = self.root.destroy)
        self.b2.grid(row=5, column=0, pady=5)
        self.root.mainloop()

gui = GUI()
