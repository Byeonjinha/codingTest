def transDateToDay(date):
    year, month, day = date.split(".")
    yearToDay = int(year) * 12 * 28
    monthToDay = int(month) * 28
    total = yearToDay + monthToDay + int(day)
    return total
    
def transTermDate(date):
    global termsDict
    termDate, termName = date.split()
    year, month, day = termDate.split(".")
    yearToDay = int(year) * 12 * 28
    monthToDay = int(month) * 28
    total = yearToDay + monthToDay + int(day) + termsDict[termName]
    return total
termsDict = {}

def solution(today, terms, privacies):
    global termsDict
    answer = []
    today = transDateToDay(today)
    for term in terms:
        termName, termPeriod = term.split()
        termsDict[termName] = int(termPeriod) * 28
    
    for privacyIdx in range(len(privacies)): 
        if today >= transTermDate(privacies[privacyIdx]):
            answer.append(privacyIdx+1)
    return answer