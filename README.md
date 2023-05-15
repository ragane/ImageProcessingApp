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

<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/cd09f781-c109-4e46-ba73-d9e329578ca0" width=75% height=75%>
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/5c9b57ea-da5e-4e66-a89a-45c76642011e" width=75% height=75%>


### 1. Colorspace
<pre>
The GUI allows to visualize and convert the image in BGR (default for OpenCV), RGB, HSV and grayscale colorspace.
The image is automatically opened in RGB when it is loaded using the <i>imread()</i> function.
To convert the color scale, we use the built-in <i>cvtColor()</i> function of the opencv library.
The user can change the values of individual channels using sliders displayed in an additional window.

BGR                          RGB                           HSV                          GRAY

<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/462027d4-3989-48ad-86e5-bfaa253fc504" width=24% height=24%> <img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/9ba9bdde-61b4-4f0c-af86-e4ee1c4a6c52" width=24% height=24%> <img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/b1aedac1-8e3f-48e1-b50e-73f776a208e7" width=24% height=24%> <img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/c299a69c-da5f-476a-9350-f5d824d59276" width=24% height=24%>
</pre>

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
