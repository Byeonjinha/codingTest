func main(){
    guard let nStr = readLine(), let n = Int(nStr) else { return }
    if n % 2 == 1 { print("SK") }
    else { print("CY")}
}
main()
