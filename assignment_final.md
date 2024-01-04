
## Task 1: Explore the data

You will work with (part of) the public dataset PAD-UFES-20, you can download the data [here](https://data.mendeley.com/datasets/zr7vgbcyr2/1). Do not forget to cite the dataset in your report. 

Go through the data (images and meta-data) that you have available to understand what's available to you and write a brief summary of your findings. For example:


* What types of diagnoses are there, and how do they relate to each other? You can use Google Scholar or other sources, to learn more background about these diagnoses. 
* Is there some missing data? Are there images of low quality? Etc.
* You can select a subset of around 100 images to focus on at the start. The only requirement is that there are at least two categories of images. 
  

## Task 2: Segment images by hand

Create segmentations for your images by hand. You will validate your automatic segmentation methods against these segmentations. 


## Task 3: Segment images automatically


## Task 4: Annotate image features by hand

Search for related work about the Asymmetry and Color features and how they are measured by dermatologists. 

Create an annotation guide for you and your group members, where you discuss at least 5 images together, and decide how to rate their Asymmetry and Color. 

Then split the images, such that each image is annotated by at least two people in your group. Save your annotations in a CSV file, such that there are as many columns as there are different annotators (+ one column for the image name), i.e. do not put annotations of diffferent people into the same column. 

Make sure your CSV file follows the guidelines outlined in Broman & Woo paper "Data organization in spreadsheets".  


## Task 5: Measure the features automatically

Create implementations for the Asymmetry and Color features using related work in image analysis. There will be multiple (similar) ways to measure each feature, if this is the case you can motivate which method you choose. You may use code available online but you need to be able to explain and modify different steps of the code.

To test your implementations, you might want to create ``toy'' images where you already know the results, for example a circle should be less asymmetric than an ellipse, etc. 

Once you are satisfied with your implementations, run them on the real images and save the features in a CSV file. 

Compare the features to your manual measurements by calculating agreement and/or visualizing the measurements. Do you agree with your algorithm? Do you see any other patterns?


## Task 6: Predict the diagnosis

For this task, you can use more images from the same dataset, or use other public data sources that you find. 

Use a cross-validation setup to train different classifiers we studied in class, and evaluate their performance with appropriate metrics. You may also use other ways of evaluating classifiers, for example inspecting images that are classified incorrectly. 

After this, select your best set of features + classifier. Train this classifier on the entire dataset (without cross-validation) and save the trained classifier. 

Then create a function that can classify an external image/mask. You can assume that the mask is provided, you do not need to apply your segmentation method. This function should measure features you used, apply any transformations etc, and finally apply your trained classifier. 

The classifier should output a probability of the image being suspicious, between 0 (healthy) and 1 (not healthy). This will be evaluated on a different set of data, which is not given to you. The external data will have masks available.

## Task 7: Open question

Use the data and your findings so far to formulate, motivate, answer, and discuss another research question of your choice. For example, you can study additional datasets, differences between groups of patients, additional types of features, etc. 


## Hand-in

You must hand in a report (PDF) and your Github repository. 

### Report

TBA: requirements for report

### Github

TBA: requirements for repository


## References

Pacheco, A. G., Lima, G. R., Salomao, A. S., Krohling, B., Biral, I. P., de Angelo, G. G., ... & de Barros, L. F. (2020). PAD-UFES-20: A skin lesion dataset composed of patient data and clinical images collected from smartphones. Data in brief, 32, 106221.

Broman, K. W., & Woo, K. H. (2018). Data organization in spreadsheets. The American Statistician, 72(1), 2-10.
