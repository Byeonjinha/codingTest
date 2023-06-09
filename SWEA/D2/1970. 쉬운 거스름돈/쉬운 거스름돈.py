T = int(input())
for tc in range(1, T + 1):
    charges = int(input())
    answer = ""
   
    answer += str(charges // 50000)+ " "
    charges %= 50000
   
    answer += str(charges // 10000)+ " "
    charges %= 10000
    
    answer += str(charges // 5000)+ " "
    charges %= 5000
    answer += str(charges // 1000)+ " "
    charges %= 1000
    
    answer += str(charges // 500)+ " "
    charges %= 500
    answer += str(charges // 100)+ " "
    charges %= 100
    
    answer += str(charges // 50)+ " "
    charges %= 50
    answer += str(charges // 10)
    charges %= 10
    
    print("#{}".format(tc))
    print(answer)