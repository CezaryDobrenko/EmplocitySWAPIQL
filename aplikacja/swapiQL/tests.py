from django.test import RequestFactory, TestCase
from graphene.test import Client

def execute_test_client_api_query(api_query, user=None, variable_values=None, **kwargs):
    """
    Returns the results of executing a graphQL query using the graphene test client.  This is a helper method for our tests
    """
    request_factory = RequestFactory()
    context_value = request_factory.get('/api/')  # or use reverse() on your API endpoint
    context_value.user = user
    client = Client(schema)
    executed = client.execute(api_query, context_value=context_value, variable_values=variable_values, **kwargs)
    return executed

class APITest(TestCase):
    def test_accounts_queries(self):
        # This is the test method.
        # Let's assume that there's a user object "my_test_user" that was already setup
        query = '''
        {
        user {
            id
            firstName
        }
        }
        '''
        executed = execute_test_client_api_query(query, my_test_user)
        data = executed.get('data')
        self.assertEqual(data['user']['firstName'], my_test_user.first_name)