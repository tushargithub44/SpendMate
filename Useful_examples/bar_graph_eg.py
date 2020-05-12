

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp','sfvcdf','ff','afdafda','fafa','afaf', 'fafda')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1,0,0,0,3,5,6]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.xlabel('Date')
plt.title('Programming language usage')
plt.show()
# plt.figure(figsize=(20,10))
