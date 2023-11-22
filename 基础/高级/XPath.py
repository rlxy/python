##xpath
#在xml文件中查找信息的一套规则/语言，根据XML的元素或者属性进行遍历
# https://www.w3school.com.cn/xpath/index.asp
#xpath 开发工具
# 开源的xpath表达式编辑工具 XMLQuire
#Chrome插件：XPath Helper
#Firefox插件 XPath Cheker

#选取节点
#nodename  选取此节点所有子节点
# / 从根节点开始选取
# // 选取节点，不考虑位置     一般组成列表返回
#. 选取当前节点
#.. 选取当前系欸但的父亲节点
#@ 选取属性
#xpath 中查找一般按照路径方法查找
'''
    school/teacher  返回所有名为的teacher节点
    //student  选取所有student的节点，不考虑位置
    school//age 选取school 后代中所有age系欸但那
    //@other  选取other属性
    //age[@detail] 选取带有属性detail的age元素
'''

#谓语 Predicates
# /School/Student[1]:选取school下面的第一个student节点
# /School/Student[last()]:选取school下面最后一个student节点
# # /School/Student[last()-1]:选取school下面倒数第二个student节点
# # /School/Student[position()<3]:选取school下面前二个student节点
# //School[@score]：选取带有属性score的student节点
# //School[@score='99']：选取带有属性score并且属性事99的student节点
# //School[@score]/Age：选取带有属性score的student节点的子节点Age

##Xpath的一些操作
# |：  或者
    #//Student[@score] | //Teacher : 选取带有属性score的Student节点和Teacher节点
# 其余不常见Xpath运算符号包括 +，-，*，div，>,<