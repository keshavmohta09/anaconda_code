import matplotlib.pyplot as plt, numpy as np
arr1 = np.arange(1,11)
arr2 = arr1*8
# plt.plot(arr1,arr2,'r--')
# plt.plot([1,5,8,9,10],[3,9,10,11,12],'r--')
# plt.xlabel('No. of cows')
# plt.ylabel('Milk in l.')
# plt.title('Graph between no. of cows and milk in l.')
# plt.show()
# plt.subplot(2,1,1)
# plt.plot(arr1,arr2,'r--')
#
# plt.subplot(2,1,2)
# plt.plot(arr2,arr1,'b--')
#
# plt.show()


'''OO method'''
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axess = fig.add_axes([0.17,0.54,0.3,0.3])
axes.plot(arr1,arr2,'.')
axess.plot(arr1,arr2,'.')
plt.savefig('graph.png',dpi=500)
plt.show()