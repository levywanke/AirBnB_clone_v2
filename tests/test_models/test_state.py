#!/usr/bin/python3
"""
Defines the TestStateDocs class and related tests.
"""

from datetime import datetime
import inspect
import models
from models import state
from models.base_model import BaseModel
import pep8
import unittest
State = state.State

class TestStateDocs(unittest.TestCase):
    """Verifies the documentation integrity and style of the State class."""
    @classmethod
    def setUpClass(cls):
        """Sets up the test environment."""
        cls.state_f = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_state(self):
        """Checks if models/state.py conforms to PEP8 standards."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors (and warnings) detected in models/state.py.")

    def test_pep8_conformance_test_state(self):
        """Checks if tests/test_models/test_state.py complies with PEP8 standards."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors (and warnings) detected in tests/test_models/test_state.py.")

    def test_state_module_docstring(self):
        """Ensures state.py has a valid module docstring."""
        self.assertIsNot(state.__doc__, None,
                         "A docstring is missing for state.py.")
        self.assertTrue(len(state.__doc__) >= 1,
                        "A docstring is missing for state.py.")

    def test_state_class_docstring(self):
        """Ensures the State class has a valid docstring."""
        self.assertIsNot(State.__doc__, None,
                         "A docstring is missing for the State class.")
        self.assertTrue(len(State.__doc__) >= 1,
                        "A docstring is missing for the State class.")

    def test_state_func_docstrings(self):
        """Verifies the presence of docstrings in State methods."""
        for func in self.state_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

class TestState(unittest.TestCase):
    """Tests the functionality of the State class."""
    def test_is_subclass(self):
        """Checks if State is a subclass of BaseModel."""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_name_attr(self):
        """Checks if State has the 'name' attribute, and it's initialized properly."""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        if models.storage_t == 'db':
            self.assertEqual(state.name, None)
        else:
            self.assertEqual(state.name, "")

    def test_to_dict_creates_dict(self):
        """Checks if the to_dict method creates a dictionary with the proper attributes."""
        s = State()
        new_d = s.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in s.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Checks if the values in the dictionary returned from to_dict are correct."""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = State()
        new_d = s.to_dict()
        self.assertEqual(new_d["__class__"], "State")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], s.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], s.updated_at.strftime(t_format))

    def test_str(self):
        """Checks if the str method has the correct output."""
        state = State()
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))
