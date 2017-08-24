hello = "Hello Initial"

def scope_changed():
    hello = "hello from scope_changed()"
    
    def change_local():
        hello = "hello local"
    
    def change_nonlocal():
        nonlocal hello
        hello = "hello nonlocal"
        
    def change_global():
        global hello
        hello = "Hello global"
    
    print("Before change_local:", hello)
    change_local()
    print("After change_local: ",hello)
    change_nonlocal()
    print("After change_local: ",hello)
    change_global()
    print("After change_global: ", hello)
    
print("Initial value:", hello)
scope_changed()
print("Outside : ", hello)