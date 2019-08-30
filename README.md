# SummerProject
Code repository for my summer project - a Django-powered poetry analysis web application.

SCANSION 

Scansion analyses any text enterred by a user and identifies any regular usage of poetic meter. It does this by parsing the text into
syllables and identifying if those syllables are stressed or unstressed, using the PROSODIC Python library developed by Ryan Heuser, 
Josh Faulk, and Arto Antilla (the GitHub repository for that project can be found here: https://github.com/quadrismegistus/prosodic).

Some text-edited features have also been implemented to allow users to understand how individual word choices can affect the overall
meter of a given line. 

Test files have been provided to test the accuracy of Scansion's identifications. They can be added to, as long as each poem is separated
by two blank lines, and the first line of the new entry is the expected poetic meter. Scansion will return if the two match, and what 
Scansion identified the meter as if it did not find a exact match. 

This project was completed as part of a MSc in Software Engineering at the University of Glasgow in 2019. 

An up to date requirements file is contained in 'requirements.txt'. Once you have downloaded the code repository into a virtual environment, 'pip install -r requirements.txt' should install the relevant packages needed to run Scansion. 




