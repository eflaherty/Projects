using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System.Threading;

class Program
{
    static void Main()
    {
        IWebDriver driver = new ChromeDriver();

        string name_url = "http://testing.todorvachev.com/selectors/name/";
        string id_url = "http://testing.todorvachev.com/selectors/id/";
        string class_url = "https://testing.todorvachev.com/class-name/";
        string css_url = "https://testing.todorvachev.com/css-path/";
        string xpath_url = "https://testing.todorvachev.com/xpath/";
        string ID = "testImage";
        string class_name = "testClass";
        string css_path = "#post-108 > div > figure > img";
        string x_path = "//*[@id=\"post-108\"]/div/figure/img";

        // find element by name
        driver.Navigate().GoToUrl(name_url);
        IWebElement element = driver.FindElement(By.Name("myName"));

        // find element by ID
        driver.Navigate().GoToUrl(id_url);
        IWebElement IDElement = driver.FindElement(By.Id(ID));
        
        // find element by class name
        driver.Navigate().GoToUrl(class_url);
        IWebElement classNameElement = driver.FindElement(By.ClassName(class_name));
        // Print out the text of the element
        Console.WriteLine(classNameElement.Text);

        // find element by CSS Path
        driver.Navigate().GoToUrl(css_url);
        IWebElement cssPathElement = driver.FindElement(By.CssSelector(css_path));

        // find element by X Path
        driver.Navigate().GoToUrl(xpath_url);
        IWebElement xPathElement = driver.FindElement(By.XPath(x_path));

        if (element.Displayed)
        {
            GreenMessage("Yes! I can see the element, it's right there!!");
        }
        else
        {
            RedMessage("Well, something went wrong, I couldn't see the element!");
        }

        if (IDElement.Displayed)
        {
            GreenMessage("Yes! I can see the ID element, it's right there!!");
        }
        else
        {
            RedMessage("Well, something went wrong, I couldn't see the ID element!");
        }

        if (classNameElement.Displayed)
        {
            GreenMessage("Yes! I can see the Class Name element, it's right there!!");
        }
        else
        {
            RedMessage("Well, something went wrong, I couldn't see the Class Name element!");
        }

        if (cssPathElement.Displayed)
        {
            GreenMessage("Yes! I can see the CSS Path element, it's right there!!");
        }
        else
        {
            RedMessage("Well, something went wrong, I couldn't see the CSS Path element!");
        }

        if (xPathElement.Displayed)
        {
            GreenMessage("Yes! I can see the X Path element, it's right there!!");
        }
        else
        {
            RedMessage("Well, something went wrong, I couldn't see the X Path element!");
        }
        
        driver.Quit();
    }

    private static void GreenMessage(string message)
    {   
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine(message);
        Console.ForegroundColor = ConsoleColor.White;
    }
    private static void RedMessage(string message)
    {   
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine(message);
        Console.ForegroundColor = ConsoleColor.White;
    }
}