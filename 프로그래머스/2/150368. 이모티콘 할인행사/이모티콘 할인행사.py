import copy

enterUsers = 0
benefit = 0

def calDiscountValue(discount, emoticonValue):
    return int((100 - discount) * 0.01 * emoticonValue)

def dfs(users, discount, emoticon, emoticons, usersPayment, enterUserArray):
    global enterUsers, benefit
    for discount in range(10, 41, 10):
        tmpUsersPayment = copy.deepcopy(usersPayment)
        tmpEnterUserArray = copy.deepcopy(enterUserArray)
        for userIndex in range(len(users)):
            user = users[userIndex]
            per, userValue = user[0], user[1]
            #가입하지 않았다면
            if not enterUserArray[userIndex]:
                # 할인율이 유저가 원하는 할인율보다 높다면
                if discount >= per:
                    tmpUsersPayment[userIndex] += calDiscountValue(discount, emoticon)
                    # 구입한 비용이 가입 비용보다 높다면
                    if tmpUsersPayment[userIndex] >= userValue:
                        tmpUsersPayment[userIndex] = 0
                        tmpEnterUserArray[userIndex] = True
            #가입했다면 패스
            else:
                continue
        
        if sum(tmpEnterUserArray) > enterUsers:
            enterUsers = sum(tmpEnterUserArray)
            benefit = sum(tmpUsersPayment)
        elif sum(tmpEnterUserArray) == enterUsers:
            if sum(tmpUsersPayment) >= benefit:
                benefit = sum(tmpUsersPayment)
        
            
        tmpEmoticons = copy.deepcopy(emoticons)
        try : 
            tmpEmoticon, *tmpEmoticons = tmpEmoticons
            dfs(users, discount, tmpEmoticon, tmpEmoticons, tmpUsersPayment, tmpEnterUserArray)
        except:
            continue
    return

def solution(users, emoticons):
    global enterUsers, benefit
    
    usersPayement = [0 for _ in range(len(users))]
    enterUserArray = [False for _ in range(len(users))]
    
    emoticon, *emoticons = emoticons
    for discount in range(10, 41, 10):
        dfs(users, discount, emoticon, emoticons, usersPayement, enterUserArray)    
    
    return [enterUsers, benefit]