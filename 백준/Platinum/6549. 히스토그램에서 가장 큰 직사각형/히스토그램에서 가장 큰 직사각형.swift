import Foundation

var list = [Int]()
while(true)
{
    
    let arr = readLine()?.split(separator: " ").map{Int($0)}
    let num = arr![0]
    if(num == 0){break}
    list = [Int](repeating: 0, count: num!)
    
    
    for i in 1...num!
    {
        list[i-1]=arr![i]!
    }
    print(solve(start: 0, end: num!-1))
}

func solve(start:Int, end:Int)->Int
{
    if(start == end) {return list[start]}
    
    let mid = (start+end)/2
    var result = max(solve(start: start, end: mid) , solve(start: mid+1, end: end))
    
    var left = mid
    var right = mid + 1
    var height = min(list[left], list[right])
    result = max(result, height*2)
    
    while(start < left || right < end)
    {
        if(start < left && right < end)
        {
            if (list[left - 1] < list[right + 1])
            {
                right += 1
                height = min(height, list[right])
                
            }else
            {
                left -= 1
                height = min(height, list[left])
            }
        }
        else if(start < left)
        {
            left -= 1
            height = min(height, list[left])
        }else if (right < end)
        {
            right += 1
            height = min(height, list[right])
        }
        result = max(result, height * (right - left + 1))
    }
    
    return result
}