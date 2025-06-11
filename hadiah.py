#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import sys

def type_slow(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def love_ascii():
    art = """
     .:::.   .:::.
    :::::::.:::::::
    :::::::::::::::
    ':::::::::::::'
      ':::::::::'
        ':::::'
          ':'
    """
    print(art)

# Awal
type_slow("Hai kamu... 😊")
time.sleep(1)
type_slow("Aku cuma mau bilang satu hal yang penting...", 0.07)
time.sleep(1.5)

# ASCII Heart
love_ascii()
time.sleep(1)

# Isi pesannya
type_slow("Sejak kenal kamu, hariku lebih berwarna~ 🌈")
type_slow("Aku suka cara kamu tersenyum,")
type_slow("cara kamu bicara, bahkan caramu diam... 😳")
time.sleep(1.5)
type_slow("Jadi...")
time.sleep(1)

# Pertanyaan
type_slow("Maukah kamu jadi pacarku? 💌 (y/n) ", 0.07)

# Respons
jawab = input().strip().lower()

if jawab == 'y':
    type_slow("YEAY!! 🎉 Aku seneng banget! 🤍", 0.07)
else:
    type_slow("Gak apa-apa... yang penting aku udah jujur. ☁️", 0.07)


# In[ ]:




