 Descriptions.
 
These descriptions explain the context, purpose, and reasoning behind each task focusing on the real-world applications.

Stack Questions

Practical (Rwanda): In MoMo, push ["PIN", "Amount", "Confirm"]. Undo 2. Which remains?

The stack represents a sequence of actions (entering PIN, amount, and confirmation) performed by a user. The "undo" operation corrects mistakes by reversing the last two actions.

Practical (Rwanda): UR pushes ["Exercise1", "Exercise2", "Exercise3"]. Undo one. Which is left?

This scenario models a submission system at the University of Rwanda (UR), where students submit exercises in a specific order. The stack tracks these submissions, with the most recent exercise at the top. 

Challenge: Reverse "STACKMODEL" using stack.
This challenge tests the ability to reverse a string ( "STACKMODEL") by leveraging a stack's LIFO property. Each character of the string is added to the stack in sequence, and then removed in reverse order to form the reversed string. 

Reflection: Why stack is good for undo but not for customer order?

For customer orders (e.g., in a shop or restaurant), a stack would unfairly prioritize the last customer, whereas a fair system requires serving the first customer first, aligning with a queue's FIFO (First In, First Out) approach.

Queue Questions

Practical (Rwanda): At RRA, 7 clients queue. After 3 served, who is next?

Clients arrive and are served in the order they join. After serving the first three clients, the task is to identify the next client in line who is client 4 as queue ensures fairness .

Practical (Rwanda): At BK ATM, 9 clients queue. Who is served second?

This scenario simulates a line at a Bank of Kigali (BK) ATM, where clients wait to use the machine. The queue follows FIFO, meaning the order of arrival determines the service order.

Challenge: Queue vs stack for voters. Which ensures fairness?

 A queue (FIFO) ensures voters are served in the order they arrive, promoting fairness and preventing line-cutting. A stack (LIFO) would serve the last voter first, which is unfair and impractical. 

Reflection: Why FIFO is linked with democracy?

 FIFO ensures that everyone is treated equally based on the time of arrival, mirroring democratic ideals like "one person, one vote" and equal access which prevents favoritism or priority based on status, fostering a sense of fairness and order. 
