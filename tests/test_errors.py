# -*- coding: utf-8 -*-
"""
In these tests we'll make sure a GraphQL error is raised as well as
checking the message of those raised exceptions as well.

Scan all types and make a test for the errors! Remember to use `with
pytest.raises(graphql.GraphQLError)`

Check Pytest chapter 2 Testing for Expected Exceptions

"""


def test_simple():
    """
    Making a simple test for CI.
    """
    assert 1 == 1
