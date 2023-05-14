# ImageProcessingApp

This is a desktop application for image processing using the OpenCV package. The most important advantage of the application is the ease of use, the ability to immediately visualize the changes made to the image. The user also has the option of adjusting the parameters of each image processing method. In addition, the user can simultaneously visualize the histogram of the processed image in RGB and gray scale. The project can be used to familiarize yourself with image processing methods using the OpenCV package and to process various types of images according to your preferences.

### Contents
1. Colorspace
2. Low-pass filters
3. High-pass filters
4. Thresholding
5. Morphological Transformation
6. Geometric Transformation
7. Brightness
8. Histogram


### Libraries & Dependencies:

The GUI is developed based on the Qt environment. It was developed using Python3 and PyQt5 version 5.
The libraries used in the project are the OpenCV package, the numpy library and matplotlib.


### Images from working app

<img src="https://user-images.githubusercontent.com/62072813/235571905-f4b0e7a7-217c-46ed-bcb4-b3bba72872aa.png" width=45% height=45%> | <img src="https://user-images.githubusercontent.com/62072813/235571909-a1d9d745-ecd7-4ada-8d83-fdd6069a599e.png" width=45% height=45%>


### 1. Colorspace

The GUI allows to visualize and convert the image in BGR (default for OpenCV), RGB, HSV and grayscale colorspace.

The image is automatically opened in RGB when it is loaded using the *imread()* function. To convert the color scale, we use the built-in *cvtColor()* function of the opencv library.
(Images from BGR, RGB, HSV, Gray)

Description of HSV and Gray


### 2. Low-pass filtering



### 3. High-pass filtering



### 4. Thresholding



### 5. Morphological transformations



### 6. Geometric transformations



### 7. Brightness



### 8. Histogram



### Resources

  The following scientific resources were used in the development of the above project:

   [OpenCV Documentation](https://docs.opencv.org/4.x/d7/da8/tutorial_table_of_content_imgproc.html)
   
   [PyQt5 Tutorial](https://www.tutorialspoint.com/pyqt5/index.htm)
   
   [Python GUIs](https://www.pythonguis.com/pyqt5-tutorial/)

### License
  [MIT License](https://github.com/ragane/ImageProcessingApp/blob/master/LICENSE)
