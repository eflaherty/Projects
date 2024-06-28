﻿using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;
using System.Threading;

class EntryPoint
{
    static IWebDriver driver = new FirefoxDriver();
    static IWebElement textBox;
    static IWebElement checkBox;
    static IWebElement radioButton;
    static IWebElement dropDownMenu;
    static IWebElement elementFromTheDropDownMenu;
    static IAlert alert;
    static IWebElement image;

    static void Main()
    {
        string text_url = "https://testing.todorvachev.com/text-input-field/";
        string check_url = "https://testing.todorvachev.com/check-button-test-3/";
        string drop_url = "https://testing.todorvachev.com/drop-down-menu-test/";
        string alert_url = "https://testing.todorvachev.com/alert-box/";
        string[] option = {"1", "3", "5"};
        //string checkBoxSelector = "#post-33 > div > p:nth-child(8) > input[type=checkbox]:nth-child(" + option + ")";
        string radio_url = "https://testing.todorvachev.com/radio-button-test/";
        string radioButtonSelector = "#post-10 > div > form > p:nth-child(6) > input[type=radio]:nth-child(" + option + ")";
        string dropDownMenuElements = "#post-6 > div > p:nth-child(6) > select > option:nth-child(3)";

        // TEXT BOX
        driver.Navigate().GoToUrl(text_url);
        textBox = driver.FindElement(By.Name("username"));
        textBox.SendKeys("TEST TEXT"); // enter text in text box input field
        Thread.Sleep(3000); // sleep for 3000 milliseconds

        // Read the text from the textbox from the variable "value" where it's
        // stored and print to console
        Console.WriteLine(textBox.GetAttribute("value"));
        Thread.Sleep(3000); // sleep for 3000 milliseconds
/* 
        // CHECK BOX
        driver.Navigate().GoToUrl(check_url);
        for (int i = 0; i < option.Length; i++)
        {
            // Check box by CSS Selector
            checkBox = driver.FindElement(By.CssSelector("#post-33 > div > p:nth-child(8) > input[type=checkbox]:nth-child(" + option + ")"));
            checkBox.Click();
            Thread.Sleep(3000); // sleep for 3000 milliseconds
            
            if (checkBox.GetAttribute("checked") == "true")
            {
                Console.WriteLine(checkBox.GetAttribute("value"));
                Console.WriteLine("The " + (i+1) + " checkbox is checked.");
            }
            else
            {
                Console.WriteLine(checkBox.GetAttribute("value"));
                Console.WriteLine("The checkbox is NOT checked.");
            }

            Thread.Sleep(3000); // sleep for 3000 milliseconds
        }
        
        // RADIO BUTTON
        driver.Navigate().GoToUrl(radio_url);
        for (int i = 0; i < option.Length; i++)
        {
            radioButton = driver.FindElement(By.CssSelector(radioButtonSelector));

            if (radioButton.GetAttribute("checked") == "true")
            {
                Console.WriteLine(radioButton.GetAttribute("value"));
                Console.WriteLine("The " + (i+1) + " radio button is checked.");
            }
            else
            {
                Console.WriteLine(radioButton.GetAttribute("value"));
                Console.WriteLine("This is one of the radio options that was not chosen.");
            }

            Thread.Sleep(3000); // sleep for 3000 milliseconds
        }  */       
 
         // DROP DOWN MENU
        driver.Navigate().GoToUrl(drop_url);
        dropDownMenu = driver.FindElement(By.Name("DropDownTest"));

        Console.WriteLine("The selected value is: " + dropDownMenu.GetAttribute("value"));
        elementFromTheDropDownMenu = driver.FindElement(By.CssSelector(dropDownMenuElements));
        
        Console.WriteLine("The third option from the drop down menu is: " + elementFromTheDropDownMenu.GetAttribute("value"));
        elementFromTheDropDownMenu.Click();
        Console.WriteLine("The selected value after clicking is " + dropDownMenu.GetAttribute("value"));
        
        Thread.Sleep(3000); // sleep for 3000 milliseconds

        for (int i = 1; i <= 4; i++)
        {
            dropDownMenuElements = "#post-6 > div > p:nth-child(6) > select > option:nth-child(" + i + ")";
            elementFromTheDropDownMenu = driver.FindElement(By.CssSelector(dropDownMenuElements));

            Console.WriteLine("The " + i + " option from the drop down menu is: " + elementFromTheDropDownMenu.GetAttribute("value"));
        }

        Thread.Sleep(5000);

        // ALERT BOX
        driver.Navigate().GoToUrl(alert_url);

        alert = driver.SwitchTo().Alert();
        Console.WriteLine(alert.Text);
        // Click on OK to accept alert
        alert.Accept();
        image = driver.FindElement(By.CssSelector("#post-119 > div > figure > img"));

        try
        {
            if (image.Displayed)
            {
                Console.WriteLine("The alert was successfully accepted and I can see the image!");
            }
        }
        catch(NoSuchElementException)
        {
            Console.WriteLine("Something went wrong!!!");
        }

/*         IWebElement email = new WebDriverWait(Driver, TimeSpan.FromSeconds(3)).Until(ExpectedConditions.ElementIsVisible(By.Id("email")));
        email.SendKeys("MyName");
        email.Submit(); */

        // textbox
        // string url = "https://testing.todorvachev.com/category/special-elements/";

//        textBox = driver.FindElement(By.Name("username"));        

        driver.Quit();
    }
}
