![adult content blurer](banner_github.jpg)
# theCensor
This project for HackSussex hackathon 2019 aims to identify and blur inappropriate adult content in a Windows browser. The objective is to remove this type of content when the user did not specifically search for it, for example, when watching a serie or a movie with friends and family. Similarly, on Instagram and Netflix.

At the moment, the model detects inappropriate content and generates pop-up images to disctract the user. We use the Yolo algorithm to locate where this content is displayed, however, we did not manage to implement it. Blurring the specific part of the screen which is undesirable is also difficult, which is why we decided to pop images in a separate window instead.

# Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

# Prerequisites

Install this file and store the root at the repository
[Keras 299x299 Image Model](https://s3.amazonaws.com/nsfwdetector/nsfw.299x299.h5)

# Methods
- nsfw_detector
- Yolo algorithm
- convolutional neural network

# Authors
- [Basile Bron](https://github.com/BasileBron)
- [Youssef Abdelrazek](https://github.com/ya222)
- Vivien Neumann
- [Elodie Muchembled](https://github.com/Elodym)
