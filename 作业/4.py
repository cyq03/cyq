����/ usr / bin / python
�� -  *  - ���룺UTF-8  -  *  -
 
�� ѧ����
   '����ѧ���Ļ���'
   ��=  0
   stu_count =  0
   stu_count_nan =  0
   stu_count_nv =  0
 
   def  __init__��self��stu_no��name��stu_class��male����
      self .stu_no = stu_no
      self .name = name
      self .stu_class = stu_class
      ���ҡ���=��
      Student.stu_count + =  1
      ��� self .male ==  ' 1 '��
         Student.stu_count_nan + =  1
      elif  self .male ==  ' 0 '��
         Student.stu_count_nv + =  1
         
   
   def  displayCount��self����
       ��ӡ �� Count������Student.stu_count
 
   def  displayStudent��self����
       ��ӡ �� Stu_no�� ������ .stu_no�� �����ƣ��������� .name�͡� Stu_class�� ������ .stu_class�� ���У�����   ���ҡ���
 
