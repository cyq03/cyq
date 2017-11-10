＃！/ usr / bin / python
＃ -  *  - 编码：UTF-8  -  *  -
 
班 学生：
   '所有学生的基类'
   stuCount =  0 
 
   def  __init__（self，stu_no，name，stu_class，gender）：
      self .stu_no = stu_no
      self .name = name
      self .stu_class = stu_class
      自我 .gender =性别
      Student.stuCount + =  1
   
   def  study（self）：
       打印 “学生可以学习”
       
   def  getStuCount（self）：
      返回 Student.stuCount

班级 PrimaryStudent（学生）：
   primaryStuCount =  0
   
   def  canRecite（self）：
        打印 “小学生可以背诵”

   def  canOral（self）：
        打印 “小学生可口语”


班级 MiddleStudent（学生）：
   middleStuCount =  0

   def  __init__（self，stu_no，name，stu_class，gender）：
      self .stu_no = stu_no
      self .name = name
      self .stu_class = stu_class
      自我 .gender =性别
      MiddleStudent.middleStuCount + =  1


   def  canChemistry（self）：
      打印 “中学生能化学”

   def  canPhyics（self）：
      打印 “中学生可以物理化学”
