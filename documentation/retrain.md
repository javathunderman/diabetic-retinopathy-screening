# Retrain the algorithm

This project has its own retraining script, but for the purposes of this tutorial, we've substituted it with the retraining script provided by Google in their "Tensorflow for Poets" tutorial. 

First ensure that you have your dataset ready. Then separate about 500 images (total, between both the diseased and nondiseased folders) and put them into a different directory than the master pool. You can determine what images you want to use, or use the predetermined lists contained in the logs directory. If you want to use the predetermined list, make sure you have a way of separating those images from the master pool, either by some Bash/Python hackery or using the script that we used earlier (available at https://gist.github.com/javathunderman/6a9f9c8a0ee29cb7a817777421685e49)

Simply run the following command:

    python retrain.py \
      --bottleneck_dir=bottlenecks \
      --how_many_training_steps=300 \
      --model_dir=inception \
      --output_graph=retrained_graph.pb \
      --output_labels=retrained_labels.txt \
      --image_dir=[whereeveryour500imagesarelocated]

This command will seek out your image directory and begin training the algorithm. Avoid increasing/decreasing the "how_many_training_steps" argument without adjusting the training set accordingly. An improper number of training steps can lead to poor accuracy numbers. 

Each of the numbers that gets printed out during the retraining process means something different. (Definitions courtesy of Google.)

The training accuracy shows the percentage of the images used in the current training batch that were labeled with the correct class.

The validation accuracy is the precision (percentage of correctly-labelled images) on a randomly-selected group of images from a different set.

Cross entropy is a loss function that gives a glimpse into how well the learning process is progressing (lower numbers are better here).

For more information, check out the Tensorflow for Poets tutorial here: https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/index.html
