For the final assignment we are still working with (part of) PAD-UFES-20, you can download the data [here](https://data.mendeley.com/datasets/zr7vgbcyr2/1). Do not forget to cite the dataset in your report. 

In this part we will be working with image features, like Asymmetry. We refer to them as "visual features" hereafter. The "visual features" each group needs to implement this year are: 

* Asymmetry
* Color variability  
* At least one feature from the 7-point checklist by [Argenziano et al](https://pubmed.ncbi.nlm.nih.gov/21175563/), for example blue white veil, dots, globules, lines, network structures, regression structures, vessels. See also slides/references from class on 6 March.
* You can add additional features in the "open question" task


## Task 3: Select the subset of images that you will work with

You will need images with masks to implement (some of) the features. You can use the images you segmented in the first part of the project, and/or collect images from other groups. You can choose to discard some images due to low quality, for example. Please document and motivate your choices in the report. 

## Task 4: Annotate image features by hand

Search for related work about your visual features and how they are measured by dermatologists. 

Create an annotation guide for you and your group members, where you discuss at least 5 images together, and decide how to rate their visual features. 

Then split the images, such that each image is annotated by at least two people in your group. Save your annotations in a CSV file, such that there are as many columns as there are different annotators (+ one column for the image name), i.e. do not put annotations of diffferent people into the same column. 

Make sure your CSV file follows the guidelines outlined in Broman & Woo paper "Data organization in spreadsheets".  

You might want to work on asymmetry and color first, because they are more intuitive, than the other features. 

## Task 5: Measure the features automatically

Create implementations for your visual features using related work in image analysis. There will be multiple (similar) ways to measure each feature, if this is the case you can motivate which method you choose. You may use code available online but you need to be able to explain and modify different steps of the code.

To test your implementations, you might want to create ``toy'' images where you already know the results, for example a circle should be less asymmetric than an ellipse, etc. 

Once you are satisfied with your implementations, run them on the real images and save the features in a CSV file. 

Compare the features to your manual measurements by calculating agreement and/or visualizing the measurements. Do you agree with your algorithm? Do you see any other patterns? You can add a section about this in your report. 


## Task 6: Predict the diagnosis

For this task, you can use more images from the same dataset, or use other public data sources that you find. 

Use a cross-validation setup to train different classifiers we studied in class, and evaluate their performance with appropriate metrics. You may also use other ways of evaluating classifiers, for example inspecting images that are classified incorrectly. 

After this, select your best set of features + classifier. Train this classifier on the entire dataset (without cross-validation) and save the trained classifier. 

Then create a function that can classify an external image/mask. You can assume that the mask is provided, you do not need to apply your segmentation method. This function should measure features you used, apply any transformations etc, and finally apply your trained classifier. 

The classifier should output a probability. For example if you trained a classifier to distinguish melanoma from other classes, your classifier should output a number between 0 (not melanoma) and 1 (melanoma). 

We will evaluate your classifier on a different set of data, which is not given to you. The external data will have masks available.


## Task 7: Open question

Use the data and your findings so far to formulate, motivate, answer, and discuss another research question of your choice. For example, you can study additional datasets, differences between groups of patients, additional types of features (for examples histograms of filtered images), etc. 


## Hand-in

You must hand in a report (PDF) and your Github repository. 

### Report

* Written using LaTeX
* Use the [ACL template](https://www.overleaf.com/latex/templates/template-for-2-columns-acl-proceedings-style/bdxxrbqzsmpv). Another 2-column template like ACM or IEEE is possible, ask if in doubt
* Do not edit the template layout (margins, font sizes etc)
* You MUST have: Introduction, some sections describing related work, methods and results, Discussion, References. See the slides for more descriptions/options for different sections
* References should be at the end. You can use any style (APA, Chicago etc) but the references should be consistent and complete
* Follow the slides for more guidelines, and check the [Coursera course](https://www.coursera.org/learn/sciwrite)
* There is no minimum number of pages of words, you should be concise. In the 2-column layout, I would expect you need 6-8 pages excluding references
  

  
### Github

* Follow the template as much as possible, the README should contain instructions on what is needed to modify to run the code
* Organized file structure and consistent formatting, see materials from 14 Feb lecture for more information
* Contain everything needed to run the code:
    - installation instruction/requirements
    - all files needed to run the code EXCEPT the original images (we have them already), such as any CSV files needed, the saved classifier etc. 
    - how to use your model on new images (outputting the **probabilities)**
* The online repository needs to have the history of the group member contributions (i.e., do not start a new clean repository but clean the existing one with a new commit). In addition, you are allowed to attach this as a file to your submission using the git log command (https://git-scm.com/docs/git-log)  


## References

Pacheco, A. G., Lima, G. R., Salomao, A. S., Krohling, B., Biral, I. P., de Angelo, G. G., ... & de Barros, L. F. (2020). PAD-UFES-20: A skin lesion dataset composed of patient data and clinical images collected from smartphones. Data in brief, 32, 106221.

Broman, K. W., & Woo, K. H. (2018). Data organization in spreadsheets. The American Statistician, 72(1), 2-10.
