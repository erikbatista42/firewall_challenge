# illumio_challenge

**How you tested your solution**
I tested my solution by creating my own CSV file containing the rules that were provided in the prompt. I then used the same test cases provided in the assignment, and created my own test cases to cover possible edge cases. Had I allotted myself more than two hours for completing the assignment, I would have taken a more robust approach to testing my solution. For instance, I would have created a CSV file with many more rules.

**Any interesting coding, design, or algorithmic choices you’d like to point out**
When I was coming up with  a solution for the problem, I  initially considered storing the parsed rules from the csv file into a data structure, like a dictionary. I realized that I was over-complicating the problem, and opted to just read the csv file line-by-line, comparing each rule to the incoming/outgoing packet. This not only made the problem easier, but also improves the runtime and memory allocation.

**Any refinements or optimizations that you would’ve implemented if you had more time**
I used the built-in ipaddress module to help me create the ipranges instead of creating it from scratch. If I had more time, I'd explicitly define the type of the parameter in the method signatures to make the code easier to understand.

**Team that I'm interested in**
I am particularly interested in the Policy team, but would love the opportunity to work with any of the listed teams:
1) Policy
2) Platform
3) Data
