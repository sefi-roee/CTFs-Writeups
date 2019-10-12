# Problem
I wrote you another [song](https://2019shell1.picoctf.com/static/c7fa1eda3444e700dfd8addb3cf8e806/lyrics.txt). Put the flag in the picoCTF{} flag format

## Hints:

## Solution:

Let's download it and take a look:
```bash
wget https://2019shell1.picoctf.com/static/c7fa1eda3444e700dfd8addb3cf8e806/lyrics.txt
cat lyrics.txt

Rocknroll is right              
Silence is wrong                
A guitar is a six-string        
Tommy's been down               
Music is a billboard-burning razzmatazz!
Listen to the music             
If the music is a guitar                  
Say "Keep on rocking!"                
Listen to the rhythm
If the rhythm without Music is nothing
Tommy is rockin guitar
Shout Tommy!                    
Music is amazing sensation 
Jamming is awesome presence
Scream Music!                   
Scream Jamming!                 
Tommy is playing rock           
Scream Tommy!       
They are dazzled audiences                  
Shout it!
Rock is electric heaven                     
Scream it!
Tommy is jukebox god            
Say it!                                     
Break it down
Shout "Bring on the rock!"
Else Whisper "That ain't it, Chief"                 
```

Again, we just use the [online interpreter](https://codewithrockstar.com/online) for this. Oh, it waits input :(
![screenshot-1](./screenshot-1.png)

We must understand what happens...
```python
Rocknroll = True                # Rocknroll is right              
Silence   = False               # Silence is wrong                
A guitar  = 136                 # A guitar is a six-string        
Tommy     = 44                  # Tommy's been down               
Music     = 1970                # Music is a billboard-burning razzmatazz!
music     = input()             # Listen to the music             
if music == 136:                # If the music is a guitar                  
    print "Keep on rocking!"    # Say "Keep on rocking!"                
rhytem    = input()             # Listen to the rhythm
if rhytem - 1970 == 0:          # If the rhythm without Music is nothing
    Tommy = 66                  # Tommy is rockin guitar
print Tommy                     # Shout Tommy!                    
Music = 79                      # Music is amazing sensation 
Jamming = 78                    # Jamming is awesome presence
print Music                     # Scream Music!                   
print Jamming                   # Scream Jamming!                 
Tommy = 74                      # Tommy is playing rock           
print Tommy                     # Scream Tommy!       
They = 79                       # They are dazzled audiences                  
print They                      # Shout it!
Rock = 86                       # Rock is electric heaven                     
print Rock                      # Scream it!
Tommy = 73                      # Tommy is jukebox god            
print Tommy                     # Say it!                                     
                                # Break it down
                                # Shout "Bring on the rock!"
                                # Else Whisper "That ain't it, Chief"   
```


And using a simple script:
```python
#!/usr/bin/env python

r = [66, 79, 78, 74, 79, 86, 73]

print 'picoCTF{{{}}}'.format(''.join(map(chr, r)))
```

*Maybe sometime, I will solve it by myself...*

Flag: picoCTF{BONJOVI}
