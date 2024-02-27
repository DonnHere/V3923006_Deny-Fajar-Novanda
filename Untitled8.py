#!/usr/bin/env python
# coding: utf-8

# In[16]:


name = "John Doe"  
message = "John Doe belajar bahasa python di Belajarpython"
print ("name[0]: ", name[0])


# In[17]:


message = 'Hello World'
print ("Updated String :- ", message[:6] + 'Python')


# In[20]:


#Cara mengakses nilai di dalam list Python
list1 = ['fisika', 'kimia', 1993, 2017]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])


# In[21]:


list = ['fisika', 'kimia', 1993, 2017]
print ("Nilai ada pada index 2 : ", list[2])
list[2] = 2001
print ("Nilai baru ada pada index 2 : ", list[2])


# In[22]:


#Contoh cara menghapus nilai pada list python
list = ['fisika', 'kimia', 1993, 2017]
print (list)
del list[2]
print ("Setelah dihapus nilai pada index 2 : ", list)


# In[23]:


#Cara mengakses nilai tuple
tup1 = ('fisika', 'kimia', 1993, 2017)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])


# In[24]:


tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
# Aksi seperti dibawah ini tidak bisa dilakukan pada tuple python
# Karena memang nilai pada tuple python tidak bisa diubah
# tup1[0] = 100;
# Jadi, buatlah tuple baru sebagai berikut
tup3 = tup1 + tup2
print (tup3)


# In[27]:


tup = ('fisika', 'kimia', 1993, 2017);
print (tup)
del tup;
print "Setelah menghapus tuple : "


# In[28]:


#Contoh cara membuat Dictionary pada Python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])


# In[29]:


#Update dictionary python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # Mengubah entri yang sudah ada
dict['School'] = "DPS School" # Menambah entri baru
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])


# In[30]:


#Contoh cara menghapus pada Dictionary Python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name'] # hapus entri dengan key 'Name'
dict.clear() # hapus semua entri di dict
del dict # hapus dictionary yang sudah ada
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])


# In[32]:


nama_lengkap = input ("Masukkan Nama Anda : ")

# menghitung jumlah huruf dari nama lengkap
jumlah_huruf = len(nama_lengkap.replace(" ",""))

# menghitung jumlah huruf vokal dari nama lengkap
huruf_vokal = "aiueoAUIEO"
jumlah_vokal = len({char for char in nama_lengkap if char in huruf_vokal})

# menghitung jumlah huruf konsonan dari nama lengkap
jumlah_konsonan = jumlah_huruf - jumlah_vokal

print("Jumlah huruf dari nama lengkap Anda adalah:", jumlah_huruf)
print("Jumlah huruf vokal dari nama lengkap Anda adalah:", jumlah_vokal)
print("Jumlah huruf konsonan dari nama lengkap Anda adalah:", jumlah_konsonan)


# In[ ]:




