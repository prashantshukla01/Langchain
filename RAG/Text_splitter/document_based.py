from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
ef scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
The output of the example code is:

After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,  #yhn kch b le skte h like markdown , JAVA , python , PHP etc.
    
    chunk_size=300,
    chunk_overlap=0
)

chunks = splitter.split_text(text)  

print(chunks)