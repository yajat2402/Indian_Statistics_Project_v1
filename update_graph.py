import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import schedule
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import mplcursors

# Create a Chrome WebDriver with headless mode
options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(0)
driver.get("https://countrymeters.info/en/India")

# Initialize empty lists for x (dates) and y (population growth)
dates = []
population_growth = []

try: 
    population_growth_today = driver.find_element(By.ID, "cp13").text
    population_growth_today = population_growth_today.replace(',','')
    population_growth_today = float(population_growth_today)

except: 
    print("Error")


# Function to update the graph
def update_graph():
    # Get the current date and population growth (you need to replace this with your data retrieval logic)
    current_date = datetime.now().strftime('%Y-%m-%d')
    # population_growth_today =  # Replace with your data retrieval logic

    # Append the new data to the lists
    dates.append(current_date)
    population_growth.append(population_growth_today)

    # Keep only the last 10 dates in the array
    if len(dates) > 10:
        dates.pop(0)
        population_growth.pop(0)

    # Plot the data
    plt.plot(dates, population_growth, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Population Growth')
    plt.title('Population Growth Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.savefig('population_growth_graph.png')  # Save the graph to a file (optional)


    # Annotate points with population growth
    for i, (date, growth) in enumerate(zip(dates, population_growth)):
        plt.annotate(f'{growth}', (date, growth), textcoords="offset points", xytext=(0, 10), ha='center')

    # Show the graph with hover functionality
    fig = plt.gcf()

    def on_hover(event):
        for i, (date, growth) in enumerate(zip(dates, population_growth)):
            contains, _ = fig.gca().get_children()[0].contains(event)
            if contains:
                fig.gca().texts[i].set_alpha(1)
            else:
                fig.gca().texts[i].set_alpha(0)

        plt.draw()

    fig.canvas.mpl_connect('motion_notify_event', on_hover)
    plt.show()
    # plt.pause(2)

# Schedule the update to occur every 24 hours at 12 AM
# schedule.every().day.at("00:00").do(update_graph)

# # Run the scheduler
# while True:
#     schedule.run_pending()
#     time.sleep(1)


update_graph()