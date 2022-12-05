import random
def generate_qn_beginner(): 
    qn_randomise = 3
    y = random.randint(0,9) 
    
    if qn_randomise == 1: #sum  
    
        total = random.randint(y,9) 
        expected_ans = total - y  
        # print("y value:",y,"total:",total,"expected:",expected_ans) 

        equation = "a + {0} = {1}".format(y, total) 
            
        return equation,expected_ans 
            
    elif qn_randomise == 2: #minus  
        #y = random.randint(0,9) 
        positive_ans = False 
        while positive_ans == False: 
            total = random.randint(0,y) 
            expected_ans = total - y 
            if expected_ans >= 0: 
                positive_ans = True 
                
        # print("y value:", y, "total:",total,"expected:", expected_ans) 
        equation = "{0} - a = {1} ".format(total, y) 
        return equation,expected_ans 
        
    elif qn_randomise == 3: #times  
        nonzero = False 
        y = random.randint(1,9)
        while nonzero == False: 
            total1 = random.randint(0,9) 
            total = total1*y 
            if total != 0: 
                nonzero = True  

        expected_ans = total1 
        # print("y value:", y, "total:",total,"expected:", expected_ans) 
        equation = "a x  {0} = {1}".format(y, total) 
        return equation,expected_ans 
        
    elif qn_randomise == 4: 
        nonzero = False 
        while nonzero == False: 
            total1 = random.randint(0,9) 
            total = total1*y 
            if total != 0: 
                nonzero = True  

        expected_ans = total1 
        # print("y value:", y, "total:",total,"expected:", expected_ans) 
        equation = "{1} / a = {0}".format(y, total) 
        return equation,expected_ans
def generate_qn_advanced(): 
         qn_randomise = random.randint(1,4) 
         y = random.randint(0,98) 
         if qn_randomise == 1: 
            total = random.randint(y,98) 
            expected_ans = total - y  
            print("y value:",y,"total:",total,"expected:",expected_ans) 
            equation = "a + {0} = {1}".format(y, total) 
             
            return equation,expected_ans 
 
         elif qn_randomise == 2: #minus  
 
            positive_ans = False 
            while positive_ans == False: 
                total = random.randint(y,98) 
                expected_ans = total - y 
                if expected_ans >= 0: 
                    positive_ans = True 
                 
            print("y value:", y, "total:",total,"expected:", expected_ans) 
            equation = "{0} - a = {1} ".format(total, y) 
            return equation,expected_ans 
 
 
         elif qn_randomise == 3: #times  
 
            nonzero = False 
            while nonzero == False: 
                total1 = random.randint(0,98) 
                total = total1*y 
                if total != 0: 
                    nonzero = True  
 
            expected_ans = total1 
            print("y value:", y, "total:",total,"expected:", expected_ans) 
            equation = "a x  {0} = {1}".format(y, total) 
            return equation,expected_ans 
 
         else: 
            nonzero = False 
            while nonzero == False: 
                total1 = random.randint(0,98) 
                total = total1*y 
                if total != 0: 
                    nonzero = True  
 
            expected_ans = total1 
            print("y value:", y, "total:",total,"expected:", expected_ans) 
            equation = "{1} / a = {0}".format(y, total) 
            return equation,expected_ans