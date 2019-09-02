from numpy import zeros
import matplotlib.pyplot as plt

h=zeros(4)
h[0]=1.6; h[1]=1.85; h[2]=1.75;h[3]=1.80

H=zeros(4)
H[0]=0.5; H[1]=0.6; H[2]=1.6; H[3]=1.85

family_member_no=zeros(4)
family_member_no[0]=0; family_member_no[1]=1; family_member_no[2]=2; family_member_no[3]=3

#plt.plot(family_member_no,h,family_member_no, H)
plt.plot(family_member_no,h,'*')

#plt.figure creates separate figures
#plt.figure()
plt.plot(family_member_no,H)
plt.legend(['h','H'])
plt.title('Height of two families')
plt.axis([0,3,0.3,2])

plt.savefig('someplot.png')
plt.savefig('someplot.pdf')
#plt.savefig('someplot.jpeg') fungerer ikke
plt.savefig('someplot.eps')

plt.xlabel('Family member number')
plt.ylabel('Height')
plt.show()