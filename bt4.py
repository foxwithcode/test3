#!/usr/bin/env python
# coding: utf-8

# In[3]:


def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
def main():
    input_string = input("Nhập chuỗi cần kiểm tra: ")
    if is_palindrome(input_string):
        print("Chuoi doi xung.")
    else:
        print("Chuoi khong doi xung.")
    
main()

