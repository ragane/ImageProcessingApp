# ImageProcessingApp

This is a desktop application for image processing using the OpenCV package. The most important advantage of the application is the ease of use, the ability to immediately visualize the changes made to the image. The user also has the option of adjusting the parameters of each image processing method. In addition, the user can simultaneously visualize the histogram of the processed image in RGB and gray scale. The project can be used to familiarize yourself with image processing methods using the OpenCV package and to process various types of images according to your preferences.

### Contents
1. [Colorspace](https://github.com/ragane/ImageProcessingApp/edit/master/README.md?plain=1)
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
The GUI allows to visualize and convert the image in BGR (default for OpenCV), RGB, HSV and grayscale.
The image is automatically opened in RGB when it is loaded using the <i>imread()</i> function.
To convert the color scale, we use the built-in <i>cvtColor()</i> function of the opencv library.
The user can change the values of individual channels using sliders displayed in an additional window.

BGR                          RGB                           HSV                          GRAY

<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/462027d4-3989-48ad-86e5-bfaa253fc504" width=24% height=24%> <img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/9ba9bdde-61b4-4f0c-af86-e4ee1c4a6c52" width=24% height=24%> <img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/b1aedac1-8e3f-48e1-b50e-73f776a208e7" width=24% height=24%> <img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/c299a69c-da5f-476a-9350-f5d824d59276" width=24% height=24%>
</pre>

### 2. Low-pass filtering
<pre>
Low pass filtering is used to remove noises from a digital image by image blurring.
It is achieved by convolving the image with a low-pass filter kernel.
It actually removes high frequency content (eg: noise, edges) from the image. 
So edges are blurred a little bit in this operation.
When using each of the filters, the user can adjust the size of the kernel using the sliders in the additional window.

All low-pass filtering was done in the image below.
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/cf8d9696-5839-4d05-a391-0464a793dc29" width=50% height=50%>

<b>2D Convolution</b>

2D Convolution filtering use a 2D convolution of the kernel with the image.
This is done by the OpenCV function <i>cv.filter2D()</i>.
The function applies an arbitrary linear filter to an image. 
In-place operation is supported. When the aperture is partially outside the image,
the function interpolates outlier pixel values according to the specified border mode.

The function does actually compute correlation, not the convolution:
<!-- function will be there !! -->

The effect of applying the 2D convolutional filter on image is presented below.
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/a5ed11a4-4603-4b16-8921-801c4d58a96d" width=50% height=50%>

<b>Image Blurring</b>

The most used averaging blurring is done by convolving image with a normalized box filter. 
It simply takes the average of all the pixels under kernel area and replace the central element. 
This is done by the OpenCV function <i>cv.blur()</i>.
The function smooths an image using the kernel:
<!-- FUNCION MATH EQuation will be -->

The effect of applying the averaging filter on image is presented below.
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/64ad7876-ac7e-4982-91fc-9506ef14efa1" width=50% height=50%>

<b>Gaussian Blurring</b>

In this, instead of box filter, gaussian kernel is used.
This is done by the OpenCV function <i>cv.GaussianBlur()</i>.
Gaussian kernel standard deviations are zeros and they are computed from ksize.width and ksize.height.
The form of the Gaussian filter coefficient matrix:
<!-- WILL BE guassian filter math equation -->

The effect of applying the gaussian filter on image is presented below.
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/768e1935-85e4-466f-95e2-cd28959e5094" width=50% height=50%>

<b>Median Blurring</b>

The function takes median of all the pixels under kernel area and central element is replaced with this median value. 
This is highly effective against salt-and-pepper noise in the images.
Median blurring is done by the OpenCV function <i>cv.medianBlur()</i>.
The function smoothes an image using the median filter with the <i>ksize × ksize</i> aperture.

The effect of applying the median filter on image is presented below.
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/508ef00a-330b-46f2-b5ab-f37c5b6608f0" width=50% height=50%>


<b>Bilateral filtering</b>

Bilateral filter takes a gaussian filter in space and gaussian filter as a function of pixel difference.
Gaussian function of space make sure only nearby pixels are considered for blurring
while gaussian function of intensity difference make sure only
those pixels with similar intensity to central pixel is considered for blurring.
It is highly effective in noise removal while keeping edges sharp.
But the operation is slower compared to other filters. 
Bilateral filtering is done by the OpenCV function <i>cv.bilateralFilter()</i>.

The effect of applying the median filter on image is presented below.
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/331edf45-4274-4737-b5ff-a2fbab842efa" width=50% height=50%>

</pre>
### 3. High-pass filtering
<pre>
A high pass filter is the basis for most sharpening methods.
An image is sharpened when contrast is enhanced between adjoining areas with little variation in brightness or darkness.
A high pass filter tends to retain the high frequency information within an image while reducing
the low frequency information.
When using each of the filters, the user can adjust the size of the kernel and along which edge
the filtering will be performed in the additional window.

<b>Sobel filtering</b>

Sobel operators is a joint Gaussian smoothing plus differentiation operation, so it is more resistant to noise.
You can specify the direction of derivatives to be taken, vertical or horizontal.
Sobel filtering is done by the OpenCV function <i>cv.Sobel()</i>.

<b>Filtering with horizontal derivatives                        Filtering with vertical derivatives </b>
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/769ffe8f-d322-4256-923a-de66db631e8b" width=50% height=50%> <img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/1229cdb8-b412-457b-a5d7-80e0bba13da8" width=50% heigh=50%>

<b>Scharr filtering</b>

This is a filtering method used to identify and highlight gradient edges/features using the first derivative. 
Performance is quite similar to the Sobel filter. 
The Scharr filter can be obtained when the kernel size of the Sobel filter is equal to -1.
The filter is automatically set to a 3x3 size, which gives better results than the Sobel 3x3 filter.

<b>Filtering with horizontal derivatives                        Filtering with vertical derivatives </b>
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/4c6584d3-8d6f-466b-af56-e5701e0da55c" width=50% height=50%> <img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/d5823b40-9dc0-462c-bcc5-5b0540e06040" width=50% heigh=50%>

<b>Laplacian filtering</b>

This is a filtering method used to identify and highlight fine edges based on the second derivative.
Laplacian uses one symmetrical kernel while Sobel and Scharr use horizontal and vertical kernels.
It is also more sensitive to noise compared to the previous ones.
When using each of the filters, the user can adjust the size of the kernel using the sliders in the additional window.
Laplacian filtering is done by the OpenCV function <i>cv.Laplacian()</i>.

The effect of applying the laplacian filter on image is presented below.
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/ef0eeb33-0df0-4f2e-a220-84b2f0ab896f" width=50% height=50%>

<b> Canny edge detection </b>

Noise Reduction

Canny Edge Detection is a popular edge detection algorithm.
Since edge detection is susceptible to noise in the image,
first step is to remove the noise in the image with a 5x5 Gaussian filter.
Next step is filtering image with a Sobel kernel in both horizontal and vertical direction
to get first derivative in both directions.
From these two images, we can find edge gradient and direction for each pixel.
Gradient direction is always perpendicular to edges. It is rounded to one of four angles representing vertical,
horizontal and two diagonal directions.
Next a full scan of image is done to remove any unwanted pixels which may not constitute the edge.
For this, at every pixel, pixel is checked if it is a local maximum in its neighborhood in the direction of gradient.
Last step is decides which are all edges are really edges and which are not.
For this, we need two threshold values, minVal and maxVal.
Any edges with intensity gradient more than maxVal are sure to be edges and
those below minVal are sure to be non-edges, so discarded.
Those who lie between these two thresholds are classified edges or non-edges based on their connectivity.
If they are connected to "sure-edge" pixels, they are considered to be part of edges.
Otherwise, they are also discarded.

Canny edge detection algorithm is done by the OpenCV function <i>cv.Canny()</i>.
When using each of the filters, the user can adjust levels of first and second thresholds for the hysteresis procedures
by using the sliders in the additional window.

The effect of applying the canny edge detection algorithm on image is presented below.
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/a8e31251-22e7-4ddf-9878-31406acb02fb" width=50% height=50%>
</pre>

### 4. Thresholding
<pre>
Image thresholding is a simple form of image segmentation.
It is a way to create a binary image from a grayscale or full-color image.
This is typically done in order to separate object or foreground pixels
from background pixels to aid in image processing.
Thresholding is done by the OpenCV function <i>cv.threshold()</i>.
When using the GUI, the user can select the type of thresholding and can adjust the level of the threshold value.

All thresholding operations was done in the image below.

<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/803417eb-5eae-4927-9180-8de691d5477b" width=50% height=50%>

We can use 4 types of thresholding:
- cv.THRESH_BINARY
<!-- math equation -->
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/7743ef7b-8609-42af-b2fc-9b0b924e721c" width=50% height=50%>


- cv.THRESH_BINARY_INV
<!-- math equation -->
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/dddf279a-c058-496d-9cd6-4812bbcf51e1" width=50% height=50%>


- cv.THRESH_TRUNC
<!-- math equation -->
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/60d19813-7be9-4cc3-9add-99eef7e25455" width=50% height=50%>


- cv.THRESH_TOZERO
<!-- math equation -->
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/7fd2fe5f-73be-4941-b295-5ec4c8a50e74" width=50% height=50%>

</pre>

### 5. Morphological transformations
<pre>
Morphological transformations are some simple operations based on the image shape.
It is normally performed on binary images.
It needs two inputs, one is our original image, second one is called structuring element
or kernel which decides the nature of operation.
Two basic morphological operators are Erosion and Dilation.
Then its variant forms like Opening, Closing, Gradient  also comes into play.

When using each of the transformations, the user can adjust the size of the kernel.

All morphological transformations was done in the image below.
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/08881d68-bd54-45ea-bfc4-255817968c1a" width=50% heigh=50%>
          
<b>Erosion</b>

The basic idea of is erode away the boundaries of foreground object.
The kernel slides through the image (as in 2D convolution).
A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1,
otherwise it is eroded (made to zero).
All the pixels near boundary will be discarded depending upon the size of kernel.
So the thickness or size of the foreground object decreases or simply white region decreases in the image.
It is useful for removing small white noises ordetach two connected objects etc.

Erosion is done by the OpenCV function <i>cv.erode()</i>.


<b>Dilation</b>

It is just opposite of erosion. Here, a pixel element is '1' if at least one pixel under the kernel is '1'.
So it increases the white region in the image or size of foreground object increases.
For the most cases like noise removal, erosion is followed by dilation.
Because, erosion removes white noises, but it also shrinks our object.
It is also useful in joining broken parts of an object.

Dilation is done by the OpenCV function <i>cv.dilate()</i>.


<b>Opening</b>

Opening is operation in which erosion is followed by dilation. 
It is useful in removing noise.

Opening is done by the OpenCV function <i>cv.cv.morphologyEx()</i>.


<b>Closing</b>

Closing is reverse of Opening, Dilation followed by Erosion.
It is useful in closing small holes inside the foreground objects, or small black points on the object.

Closing is done by the OpenCV function <i>cv.cv.morphologyEx()</i>.


<b>Morphological Gradient</b>

It is the difference between dilation and erosion of an image.
The result will look like the outline of the object.

Morphological gradient is done by the OpenCV function <i>cv.cv.morphologyEx()</i>.


<b>Erosion                  Dilation                Opening                   Closing                Gradient
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/02240e82-564e-4245-a4d7-5bb1f7e48652" width=20% height=20%> <img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/314947c7-a042-4e30-8bc0-c80769962a01" width=20% height=20%> <img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/8c265528-e0f4-45e8-b279-67be63903ca4" width=20% height=20%> <img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/8aa9656b-a970-424f-bbc7-f08180d09c6d" width=20% height=20%> <img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/bee32d2a-562a-4fc9-9197-6f33acab8e6a" width=20% height=20%>

</pre>

### 6. Geometric transformations
<pre>
<b>Scaling</b>
Scaling is just resizing of the image. Different interpolation methods are used.
Preferable interpolation methods are cv.INTER_AREA for shrinking and cv.INTER_CUBIC (slow) & cv.INTER_LINEAR for zooming.
The user can adjust the size of the image in the additional window.

The effect of scaling image is presented below.
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/91b96204-5d0f-4d3d-849b-f3afc43d29de" width=50% height=50%> <img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/1a4e6109-51f0-4ae9-8dc7-bcde7102884e" width=50% height=20%>


<b>Translation</b>
Translation is the shifting of object's location. If you know the shift in (x,y) direction
The user can adjust the size of the shift (x, y) in the additional window.

The effect of translation image is presented below.
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/4a1e8b82-739a-4fdd-9f1b-d7a7e6799d16" width=50% height=50%>


<b>Rotation</b>
Rotation of an image for an angle θ is achieved by the transformation matrix.
OpenCV provides scaled rotation with adjustable center of rotation so that you can rotate at any location you prefer.
The user can adjust the size of rotation in additional window.

The effect of rotate image is presented below.
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/7291c8ea-478d-4d81-9f71-b4db2211dec2" width=50% height=50%>


</pre>


### 7. Brightness
<pre>
In order to change the image, we use the OpenCV package function convertScaleAbs().
Changes in the brightness value can be adjusted by the user using the slider in the range of [-127, 127].

The effect of changing brightness of image is presented below.
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/6750324b-91c9-4837-a535-3ca840edaaa0" width=50% height=50%>
</pre>
### 8. Histogram
<pre>
Histogram is a graph or plot, which gives you an overall idea about the intensity distribution of an image.
It is a plot with pixel values (ranging from 0 to 255)
in X-axis and corresponding number of pixels in the image on Y-axis.

It is used to better understand the image.
By looking at the histogram of an image, you get intuition about contrast, brightness,
intensity distribution etc of that image. 
In the interface, the user can get a histogram of the color image,
each of the colors in the RGB scale is reflected by its color.
In addition, it can visualize the histogram of the image in grayscale.

The histograms are shown below. RGB on the left, grayscale on the right.
<img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/f4163102-b571-4430-a222-b7f146d104ce" width=50% height=50%> <img src="https://github.com/ragane/ImageProcessingApp/assets/62072813/ec71f461-8cbb-4603-b04b-60bd27960fa4" width=50% height=50%>

</pre>

### Resources

  The following scientific resources were used in the development of the above project:

   [OpenCV Documentation](https://docs.opencv.org/4.x/d7/da8/tutorial_table_of_content_imgproc.html)
   
   [PyQt5 Tutorial](https://www.tutorialspoint.com/pyqt5/index.htm)
   
   [Python GUIs](https://www.pythonguis.com/pyqt5-tutorial/)

### License
  [MIT License](https://github.com/ragane/ImageProcessingApp/blob/master/LICENSE)
