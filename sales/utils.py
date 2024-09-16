from books.models import Book   #you need to connect parameters from books model
from io import BytesIO 
import base64
import matplotlib.pyplot as plt
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

#define a function that takes the ID
def get_bookname_from_id(val):
    try:
        #this ID is used to retrieve the name from the record
        bookname = Book.objects.get(id=val).name
    except ObjectDoesNotExist:
        # If the book does not exist, return a default value
        bookname = "Unknown Book"
    #and the name is returned back
    return bookname

def get_graph():
    #create a BytesIO buffer for the image
    buffer = BytesIO()         

    #create a plot with a bytesIO object as a file-like object. Set format to png
    plt.savefig(buffer, format='png')

    #set cursor to the beginning of the stream
    buffer.seek(0)

    #retrieve the content of the file
    image_png=buffer.getvalue()

    #encode the bytes-like object
    graph=base64.b64encode(image_png)

    #decode to get the string as output
    graph=graph.decode('utf-8')

    #free up the memory of buffer
    buffer.close()

    #return the image/graph
    return graph

#chart_type: user input o type of chart,
#data: pandas dataframe
def get_chart(chart_type, data, **kwargs):
    #switch plot backend to AGG (Anti-Grain Geometry) - to write to file
    #AGG is preferred solution to write PNG files
    plt.switch_backend('AGG')  
    # Format the date_created column to a more readable format
    data['date_created'] = data['date_created'].apply(lambda x: x.strftime('%B %d, %Y'))
        # Retrieve book names using the get_bookname_from_id function
    data['book_name'] = data['book_id'].apply(get_bookname_from_id)
    #specify figure size
    fig, ax = plt.subplots(figsize=(6, 3))  # Use fig and ax for more control

    #select chart_type based on user input from the form
    if chart_type == '#1':
        print(data[['book_name', 'quantity']])  # Debug: Print data for bar chart
        ax.bar(data['book_name'], data['quantity'])
        ax.set_xlabel('Book Name')
        ax.set_ylabel('Quantity')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

    elif chart_type == '#2':
        #generate pie chart based on the price.
        #The book IDs are sent from the view as labels
        labels = kwargs.get('labels')
        # Retrieve book names using the get_bookname_from_id function
        book_names = [get_bookname_from_id(label) for label in labels]        
        # Debug: Print the book names
        print("Book names:", book_names)
        ax.pie(data['price'], labels=book_names, autopct='%1.1f%%')  # Add percentage display

    elif chart_type == '#3':
        print(data[['book_name', 'price']])  # Debug: Print data for line chart
        ax.plot(data['book_name'], data['price'])
        ax.set_xlabel('Book Name')
        ax.set_ylabel('Price')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    else:
        print('unknown chart type')

    #specify layout details
    plt.tight_layout()
    #render the graph to file
    chart = get_graph() 
    return chart