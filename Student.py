class Student:
    student_id__ = 0
    def __init__(self, name, age):
        Student.student_id__ += 1
        if not (self._cheack_age(age) and self._cheack_name(name)):
            raise ValueError()
        self.m_name = name
        self.m_age = age
    def get_name(self):
        return self.m_name
    def get_age(self):
        return self.m_age
    def get_id(self):
        return self.student_id__
    def set_name(self, name):
        if not self._cheack_name(name):
            raise ValueError()
        self.m_name = name
    def set_age(self, age):
        if not self._cheack_age(age):
            raise ValueError()
        self.m_age = age
    @staticmethod
    def _cheack_name(name):
        list_name = name.split()
        for i in range(len(list_name)):
            list_name[i:i+1] = list_name[i].split('-')
        for i in list_name:
            if not i.isalpha():
                return False
        return True
    @staticmethod
    def _cheack_age(age):
        if age <= 0:
            return False
        return True
