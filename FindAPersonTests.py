import unittest
class Crowdmap(object):
	def get_all_posts_for(self,param):
		pass


class FindAPersonTests(unittest.TestCase):
	def setUp(self):
		self.crowdmap = Crowdmap()
		
	def test_getAllPostsForName(self):
		self.assertFalse(True)
			posts = self.Crowdmap.get_all_posts_for("Or")
			self.assertIn("Or",posts)