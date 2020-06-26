
# Statistical Inference Chapter 2 MATH 1280

## Sampling and data structures
### The sampled data
The aim in statistics is to learn the characteristics of a population on the basis of a sample from the population. An essential part of this analysis involves consideration of variation in the data.

#### Variation in data
To some extent the assessment of variation and the quantification of its contribution to uncertainties in making inference is the statisticians main concern. 

Be aware that if an investigator collects data, the data may vary somewhat from the data someone else is taking for the same purpose. However, if two investigators or more are taking data from the same source and get very different results, it is time to reevaluate their data-collection methods and data recording accuracy.

#### Variations in samples
A sample is often called the number of observations. Random sampling is exactly what it sounds like, sampling from the population at random. Cluster sampling is where one would take parts of a population, like an entire state or and entire classroom of people. If both methods for sampling are used they will probably have different outcomes, if larger sample sizes are taken then the outcome will likely come closer to what the real average is, while still likely having different outcomes. 

#### Frequency
A frequency is the number of times a given datum occurs in a data set. The outcome of dividing an object by a number is a division of each element in the object by the given number. This operation gives us the relative frequencies, which should always sum up to equal 1.

The cumulative relative frequency is the accumulation of previous relative frequencies. To find the cumulative relative frequency of the current value, add all the previous relative frequencies to the relative frequency of the current value. Alternatively we may apply the function "cumsum" to the sequence of relative frequencies.

Using `data.frame` creates an R data frame, which is similar to a Pandas DataFrame and is the standard way of storing statistical data.

#### Critical evaluation
Common problems that occur in data that one should be aware of:
* Problems with samples: A sample should be representative of a population, if it is not it is biased, and biased samples can produce inaccurate and invalid results.
* Data quality: Inaccurate handling of forms, mistakes in the input of data. 
* Self-selected samples: Responses only by people that choose to respond are often biased.
* Sample size issues: Samples that are too small may be unreliable.
* Undue influence: Collecting data or asking questions in a way that influences the response.
* Causality: A relationship between two variables does not mean that one causes the other to occur. They may be correlated.
* Self-funded or self-interest studies: A study performed by a person or organization in order to support their claim.
* Misleading use of data: Improperly displayed graphs and incomplete data.
* Confounding (Confusing): When the effects of multiple factors on a response cannot be separated. 

### Reading data into R
#### Saving the file and setting the working directory
Use the following command to read a csv file and save it into R as a data frame:
```r
ex.1 <- read.csv("ex1.csv")
```
A URL can be used as an argument for the `read.csv` function.

When the values that of the variable are numerical we say that is is a quantitative or a numerical variable. On the other hand if the variable has qualitative or level (tiered, categorical) values we say that it is a factor. For example, `sex` is a factor and height is a numeric variable.


#### Data types
Rows in a table, csv or data frame are called observations and correspond to subjects.

The columns of R data frames represent variables, or measurements recorded, for each subject in the sample. R associates with each variable a type that characterizes the content of the variable. The two major types are:
* Factors or qualitative data. The type being "factor".
* Quantitative data. The type being "numeric".

Qualitative data are not as widely used as quantitative data because many numerical techniques do not apply to the qualitative data. Fro example, it does not make sense to find an average hair color or blood type.

Quantitative data is numerical data. It can be either discrete or continuous. All data that is the result of counting is called quantitative discrete data, and can only take certain numerical values.

Quantitative continuous data is measured on a continuous scale, such as weight or volume.

R saves variables that contain non-numeric values as factors. Otherwise, the variables are saved as numeric. The variable type is important because different statistical methods are applied to different data types. One should make sure that the variables that are analyzed have the appropriate type. Especially that factors using numbers to denote the levels are labeled factors. Otherwise R will treat them as quantitative data.

## Glossary
* Population: The collection, or set, of all individuals, objects, or measurements whose properties are being studied.
* Sample: A portion of the population understudy. A sample is representative if it characterizes the population being studies.
* Frequency: The number of times a value occurs in the data.
* Relative frequency: The ratio between the frequency and the size of data.
* Cumulative relative frequency: The term applies to an ordered set of data values from smallest to largest. The cumulative relative frequency is the sum of the relative frequencies for all values that are less than or equal to the given value.
* Data frame: A tabular format for storing statistical data. Columns correspond to variables and rows correspond to observations.
* Variable: A measurement that may be carries out over a collection of subjects. The outcome of the measurement may be numerical, which produces a quantitative variable, or it may be non-numeric, in which case a factor is produced.
* Observation: The evaluation of a variable (or variables) for a given subject.
* CSV files: A digital format for storing data frames.
* Factor: Qualitative data that is associated with categorization or the description of an attribute.
* Quantitative: Data generated by numerical measurements

## Discuss in the forum
It is sensible so that all the various tools for quantitative data analysis are made available to use that would be otherwise unable to be used with a string variable for instance. This is sometimes called one-hot encoding, and creating dummy variables.