print('考试成绩判断')
grade =input('请输入你的分数：')
grade = int (grade)
if 100 >= grade >=90 :
    print('优秀')
elif 90 > grade >= 80 :
    print('良')
elif 80 > grade >= 70 :
    print('中')
elif 70 > grade >= 60 :
    print('平')
elif grade < 60 :
    print('不及格')
else :
    print('请输入一个正确的分数')