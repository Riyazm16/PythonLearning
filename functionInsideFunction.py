def display(name):
    def message():
        return "hello"
    result  = message()+name
    return result

ans = display("Riyaj")

print(ans)