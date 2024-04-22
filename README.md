# Assignment_4_CV

DepthAI Object Tracking Application

Description:
This project implements an application that uses the Luxonis DepthAI camera to perform object tracking and estimate dimensions in real-time. The application runs as a web-based interface, allowing users to access it from any device with a web browser. It leverages the Flask framework for the backend and integrates the DepthAI SDK for object tracking and depth estimation.

Features:
- Real-time object tracking using the DepthAI camera
- Spatial calculation to estimate dimensions of tracked objects (i.e. me)
- Web-based interface for easy access from any device

Usage:
1. Connect the Luxonis DepthAI camera to your computer.
2. Run the Flask application: python Application_4.py
3. Open a web browser and navigate to http://localhost:5000 to access the application.
4. You should see the live camera feed with object tracking and dimension estimation. (video of demonstration  attached in repository main thread)


Additional Notes:
The flask application displays only the heading but the actual window for the depthAI opens separately although the idea
was to implement a video player widget.
I used myself as the object to be tracked as it was getting tricky to fix the stereo cam somewhere and track an object that might be moving.
