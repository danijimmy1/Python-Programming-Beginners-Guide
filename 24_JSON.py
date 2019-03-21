# JSON : JavaScript Object Notation
import json

# Load json data from file use json.load(f)
# Load json data from string use json.loads(s)
# Write json object to a file use json.dump(j, f)
# Output json object as string

# Loading the json data from the file created 24_movie_1.txt
json_file = open('./24_movie_1.txt', "r", encoding = "utf-8")
movie = json.load(json_file)
json_file.close()
print(movie)
print("+"*80)
print(movie['office'])

print("*+"*80)
# Loading json data using json.loads(s)
value  = """
            {
                "title" : "Tron: Legacy",
                "composer" : "Daft Punk",
                "release_year" : 2010,
                "budget" : 17000000,
                "actors" : null,
                "won_oscar": false
            }
        """
tron = json.loads(value)
print(tron)

print("@"*80)
# To cnvert dictionary into valid json string use json.dumps()
print(json.dumps(movie))

print("&"*80)
# Writing data to a file
movie2 = {}
movie2["title"] = "Minority Report"
movie2["director"] = "Steven Spielberg"
movie2["composer"] = "John Williams"
movie2["actors"] = ["Tom Cruise", "Colin Farrell", "Samantha Morton", "Max Von Sydow"]
movie2["is_awesome"] = True
movie2["buget"] = 102000000
movie2["cinematographer"] = "Janusz Kami\u0144ski"
file2 = open("./24_movie_2.txt", "w", encoding = "utf-8")
json.dump(movie2, file2, ensure_ascii = False)
file2.close()
print("JSON File saved successfully!!!")