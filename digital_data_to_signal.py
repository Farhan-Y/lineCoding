import numpy as np

class dataToSignal:
  
    def __init__(self , data , V=1):
        self.data = data
        self.V = V

       
    def transform(self,val):
        """essentialy chaning the scale from [0,1] to [-V,V]. assuming the data are 0's and 1's"""
        return (int(val)*2 -1)* self.V


    def invert(self,bit):
        
        if (bit=='0'):
            return '1'
        elif (bit=='1'):
            return '0'
        else:
            return None
    
    def NRZ(self): # more specificly unipoplaar Non-return-to-zero
        # take the input data and turn it into an equivalent list (since it's unipolar). 
        return list(map(lambda x : int(x)*self.V , list(self.data) ))
       

    def NRZL(self): # aka Non-return-to-zero inverted, non-return to zero IBM
        return list(map(self.transform, list(self.data) ))
        # can alterantively be written as: return list(map(lambda x : self.V(2*int(x)-1) , list(self.data) ))

    def NRZI(self , nrzm = True , start='1' ): # NRZ invert
        '''
        nrzm arg choose the preferred convention.
        start indicate the first bit in our signal.
        '''

        nrzi=start
        if nrzm:
            for i in range(len(self.data)):
                bit = self.data[i]
                prev_bit = nrzi[-1]
                nrzi +=  self.invert(prev_bit) if bit == '1' else prev_bit     
        else :
            for i in range(len(self.data)):
                bit = self.data[i]
                prev_bit = nrzi[-1]
                nrzi +=  self.invert(prev_bit) if bit == '0' else prev_bit

        return list(map(self.transform, list(nrzi) ))

    def toManchester(self , ieee802dot3 =False): # also known as Biphase L
        """
        return the manchers of the given string
        manchster is calculated by xoring the data with a clock with twice the bit rate
        """
        # this encoding is for mancher per G.E encoding and is differrent than 802.3 encoding for manchester

        if ieee802dot3 == False:   
            clock = [0,1] * len(self.data) # clock is o form 0101... if wish to implement ieee encoding change '01' to '10'
        else:   
            clock = [1,0] * len(self.data) # change the implementation if ieee802dot3 == True

        data = list(map(lambda x : int(x), list(self.data)) ) # change data string to list of int

        j=0
        manchester=[]
        for i in range(len(self.data)):
            manchester.append(data[i] ^ clock[j] )
            j+=1
            manchester.append(data[i] ^ clock[j] )
            j+=1

        # ESSENTIALY 0 WILL BE LOW_HIGH AND 1 WILL BE HIGH_lOW.
        # VICE VERSA IS ALSO ANTHER CONNVENTION IS POSSIBE IF CLOCK BE SET TO  [1,0] 

        return list(map(self.transform, list(manchester) ))    




    def toDifferentailManchester(self):   # also known as biphase mark code
        '''
        the transition in the middle is garanteed.
        if the bit is bit is 1 no transtion at the end otherwise another transition at the end.
        '''
        
        #  This method like Manchester use twice the bandwidth
        
        mandiff = '10' if self.data[0]=='1' else  '01'   
        j=2
        for i in range(1,len(self.data)) :
            if(self.data[i]=='1'):               
                mandiff += mandiff[j-1]
                j+=1
                mandiff += self.invert(mandiff[j-1])
                j+=1

            if(self.data[i]=='0'):
                mandiff += self.invert(mandiff[j-1])
                j+=1
                mandiff += self.invert(mandiff[j-1])
                j+=1

        return  list(map(self.transform, list(mandiff) ))
    
