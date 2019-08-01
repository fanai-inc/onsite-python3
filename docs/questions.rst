==========
Question 1
==========

Given a list::

    mylist = list(range(1_000_000))

What is a concern with trying to remove items from the front?::

    for x in range(1000):
        mylist.pop()

What would be a better alternative and why?


==========
Question 2
==========

I have a function in a utility module::

    # util.py
    def add_to(mylist, otherlist):
        for item in otherlist:
            mylist.apppend(item)

I have diagnosed a heavy bottleneck when calling this function with
extremely large arguments.  Why?::

    one, two = list(range(1_000_000)), list(range(5_000_000))
    util.add_to(one, two)  # really slow
