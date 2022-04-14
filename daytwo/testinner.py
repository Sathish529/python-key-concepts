def outer(state):
    element=state
    print("element in outer ",element)
    def inner(data):
        element= "test"
        inside = data
        print("element in inner", element)
        print("inside in inner", inside)
    inner("first Call")
    print("element in outer ",element)
    return inner
        
outer("Strong")
