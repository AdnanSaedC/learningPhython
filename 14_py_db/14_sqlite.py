import sqlite3
# it is a lightweight db comes with python

# creating a connection
connection = sqlite3.connect('youtube_videos.db')

# cursor is used to perform operation on the db
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS video(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
               )
""")

# __ means dundher


def add_video():
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    cursor.execute("INSERT INTO video(name,time) VALUES (?,?)",(name,time))
    connection.commit()

def list_all_videos():
    print("\n\n")
    # here cursor object hold everything
    cursor.execute("SELECT * FROM video")
    for row in cursor.fetchall():
        print(row)

def update_video():
    list_all_videos()
    name = input("Enter new name: ")
    time = input("Enter new time: ")
    id = input("Enter the id: ")
    cursor.execute("UPDATE video SET name=?,time=? WHERE id=?",(name,time,id))
    connection.commit()
        
    


def delete_video():
    list_all_videos()
    user_index = int(input("Enter the index of the dic you want to delete: "))
    cursor.execute("delete from video where id = ?",(user_index,))
    # when you are giving a single parameter then use comma because without comma tuple wont form
    connection.commit()




def main():
    while True:
        print("\nYouTube Manager")
        print("please select an option: ")
        print("1. Add Video")
        print("2. View Videos")
        print("3. update Video")
        print("4. delete Video")
        print("5. exit")

        userChoice = int(input("Enter your choice (1-5): "))
        match userChoice:
            case 1:
                add_video()
            case 2:
                list_all_videos()
            case 3:
                update_video()
            case 4:
                delete_video()
            case 5:
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")
    connection.close()

if __name__ == "__main__":
    main()

# thisis the standard practice it makes the file run only this file is bein run not when this file is being imported simple