import unittest
import sys
from typing import List, Dict, Any
from tensor_field import TensorField
from spoke_interface import SpokeAdapter
from docking_shell import DockingShell

class MockSpoke(SpokeAdapter):
    """Mock Spoke for testing."""
    def __init__(self, state_size=100):
        self._state_size = state_size
        self._last_token = None
    
    @property
    def name(self) -> str:
        return "MockSpoke_Test"
    
    def get_voxel_state(self) -> List[float]:
        return [0.5] * self._state_size
    
    def receive_token(self, token: List[float]) -> Dict[str, Any]:
        self._last_token = token
        return {"status": "OK", "received": len(token)}

class TestTensorField(unittest.TestCase):
    """Test the TensorField component."""
    
    def test_initialization(self):
        """Test TensorField initializes correctly."""
        tf = TensorField(shape=(10, 10, 10))
        self.assertEqual(len(tf.state_tensor), 1000)
        self.assertEqual(len(tf.rag_memory), 0)
    
    def test_update_state(self):
        """Test state updates."""
        tf = TensorField(shape=(5, 5, 5))
        new_state = [1.0] * 125
        tf.update_state(new_state)
        self.assertEqual(tf.state_tensor, new_state)
    
    def test_eigen_embedding(self):
        """Test eigenvalue computation."""
        tf = TensorField(shape=(5, 5, 5))
        tf.update_state([0.5] * 125)
        embedding = tf.compute_eigen_embedding()
        
        # Should return normalized eigenvalues
        self.assertIsInstance(embedding, list)
        self.assertGreater(len(embedding), 0)
        # Check normalization (sum should be ~1.0)
        self.assertAlmostEqual(sum(embedding), 1.0, places=5)
    
    def test_rag_ingestion(self):
        """Test RAG knowledge ingestion."""
        tf = TensorField(shape=(5, 5, 5))
        
        # Ingest knowledge
        vec = [1.0, 2.0, 3.0, 4.0, 5.0]
        tf.ingest_knowledge("test_concept", vec)
        
        self.assertEqual(len(tf.rag_memory), 1)
        self.assertEqual(tf.rag_keys[0], "test_concept")
    
    def test_rag_unification(self):
        """Test RAG vector similarity search."""
        tf = TensorField(shape=(5, 5, 5))
        
        # Ingest multiple concepts
        tf.ingest_knowledge("concept_a", [1.0, 0.0, 0.0])
        tf.ingest_knowledge("concept_b", [0.0, 1.0, 0.0])
        tf.ingest_knowledge("concept_c", [0.0, 0.0, 1.0])
        
        # Query with vector similar to concept_a
        query = [0.9, 0.1, 0.0]
        results = tf.map_rag_unification(query, top_k=2)
        
        self.assertEqual(len(results), 2)
        # First result should be concept_a (highest similarity)
        self.assertEqual(results[0][0], "concept_a")

class TestDockingShell(unittest.TestCase):
    """Test the DockingShell Hub."""
    
    def test_initialization(self):
        """Test Hub initializes correctly."""
        hub = DockingShell(tensor_shape=(5, 5, 5))
        self.assertIsNotNone(hub.tensor_field)
        self.assertIsNone(hub.active_spoke)
    
    def test_docking(self):
        """Test spoke docking."""
        hub = DockingShell(tensor_shape=(10, 10, 10))
        spoke = MockSpoke(state_size=1000)
        
        hub.dock(spoke)
        self.assertEqual(hub.active_spoke, spoke)
    
    def test_cycle_without_spoke(self):
        """Test cycle fails without docked spoke."""
        hub = DockingShell(tensor_shape=(5, 5, 5))
        
        with self.assertRaises(RuntimeError):
            hub.cycle()
    
    def test_full_cycle(self):
        """Test complete Hub cycle."""
        hub = DockingShell(tensor_shape=(10, 10, 10))
        spoke = MockSpoke(state_size=1000)
        hub.dock(spoke)
        
        # Prime RAG
        for i in range(3):
            vec = [float(i)] * 1000
            hub.tensor_field.ingest_knowledge(f"concept_{i}", vec)
        
        # Run cycle
        result = hub.cycle()
        
        # Validate result structure
        self.assertIn("eigen_state_preview", result)
        self.assertIn("rag_context", result)
        self.assertIn("feedback", result)
        
        # Validate spoke received token
        self.assertIsNotNone(spoke._last_token)
        self.assertGreater(len(spoke._last_token), 0)

class TestIntegration(unittest.TestCase):
    """Integration tests for the full system."""
    
    def test_multi_cycle_stability(self):
        """Test multiple cycles maintain stability."""
        hub = DockingShell(tensor_shape=(8, 8, 8))
        spoke = MockSpoke(state_size=512)
        hub.dock(spoke)
        
        # Prime RAG
        for i in range(5):
            vec = [float(i) * 0.1] * 512
            hub.tensor_field.ingest_knowledge(f"stable_concept_{i}", vec)
        
        # Run multiple cycles
        for _ in range(10):
            result = hub.cycle()
            self.assertIsNotNone(result)
            self.assertIn("feedback", result)
        
        # Check history accumulation
        self.assertEqual(len(hub.eigen_manifold_history), 10)

def run_tests():
    """Run all tests and return results."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestTensorField))
    suite.addTests(loader.loadTestsFromTestCase(TestDockingShell))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
