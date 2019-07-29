# Flood Simulator

## Abstract

This project utilizes numerical methods to simulate the flow of heavy rainfall. Insight from this data can help determine the risk of flood damage in an area or simulate the effects of proposed water infrastructure like dams.

## Variables affecting rain flow

Rain flows between 2 adjacent locations proportional to the rain at the source location, the slope between the 2 points taking height as the sum of elevation and water level, and the global time step constant.

This method resembles Euler's Method which is known to be only 1st degree accurate. Other, more accurate methods exist. Runge-Kutta is a 4th order accurate method.

## Simulating a flood on Mount Cosine

The simulation initializes the simulation with 1/2 inch of rain, evenly distributed over the map. This is a torrential downpour on Mount Cosine. After all, the mountain is only 2 inches tall (from -1 to 1). The water flows off the peaks into the 4 surrounding lakes.

![Mount Cosine Gif](/Present/MountCosine.gif)
