import requests
import unittest

class LoginTest(unittest.TestCase):
      def testlogin(self):
          url = "http://www.jasonisoft.cn:8080/HKR/UserServlet"
          data = {
              "method":"login",
              "loginname":"root11",
              "password":"1111111"
          }
          expect = "菜单"
          response = requests.get(url=url,data = data)
          response.encoding = "utf-8"
          data = response.text

          self.assertIn(expect,data)

      def testfindAllTeacher(self):
          url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllTeacher"
          data = {

          }
          #期望数据
          expect = 200
          #调用测试接口
          response = requests.get(url=url, data=data)
          response.encoding = "utf-8"

          #取出状态码和响应数据
          code = response.status_code
          txt = response.text

          #断言
          print(txt)
          self.assertEqual(expect,code)

      def testfindAllMenu(self):
          url = "http://www.jasonisoft.cn:8080/HKR/MenuServlet?method=findAllMenu"
          data = {

          }


          expect = 200

          response = requests.get(url=url, data=data)
          response.encoding = "utf-8"
          code1 = response.status_code
          txt1 = response.text

          print(txt1)
          self.assertEqual(expect, code1)

      def testfindAllStudent(self):
          url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllStudent"
          data = {

          }
          expect = 200

          response = requests.get(url=url, data=data)
          response.encoding = "utf-8"
          code2 = response.status_code

          self.assertEqual(expect, code2)




      def   testfindByUsername(self):

          url = "http://www.jasonisoft.cn:8080/HKR/TeacherServlet?method=findByUsername"
          data={

          }
          expect=200

          response = requests.post(url=url,data=data)
          response.encoding="utf-8"
          code3 = response.status_code

          self.assertEqual(expect,code3)


      def  testfindByUsernameAndPhone(self):

          url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findByUsernameAndPhone"
          data={"username":"jason",

                  "phoneNumber":""

          }
          ecpect = 200

          respone = requests.post(url=url,data=data)
          respone.encoding="utf-8"
          code4 = respone.status_code


          self.assertEqual(ecpect,code4)



      def testfindAllCourse(self):
          url = "http://www.jasonisoft.cn:8080/HKR/CourseServlet?method=findAllCourse"
          data = {

          }
          ecpect = 200
          respone = requests.post(url=url, data=data)
          respone.encoding = "utf-8"
          code5 = respone.status_code


          self.assertEqual(ecpect, code5)





