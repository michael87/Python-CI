"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from models import Projects


class PositiveTest(TestCase):
    def test_creating_user(self):
        """
        Always create the project with required parameters
        - Project name
        - Project owner
        - Project description
        """
        
        self.Project = Projects(
            project_name = "test message",
            account_id = 1,
            language = 'nl',
            present_languages = 'nl',
            has_attachment = True

        )
        self.M.save()
        self.assertEqual(1 + 1, 2)
