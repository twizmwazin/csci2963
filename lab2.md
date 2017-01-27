Lab #2
=====

####Why it is important to choose a license
Choosing a license is critical to a project, as it gives clear permissions and
requirements of users and contributors. By using a license, the copyright
holder can encourage users to test the project and potentially recruit new
contributors. Additionally, a license can be used to protect the original
developer, by preventing users from holding the developer liable for any issues
that may occur during use of the software.

####Why a project without a license should be avoided
Without a license, users have no rights or permissions to use a piece of
software. Legally, the "default" license is "All rights reserved" by the
original author. Using an unlicensed project could lead to future lawsuits,
as the author does not explicitly state what the user can do.

####Why the Web beat Gopher
I fully agree with the argument made by the author. Any application or system
in widespread use would need a strong development effort behind this. While
this can occasionally be done by a single company, releasing source and
crowd-sourcing contributions and ideas allows a technology to expand and mature
much faster than a single company could manage internally. The world wide web,
Linux kernel, and Apache HTTP servers are all examples of this.

####Linux Kernel License Justification
The Linux kernel uses the GPLv2 for a handful of reasons. Linus Torvalds
believes that everyone should be able to share and adapt the kernel to their
own needs, at no cost. He chose the GPL over a more permissive license because
he also believes that in return for being able to use the kernel at no cost, it
is fair to ask that all changes be contributed back to the project, to improve
the kernel for everybody. When Stallman published the GPLv3 to address the
"Tivoization" issue, Torvalds was very much against the new license and stated
that Linux would not be adopting the new license (at the same time I'm not sure
it would have been possible, considering the many different copyright holders).
Torvalds believed that requiring distributors to make modifications installable
on the device is unnecessary, so long as the source is disclosed to potentially
be adopted upstream. This highlights a difference in beliefs between groups
such as the FSF and the OSI. The FSF is more concerned with individual
freedoms, while the OSI is more concerned with the pure technical benefits of
sharing source code freely.

####Example Project with License
Kevin's Counting Program, GPLv3

####Comparing Licenses
The GPL, LGPL, Apache, and BSD Licenses are all very different, and serve
different purposes. The GPL and LGPL serve similar purposes for different types
of projects. Both require sharing changes and improvements, which is best for
the common good, as everyone will be able to benefit from each others' work.
The main difference between the license is that the GPL is viral, and any
project linking with a GPL project must also be available under the GPL or a
compatible license. The Apache and BSD licenses (side note: there are numerous
BSD licenses, with fairy different terms, making it incredibly vague to group
them as if they were a single license.) are more favorable for companies.
Libraries released under similar permissive licenses can be used to build
larger applications. The Apache 2.0 License diverges from many other permissive
license including the 2-clause and 3-clause BSD licenses by including patent
clauses, which could be useful in certain projects. All of the mentioned
licenses are generally good for developers, as they impose no restrictions on
developers using the program or adding additional features.

####Project
I am not sure exactly what I want to do, although I'd like to improve the
usability of shells. Bash lacks built-in functionality, fish lacks a decent
plugin ecosystem, and zsh runs too slowly when fully configured. I think it
would be useful to create a new shell, perhaps using a less-used langauge (no
actual reason than for fun and learning) that has built-in functionality
similar to zsh and fish, while retaining POSIX compatibility. The benefit here
over zsh would be preformance, where autocompletion can be as powerful as fish,
and we can use a system language to extend functionality rather than shell
scripts. This kind of project would need an immense amount of research, but it
could become an impressively usable shell.

Website | License Present | License
---------|:----------|:-------
[Better eBinder](https://github.com/kburk1997/betterebinder) | Yes | MIT
[ChestShopPro](https://github.com/connection-lost/ChestShopPro) | Yes | GPLv3
[HoverZoom](https://github.com/extesy/hoverzoom) | Yes | MIT
[OpenJavascriptWhiteboard](https://github.com/paulsambolin/draw) | Yes | Apache 2.0
[Servo](https://github.com/servo/servo) | Yes | MPL 2.0
