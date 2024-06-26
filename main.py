def main():
    result = False
    while result == False:
        num = int(input('Enter your input: '))
        if num > 0 and num <100:
            number = num
            result = True
        else:
            result = False 
    print('Output: ')
    print(number)    
    return (result)
    ########################################
    # Do not delete the return statement
    ########################################

if __name__ == '__main__':
    main()
