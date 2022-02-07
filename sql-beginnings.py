import sqlite3


db = 'my.db'
con = sqlite3.connect(db)
cursor = con.cursor()


# todo: change to dictionary and then convert to this command,
# ideally encapsulating CREATE TABLE IF NOT EXISTS into its own function
# someone has surely done this before, but it's a great exercise even if so

create_table_cmd = """CREATE TABLE IF NOT EXISTS logs (
                             id INT AUTO_INCREMENT PRIMARY KEY DEFAULT 0,
                             duration_given INT NOT NULL,
                             start_time TIMESTAMP,
                             end_time TIMESTAMP,
                             label varchar(500),
                             type varchar(20)
);
"""

cursor.execute(create_table_cmd)

con.commit()




def insert_new_pomo_row(duration, label, pomo_type):
    current_time = "help"

    cursor.execute("INSERT INTO logs (duration_given, label, type) VALUES (" + str(duration) + ", '" + label + "', '" + pomo_type + "') ;")

# it would be better to take a dict! just require that certain keys be present somehow?




sample_cols = [
    "id", 
    "duration_given", 
    "start_time", 
    "end_time", 
    "label", 
    "type"
]

# [a for a in cursor.execute("SELECT " + ', '.join(sample_cols) + " FROM logs;")]


def select(table, field_list):
    return [record for record in
            cursor.execute("SELECT " + ', '.join(field_list) + " FROM " + table + ";")]




# next step: add a variable storing the default pomo length, reading
# from an environment variable or falling back to 25m

# next step: write a function that takes (a) a label and (b) a length
# for the pomodoro, and outputs a dicitonary containing
# - the start time
# - the pomo's length
# - the pomo's type
# - the pomo label