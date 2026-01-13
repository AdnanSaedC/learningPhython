# file = open('youtube.txt','w')

# try:
#     file.write("hi")
# finally:
#     file.close()

# this was the old syntax the new one is
# with open('youtube.txt','w') as file:
#     file.write("hello")

# look another thing is json is not an object it an be string array etc

import json

fileName = 'youtube.txt'

def load_data():
    try: #we have added try except because we wantef to handle a specific exception case
        with open(fileName,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def save_data_helper(videos):
    with open(fileName,'w') as file: #we are overwrite the file here because json doesnot works well with append {[]} might be {[]}{[]} for next time
        json.dump(videos,file)


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    if name is None and time is None:
        exit()

    
    videos.append({"name":name,"time":time})
    save_data_helper(videos)

def list_all_videos(videos):
    print("\n\n")
    for index,video in enumerate(videos,start=1):
        print(f"{index}-{video['name']}-{video['time']}")
    print("\n\n")

def update_video(videos):
    list_all_videos(videos)
    user_index = int(input("Enter the index of the dic you want to update: "))
    if user_index >= 1 and user_index<= len(videos):
        videos[user_index-1]['name'] = input("Enter new name: ") #look the actual video list is diffrent and the list in which we are operating while display is diffrent
        videos[user_index-1]['time'] = input("Enter new time: ")
        save_data_helper(videos)
        print("updated successfully")
    else:
        print("Invalid index")
        
    


def delete_video(videos):
    list_all_videos(videos)
    user_index = int(input("Enter the index of the dic you want to delete: "))
    if user_index >= 1 and user_index<= len(videos):
        del videos[user_index-1]
        save_data_helper(videos)
        print("deleted successfully")
    else:
        print("Invalid index")




def main():
    videos=load_data()
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
                add_video(videos)
            case 2:
                list_all_videos(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

# thisis the standard practice it makes the file run only this file is bein run not when this file is being imported simple