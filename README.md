## Car Crash  Simulation
By Estella Yee & Kobe Lee

## Overview
Our project is a car crash simulation that models the physics of vehicle collisions under various conditions. 
The user will have the option to customize the scenario by selecting different surface types, car sizes, elasticity, and collision targets. 
Our project will be concrete, visually appealing (lots of crashing), and interactive! This simulation is grounded in two core physics concepts: momentum and friction. 
The total momentum of the system (p = mv) is tracked before and after the collision. A slider lets the user set the elasticity coefficient, which determines the percentage of momentum that is transferred to the target. 
An elastic collision will have kinetic energy conserved throughout the entire simulation, whereas an inelastic collision will have a loss of kinetic energy. 
The user will also be able to select between different surface types, which will determine the coefficient of friction applied to the car before and after the collision, and thus affect its acceleration throughout the simulation. 

## Customizable Features

**Scenario Options**
| Option | Choices |
|---|---|
| Surface | Asphalt, Wet Road, Ice |
| Car Size | Small (800 kg), Medium (1400 kg), Large (2500 kg) |
| Target | Tree (~immovable), Parked Car (2000 kg), Moose (700 kg), Truck (10,000 kg) |
| Elasticity | 0.0 (perfectly inelastic) → 1.0 (perfectly elastic) |

**Real-Time Graphs**
1. **Kinetic Energy vs. Time** — shows energy distribution and friction dissipation
2. **Momentum vs. Time** — shows whether momentum is conserved or reduced by friction
3. **KE Lost vs. Elasticity** (bar graph) — visualizes the trade-off between elasticity and energy loss

---

## Instructions

| Control | Description |
|---|---|
| Surface buttons | Switch between Asphalt, Wet Road, and Ice |
| Car Type buttons | Change car size/mass |
| Target buttons | Select the collision target |
| Elasticity slider | Set *e* from 0.0 (inelastic) to 1.0 (elastic) |
| Start / Restart | Begin or reset the simulation |

---

## Physics

**Post-Collision Velocities**

Computed using the generalized collision formula with coefficient of restitution *e*:

```
v1_f = (m1·v1 + m2·v2 - m2·e·(v1 - v2)) / (m1 + m2)
v2_f = (m1·v1 + m2·v2 + m1·e·(v1 - v2)) / (m1 + m2)
```

**Elasticity** (*e*, coefficient of restitution)
- *e* = 1.0 → perfectly elastic: kinetic energy fully conserved
- *e* = 0.0 → perfectly inelastic: maximum kinetic energy lost
- Values in between model real-world collisions

**Friction**

Each surface has a coefficient of kinetic friction (μ) that decelerates the car before the collision and slows both objects afterward:

```
a = -μ · g
```

| Surface | μ |
|---|---|
| Asphalt | 0.40 |
| Wet Road | 0.05 |
| Ice | 0.00 |
