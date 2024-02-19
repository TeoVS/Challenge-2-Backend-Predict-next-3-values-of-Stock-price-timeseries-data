# Challenge-2-Backend-Predict-next-3-values-of-Stock-price-timeseries-data

## Application

This is a Python application that can select CSV files from folders, create a new data frame according to the instructions provided, and output a CSV file with the modifications. 
I decided to follow the algorithm provided but I modified the way you input information, changing it from being able to input only the values 1 or 2 to being able to write the name of the deal you want without the extension (".csv"). I accomplished that by first looking for all the files that contain the extension and then storing them in a dictionary in lowercase so no later problems should appear when the user tries to type the deal when prompted (this was made redundant when the user is prompted for the deal), secondly after the user inputs the deal name the "pandas" functionality comes when the function reads the CSV file, knowing it has no header it adds the 3 headers and another function that transforms the time that is a string under a "datetime" and also formatting accordingly.
The first defined function is the one that selects the sample by firstly setting a range starting from 0 and having a maximum of "the length of the data frame - 10" because for example if the data frame contains 100 points it shouldn't be able to pick the random one to be the point 99 because there would be no 10 consecutive points to enumerate. This function returns the 10 points necessary for the prediction.
The second function is the one that applies the prediction logic and writes the new CSV file accordingly. Firstly we define with "n" the 10 points obtained above, with "n1" the second largest number (first prediction), with "n2" half the difference between "n" and "n1" added to "n" (second prediction) and lastly with "n3" the 1/4th the difference between "n1" and "n2" added to "n2" (third and last prediction). Up next we write the rows using "pandas" function where the name remains unchanged from the previous row, the date takes the previous information and adds days accordingly, making the dates continuous, and lastly, the stock price is updated using the newly defined variables, the price is also rounded to 2 decimals, and then the function returns the total. 

 
## Installation

Download the application from GitHub
After downloading the application drag and drop the Python file next to the folders that contain CSV files (a zip file was provided for the task that contained 3 simple folders named "LSE", "NASDAQ", and "NYSE" with multiple CSV files within) open up the app by double-clicking it, click on the terminal tab at the bottom of the screen, and then click next to the path, use the package manager pip ("pip install pandas") to install the package called "pandas" but others packages were used that did not require installation such as "os" and "glob". After everything is installed there is one modification that needs to be done to the code for it to work while having the file browser open, copy the location of the 3 files and the Python app and paste at line 5 "stocksPath = "your\\path\\here" after the equal sign making sure you keep the quotations and add an extra "\" every time you see one from the path you have copied.
After these steps, the app should be ready to run.

## Usage

After the installation process, all that is left is to run the application by pressing "Ctrl" + "Alt" + "N", you should be prompted with a text saying "Files found:" followed by a dictionary containing all the CSV paths found by the app. Next up you will be prompted with "Deal name:" where you should input the name of the deal (either uppercase or lowercase works as long as it is present within the folders) that you want to apply the prediction function without the extension (in this case ".csv"). Following this, a new file was created called "deal_out.csv" that contains the requirements (in this case the 10 consecutive points starting from a random one plus the extra 3 points using the prediction algorithm provided)

## Materials/libraries used in the making of this project


[OS](https://docs.python.org/3/library/os.html)
[GLOB](https://docs.python.org/3/library/glob.html)
and multiple links from [pandas](https://pandas.pydata.org/docs/user_guide/) that explain the functionality like [concat](https://pandas.pydata.org/docs/user_guide/merging.html#concat), [data frame iloc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html), [datetime](https://pandas.pydata.org/docs/user_guide/timeseries.html), [random sample](https://pandas.pydata.org/docs/whatsnew/v0.16.1.html#sample) 
