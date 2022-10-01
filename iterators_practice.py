#Practica de los iteradores
import time

class FiboIter():
    global max
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self 
    
    def __next__(self):
        if self.n2 < max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.n1
        else:
            raise StopIteration

if __name__== "__main__":
    max = int(input("Valor maximo al que llegara la sucesion? "))
    finocacci = FiboIter()
    for element in finocacci:
        print(element)
        time.sleep(0.05)