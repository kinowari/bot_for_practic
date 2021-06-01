def calculator(string):
    numbers=[]
    operation=[]
    original=[]
    priority={'+':1,'-':1,'*':2,'/':2}
    num=''
    lenght,len2=0,0
    for char in string:
        lenght += 1
        if char!='+' and char!='-' and char!='*' and char!='/' and char!='(' and char!=')':
            if lenght == len(string):
                original.append(int(char))
            num+=char
        else:
            if num!='':
                original.append(int(num))
                num=''
            original.append(char)

    #print(original)
    len1=len(original)
    for el in original:
        len2+=1
        #print(operation)
        if len1 == len2:
            #print('lol')
            if type(el) is int:
                numbers.append(el)
            while True:
                #print(operation)
                #print('lll')
                if operation == []:
                    break
                elif operation[-1] == '(':
                    operation.pop()
                    break
                op = operation.pop()
                num2 = numbers.pop()
                num1 = numbers.pop()
                if op == '*':
                    numbers.append(num1 * num2)
                if op == '/':
                    numbers.append(num1 / num2)
                if op == '+':
                    numbers.append(num1 + num2)
                if op == '-':
                    numbers.append(num1 - num2)

        if type(el) is int:
            numbers.append(el)
            #print(numbers)
        elif el=='+' or el=='-':

            while True:

                if operation !=[]:

                    op = operation[-1]
                    if priority.get(op) == 1 or op == '(':
                        operation.append(el)
                        break
                    else:
                        op = operation.pop()
                        num2 = numbers.pop()
                        num1 = numbers.pop()
                        if op == '*':
                            numbers.append(num1 * num2)
                        if op == '/':
                            numbers.append(num1 / num2)

                elif operation ==[] :
                    operation.append(el)
                    break


                else:
                    num2 = numbers.pop()
                    num1 = numbers.pop()

                    if operation[-1] == '*':
                        numbers.append(num1*num2)
                    else: numbers.append(num1/num2)


        elif el=='*' or el=='/':
            operation.append(el)


        elif el=='(':
            operation.append('(')
        elif el==')':
            #print('lol')
            while True:

                #print(op)
                if operation==[]:
                    break
                elif operation[-1]=='(':
                    operation.pop()
                    #print('olo')
                    break
                op = operation.pop()
                num2 = numbers.pop()
                num1 = numbers.pop()
                if op=='*':
                    numbers.append(num1*num2)
                if op=='/':
                    numbers.append(num1/num2)
                if op=='+':
                    numbers.append(num1+num2)
                if op=='-':
                    numbers.append(num1-num2)

    return numbers[0]

#calculator('1+2+(4+8)')






