Templite
==============

A light-weight, fully functional, general purpose Python templating engine that fits in one single file.

I'm am not the author, credits go to Thimo Kraemer and Tomer Filiba. You can get the original source _here.

I'm just packaging it and making it available on pypi and github to give it visibility.

Usage example :

```
from templite import Templite

template = r"""
This we already know:
<html>
    <body>
        ${
        def say_hello(arg):
            emit("hello ", arg, "<br>")
        }$

        <table>
            ${
                for i in range(10):
                    emit("<tr><td> ")
                    say_hello(i)
                    emit(" </tr></td>\n")
            }$
        </table>

        ${emit("hi")}$

        tralala ${if x > 7:
            say_hello("big x")}$ lala

        $\{this is escaped starting delimiter

        ${emit("this }\$ is an escaped ending delimiter")}$

        ${# this is a python comment }$

    </body>
</html>

But this is completely new:
${if x > 7:}$
    x is ${emit('greater')}$ than ${print x-1}$ Well, the print statement produces a newline.
${:else:}$
 This terminates the previous code block and starts an else code block
 Also this would work: $\{:end}\$$\{else:}\$, but not this: $\{:end}\$ $\{else:}\$
${:this terminates the else-block
only the starting colon is essential}$

So far you had to write:
${
    if x > 3:
        emit('''
            After a condition you could not continue your template.
            You had to write pure python code.
            The only way was to use %%-based substitutions %s
            ''' % x)
}$

${if x > 6:}$
    With Templite+ it does not break your template ${print x}$
${:elif x > 3:}$
    This is great
${:endif}$

${for i in range(x-1):}$  Of course you can use any type of block statement ${i}$ ${"fmt: %s" % (i*2)}$
${:else:}$
Single variables and expressions starting with quotes are substituted automatically.
Instead $\{emit(x)}\$ you can write $\{x}\$ or $\{'%s' % x}\$ or $\{"", x}\$
Therefore standalone statements like break, continue or pass
must be enlosed by a semicolon: $\{continue;}\$
The end
${:end-for}$
"""

t = Templite(template)
print t.render(x=8)
```

Which outputs :

```
This we already know:
<html>
    <body>


        <table>
            <tr><td> hello 0<br> </tr></td>
<tr><td> hello 1<br> </tr></td>
<tr><td> hello 2<br> </tr></td>
<tr><td> hello 3<br> </tr></td>
<tr><td> hello 4<br> </tr></td>
<tr><td> hello 5<br> </tr></td>
<tr><td> hello 6<br> </tr></td>
<tr><td> hello 7<br> </tr></td>
<tr><td> hello 8<br> </tr></td>
<tr><td> hello 9<br> </tr></td>

        </table>

        hi

        tralala hello big x<br> lala

        ${this is escaped starting delimiter

        this }$ is an escaped ending delimiter



    </body>
</html>

But this is completely new:

    x is greater than 7
 Well, the print statement produces a newline.


So far you had to write:

        After a condition you could not continue your template.
        You had to write pure python code.
        The only way was to use %-based substitutions 8



    With Templite+ it does not break your template 8



  Of course you can use any type of block statement 0 fmt: 0
  Of course you can use any type of block statement 1 fmt: 2
  Of course you can use any type of block statement 2 fmt: 4
  Of course you can use any type of block statement 3 fmt: 6
  Of course you can use any type of block statement 4 fmt: 8
  Of course you can use any type of block statement 5 fmt: 10
  Of course you can use any type of block statement 6 fmt: 12

Single variables and expressions starting with quotes are substituted automatically.
Instead ${emit(x)}$ you can write ${x}$ or ${'%s' % x}$ or ${"", x}$
Therefore standalone statements like break, continue or pass
must be enlosed by a semicolon: ${continue;}$
The end
```

.. _here: http://www.joonis.de/en/code/templite
