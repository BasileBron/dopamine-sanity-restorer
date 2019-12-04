![adult content blurer](banner_github.jpg)
# theCensor
This project for HackSussex hackathon 2019 aims to identify and close inappropriate adult content in a Window or browser. The objective is to remove this type of content when the user did not specifically search for it.

At the moment, the model detects inappropriate content and execute the hotkey ```Ctrl+W``` to close the windows or tab that has the toxic content.

# Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

# Prerequisites

Download this file and move it at the root of the repository
[Keras 299x299 Image Model](https://s3.amazonaws.com/nsfwdetector/nsfw.299x299.h5)

# How does it work
The code will only take screenshot of the **active windows**, mainly for performance reason but also to only close windows that contain the explicit content. Then a convolutional neural network will decide if the content is explicit or not.
here is the [model](https://github.com/GantMan/nsfw_model)

# Current state of the project
It work well but still have a lot of false positive which is mainly du to the fact that screenshots of a screen are really different from the data that the model has been trained on.

# Authors
- [Basile Bron](https://github.com/BasileBron)
- [Youssef Abdelrazek](https://github.com/ya222)
- Vivien Neumann
- [Elodie Muchembled](https://github.com/Elodym)
