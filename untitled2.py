import string
puncs = string.punctuation

phrase = 'purple cow'
story = 'Purple cows are cool!'


### where I left of:
### lin 12 'in' doesn't work for this example

for punc in puncs:    
    if punc in story:
        story = story.replace(punc, ' ')

spcae_char = ' '        
sp_story = story.split()
final_story = spcae_char.join(sp_story)

print(final_story)

def is_phrase_in(phrase, story):
    if phrase in story.lower():
        return True
    return False
#
print(is_phrase_in('purple cow ', 'PURPLE COW'))



#txt = "banana         "
#
#x = txt.strip()
#
#print("of all fruits", x, "is my favorite")



# Story : lower(), 




## .join() with lists
#numList = ['1', '2', '3', '4']
#separator = ', '
#print(separator.join(numList))
#
## .join() with tuples
#numTuple = ('1', '2', '3', '4')
#print(separator.join(numTuple))
#
#s1 = 'abc'
#s2 = '123'
#
## each element of s2 is separated by s1
## '1'+ 'abc'+ '2'+ 'abc'+ '3'
#print('s1.join(s2):', s1.join(s2))
#
## each element of s1 is separated by s2
## 'a'+ '123'+ 'b'+ '123'+ 'b'
#print('s2.join(s1):', s2.join(s1))