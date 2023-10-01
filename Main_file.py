import requests
from bs4 import BeautifulSoup
import csv
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import IndicesCalculation

    # Get the data from the table
def calculate_author_indices():
    # Get the data from the table
    data = []
    for item in table.get_children():
        values = table.item(item, 'values')
        data.append(values)

    # Separate data into lists for each column
    pubid = [int(item[0]) for item in data]  # Publication Id
    column2 = [item[1] for item in data]  # Title
    citation = [int(item[2]) for item in data]  # Citation
    pubyear = [int(item[3]) for item in data]  # Year
    author = [int(item[4]) for item in data]  # Authors

    # Calculate Author Indices and store them in a dictionary
    author_indices={
        'Total Publication': IndicesCalculation.publication_count(pubid),
        'Total Citation': IndicesCalculation.citation_count(citation),
        'Total Years': IndicesCalculation.total_years(pubyear),
        'Citation/Years': IndicesCalculation.cite_per_years(citation, pubyear),
        'Citation/Paper': IndicesCalculation.cite_per_paper(citation, pubid),
        'Author/Paper': IndicesCalculation.Author_paper(pubid, author),
        'Cites/Author': IndicesCalculation.cites_author(citation, pubid, author),
        'Paper/Author': IndicesCalculation.papers_author(pubid, author),
        'H index': IndicesCalculation.h_index_f(citation, pubid),
        'G index': IndicesCalculation.g_index_f(citation, pubid),
        'H2 index': IndicesCalculation.h2_index_f(citation, pubid),
        'W index': IndicesCalculation.w_index_f(citation, pubid),
        'F index': IndicesCalculation.f_index(citation, pubid),
        'T index': IndicesCalculation.t_index(citation, pubid),
        'Woginger index': IndicesCalculation.woginger_index(citation, pubid),
        'H core citation': IndicesCalculation.h_core_citation(citation, pubid),
        'M index': IndicesCalculation.m_index(citation, pubid),
        'Tappered h index': IndicesCalculation.tappered_h_index(citation, pubid),
        'Maxprod index': IndicesCalculation.Maxprod_index(citation, pubid),
        'Wu index': IndicesCalculation.wu_index(citation, pubid),
        'PI index': IndicesCalculation.pi_index(citation, pubid),
        'Weighted h index': IndicesCalculation.weighted_h_index(citation, pubid),
        'Gh index': IndicesCalculation.Gh_index(citation, pubid),
        'A index': IndicesCalculation.A_index(citation, pubid), 
        'R index': IndicesCalculation.R_index(citation, pubid),
        'Rm index': IndicesCalculation.Rm_index(citation,pubid),
        'X index': IndicesCalculation.x_index(citation,pubid), 
        'H2 upper index': IndicesCalculation.h2upper_index(citation, pubid),
        'H2 center index': IndicesCalculation.h2center_index(citation, pubid),
        'H2 lower index': IndicesCalculation.h2lower_index(citation, pubid), 
        'K dash index': IndicesCalculation.k_dash_index(citation, pubid),
        'I10 index': IndicesCalculation.iten_index(citation, pubid),
        'Normalized h index': IndicesCalculation.normalized_h_index(citation, pubid),
        'Platinium h index': IndicesCalculation.platinium_h_index(citation, pubid, pubyear),
        'M Qoutient index': IndicesCalculation.m_qoutient_index(citation, pubid, pubyear),
        'HI index': IndicesCalculation.HI_index(citation, pubid, author),
        'Aw index': IndicesCalculation.AW_index(citation, pubid, pubyear),
        'Ar index': IndicesCalculation.Ar_index(citation, pubid, pubyear),
        'V index': IndicesCalculation.v_index(citation, pubid, pubyear),
        'Hm index': IndicesCalculation.hm_index(citation, pubid, author),
        'Gm index': IndicesCalculation.gm_index(citation, pubid, author),
        'Hf index': IndicesCalculation.hf_index(citation, pubid, author),
        'gf index': IndicesCalculation.gf_index(citation, pubid, author),
        'gF index': IndicesCalculation.gF_index(citation, pubid, author),
        'Hi index': IndicesCalculation.hi_index(citation, pubid, author),
        'K norm index': IndicesCalculation.k_norm_index(citation, pubid, author),
        'W norm index': IndicesCalculation.w_norm_index(citation, pubid, author),
        'P index': IndicesCalculation.P_index(citation, pubid),
        'Q2 index': IndicesCalculation.q_sq_index(citation, pubid),
        'E index': IndicesCalculation.e_index(citation, pubid),
        'Pure h index': IndicesCalculation.pure_h_index(citation, pubid, author),
        'fractional g index': IndicesCalculation.fractional_g_index_f(citation, pubid, author),        
        'fractional h index': IndicesCalculation.fractional_h_index_f(citation, pubid, author),        
        'AWCR index': IndicesCalculation.AWCR_index_f(citation, pubid, pubyear),   
        'K index': IndicesCalculation.k_index(citation, pubid, author),
        'h dash index': IndicesCalculation.h_dash_index(citation, pubid),   
        'hl norm': IndicesCalculation.hl_norm(citation, pubid,  author),        
        'hc index': IndicesCalculation.hc_index(citation, pubid, pubyear),
        'ha index': IndicesCalculation.ha_index(citation, pubid, pubyear),   
        'hi index': IndicesCalculation.hi_index_s(citation, pubid,  author),        
        'Rational h index': IndicesCalculation.rational_h_index(citation, pubid),
        'Real h index': IndicesCalculation.real_h_index(citation, pubid),   
        'Normalized hi index': IndicesCalculation.Normalized_HI_index(citation, pubid, author)
        }


    # Clear existing rows in the parameter table
    for row in param_table.get_children():
        param_table.delete(row)

    # Insert the parameter data into the parameter table
    for key, value in author_indices.items():
        param_table.insert("", "end", values=(key, value))


