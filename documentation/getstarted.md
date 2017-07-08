# Get Started

**(Note: DO NOT USE THIS ALGORITHM IN A REAL LIFE SCENARIO. IT IS NOT FIT FOR REAL WORLD USE.)**

This is a gross oversimplification of how Tensorflow and machine learning works. If you want to know this works in detail, I suggest the Tensorflow for Poets tutorial by Google, which is available here: https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/index.html. The algorithm and files contained in this repository and that tutorial are quite similar, and that will also guide you through some stuff that I've decided to leave out of this tutorial.

This algorithm uses a few different files, so let's walk through them. 

## Definitions

**arch.py** - this is one of the main files. It takes a list of retinal images (contained in a CSV file) and runs the algorithm (contained in labelimage.py) to classify the images as either showing signs of diabetic retinopathy, or clear of it. 

**labelimage.py** (not to be confused with label_image.py) - subroutine that takes an image and runs it through the graph file in order to classify it (retrained_graph.pb)

**retrained_graph.pb** - the heart of the algorithm. This contains the methods that Tensorflow uses to classify an image. Open it, and you'll find a bunch of binary stuff. (If you want to retrain the algorithm, see retrain.md)

**label_image.py** - this file allows you to classify an image without preparing a CSV list. It's helpful if you want to just test one file rather than something like twenty. 

**retrain.py** - see retrain.md. 

**dataset.csv** - this file is the "answer key", as it contains the clinician-graded classifications of each image, on a scale from 1-4. 

**dataindex.csv** - this is the file that arch.py uses to see what files to run through the algorithm. 

**retrained_labels.txt** - this is the list of classifications that the algorithm could assign to a single image. (Don't modify this file without retraining retrained_graph.pb. If you want to know how to do that, see retrain.md)

**bottlenecks/** - this is a Tensorflow system area. For the purposes of this tutorial, it should be left alone. If you want to learn more about what's in here, see the Tensorflow for Poets article by Google)

**logs/** - see the README.md contained in that directory. 

**inception/** - this is a software package that Tensorflow uses to make sense of image data that it receives. 

## Quick start 

1. Install Python and Tensorflow. (You can find a tutorial on the Tensorflow website on how to do this.) In the course of developing this project, we used a python 2.7 install with a corresponding Tensorflow for python 2.7 install. 

2. Clone/download this repository and the dataset. (Dataset here: https://www.kaggle.com/c/diabetic-retinopathy-detection/data. You will need all of the "train.00x.zip" files, the training_labels.zip file, and some method to separate them into different directories based on that master list. You can use our sorting script, which is available here: https://gist.github.com/javathunderman/6a9f9c8a0ee29cb7a817777421685e49. We will publish a more organized subset of this entire dataset soon, but for right now you can use that.)

3. Fill out dataindex.csv with the file addresses of the images you want to test. (Unless you have a system with a lot of resources on tap, don't go over 10 images in a single batch. It tends to overload the graph file and cause all sorts of issues.)

4. Run "python arch.py", and it will start printing out the results of each image. It will also automatically generate a log file in the root directory of the repository to store the output of a batch. If you plan on saving the contents of that log file, ensure that you rename it something different so that it is not overwritten by the next batch of output. 

5. Profit. If you want to go further, check out retrain.md for information on how to retrain the algorithm on your own training set or check out the Tensorflow for Poets tutorial for more information. 



