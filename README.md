
# Uni Marks Calculator

This repository contains a Python script that implements a Uni Marks Calculator using Streamlit. The application allows users to calculate their weighted marks based on input values for various subjects and assessments. This README provides a brief overview of the project and instructions on how to use the application.

## Introduction

The Uni Marks Calculator is a Streamlit web application that enables students to calculate their overall marks for a set of subjects with different credit weights and assessments. The application is useful for individuals pursuing courses or degrees where different subjects have varying credit values and assessment weights. The current parameters are set for people studying MSc Data Science at the University of Sheffield.

The application has two groups of subjects:

-   Group 1: Subjects with multiple assessments, each having its own weightage and a final credit value.
-   Group 2: Subjects with only one assessment, but each subject has its own credit value.

## Installation

To run the Uni Marks Calculator on your local machine, follow these steps:

1.  Clone this GitHub repository to your local machine using the following command:
2.  Change into the project directory:
3.  Install the required dependencies using `pip`:
```bash
pip install streamlit
``` 

## Usage

To use the Uni Marks Calculator, execute the following command in the project directory:

```bash
streamlit run app.py
```

The command will launch a local Streamlit server, and you will be provided with a URL to access the application in your web browser.

## Customization

The Uni Marks Calculator is designed to handle two groups of subjects. However, you can easily customize the subjects and their properties. Here's how you can do it:

1.  Open the `weighted_marks_estimator.py` script in your preferred text editor.
    
2.  Modify the lists `subjects_1` and `subjects_2` to include the names of your desired subjects in Group 1 and Group 2, respectively.
    
3.  Customize the default parameters for credits and weights in `default_subjects_1_credits`, `default_subjects_1_weights1`, `default_subjects_1_weights2`, `default_subjects_2_credits`, and `default_subjects_2_weights`. Make sure the lists have the same length as the subjects you defined.
    
4.  Run the application using the instructions provided in the `Usage` section to see the updated subjects and parameters.
    

## Contributing

Contributions to this project are welcome! If you find any issues or have ideas for improvements, please feel free to create a GitHub issue or submit a pull request with your proposed changes.

When contributing, please follow the existing coding style and ensure that your changes do not break the existing functionality. Moreover, kindly document any new features or major changes you introduce.

## License

This project is licensed under the [MIT License](https://en.wikipedia.org/wiki/MIT_License). You are free to use, modify, and distribute the code as per the terms of this license.

----------

Enjoy using the Uni Marks Calculator! If you have any questions or need assistance, feel free to reach out to the project maintainers. Happy learning!
