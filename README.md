# SelfDrivingCar

Self Driving car, A raspberry Pi based RC car is a self-driving, or autonomous vehicle that has the ability to follow a logical course of action to achieve set goals by the users when it comes to driving to a designated location.


# Requiremnets

 1. Raspberry Pi Model 4 or later
 2. L298n Motor Driver with motors and wheels attached to it
 3. Camera
 4. Ultrasonic Sensor
 5. Servo Motors
 

# Libraries Used

 1. <b>RPi.GPIO</b>: This package provides the class to control the GPIO pins on a Raspberry Pi, used in this project to control the H-Bridge that controls the motors, the camera, the ultrasonic sensor as well as the servo motors that controls the camera and ultrasonic sensor.
 2. <b>PyGame</b>: This a python library that is mainly used for creating and developing game using python, used in this project to detect key presses from a keyboard for manual control of the car.
 3. <b>CV2</b>: CV2 is the open cv library that allows image processing, used in this project to process images and prepare them for machine learning
 4. <b>Numpy</b>: Is a python library used to work with arrays, its used in this project to train the data.
 5. <b>Pandas</b>: Pandas is a python library used for data analysis, used in this application for saving data into csv file.	
 6. <b>TensorFlow</b>: TensorFlow is a python library used for machine learning, used in this project to train the data.
 7. <b>Scikit-learn</b>: Scikit learn is another library used for machine learning, used it for some functions I couldn’t do with Tensor Flow.
 8. <b>Imgaug</b>: Imgaug is python library used for image augmentation and used in the project to train the AI.


# Design
Throughout the whole process of completing this project, I had one aim in my mind, modularity, not only in the hardware, but in the software as well, which means I will be able to add and remove devices and sensors very easily without having to revamp my code completely.
The idea of Modularity is creating multiple files of code, and linking them together to complete a complete project, where I will have a main file, and that file would be connected to multiple modules such as motor, camera, keyboard, joystick and detection algorithms like face and lane, each of these modules will have their own code that can run on its own, and if needed can be called by the main script, this way, modules will only input and output meaningful information making the process modular and easy to manage, for example if I wanted to change the motor driver, I can simply just replace the motor driver module rather than changing the whole code.
Having a modular code will allow me to use the same modules for other projects as well.

![](/Images/Modularity.PNG)


# Lane Detection

For this project, I created a module for lane detection using machine learning, where the car will detect the road lanes, and will drive between the road lanes autonomously without human intervention.
The modules I will be using are the motor module and the webcam and ultrasonic sensor modules.
The reason that I have a separate module for the webcam instead of it being in the lane detection module is that later on when I will be writing the object classification module for road signs, I will be using the same webcam module, by having it in a separate module I will not have to repeat my code and will make the code more flexible.
So I have one module that capture the images, and then It will send it to the main module, and from then the main module can send the images to different modules that requires it.
In this case, it will be required by the Lane module, so I will send the image, and the Lane module will send back the curve value of how much the vehicle needs to turn and in which direction.
There is also a utilities file, that is linked only to the lane module, and it will contain supporting functions, so the main lane module is not very clustered with codes.
Once the curve from the lane modules is in the Main module, I send the curve to the motor module, that will turn the motors based on the speed and turn provided by the lane module.

![](/Images/LaneDetectionModule.PNG)


#Machine Learning

I divided the training of the data into different steps. 
# Requiremnets
 1. I import the information from the data collection module, which are the image and the steering angle, using Panda’s framework I balance the data. 
Next I visualize the data and balance them.
 2. I prepare the data for processing, which means I bring the data out of the panda format and put it into a list format for the ease of use later on.
 3. I use the split method to split the data for validation and for training.
 4. Due to the fact that I do not have a lot of data set, I will augment the data so I can use it in different scenarios, from moving the image left and right, zooming in and out, increase and decrease the brightness and flip it as well.
 5. I preprocess the images, from cropping, changing the color space, adding blur, resizing and normalizing so we end up with only valuable data.
 6. I created a TensorFlow model and start the training. 
 7. Training is done, I save the model, into a model.h5 file. 
 8. I plot the result using matplotlib.

![](/Images/DataTrainingSteps.PNG)


#Result

The final result of this project, is an autonomous car, that can detect the road lines using image processing and machine learning to detect the center of the road and make sure to not drift off it, using ultrasonic sensors detect object on the road that prevents the car from further driving to avoid collision, a car that can detect traffic signs and based on the traffic sign read what it states and react based on logic accordingly with little to no error. 
The motors connected to the h-bridge works perfectly when they receive enough power, which in this case is 12V.
The Raspberry Pi successfully communicates with the H-Bridge, Camera, Ultrasonic Sensor and the Servo Motors, when supplied with 5V power.
The car was detecting the road and the road signs from the camera images. And the trained data was successfully able to predict the correct speed and turn angle for the car to drive on the road.

![](/Images/TheSelfDrivingCar.PNG)


#Built With

- Python Programming Language
- Raspberry Pi Module 4


#To Do
I am planning for the car further development, as I would like to implement a Radar on the car to see how ill that affect the performance.


# Authors

- Radvan Khammud

