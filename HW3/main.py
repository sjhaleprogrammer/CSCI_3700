from flask import Flask, render_template
import util

# create an application instance
# all requests it receives from clients to this object for handling
# we are instantiating a Flask object by passing __name__ argument to the Flask constructor. 
# The Flask constructor has one required argument which is the name of the application package. 
# Most of the time __name__ is the correct value. The name of the application package is used 
# by Flask to find static assets, templates and so on.
app = Flask(__name__)

# evil global variables
# can be placed in a config file
# here is a possible tutorial how you can do this
username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

# route is used to map a URL with a Python function
# complete address: ip:port/
# 127.0.0.1:5000/
@app.route('/')
# this is how you define a function in Python
def index():
    # this is your index page
    # connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # execute SQL commands
    record = util.run_and_fetch_sql(cursor, "SELECT * from customer;")
    if record == -1:
        # you can replace this part with a 404 page
        print('Something is wrong with the SQL command')
    else:
        # this will return all column names of the select result table
        # ['customer_id','store_id','first_name','last_name','email','address_id','activebool','create_date','last_update','active']
        col_names = [desc[0] for desc in cursor.description]
        # only use the first five rows
        log = record[:5]
        # log=[[1,2],[3,4]]
    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    # using render_template function, Flask will search
    # the file named index.html under templates folder
    return render_template('index.html', sql_table = log, table_title=col_names)


@app.route('/api/update_basket_a/')
def update_basket_a():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    
    record = ''
    try:
        cursor.execute("INSERT INTO basket_a VALUES (5, 'Cherry');")
        cursor.connection.commit()
        record = "Success!"
    except(Exception, util.Error) as error:
        record = f"Error while executing SQL code: {error}"

    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    
    return render_template('update_basket_a.html', output = record)

@app.route('/api/unique/')
def unique():
	cursor, connection = util.connect_to_db(username,password,host,port,database)
	
	record = util.run_and_fetch_sql("SELECT fruit_a FROM basket_a UNION SELECT fruit_b FROM basket_b")
    if record == -1:
        # you can replace this part with a 404 page
        print('Something is wrong with the SQL command')
    else:
        # this will return all column names of the select result table
        col_names = [desc[0] for desc in cursor.description]
        # only use the first seven rows
        log = record[:7]	
	# disconnect from database
    util.disconnect_from_db(connection,cursor)
   	# using render_template function, Flask will search
    # the file named unique.html under templates folder
    return render_template('unique.html', sql_table = log, table_title=col_names)


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

