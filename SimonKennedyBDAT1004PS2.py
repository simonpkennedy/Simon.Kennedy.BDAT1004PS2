#!/usr/bin/env python
# coding: utf-8

# Problem Set 2
# Question 1
# 
# When the last expression (a) is evaluated, the value 6 is displayed.
# When the first function b() is executed, 2 is added to the value of variable a which is set to 0. 0+2=2
# When the second function b() is executed, 2 is added to the current value of a at 2. 2+2=4
# when the third function b() is executed, 2 is added to the current value of a at 4. 4+2=6

# Problem Set 2
# Question 2

# In[2]:


class myError(Exception):
    pass
raise myError('Filename not found.')


# Problem Set 2
# Question 3
# Part 1

# In[ ]:


class Marsupial


# Problem Set 2
# Question 3
# Part 2

# In[ ]:


class Marsupial
    class Kangaroo


# Problem Set 2
# Question 4

# In[ ]:


def collatz(x):
    
    collatzlist=[x]
    
    if x == 1 :
        return[1]
    
    elif x%2==0:
        collatzlist.append(collatz(n//2))
        
    else:
        collatz.append(collatz(3*x+1))
        
    return collatzlist
collatz(10)


# Problem Set 2
# Question 5

# In[35]:


def binary(n):
    
    if (n>0):
        binary((int)(n/2))
        print(n%2, end='')
              
n = int(input('Please enter a positive integer value: '))
print ('Your number in binary is: ', end='')
binary(n)


# Problem Set 2
# Question 6

# In[ ]:





# Problem Set 2
# Question 7

# In[ ]:





# Problem Set 2
# Question 8

# In[ ]:





# Problem Set 2
# Question 9 a)

# In[45]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

for w in range(len(words)):
    
    words[w]=words[w].upper()
    
print(words)


# Problem Set 2
# Question 9 b)

# In[47]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

for w in range(len(words)):
    
    words[w]=words[w].lower()
    
print(words)


# Problem Set 2
# Question 9 c)

# In[86]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

for w in(words):

    wordlen=len(w)
    
    print(wordlen, end=' ')


# Problem Set 2
# Question 9 d)

# In[93]:


words1 = ['THE', 'QUICK', 'BROWN', 'FOX', 'JUMPS', 'OVER', 'THE', 'LAZY', 'DOG']
words2 = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
words3 = [3, 5, 5, 3, 5, 4, 3, 4, 3]

words4 = words1 + words2 + words3
print(words4)


# Problem Set 2
# Question 9 e)

# In[62]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

for w in (words):
    
    wordlen=len(w)
    
    if wordlen >= 4:
        print(w, end=' ')

