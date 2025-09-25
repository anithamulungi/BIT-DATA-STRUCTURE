stack=[]
stack.append("PIN")
stack.append("Amount")
stack.append("Confirm")

stack.pop()
stack.pop()
print("when we undo 2 we remain with:",stack)


stack=[]
stack.append("Exercise1")
stack.append("Exercise2")
stack.append("Exercise3")

stack.pop()
print("when we undo 1 we are left with:",stack)

#queue
queue=[]
queue.append("Client 1")
queue.append("Client 2")
queue.append("Client 3")
queue.append("Client 4")
queue.append("Client 5")
queue.append("Client 6")
queue.append("Client 7")

queue.pop(0)
queue.pop(0)
queue.pop(0)
print("the next client served is:",queue[0])

queue=[]
queue.append("client 1")
queue.append("client 2")
queue.append("client 3")
queue.append("client 4")
queue.append("client 5")
queue.append("client 6")
queue.append("client 7")
queue.append("client 8")
queue.append("client 9")

queue.pop(0)
print("the client served second is:",queue[0])






