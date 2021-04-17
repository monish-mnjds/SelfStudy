### 1. Tell me about yourself.
**NOTE: Please Note the below are the sample answers. You can alter it to suite your profile.**
* I am Ram.
* I Graduated in the year-2015 in Electronics and Communication engineering.
* After Graduation I got an opportunity to work with IBM.
* In IBM, I started working as a Manual/Automation test engineer. And I was working on online shopping application.
* I worked in IBM for about 2 years and then I got an opportunity to work HP. 
* From past 1 year I am working in HP as Senior Automation test engineer.

### 2. Explain about your project.
**NOTE: Please keep that the explanation about project brief and crisp. Do not go in-depth and try to explain different features of the application.**
* I am working for American Airlines account/client.And i am working on online shopping cart application.
* This application allows the AA employees to shop electronic gadgets online in discounted price.
* I am completely into automating this online shopping portal.
 
### 3. Explain the framework or what kind of framework you are using.
* We are using DataDriven framework with POM approach or design pattern with pytest unittest framework.
* Explain the framework structure. (Like Data, Library, POM, Tests, Reports, Screenshot)
* All common functionalities of the application would be maintained in a separate POM class called "BasePage".
* All other POM classes will inherit "BasePage".
* Similarly the common functionalities for all the test scripts would be maintained in a separate class called "BaseTest". (Like Launching browser, navigating to URL, login, logout and closing the browser)
* All the test scripts will inherit from "BaseTest". So we do not have to write the code for common functionalities as mentioned in the above step in each and every test script. This avoids duplication of code.
* Explain how you are maintaining the test data and locators. Like, for each page we create a separate work sheet and maintain all the locators in that worksheet and we maintain separate test data sheet where we divide the test data based on modules. We maintain separate worksheet in excel for each module. The test data required for all the test cases for each module will be maintained in the corresponding worksheet.(Do not start explaining the logic of how data and locators are being read from excel sheet).
* All generic functions for clicking on element, entering text, selecting item from the list box would be maintained in a separate class called "SeleniumWrapper".
* We have written a wait decorator for Synchronisation. Each generic function is being decorated with wait decorator. So, before performing any action on a web element, the decorator checks if the element is visible and enabled.
* To run the test suite, we have written a driver script. We have written a logic to read the excel and get all the test scripts which has "Execute" column "Yes" and execute the test suite.
* We can run all the failed test's using command **pytest --last-failed --last-failed-no-failures none**  
* HTML reports will be generated in "Reports" folder and all the screenshots will be taken in "Screenshots" folder.

### 4. What are your current roles and responsibility in the project.
* Automation script development and execution, reporting etc.
* Interacting with developers and manual testers in understanding the functionality better, reproducing the defects found during automation, etc. (Please add if you need to add any other responsibility)

### 5. What are the challenges that you have faced in your project while automating.
* The main challenge is automating in Agile environment. Where the objects and the application scenario flows are constantly changing.
* Could not verify the order confirmation email after placing the order. (Verify the contents of the email).
* Could not verify the exact image of the product that is being added to the cart (Image Comparison).
* Forgot Password functionality, we could not read the password that was being sent to the email.
* We had to wait for the user data required for registration or for creating user profile from the clients. We could not create our own dummy data or mock data for user registration.
* Could not automate taking print out of the invoice.
* We could not verify the contents of the invoice generated in pdf.
* Could not verify recently viewed products.
* Add any other challenges that you have faced in your project.

### 6. What are the bugs that you found through automation
* Even though the product was out of stock we were able to add the product to the cart.
* Total was not getting calculated properly if we add more than one product.
* Items were not getting sorted property.
* While filtering the product for a particular category, the application was displaying products of other categories as well.

### 7. Did you find any Blocker or show stopper issue through automation.
* Our application is completely stable and through automation we could not find out any blocker issue as such.

### 8. How test case allotment happens your project for day to day automation.
* Each user story is broken down into different test cases.
* Lead assigns test cases based on complexity and experience in the project.
* Test cases are catagorised based on number of steps. If the test case has less than 4-6 steps  
then it is catagorised as simple, if the steps are between 8-12 steps then it is catagorised as medium complexity and if the steps are more than 12 steps, then it is catagorised as complex.