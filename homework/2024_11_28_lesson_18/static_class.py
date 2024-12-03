class Container:
    is_empty = True
    value    = None


def setConteinerValue(class_ref:Container, new_value: int):
    class_ref.value = new_value
    class_ref.is_empty = False

def unsetConteinerValue(class_ref:Container):
    class_ref.value = None
    class_ref.is_empty = True

def printContainerValue(class_ref:Container):
    if class_ref.is_empty == False:
        print(f"Container<{class_ref.value}>")
    else:
        print("Container is empty")

printContainerValue(Container)
setConteinerValue(Container, 123)
printContainerValue(Container)
unsetConteinerValue(Container)
printContainerValue(Container)


