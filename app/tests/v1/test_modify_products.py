import unittest
from flask import json
from app import create_app


class TestModifyProducts(unittest.TestCase):
    """Tests for user modifying and deleting products"""

    def setUp(self):
        """Set up for configuration and testing env"""
        self.app = create_app('testing')
        self.test_client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.client = self.app.test_client()

        self.login_admin = json.dumps({
            "email": "brian@gmail.com",
            "password": "1234"})

        admin_login = self.client.post('/api/v1/login',data=self.login_admin,
          						content_type = 'application/json') 
        self.assertEqual(admin_login.status_code, 200)
        self.token_admin = json.loads(login_admin.data.decode()).get("x-api-key")

   
    def test_modify_product(self):

    	update_product = self.client.put('/api/v1/products/1', headers = dict(Authorization ="Bearer "+ self.token_admin),
    	 data=json.dumps({
    		"product_id":1,
    		"inventory":46
    		}), content_type= "application/json" ) 
    	result = json.loads(update_product.data.decode())
    	self.assertEqual(result['output':'product inventory updated'])
    	self.assertEqual(update_product.stats_code, 200)

    def test_delete_product(self):

    	delete_product = self.client.delete('/api/v1/products/1', headers = dict(Authorization ="Bearer "+ self.token_admin), 
    		data=json.dumps({
    		"product_id":1
    		
    		}), content_type="application/json")
    	result = json.loads(delete_product.data.decode())
    	self.assertEqual(result['output':'product has been deleted'])
    	self.assertEqual(delete_product.stats_code, 200)


