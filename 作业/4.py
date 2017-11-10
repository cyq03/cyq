＃！/ usr / bin / python
＃ -  *  - 编码：UTF-8  -  *  -
 
班 学生：
   '所有学生的基类'
   男=  0
   stu_count =  0
   stu_count_nan =  0
   stu_count_nv =  0
 
   def  __init__（self，stu_no，name，stu_class，male）：
      self .stu_no = stu_no
      self .name = name
      self .stu_class = stu_class
      自我。男=男
      Student.stu_count + =  1
      如果 self .male ==  ' 1 '：
         Student.stu_count_nan + =  1
      elif  self .male ==  ' 0 '：
         Student.stu_count_nv + =  1
         
   
   def  displayCount（self）：
       打印 “ Count：”，Student.stu_count
 
   def  displayStudent（self）：
       打印 “ Stu_no： ”，自 .stu_no， “名称：”，自我 .name和“ Stu_class： ”，自 .stu_class， “男：”，   自我。男
 
