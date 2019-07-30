# Flood Simulator

## Abstract

This project utilizes numerical methods to simulate the flow of water during heavy rainfall. Insight from this data can help determine the risk of flood damage in an area or the ecological effects of proposed water infrastructure like dams.

## Variables affecting rain flow

Rain flows between 2 adjacent locations proportional to the rain at the source location, the slope between the 2 points, and the global time step constant.

This method resembles Euler's Method which is known to be only 1st order accurate. Instability is made obvious when the simulation is run for a long time or with too large a time step constant. Other, more accurate methods exist. Runge-Kutta is a 4th order accurate method with good support in the default libraries in MatLab, but that would also mean arrays start at 1.

## Simulating a flood on Mount Cosine

The simulation initializes the simulation with 1/2 inch of rain, evenly distributed over the map. This is a torrential downpour on Mount Cosine. After all, the mountain is only 2 inches tall (from -1 to 1). The water flows off the peaks into the 4 surrounding lakes: Lake Euler, Lake Gauss, Lake Cantor, and Lake Riemann.

![Mount Cosine Gif](/Present/MountCosine.gif)
