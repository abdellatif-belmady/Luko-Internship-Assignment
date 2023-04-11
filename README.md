# Luko-Internship-Assignment

This code is a Python script using the Selenium library to automate web navigation tests. It uses the Chrome browser to navigate to the website [https://devnoscope.luko.eu/my-account/sign-in?lang=en](https://devnoscope.luko.eu/my-account/sign-in?lang=en). The test aims to add a credit card.

The script starts by importing the necessary modules and initializing the **Chrome driver**. Then, it creates a `CreditCardTest` class that inherits from the **unittest.TestCase** class. The `setUp` method is called before each test and allows to log in to the website using the driver's `get` method and the link [https://devnoscope.luko.eu/my-account/sign-in?lang=en](https://devnoscope.luko.eu/my-account/sign-in?lang=en).

The script waits for 5 seconds for the page to fully load, then clicks on the **cookies** button to accept the cookies. Then, it defines a `test_add_credit_card` method to add a credit card.

The test starts by logging into the system using HTML elements such as ***username***, ***password***, and ***login_button***. Then, the navigation menu is searched using the CSS selector **#side-menu-nav** and the corresponding elements are stored in the **nav_menu** variable. The script then iterates over the menu elements and clicks on the **Payment methods** element.

Then, it searches for the **Add payment method** button and clicks on it. It then searches for the elements of the **Credit card** menu and enters the credit card details such as the ***card number***, ***expiration date***, and ***CVC*** code. Finally, it clicks on the **Authorize** and **Submit** buttons to add the credit card.

The `tearDown` method is called after each test and allows to close the browser. The script uses `unittest.main()` to run the tests.