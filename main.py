import Formulas

if __name__ == "__main__":

    excludeList = ["datetime", "Symbol", "solve", "getMissingValue", "Array", "symbols", "summation", "printList"]
    functionList = [function for function in dir(Formulas) if "_" not in function and function not in excludeList]
    
    while(1):
        print("Available functions: ")
        for function in functionList:
            
            if functionList.index(function) > 9:
                print(f"    {functionList.index(function)}  {function}")
            else:
                print(f"    {functionList.index(function)}   {function}")

        function = input("Please choose a function or -h [function] for help: ")
        print()
        if "-h" in function:
            value = function.split(" ")[1]
            help(getattr(Formulas, f"{functionList[int(value)]}"))
        elif function == 'c':
            print("Adeus Amigo")
            exit()
        else:
            result = getattr(Formulas, f'{functionList[int(function)]}')()
