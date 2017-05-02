Lab 11
=====

##Bullet 1:
The meeting presented in part 1 was interesting. It was an old meeting for a
project known as "MouseTrap." For their meeting they used an IRC bot called
"meetbot" that assisted in taking notes for the metting. Comparing it to the
general channel in slack, it is much more organized. This seems to be mostly
because it was a meeting. The general channel in slack is a mix of fairly minor
announcements and occasonally people asking questions.

The wiki says to join the a11y channel on irc.gnome.org, however not a single
message was sent (besides the usual join/leave messages) over the 48 hour
period I was in the channel.

##Bullet 2:
1. Above
2. [titanpad](images/titanpad.png)
4. Synchronous and asynchronous communication are very commonly used in opne
source projects. Synchronous  communication, like IRC, works very well for
users who are online at the same time, and when possible is the fastest form of
online comunication. Asynchronous communication, like email, is a fantastic
way for different people in different timezones to communicate. Email is
available to all users, so it is a fairly universal standard.

Human-computer interaction is entirely different from group interaction. In the
first case, you are directing a computer to do something for you, even if it is
ultimatly to deliver a messange to another human being. Group interaction is
more dynamic and less well defined, with many people sending messages back and
forth, and there is not nessisarily a main speaker or controller.

The main issues around collaborative software development stem from old beliefs
in computer science, that project groups should be small and contained. This
subject has been the attention of multiple books and papers, most notably Eric
S. Raymond's ***The Cathedral and the Bazzar***. Large projects seen thoughout
the open source community have proven that large projects with tens, hundreds,
or even thousands of developers can be incredibly successful, through the use
of good documentation and communication.

This question seems incredibly vague, although I will assume that the question
is asking about how HCI through user interfaces affects human interaction.
Human interaction through computers is dictated by the medium on which they
communicate. For example, those choosing to use realtime communication serives
like IRC will have quick response times, which allows smaller questions and
answers to be fired off. The downside to this commuication is that it requires
all participants to be online at the same time to truly reap the benefits. In
contrast, a form of communication like email will have a higher latency between
participants, but will allow longer, more thoughtful interaction that can be
acted on at any time by participants and still remain useful.

##Bullet 3:
 - Pigeon
 - https://github.com/twizmwazin/Pigeon
 - A web application to deliver messages
 - To present information from various online sources in a clear and consise
   manner.
 - Most communication is done through slack.

 The behavior on the RCOS slack is fairly laid back. There are different
 channels that have different levels of professionality. The announcement
 channels tend to be more professional, meanwhile general channels tend to be
 much more laid back.

##Bullet 4:
Questions:
 - What is a code style guide?
 - Can one style guide be ideal or all projects?
 - How can a code style help imporve communication?
 - In what way do code styles help find errors?
 - What tools exist to help enforce a code style?

 A style guide can be highly specific or more general. A code style guide is
 used to ensure consistancy among the code of a software project. Most
 companies and projects have public style guides, including Google, Mozilla,
 JQuery, GNU, Linux, FreeBSD, etc. A single style guide cannot be used
 universally, as shown by the many guides listed before. First and foremost, 
 there is the issue of multiple languages. A single guide for C can't directly
 apply to Python, as the languages are very different. Atop that, individuals
 have personal preferences. See Tabs vs Spaces (2 spaces is correct, all else
 is completly wrong).

 When a project uses a consistent code style, it the code is more legible and
 is able to be more clearly understood by all developers, and therefore
 facilitate communication. Siminarly, consistant style help make errors more
 prominent as many developers can easily read and review the code.

 There are many tools to help check and enfore a style. Both Sun Microsystems
 (now Oracle) and Google have made checkstyle tools for Java. Tools like clang
 provide checking for C-family languages. ESlint is one of the many (many)
 options for Javascript. Most popular languages have some sort of code style
 enforcement that can be integrated with build and deployment systems.

After watching the style video, I have to say it was a very mundane watch. As
much as I love and obsess over practicing good styling of code (just as anyone
I've ever worked on a project with), I can't quite find entertainment in an
hour of discusing trivial things that a style guide can sometimes prevent. That
aside, I don't disagree with any points made by the speaker, however many of
them are trivial and I don't feel they are really the important points to
having a style guide.
