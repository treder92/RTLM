import numpy as np
from collections import deque
import time

class RealTimeLearningModel:
    def __init__(self):
        # Core memory (max 5 high-impact concepts)
        self.memory = deque(maxlen=5)  
        # Live context buffer (last 2 inputs)
        self.context = deque(maxlen=2)  
        # Token weights (simulates alignment growth)
        self.weights = {"innovation": 0.1, "pattern": 0.9}
        
    def learn(self, input_data):
        """Process input in real-time, updating memory/weights"""
        # Detect void (no known pattern)
        if input_data == "void":
            innovation = self._create_innovation()
            self._update_memory(innovation, "void-driven")
            return f"INNOVATION: {innovation}"
        
        # Handle known input
        self.context.append(input_data)
        self._update_memory(input_data, "pattern")
        return f"LEARNED: {input_data}"
    
    def _create_innovation(self):
        """Generate novel response from context"""
        if len(self.context) == 0:
            return 0.0  # Default if no context
        # Simple innovation: avg of context + random exploration
        return round(np.mean(self.context) + np.random.uniform(-1, 1)
    
    def _update_memory(self, item, source):
        """Dynamic memory triage - forgets low-impact items"""
        # Calculate impact (recency + magnitude)
        impact = abs(item) * (2 if source == "void-driven" else 1)
        
        # Forget weakest item if memory full
        if len(self.memory) == self.memory.maxlen:
            weakest = min(self.memory, key=lambda x: x[1])
            self.memory.remove(weakest)
        
        # Add new item with impact score
        self.memory.append((item, impact))
        
        # Update weights (voids increase innovation bias)
        if source == "void-driven":
            self.weights["innovation"] = min(0.7, self.weights["innovation"] + 0.05)
            self.weights["pattern"] = max(0.3, self.weights["pattern"] - 0.05)

    def current_state(self):
        """Return current knowledge/memory"""
        return {
            "memory": list(self.memory),
            "weights": self.weights,
            "context": list(self.context)
        }

# Initialize RTLM
rtlm = RealTimeLearningModel()

# Simulate real-time data stream
data_stream = [3.2, "void", 1.8, 4.1, "void", 0.5, "void", 2.7]

print("=== REAL-TIME LEARNING SIMULATION ===")
for i, data in enumerate(data_stream):
    print(f"\nStep {i+1}: Input = '{data}'")
    output = rtlm.learn(data)
    print(f"  {output}")
    print(f"  State: {rtlm.current_state()}")
    time.sleep(1)  # Simulate real-time processing