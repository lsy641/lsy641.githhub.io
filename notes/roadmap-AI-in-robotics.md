# A Roadmap for AI in Robotics - Reading Notes

## About the Paper

**Paper:** [A roadmap for AI in robotics](https://www.nature.com/articles/s42256-025-01050-6) <br>

**Authors:** Aude Billard et al.  <br>

**Journal:** Nature Machine Intelligence  <br>

**Published:** June 19, 2025  <br>

**DOI:** https://doi.org/10.1038/s42256-025-01050-6  <br>

This perspective paper provides a roadmap for integrating AI into robotics, addressing both short-term and long-term challenges. The authors assess AI's achievements in robotics since the 1990s and propose research directions for the future.


## Key Points

### A Brief History

Robot research started in the 1960s. AI has been used in robotics since the 1990s.

Two types of algorithms and data gathering:

1. **Learning from demonstrations**
    * **Convention:** Expert demonstration data collection
    * **Limitation:** Hard to get large demonstration data
    * **Improvement:** 
        1. Learning from larger but suboptimal demonstrations
        2. Active learning/behavioral cloning
2. **Reinforcement learning**
    * **Convention:** Balance between exploitation and exploration
    * **Limitation:** Exploration is expensive and does not scale easily
    * **Improvement:**
       1. Large-data learning 
       2. Ensure good prior knowledge (*)
       *I was told a viewpoint that LLMs provide good prior knowledge so RL finally works*

### Applications

1. E-commerce warehouse robotics
2. Autonomous driving
3. Soft robotics (*)
   *I feel soft robotics has much more potential than hard robotics like quadrupeds and humanoids. But this direction is both interesting and challenging.*

### Short- and Medium-term Challenges

1. **Data collection challenge**
    * Harm to humans (such as autonomous flying)
    * Privacy (such as terrestrial navigation)
    * Additional challenges when collecting scenario data requiring human interaction 
    * Efficiently utilizing robot-specific sensing data (like electromagnetic spectrum)
2. **Sim-to-real problem**
    * Classic simulators: Algoryx, Bullet, Gazebo, IsaacSim, MuJoCo, RoboDK, Genesis. Guarantee good locomotion on complex terrains and object manipulation.
    * Challenges: Cannot handle complex real environment conditions (such as contact forces and deformable surfaces)
    * Promise: Real-time adaptation with small data
3. **Leveraging large generative models in robotics**
    * Opportunity: Combining Internet-scale visual–language tasks and robotic trajectory data
    * Challenge: Reasoning, logic, feasibility of planning
4. **Prior knowledge and combining AI with control methods**
    * Such combination is crucial. 
    They put an example as justification: "In aerial robotics, neither learning nor aerodynamics-based control alone can help solve the challenge of approximating the agility of birds' flight: coupling sensing and perception with the full body dynamic, allowing a drone to have instant reactions in flight and cancel perturbations, or on the contrary profit from the wind, efficiently combining flapping of wings and gliding (in the case of a winged drone) to save energy. These challenges will require a combination of learning for building improved aerodynamics models with control methods for guaranteeing flight stability." *(I need more time to think about how this example justifies the combination is necessary)*
    * Another justification is LLM hallucination. 
    *(I don't know whether it is a valid justification for such combination. LLMs can still combine with real-time adaptive learning methods instead of control methods)*
    * Another justification is large models' low reasoning efficiency. 
    They take more steps (reasoning) for an action, hard to achieve agility.

### Long-term Challenges

Continuously acquiring new knowledge is the most challenging, long-term promise since the 1990s.

1. **Lifelong learning**
    * Technical challenge: Requiring paradigm shift from input-output learning and expert systems to something new. In a new paradigm, how can we test and know the performance is good? How do we select things to forget and make room for learning new things?
    * Regulatory issues: Verify an evolving system maintains the safety and reliability standards requested for market certification as its capabilities change with new learning. 
    * Transfer learning ability: After 5 or 8 years of operation, a robot may have to mount a different gripper or a different motor. The acquired knowledge that allows the robots to pick up and manage different objects may not automatically transfer to a slightly modified platform. *(My thought: Humans don't change much of their organism structure through evolving, that is why our knowledge can be passed down and re-used. Should robots have such inheritance? Or at least create an abstractive structure shared by all robotics)*
2. **Transfer Learning**
    * What to transfer
    * How to transfer
    * When to transfer
3. **Safe-exploration**
    * Challenges: Dealing with incomplete observability, making live explorations, balance between efficiency and safety

---

*Notes by Siyang Liu - Last updated: August 007, 2025*
