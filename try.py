from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import time
import schedule
import mplcursors
import os
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))




# Initialize empty lists for x (dates) and y (population growth)
dates = []
population_growth = []

# current_population = 0
# births_today = 0
# deaths_today = 0
# deaths_year_todate = 0
# population_growth_today = 0
# current_males = 0
# current_females = 0
# births_year_todate = 0

def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center')

# def piechart():
#     try:
        
#         labels = 'Males', 'Females'
#         numbers = [current_males, current_females]
#         fig, ax = plt.subplots()
#         ax.pie(numbers, labels=labels, autopct='%1.1f%%')
#         # plt.show(block=False)  # Show the plot in non-blocking mode
#         # plt.pause(1)  # Pause for 1 seconds
#         plt.savefig('./templates/images/mf_ratio.png')

#     finally:
#         driver.quit()  # Close the WebDriver
#         plt.close()  # Close the plot window
#         # time.sleep(10)

# def linechart():
#     try:
#         birth_rate = (births_year_todate/current_population)*1000
#         x = ['2019','2020','2021','2022','2023']
#         y = [17.806, 17.592, 17.377, 17.163, birth_rate]
#         plt.plot(x,y, marker='o')
#         plt.xlabel("Year")
#         plt.ylabel("Birth Rate")
#         plt.yticks(range(15,int(birth_rate+2.0)))
#         # plt.show(block=False)
#         # plt.pause(2)
#         plt.savefig('./templates/images/birth_rate.png')
    

#     finally:
#         driver.quit()
#         plt.close()
#         # time.sleep(10)


def func():
    
    try:
        # Create a Chrome WebDriver with headless mode
        options = Options()
        options.add_argument("--headless")

        driver = webdriver.Chrome(options=options)

        driver.implicitly_wait(0)
        driver.get("https://countrymeters.info/en/India")


        current_population = driver.find_element(By.ID, "cp1").text
        births_today = driver.find_element(By.ID, "cp7").text
        deaths_today = driver.find_element(By.ID, "cp9").text
        deaths_year_todate = driver.find_element(By.ID, "cp8").text
        population_growth_today = driver.find_element(By.ID, "cp13").text
        population_growth_today = population_growth_today.replace(',','')
        population_growth_today = float(population_growth_today)
        current_males = driver.find_element(By.ID, "cp2").text
        current_females = driver.find_element(By.ID, "cp3").text
        births_year_todate = driver.find_element(By.ID, "cp6").text
        current_males = str(current_males) # converted this var to string
        current_males = current_males.replace(',','') # removed , from str
        current_males = float(current_males) # converted string to float
        current_females = str(current_females)
        current_females = current_females.replace(',','')
        current_females = float(current_females)
        current_population = str(current_population)
        current_population = current_population.replace(',', '')
        current_population = float(current_population)
        deaths_year_todate = deaths_year_todate.replace(',', '')
        births_year_todate = births_year_todate.replace(',', '')
        births_year_todate = float(births_year_todate)


        
        #Mortality Rate of 2023 till now
        mortality_rate = round(float(deaths_year_todate)/current_population,4)
        # print(mortality_rate)
        years = ['2023', '2022', '2021', '2020', '2019']
        pop = [current_population, 1417173173, 1393409038, 1396387127, 1383112050]

        # Bar Graph plotted 
        plt.bar(years, pop, width=0.7)
        addlabels(years, pop)
        plt.xlabel("Years")
        plt.ylabel("Population")
        plt.title("Comparison of population in different years")
        plt.yticks([0,2e9])

        # plt.show(block=False)  # Show the plot in non-blocking mode
        # plt.pause(2)  # Pause for 2 seconds
        plt.savefig('./templates/images/pop.png') #saved the file to this directory
        plt.close()

        #Pie Chart
        labels = 'Males', 'Females'
        numbers = [current_males, current_females]
        fig, ax = plt.subplots()
        ax.pie(numbers, labels=labels, autopct='%1.1f%%')
        # plt.show(block=False)  # Show the plot in non-blocking mode
        # plt.pause(1)  # Pause for 1 seconds
        plt.savefig('./templates/images/mf_ratio.png')
        plt.close()


        #Population Growth Graph
        current_date = datetime.now().strftime('%Y-%m-%d')

        # Append the new data to the lists
        if not dates or current_date != dates[-1]:
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
        # for i, (date, growth) in enumerate(zip(dates, population_growth)):
        #     plt.annotate(f'{growth}', (date, growth), textcoords="offset points", xytext=(0, 10), ha='center')

        # # Show the graph with hover functionality
        # fig = plt.gcf()

        # def on_hover(event):
        #     for i, (date, growth) in enumerate(zip(dates, population_growth)):
        #         contains, _ = fig.gca().get_children()[0].contains(event)
        #         if contains:
        #             fig.gca().texts[i].set_alpha(1)
        #         else:
        #             fig.gca().texts[i].set_alpha(0)

        #     plt.draw()

        # fig.canvas.mpl_connect('motion_notify_event', on_hover)

        plt.savefig('./templates/images/pop_growth.png')
        plt.close()

        #Birth Rate Graph
        birth_rate = round((births_year_todate/current_population)*1000,4)
        x = ['2019','2020','2021','2022','2023']
        y = [17.806, 17.592, 17.377, 17.163, birth_rate]
        plt.plot(x,y, marker='o')
        plt.xlabel("Year")
        plt.ylabel("Birth Rate")
        plt.yticks(range(15,int(birth_rate+2.0)))
        # plt.show(block=False)
        # plt.pause(2)
        plt.savefig('./templates/images/birth_rate.png')
        plt.close()




        template = env.get_template('template.html')
        rendered_html = template.render(current_population=current_population, population_growth_today=population_growth_today,mortality_rate=mortality_rate, birth_rate=birth_rate)


        output_file_path = 'templates/pages/new2.html'

        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        with open(output_file_path,'w') as output_file:
            output_file.write(rendered_html)


        print(f'Rendered HTML saved to {output_file_path}')

    finally:
        driver.quit()  # Close the WebDriver
        plt.close()  # Close the plot window



# Function to update the graph
# def update_graph():
    # Get the current date and population growth (you need to replace this with your data retrieval logic)
    
    # plt.show()
    # plt.pause(2)

# Schedule the update to occur every 24 hours at 12 AM
# schedule.every().day.at("00:00").do(update_graph)

while True:
    func()
    # piechart()
    # linechart()
    # schedule.run_pending()
    # update_graph() 
