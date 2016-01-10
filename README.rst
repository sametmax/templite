Templite
==============

A light-weight, fully functional, general purpose Python templating engine that fits in one single file.

I'm not the author, credits go to Thimo Kraemer and Tomer Filiba. You can get the original source here_.

I'm just packaging it and making it available on pypi and github to give it visibility.

(If the authors want the repository ownership, please contact me)

Usage example::

    from templite import Templite

    template = r"""

    This template demonstrates the usage of Templite.

    Within the defined delimiters we can write pure Python code:

    ${
        def say_hello(name):
            write('Hello %s!' % name)
    }$

    And now we call the function: ${ say_hello('World') }$

    Escaped starting delimiter: $\{
    ${ write('Escaped ending delimiter: }\$') }$

    Also block statements are possible:

    ${ if x > 10: }$
    x is greater than 10
    ${ :elif x > 5: }$
    x is greater than 5
    ${ :else: }$
    x is not greater than 5
    ${ :end-if / only the starting colon is essential to close a block }$

    ${ for i in range(x): }$
    loop index is ${ i }$
    ${ :end-for }$

    ${ # this is a python comment }$

    Single variables and expressions starting with quotes are substituted
    automatically:
    Instead ${write(x)}$ you can write ${x}$ or ${'%s' % x}$ or ${"", x}$
    Therefore standalone statements like break, continue or pass
    must be enlosed by a semicolon: $\{continue;}\$

    To include another template, just call "include":
    ${ include('template.txt') }$
    """

    t = Templite(template)
    print t.render(x=8)



    """


Which outputs ::


    This template demonstrates the usage of Templite.

    Within the defined delimiters we can write pure Python code:



    And now we call the function: Hello World!

    Escaped starting delimiter: ${
    Escaped ending delimiter: }$

    Also block statements are possible:


    x is greater than 5



    loop index is 0

    loop index is 1

    loop index is 2

    loop index is 3

    loop index is 4

    loop index is 5

    loop index is 6

    loop index is 7




    Single variables and expressions starting with quotes are substituted
    automatically:
    Instead 8 you can write 8 or 8 or 8
    Therefore standalone statements like break, continue or pass
    must be enlosed by a semicolon: ${continue;}$

    To include another template, just call "include":
    This is the content of template.txt
.. _here: http://www.joonis.de/en/code/templite
