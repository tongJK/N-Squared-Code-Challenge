import json
import string
import random
from faker import Faker

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Schools, Students


class SchoolsViewSetTestCase(APITestCase):

    def setUp(self):

        self.schools_1 = Schools(sc_name="Rose Garden School", sc_max_st=100)
        self.schools_1.save()

        self.schools_2 = Schools(sc_name="prepare udom", sc_max_st=200)
        self.schools_2.save()

    def test_school_creation(self):

        data = {"sc_name": "Dorm Palace", "sc_max_st": 120}

        response = self.client.post('/schools/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["sc_name"], 'Dorm Palace')
        self.assertEqual(Schools.objects.count(), 3)
        self.assertEqual(Schools.objects.last().sc_name, 'Dorm Palace')

    def test_all_schools_detail_retrieve(self):
        response = self.client.get("/schools/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_one_school_detail_retrieve(self):
        response = self.client.get(f'/schools/{self.schools_2.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["sc_name"], 'prepare udom')

    def test_school_update(self):
        response = self.client.patch(f'/schools/{self.schools_1.id}/', {"sc_name": "Dorm Palace"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'sc_name': 'Dorm Palace', 'sc_max_st': 100})

    def test_school_delete(self):
        response = self.client.delete(f'/schools/{self.schools_2.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class StudentsViewSetTestCase(APITestCase):

    def setUp(self):

        self.schools_1 = Schools(sc_name="Rose Garden School", sc_max_st=100)
        self.schools_1.save()

        self.schools_2 = Schools(sc_name="prepare udom", sc_max_st=200)
        self.schools_2.save()

        self.fake = Faker()

        self.fake_name_1 = self.fake.name()
        self.students_1 = Students(st_first_name=self.fake_name_1.split(' ')[0],
                                   st_last_name=self.fake_name_1.split(' ')[1],
                                   st_ident=''.join(random.choices(string.digits, k=6)),
                                   st_school=Schools.objects.get(id=self.schools_1.id))
        self.students_1.save()

        self.fake_name_2 = self.fake.name()
        self.students_2 = Students(st_first_name=self.fake_name_2.split(' ')[0],
                                   st_last_name=self.fake_name_2.split(' ')[1],
                                   st_ident=''.join(random.choices(string.digits, k=6)),
                                   st_school=Schools.objects.get(id=self.schools_1.id))
        self.students_2.save()

    def test_student_creation(self):

        self.fake_name_3 = self.fake.name()
        data = {"st_first_name": self.fake_name_3.split(' ')[0],
                "st_last_name": self.fake_name_3.split(' ')[1],
                "st_school": self.schools_1.id}

        response = self.client.post('/students/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["st_first_name"], self.fake_name_3.split(' ')[0])
        self.assertEqual(Students.objects.count(), 3)
        self.assertEqual(Students.objects.last().st_first_name, self.fake_name_3.split(' ')[0])

    def test_all_students_detail_retrieve(self):
        response = self.client.get("/students/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_one_student_detail_retrieve(self):
        response = self.client.get(f'/students/{self.students_1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["st_first_name"], self.students_1.st_first_name)

    def test_school_update(self):
        response = self.client.patch(f'/students/{self.students_1.id}/', {"st_first_name": "Sinister",
                                                                          'st_last_name': 'Tong'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'st_first_name': 'Sinister',
                                                        'st_last_name': 'Tong', 'st_school':
                                                            self.students_1.st_school.id})

    def test_school_delete(self):
        response = self.client.delete(f'/students/{self.students_2.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
