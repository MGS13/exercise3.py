# Exercise 03: Calculating Values

## Learning Objectives
1. Students will understand how to use simple mathematical operators to calculate cumulative totals and subtotals
2. Students will be able to apply discount calculations to solve their problems briefs, using if statement selection and percentage based reductions in value
3. Students will be familiar with the `+=` and `*=` operators to add to existing variable vlues
4. Students will have experience of developing *2D lookups* to identify the value of an item as expressed in a table using two value, having practices the skill using *nested if* statements
5. Students will be able to perform simple analysis on large bodies of text using the simple `count()` method in different combinations
 
## Overview
This unit takes around two hours to complete, however the key aspects to this session are the first three sub sections, if you're struggling for time you can omit the text skills *but* be prepared to cover this if it comes up in the allocated NEA project.

The aim is to break down the process of calculation and demonstrate the process of decomposition and abstraction to the students so that they are able to approach any calculation that is given to them in an NEA situation.

Cost calculators follow both a one-and-done method, as well as a looping cumulative total calculator. The complexity of the cumulative total calculator is not too bad, but the logical complexity i.e. students understanding what they have to do, is usually a stumbling block - it would be with focusing on the differences between these two methods and what they can achieve with each.

Discount calculations are also quite a straightforward thing, but take time to explain and show what `+=` and `*=` are actually doing as these are key concepts going forward. You may have to explicitly teach the `round` method as this isn't a pre-requisite in most schemes of work, but it does simplify currency calculations enormously.

The lookup calculator is something that students often find overwhelming when in reality it's just a bunch of nested if statements, push the idea that nesting the if statements means that copy-and-paste is an option, if students were to use the naive way i.e. `if(this==that and other==thing)` then they would have to manually express every combination needed. The NEA is extremely time constrained so sell them on this idea.

The text calculation section is essentially reusing the `count` method but trying to develop students' problem solving skills and pointing out that most things that are asked for can be abstracted away to something that can be achieved with a simple command like `count` and some simple maths. To my knowledge this has only been used a few times by a few NEA variants but it is possible to see it crop up again.

## Delivering the content in class

1. ***Simple Cost Calculator*** (15 minutes) Model the builds of the different cost calculations, paying particular attention to how the cumulative calculation is different from a straight-up total and why that's important to understand the difference. Ask student to build their own version of each of the code samples.

2. ***Discount Calculation*** (20 minutes) Talk the students through how a discount is applied in the first scenario with some test data that you make up - students could work the discounts out independently without developing and code. Have a discussion about the time it takes to work it out, the change of an error happening and how turning this into an algorithm will make it more reliable and faster to calculate. Reintroduce the `+=` and `*=` operators and ask the students to demonstrate their knowledge of adding to variable values. Clarify the `round()` function, in particular the fact that it doesn't *change* the value unless you make an assignment manually, it just displays the data rounded. Ask the students to implement the code.

3. ***Lookup Calculator*** (25 minutes) Ask the students to manually identify the prices of a few items to get them to understand the basics. Consider the instanciated values and lead a discussion of why that is important. Consolidate the concept of nesting and make sure to push the idea that this means copy and pasting can reduce the amount of time needed to work on it. Ask students to build the code as this will shine a light on all the students that have been unsure about what the indentation was all about. Make time to put those students in an intervention group because they will struggle with that in the NEA.

4. ***Text Calculations*** (20 minutes) Demonstrate how the `count` command works with blocks of text - especially spaces. Immediately set the student to work on the examples and try and lead conversations about thinking around the problem and making use of the skills you've got to get the results you need. 

5. ***Task*** (40 minutes)  Students may need more time than this as there are some abstraction and logical thinking problems that some may get stuck with.


  