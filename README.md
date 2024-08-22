# linear-data-regression
The python script is used to test two methods of calculating the correlation coefficient and the regression line for a set of bivariate data.
## Method 1
This method uses the following formula for the calculation of correlation coefficient:
$$r=\frac{1}{n-1}\sum_{i=1}^{n} \frac{(x_i-\bar{x})(y_i-\bar{y})}{\sigma_x\cdot \sigma_y}\$$
Then the gradient is calculated as:
$$m=r\cdot \frac{\sigma_y}{\sigma_x}$$
## Method 2
For the second method, we first calculate the gradient of the line using:
$$m=\frac{\overline {x \cdot y} -\bar x \cdot \bar y}{\overline {x^2}- \bar x ^2}$$
Then correlation coefficient is calculated by:
$$r=m \cdot \sqrt\frac{\overline {x^2}- \bar x ^2}{\overline {x \cdot y} -\bar x \cdot \bar y}$$
Though both methods differ in calculation, the end result is same and the correlation coefficient, gradient, and the regression line is exactly the same for the same set of data points.
## Requirements
* matplotlib
* numpy
Install them using:
`pip install matplotlib numpy`
## Usage
1. Run the script.
2. Input data pairs in the form x y.
3. Enter -1 to terminate input and display statistics and plots.

