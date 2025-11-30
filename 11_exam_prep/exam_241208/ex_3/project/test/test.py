from unittest import TestCase, main

from project.senior_student import SeniorStudent


class SeniorStudentTest(TestCase):
    def setUp(self):
        self.senior_student = SeniorStudent("1234", "John", 3.5)
    
    def test_init(self):
        self.assertEqual("1234", self.senior_student.student_id)
        self.assertEqual("John", self.senior_student.name)
        self.assertEqual(3.5, self.senior_student.student_gpa)
        self.assertEqual(set(), self.senior_student.colleges)
    
    def test_student_id_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.senior_student.student_id = "123"
        self.assertEqual("Student ID must be at least 4 digits long!", str(ex.exception))
        self.assertEqual("1234", self.senior_student.student_id)
    
    def test_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.senior_student.name = ' '
        self.assertEqual("Student name cannot be null or empty!", str(ex.exception))
        self.assertEqual("John", self.senior_student.name)
    
    def test_student_gpa_equal_to_one_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.senior_student.student_gpa = 1
        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))
        self.assertEqual(3.5, self.senior_student.student_gpa)
    
    def test_student_gpa_less_than_one_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.senior_student.student_gpa = 0
        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))
        self.assertEqual(3.5, self.senior_student.student_gpa)
    
    def test_apply_to_college_failed(self):
        result = self.senior_student.apply_to_college(4.0, 'abc')
        self.assertEqual("Application failed!", result)
    
    def test_apply_to_college_success(self):
        result = self.senior_student.apply_to_college(3.0, 'abc')
        self.assertEqual("John successfully applied to abc.", result)
        self.assertIn('ABC', self.senior_student.colleges)
        
        result = self.senior_student.apply_to_college(3.0, 'def')
        self.assertEqual("John successfully applied to def.", result)
        self.assertIn('ABC', self.senior_student.colleges)
        self.assertIn('DEF', self.senior_student.colleges)
    
    def test_update_gpa_failed(self):
        result = self.senior_student.update_gpa(1)
        self.assertEqual("The GPA has not been changed!", result)
        self.assertEqual(3.5, self.senior_student.student_gpa)
        
        result = self.senior_student.update_gpa(0)
        self.assertEqual("The GPA has not been changed!", result)
        self.assertEqual(3.5, self.senior_student.student_gpa)
    
    def test_update_gpa_success(self):
        result = self.senior_student.update_gpa(4.0)
        self.assertEqual("Student GPA was successfully updated.", result)
        self.assertEqual(4.0, self.senior_student.student_gpa)
    
    def test_student_equality(self):
        senior_student_2 = SeniorStudent("2345", "Peter", 3.5)
        result = self.senior_student == senior_student_2
        self.assertTrue(result)
        
        senior_student_2.student_gpa = 4.0
        result = self.senior_student == senior_student_2
        self.assertFalse(result)


if __name__ == '__main__':
    main()
