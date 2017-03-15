import unittest
import pointingutils as point
import numpy as np

class pointingutilstests(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

class test_rigid_body_kinematics(pointingutilstests):

	def test_output(self):
	
		# Set up inputs
		quaternion   = np.array([0,0,0,1])
		angular_rate = np.array([0,0,0])
		
		# Call method
		deriv = point.rigid_body_kinematic(quaternion, angular_rate)
		   
		# Check dimensions and type
		self.assertEqual(len(deriv), 7, 
												 "Incorrect output dimension.")
		self.assertTrue(type(deriv) is np.ndarray, "Incorrect output type.")
													  
		# Check values
		self.assertTrue( np.array_equal(deriv, np.array([0,0,0,0,0,0,0])), 
													 "Incorrect output value.")
        
class test_quaternion2dcm(pointingutilstests):

    def test_types(self):
        
        # 
        quaternion      = np.array([0,0,0,1])
        quaternion_list = [ quaternion, quaternion, quaternion ]
        
        #
        dcm_single = point.quaternion2dcm(quaternion)
        dcm_multi  = point.quaternion2dcm(quaternion_list)
        
        #
        self.assertEqual(type(dcm_single), np.ndarray, 
                                                      "Incorrect output type.")
        self.assertEqual(type(dcm_multi), list, "Incorrect output type." )
    
    def test_identity(self):
    
        # 
        quaternion      = np.array([0,0,0,1])
        quaternion_list = [ quaternion, quaternion, quaternion ]
        
        #
        dcm_single      = point.quaternion2dcm(quaternion)
        dcm_multi       = point.quaternion2dcm(quaternion_list)
        
        #
        self.assertTrue((dcm_single == np.eye(3)).all(), 
                                                  "Incorrect identity result.")
        for dcm in dcm_multi:
            self.assertTrue((dcm == np.eye(3)).all(), 
                                                  "Incorrect identity result.")
                                                  
    def test_values(self):
        
        # 
        quaternion      = np.array([0.5,0.5,0.5,0.5])
        
        #
        dcm_single = point.quaternion2dcm(quaternion)
        
        # 
        result     = np.array([[0,0,1], [1,0,0], [0,1,0]])
        
        #
        self.assertTrue((dcm_single == result).all(), 
                                                     "Incorrect value result.")
        for row in dcm_single:
            self.assertTrue(np.isclose(np.linalg.norm(row),1),
                                                "Incorrect dcm row magnitude.")
        