from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student1 = Student('John', {'Python': ['A'], 'JS': ['B', 'C']})
        self.student2 = Student('Mark')
    
    def test_init_with_courses(self):
        self.assertEqual('John', self.student1.name)
        self.assertEqual({'Python': ['A'], 'JS': ['B', 'C']},
                         self.student1.courses)
    
    def test_init_no_courses(self):
        self.assertEqual('Mark', self.student2.name)
        self.assertEqual({}, self.student2.courses)
    
    def test_enroll_existing_course(self):
        result = self.student1.enroll('Python', ['B', 'C'])
        self.assertEqual('Course already added. Notes have been updated.',
                         result)
        self.assertEqual({'Python': ['A', 'B', 'C'], 'JS': ['B', 'C']},
                         self.student1.courses)
    
    def test_enroll_new_course(self):
        result = self.student2.enroll('Python', ['A', 'B'], 'Y')
        self.assertEqual('Course and course notes have been added.', result)
        self.assertEqual({'Python': ['A', 'B']}, self.student2.courses)
    
    def test_enroll_new_course_with_empty_course_notes(self):
        result = self.student2.enroll('C#', ['A'], '')
        self.assertEqual('Course and course notes have been added.', result)
        self.assertEqual({'C#': ['A']}, self.student2.courses)
    
    def test_enroll_new_course_with_various_course_notes(self):
        result = self.student2.enroll('Python', ['A'], 'B')
        self.assertEqual('Course has been added.', result)
        self.assertEqual({'Python': []}, self.student2.courses)
    
    def test_add_notes_existing_course(self):
        result = self.student1.add_notes('Python', 'B')
        self.assertEqual('Notes have been updated', result)
        self.assertEqual({'Python': ['A', 'B'], 'JS': ['B', 'C']},
                         self.student1.courses)
    
    def test_add_notes_non_existing_course(self):
        with self.assertRaises(Exception) as e:
            self.student1.add_notes('C#', 'A')
        self.assertEqual('Cannot add notes. Course not found.',
                         str(e.exception))
    
    def test_leave_existing_course(self):
        result = self.student1.leave_course('Python')
        self.assertEqual('Course has been removed', result)
        self.assertEqual({'JS': ['B', 'C']}, self.student1.courses)
    
    def test_leave_non_existing_course(self):
        with self.assertRaises(Exception) as e:
            self.student2.leave_course('Python')
        self.assertEqual('Cannot remove course. Course not found.',
                         str(e.exception))
        self.assertEqual({}, self.student2.courses)


if __name__ == '__main__':
    main()