def download_authors_csv():
    # Get the data from the table
    data = []
    for item in table.get_children():
        values = table.item(item, 'values')
        data.append(values)

    # Open a file dialog for saving the CSV file
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Authors_Puplication_info", "*.csv")])

    # Check if the user canceled the file dialog
    if not file_path:
        return

    # Write the data to the selected CSV file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Row Number", "Title", "Citation", "Year", "Authors"])
        writer.writerows(data)

    print(f"CSV file saved at '{file_path}'.")


def download_authors_publication_csv():
    # Get the data from the table
    data = []
    for item in param_table.get_children():
        values = param_table.item(item, 'values')
        data.append(values)

    # Open a file dialog for saving the CSV file
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Authors_Parameters", "*.csv")])

    # Check if the user canceled the file dialog
    if not file_path:
        return

    # Write the data to the selected CSV file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Parameter Name", "Parameter Value"])
        writer.writerows(data)

    print(f"CSV file saved at '{file_path}'.")


def scrape_google_scholar_publications(profile_url):
    # Define a function to fetch additional publications using AJAX requests
    def fetch_more_publications(url, start):
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        params = {
            "view_op": "list_works",
            "cstart": start,
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return response.text
        else:
            return None

    # Start with the first page
    start = 0

    # Initialize a list to store publication information
    publications = []

    # Initialize a set to keep track of seen publication titles
    seen_titles = set()

    # Initialize a counter for row numbers
    row_number = 1

    while True:
        page_content = fetch_more_publications(profile_url, start)

        if page_content is None:
            print("Failed to retrieve additional publications.")
            break

        soup = BeautifulSoup(page_content, "html.parser")

        # Locate the elements containing publication information
        publication_elements = soup.find_all("a", class_="gsc_a_at")
        publication_year_elements = soup.find_all("span", class_="gsc_a_h gsc_a_hc gs_ibl")
        author_list_elements = soup.find_all("div", class_="gs_gray")

        # Extract and store publication information
        for i in range(len(publication_elements)):
            publication_name = publication_elements[i].text
            publication_year = publication_year_elements[i].text if i < len(publication_year_elements) else ""

            # Locate the correct gs_gray element that follows the current gsc_a_at element
            current_publication = publication_elements[i]
            next_sibling = current_publication.find_next_sibling("div", class_="gs_gray")
            authors_text = next_sibling.text.strip() if next_sibling else ""

            # Extract citation from the parent element of the publication name
            citation_element = current_publication.find_parent("tr").find("td", class_="gsc_a_c")
            if citation_element.text.strip() == '':
                citation = '0'
            else:
                citation = citation_element.text.strip()

            # Check if the publication title has been seen before
            if publication_name not in seen_titles:
                # Split the authors_text by commas and count the authors
                authors = authors_text.split(',')
                num_authors = len(authors)

                publication_info = [
                    row_number,  # Row number starting from 1
                    publication_name,
                    citation,
                    publication_year,
                    num_authors  # Save the count of authors
                ]
                publications.append(publication_info)
                seen_titles.add(publication_name)
                row_number += 1  # Increment the row number

        # Check if there are more pages to load
        if len(publication_elements) < 10:  # Google Scholar typically loads 10 publications per page
            break

        # Update the starting point for the next request
        start += 10

    return publications

def populate_table():
    # Get the Google Scholar profile URL from the input field
    profile_url = url_entry.get()
    url_entry.delete(0, tk.END) 
    # Call the scraping function to get the publications
    publications = scrape_google_scholar_publications(profile_url)

    # Clear any existing rows in the table
    for row in table.get_children():
        table.delete(row)

    # Insert the publication data into the table
    for publication in publications:
        table.insert("", "end", values=publication)
    
# Create the main window
window = tk.Tk()
window.title("Google Scholar Publications")
window.geometry("1300x650")

# Create a frame for the left side of the window
center_frame = ttk.Frame(window)
center_frame.pack(side="top", padx=20, pady=10, fill="both")

# Create an input field for entering the Google Scholar profile URL
url_label = tk.Label(center_frame, text="Google Scholar URL:")
url_label.pack(anchor="center")
url_entry = tk.Entry(center_frame, width=50)
url_entry.pack(anchor="center")

# Create a button to fetch and display the publications
left_frame = ttk.Frame(window)
left_frame.pack(side="left", padx=10, fill="both")

fetch_button = tk.Button(left_frame, text="Fetch Author Publications", command=populate_table)
fetch_button.pack(anchor="center")

# Create a frame for the table and scrollbar within the left frame
table_frame = ttk.Frame(left_frame)
table_frame.pack(fill="both")

# Create a table to display the publication information with styling
style = ttk.Style()
style.configure("Custom.Treeview", background="white", fieldbackground="white")
columns = ("Publication Id", "Title", "Citation", "Year", "Authors")
table = ttk.Treeview(table_frame, columns=columns, show="headings", height=25, style="Custom.Treeview")
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100)
table.pack(side="left", fill="both")

