#globel scope
# fname='zero'
# print("before:outside the function:",fname)
# def gbscope():
#     print("inside the function:",fname)
# gbscope()
# print("after:outside the function:",fname)

#local scope
# def localscope():
#     fname='hero'  #local variable
#     print('my name is',fname)
# localscope()
# print('my name is',fname)

# def diplayname(name):  #parameters acts like local variable
#     print("my name is:",name)
# diplayname('hero')
# print("my name is:",name)


# fname='global'
# def myfun():
#     global fname
#     fname='local'
#     print("insdie function:",fname)
# myfun()
# print("outside function:",fname)

#nested functions
# def outerfunc():
#     print("iam outer function")
#     def innerfun():
#         print("iam inner function")
#     innerfun()
# outerfunc()

#accessing
# def outerfunc():
#     print("iam outer function")
#     def innerfun():
#         print("iam inner function")
#     # innerfun()✅
# outerfunc()
# # innerfunc()❌


#enclosing scope
# def outrfunc():
#     #enclosing scope
#     myname='hero'
#     def innerfunc():
#         print("my name is:",myname)
#         print("iam inner function")
#     innerfunc()
#     print("my name is::",myname)
# outrfunc()

#modification of enclosing variable
# def outrfunc():
#     #enclosing scope
#     myname='hero'
#     def innerfunc():
#         nonlocal myname
#         myname='zero'
#         print("my name is:",myname)
#     innerfunc()
#     print("my name is::",myname)
# outrfunc()

#example for global,non local ,direct modification
# myname='hero'
# def outerfunc():
#     global myname   #global variable modification
#     myname='zero'
#     gender='female'
#     secondname='sai'
#     print("my name is:",myname)
#     def innerfunc():
#         nonlocal gender     #local variable modification
#         gender='male'
#         secondname='ram'      #direct modification
#         print("my gender is:",gender)
#         print("second name is:",secondname)
#     innerfunc()
#     print("my gender is:",gender)
#     print("second name is:",secondname)
# outerfunc()
# print("my name is:",myname)

#built in scope
# import builtins
# print(dir(builtins))

#scope chain
# # myname='hero'
# def outerfunc():
#     # myname='zero'
#     def innerfunc():
#         # myname='sai'
#         print('inside innerscope,',myname)
#     innerfunc()
# outerfunc()

#ex-2
# def outerfunc():
#     def innerfunc():
#         print(len('hero'))  #len method located in built in scope
#     innerfunc()
# outerfunc()

#lexical scope
# gvar='iam global variable'
# def outerfunc():
#     evar='iam enclosing variable'
#     def innerfunc():
#         lvar='iam local  variable'
#         print("global variable:",gvar)
#         print("enclosing variable:",evar)
#         print("local variable:",lvar)
#     innerfunc()
#     print("global variable:",gvar)
#     print("enclosing variable:",evar)
#     print("local variable:",lvar)
# outerfunc()
# print("global variable:",gvar)
# print("enclosing variable:",evar)
# print("local variable:",lvar)

#lexical scope task
# gvar='global variable'
# def outsidefun():
#     evar1='enclosing variable 1'
#     def insidefun1():
#         evar2='enclosing variable 2'
#         def innerfun2():
#             lvar='local variable'
#             print("-------inside the nested function")
#             print("global varaible:",gvar) ✅
#             print("enclosing variable 1:",evar1)✅
#             print('enclosing variable 2:',evar2)✅
#             print('local variable :',lvar)✅
#         innerfun2()
#         print("-------inside the first inner function")
#         print("global varaible:",gvar)✅
#         print("enclosing variable 1:",evar1)✅
#         print('enclosing variable 2:',evar2)✅
#         print('local variable :',lvar)❌
#     insidefun1()
#     print("global varaible:",gvar)✅
#     print("enclosing variable 1:",evar1)✅
#     print('enclosing variable 2:',evar2)❌
#     print('local variable :',lvar)❌
# outsidefun()
# print("-------inside the nested function")
# print("global varaible:",gvar)✅
# print("enclosing variable 1:",evar1)✅
# print('enclosing variable 2:',evar2)✅
# print('local variable :',lvar)✅