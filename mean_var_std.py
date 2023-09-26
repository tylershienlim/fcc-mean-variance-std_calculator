import numpy as np

def calculate(list):
    #List must contain nine numbers
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    #Change list into numpy array
    a = np.array(list)

    #Calculate flattened
    flat = []
    flat.append(np.mean(a))
    flat.append(np.var(a))
    flat.append(np.std(a))
    flat.append(max(list))
    flat.append(min(list))
    flat.append(sum(list))

    #Change numpy array into matrix
    matrix = a.reshape(3, 3)

    #Calculate for each row in matrix
    axis2 = []

    for row in matrix:
        temp = []
        temp.append(np.mean(row))
        temp.append(np.var(row))
        temp.append(np.std(row))
        temp.append(np.max(row))
        temp.append(np.min(row))
        temp.append(np.sum(row))

        axis2.append(temp)

    #Calculate for each column in matrix
    b = matrix.T
    axis1 = []

    for row in b:
        temp = []
        temp.append(np.mean(row))
        temp.append(np.var(row))
        temp.append(np.std(row))
        temp.append(np.max(row))
        temp.append(np.min(row))
        temp.append(np.sum(row))

        axis1.append(temp)
    
    
    print("flat:\n")
    print(flat)
    print("\n")

    print("axis1:\n")
    print(axis1)
    print("\n")

    print("axis2:\n")
    print(axis2)
    print("\n")
    

    calculations = {
        'mean':[],
        'variance':[],
        'standard deviation':[],
        'max':[],
        'min':[],
        'sum':[],
    }

    #Add axis1, then axis2
    

    #Lastly add flattened

    return calculations