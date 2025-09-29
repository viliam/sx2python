## About

In high school, I enrolled in a course on programming in Assembler. On the first day, the teacher told us: 'With Assembler, you can earn millions—or nothing. It's unlikely that Intel will hire you to design new CPU processors, so the 'nothing' is probably your path.

With **syntax and semantic analysis**, the situation is similar. It's perhaps even less likely that you'll design a new language that the market will accept and adopt.

So why am I reopening my thesis and reworking it? Maybe because it makes me happy—and yes, I do have fun. That could be it. But the answer is different and simpler: training and knowledge. By rewriting my thesis code in a new language, I can prove to myself (and to potential clients) that I have a deep understanding of the language and can solve complex problems with it.

How could you become more familiar with a language like Python than by writing a syntax analyzer in Python for Python itself?
## Theory

Before we jump into it, let's take a quick look at the theory.

https://en.wikipedia.org/wiki/Chomsky_hierarchy

We have four types of languages: Regular, Context-free, Context-sensitive, and Recursively Enumerable. For our purposes, we will be working with the first three types.

### Regular 
Regular language is the simplest type; we can think of it as a linear language. For example, it can be used to define the grammar of a function.

FUNCTION →  “def” , NAME, ARGUMENTS, RETURN_TYPE, BODY

All functions in Python start with the reserved word def, followed by the name of the function. Next, we define the function's arguments, data type of return value, and body of the function. When reading sentences in a regular language, we don’t need to remember much—just the last word we read. As we read from left to right, like humans naturally do, we can predict what kind of word will follow the one we've just read. No surprises.

### Context-free 
   Context-free languages are an extension of regular languages. This means all regular languages are also context-free, but the reverse is not true. Some context-free languages do not belong to the category of regular languages.
    What’s new? Mathematical brackets. Each time we open a bracket, we need to close it somewhere. We can still read the language linearly, but when we encounter a closing bracket, we somehow need to remember whether we’ve seen an opening bracket before. And by the end, we must ensure that all brackets have been properly closed.
    To achieve that, a simple counter can help us. Each time we read an opening bracket, we increase the counter. When we read a closing bracket, we decrease it. While reading, the counter must stay at zero or above. And at the end, the counter should be zero, which means all brackets were properly closed.

*Wau, here I have to stop for a while. Previously I was working with java-like languages. The good thing about it was that I could completely ignore the new line character and replace it with just empty space. 
In the Python language a new line character means the end of a statement. 
Also, there are cases where the new line character can be ignored inside the parenthesized expression. 
Where are brackets for blocks? Long story short, I can't use the same approach as I used in my thesis. I have to figure out something new. Challenge accepted.*     

### Context-sensitive 
   What does the context mean for programming languages? At one place we are defining a variable. The variable has a name and a type. Later in code we can use the variable. From context, by the name we know the type of variable. The same with functions or classes.
    From a first look it could seem scary and complicated, but it's actually quite simple. At the first step we parse the code as it is a Context-free language (syntax analyze). Result of it is an Abstract Syntax Tree (AST) https://en.wikipedia.org/wiki/Abstract_syntax_tree
    Sematic analysis of the AST does the check if the context in the code is correct. We can traverse the AST, for example, by Visitor pattern 
 
## Syntax and sematic analysis
   Ok, let's put it all together. 
    What I have learned during working on my thesis is that by syntax analysis I do parsing of the code and create the AST. 
    As a next step, I do semantic analysis on the AST.
    During the syntax analysis I worked only with Context-free languages. 
    It is not a coincidence that I use a parse strategy similar as Finite-state automat does for Regular languages. 
    I don't have to remember anything, only the state where I am and the next state based on the character that I am reading now.
    No need to read the whole text at once, just linearly reading from left to right. 
    Based on the current character, I was able to decide in which state I am and where I am going to. 
    The solving the problem with open-close branches was even more simple. 
    No need to remember anything, the fact if the branch is open lies inside the stacktrace.
    To my surprise, with Python the situation is different and more complicated. 
    As mentioned before, there are different rules for new lines in case we are reading inside parenthesized expression. 
    But what is more interesting is the fact that Python syntax is a Context-sensitive language. 
    In blocks the parentheses are not required. 
    Instead, empty spaces are in use. 
    For the next statement by empty spaces at the beginning of the line, we decide if we are still inside the block or not.
    Now we have to remember more. 
    For each block we have to remember how many empty spaces are allowed for its statements.
    
   The question is, why the creator of Python did the syntax analysis in a different, mode complicated way? 
    Although those days we already had the knowledge how easily we can do syntax analyzes when the language is defined properly.
    I believe the answer is straightforward.
    The complexity of doing the syntax analyzes this way it's not so high, and it brings a benefit. 
    In the end, the code written in Python is more readable and easier to understand.

## Conclusion
   So far so good, but I am still at the beginning, although I am parsing language tokens. 
    Also, I break down syntax analyzes for expression. What's the hardest part.
    But what about my knowledge of learning Python?

   As _Luciano Ramalho_ in his book _Fluent Python_ mentioned. 
    Experienced programmers can start programing in Python in a few hours.
    So intuitive and user-friendly the Python language is.
    I do agree with him, and also I do agree that my code is not pythonic yet. 
    I just followed style and patterns from languages that I've learned before.
    Let's eat a little bit of theory, become more pythonic, and then I will definitely come back here to continue.

*To be continued ...*