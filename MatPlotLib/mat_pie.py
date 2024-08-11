import matplotlib.pyplot as plt

values1=[1000,7000,2000]
labels1=['Home','College','Extra']

values2=[90,75,83,41]
labels2=['Maths','Science','History','Sanskrit']

fig, axs = plt.subplots(2, 1)    #2 rows and 1 column

#if i dont provide labels it will throw error
axs[0].pie(values1,labels=labels1,colors=['g','blue','grey'],autopct='%0.2f%%',radius=1.5,textprops={'size': 'smaller'})
axs[1].pie(values2,labels=labels2,radius=1,autopct='%0.2f%%',explode=[0.2,0,0,0])
plt.show()