# Create a vertical scrollbar for the table
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
scrollbar.pack(side="right", fill="y")
table.configure(yscrollcommand=scrollbar.set)

# Create a button to download CSV
download_button = tk.Button(left_frame, text="Download Authors Data In CSV", command=download_authors_csv)
download_button.pack(anchor="center")

# Create a frame for the right side of the window
right_frame = ttk.Frame(window)
right_frame.pack(side="right", padx=30, fill="both")

calculate_button = tk.Button(right_frame, text="Calculate Author Indices", command=calculate_author_indices)
calculate_button.pack(anchor="center")

# Create a frame for the parameter table within the right frame
param_frame = ttk.Frame(right_frame)
param_frame.pack(fill="both")

# Create a table to display parameter names and values
param_columns = ("Parameter Name", "Parameter Value")
param_table = ttk.Treeview(param_frame, columns=param_columns, show="headings", height=25)
for col in param_columns:
    param_table.heading(col, text=col)
    param_table.column(col, width=220)
param_table.pack()

param_scrollbar = ttk.Scrollbar(param_frame, orient="vertical", command=param_table.yview)
param_table.configure(yscrollcommand=param_scrollbar.set)
param_table.pack(side="left", fill="both")
param_scrollbar.pack(side="right", fill="y")

# Create a button to download CSV
download_button = tk.Button(right_frame, text="Download Authors Parameters In CSV", command=download_authors_publication_csv)
download_button.pack(anchor="center")

# Start the GUI event loop
window.mainloop()