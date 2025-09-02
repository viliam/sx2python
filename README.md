## About

In high school, I enrolled in a course on programming in Assembler. On the first day, the teacher told us: 'With Assembler, you can earn millions—or nothing. It's unlikely that Intel will hire you to design new CPU processors, so the 'nothing' is probably your path.’

With syntax and semantic analysis, the situation is similar. It's perhaps even less likely that you'll design a new language that the market will accept and adopt.

So why am I reopening my thesis and reworking it? Maybe because it makes me happy—and yes, I do have fun. That could be it. But the answer is different and simpler: knowledge. By rewriting my thesis code in a new language, I can prove to myself (and to potential clients) that I have a deep understanding of the language and can solve complex problems with it.

How can you become more familiar with a language like Python than by writing a syntax analyzer in Python—for Python? Next steps would be Kotlin and GoLang.

## Theory

Before we jump into it, let's take a quick look at the theory.

https://en.wikipedia.org/wiki/Chomsky_hierarchy

We have four types of languages: Regular, Context-free, Context-sensitive, and Recursively Enumerable. For our purposes, we will be working with the first three types.

### Regular 
Regular language is the simplest type; we can think of it as a linear language. For example, it can be used to define the grammar of a function.

FUNCTION →  “def” , NAME, ARGUMENTS, RETURN_TYPE, BODY

All functions in Python start with the reserved word def, followed by the name of the function. Next, we define the function's arguments, data type of return value and body of function. When reading sentences in a regular language, we don’t need to remember much—just the last word we read. As we read from left to right, like humans naturally do, we can predict what kind of word will follow the one we've just read. No surprises.

### Context-free 
  Context-free languages are an extension of regular languages. This means all regular languages are also context-free, but the reverse is not true. Some context-free languages do not belong to the category of regular languages.
  What’s new? Mathematical brackets. Each time we open a bracket, we need to close it somewhere. We can still read the language linearly, but when we encounter a closing bracket, we somehow need to remember whether we’ve seen an opening bracket before. And by the end, we must ensure that all brackets have been properly closed.
  To achieve that, a simple counter can help us. Each time we read an opening bracket, we increase the counter. When we read a closing bracket, we decrease it. While reading, the counter must stay at zero or above. And at the end, the counter should be zero, which means all brackets were properly closed.

### Context-sensitive 

  *To be continued ...*