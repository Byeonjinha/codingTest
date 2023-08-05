func main(){
    guard let nStr = readLine(), let n = Int(nStr) else { return }
    if n % 5 == 0 {
        print(Int(n / 5))
        return
    }
    var k = Int(n / 5)
    while true {
        if ( n - ( k * 5 )) % 2 == 0 {
            break
        } else {
            k -= 1
        }
    }
    if k < 0 {
        print(-1)
    } else {
        print( k + (n - (k * 5)) / 2)
    }
}
main()


