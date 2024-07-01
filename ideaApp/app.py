from flask import Flask, request



app= Flask(__name__)

#Create the Idea repository. This where ideas will be Store
ideas={
    1:{
        "id":1,
        "idea_name":"ONDC",
        "idea_description":"Details about ONDC",
        "idea_author":"Govind"
    },
    2:{
        "id":2,
        "idea_name":"Save Soil",
        "idea_description":"Details about Saving Soil",
        "idea_author":"Ankit Sharma"
    }
    }

'''
Create an RESTfull endpoint for fetching all the ideas
'''
@app.get("/ideaapp/api/v1/ideas")
def get_all_ideas():
    #I need to read the query param
    idea_author=request.args.get("idea_author")

    if idea_author:
        #Filter the idea created by this author
        idea_res={}
        for key,value in ideas.items():
            if value["idea_author"]==idea_author:
                idea_res[key]=value
        return idea_res
    #Logit to fetch all the ideas and support query params
    return ideas

'''
Create a RESTful endpoint for creating a new idea
'''
@app.post("/ideaapp/api/v1/ideas")
def create_idea():
    #Logic to create a new idea
    try:
        #first read the request body
        request_body=request.get_json()

        #Check if the idea id passed is not present already
        if request_body["id"] and request_body["id"] in ideas:
            return "idea with the same id already present",400

        #Insert the passed idea in the ideas dictionary 
        ideas[request_body["id"]]=request_body

        #return the response saying idea got saved
        return "idea created and saved successfully",201
    except KeyError:
        return "id is missing",400
    except :
        "Some internal server error",500
'''
End point to fetch idea based on the idea id
'''
@app.get("/ideaapp/api/v1/ideas/<idea_id>")
def get_idea_id(idea_id):
    try:
        if int(idea_id) in ideas:
            return ideas[int(idea_id)],200
        else:
            return "idea id passed is not present",400
    except:
        return "Some internal error happend",500
'''
Endpoint for updating the idea
'''
@app.put("/ideaapp/api/v1/ideas/<idea_id>")
def update_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas[int(idea_id)]=request.get_json()
            return ideas[int(idea_id)],200
        else:
            return "idea id passed is not present",400
    except:
        return "Some internal error happend",500
'''
Endpoint to delete an idea
'''
@app.delete("/ideaapp/api/v1/ideas/<idea_id>")
def delete_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas.pop(int(idea_id))
            return "idea got successfully removed"
        else:
            return "idea id passed is not present",400
    except:
        return "Some internal error happend",500
    



#If I want to run by default(without flask run)
if __name__=="__main__":
    app.run(port=9999)


