# Matilda Cupcake Financials Script

A script that answer's financial questions about Matilda's cupcake company. 

## Project

You're working with an accountant named Arthur. Arthur has a client, Matilda.  Matilda is 68 years old and sells cupcakes.  Matilda is not a big fan of 
spreadsheets, accounting software, or computers in general really. Every so often Matilda sends Arthur three files:

- Basic.txt, Delux.txt, and Total.txt

Naturally, as any savvy business owner, Matilda wants to understand her business.  So she sends Arthur those files and wants to know: "How much money did I make 
last year? How much money do I make in a typical month?  Can you help, please? I do need your help,  I'm very busy baking cupcakes, and my arthritis flares 
up when I spend a whole day on the calculator."

To be totally honest, Arthur is not Matilda's biggest fan right now.  Arthur is glad he finally got her to type up this info and email it instead of faxing it, 
but she flat out won't do anything more complicated than this.

It could be worse, Matilda is a woman of routine:
- These documents never have dates, each line was entered on a different day.  
- The bottom-most row is always 'Today', the row above that is 'Yesterday', and so on.
- The files are always lined up perfectly, you never have to worry about them being 'out of sync' or anything like that.
- Basic.txt is the number of basic cupcakes she sold on that day, and they cost $5.  
- Deluxe.txt is the number of Deluxe cupcakes (they have sprinkles!) sold on that day, and they cost $6.  
- Total.txt is the total money she made (let's not even think about taxes yet, ugh).

Matilda every so often wants to know:
- Yearly Revenue Totals
- Monthly Revenue Totals
- Weekly Revenue Totals

I'll bet that this week you can code something up that will take these text files in and spit those answers out, whenever she asks.

If you want to get fancy, here's how you might take it even further:
- Break these stats down by item.
- Generate a graph of the data, Matilda loves charts
- Get creative with the input.  Maybe you can think of something she'll actually use.

Now, how are you going to attack this project? Everyone has a graveyard of unfinished projects, how are you going to make this one different? When you're working 
at a company, you've got this built in mechanism to force you to work on whatever you should be working on. For your own stuff, there's none of that.
Why work on your project when you could be relaxing? Or scrolling through HackerNews, or whatever your preferred method of
procrastination is. 

What's the best way to do that? Planning. 

Not that procrastination planning where you think about stuff and dream about how awesome it'll be. Real planning, where we make commitments and stuff. 
Let's dive in. 

### What

The first step is to decide what. Remember how I said we weren't going to dream about this finished product? I lied. Take a second and think 
about your perfect vision of this project. 

Now cut it in half. Take about half of the things in that vision, and just decide now not to do them. The reality is that in software, things always take 
longer than we anticipate. We almost always have to skip features at the end that we planned for, so why not do it in advance? We can always add them back 
in if we have time. 

This also includes spending time on stuff you don't know. Research is an important part of development, and it's OK to spend time on it. 

### When
The second step is to decide when. Think about the week ahead. If you use a calendar or a planner, get that in front of you. 

When is weekly project time? I sometimes catch myself thinking that something will happen "sometime this week". I've looked around, and I haven't found a 
calendar that has a box with that label. 

Take a minute and schedule some specific times to work on this project. It can just be a few minutes here and there, you don't have to be staying up late every 
night to get this done if you don't want to. A half hour 3 times a week is way more than none at all. 

If you aren't able to schedule as much time as you want, that's OK! Block out as much time as you can, and then go back to step one and cut out some more project. 

### Commit 

The third step is to commit.  Take your answers to the first two parts and put them in here. This is a crucial part of the process. It's really easy to let 
ourselves slip, but when you commit yourself to someone else, it kicks things up a notch. I read all of these submissions, and I have an idea of how these 
projects tend to go. If you don't take the time now and plan what, when, and commit, you won't submit anything this week. But if you do, it increases your 
chances dramatically. 

If you need some help at any point during the week, submit a help request here!  I'll try and connect you with a mentor or send you some resources.Good luck, 
I'll check in later this week!


## Project Breakdown

### Worksheet

***What does your finished project look like?***
A script that we can put in a crontab, lambda function or jenkins jobs that does the following:
1. Connects to a email (gmail) account, searches for Matilda's email, downloads the email attachments with Basic.txt, Delux.txt, and Total.txt
2. Parses the data in these Basic.txt, Delux.txt, and Total.txt files and put them in-memory
3. Then takes the in-memory data, run our calculations.
4. Finally it generates a email reports and sends it back to Matilda via email.

Assumptions:
- Matilda will only use email and nothing more. Per this detail "Arthur is glad he finally got her to type up this info and
email it instead of faxing it, but she flat out won't do anything more complicated than this." This assumes we can get
Matilda to email Arthur the files and that she will view the generates email. With this assumption the above process will
be automate.

***What do you need to learn before you start?***
- To learn how to connect to gmail API, (require gmail API dependencies in script, should be straight forward)
- To learn how to match up dates and numbers in the files.
- Determine if in-memory data parsing will work for this. If lots of data, a persistent model might work better.
`- RDS, write to file...etc.

***When will you spend time on your project?***
    - 3-4 times MWF evening this week.


### Minimum Requirements
- [ ] Answer: How much money did I make last year? (Yearly Revenue Totals)
- [ ] Answer: How much money do I make in a typical month? (Monthly Revenue Totals)
- [ ] Answer: How much money do I make in a typical week? (Weekly Revenue Totals)

### Extras / Optionals
- [ ] Break these stats down by item.
- [ ] Generate a graph of the data, Matilda loves charts
- [ ] Get creative with the input.  Maybe you can think of something she'll actually use.

### Components
- Authenticator




