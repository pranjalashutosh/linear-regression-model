from collections import defaultdict
from collections import Counter

users = [
    {"id":0, "name":"Hero"},
    {"id":1, "name":"Dunn"},
    {"id":2, "name":"Sun"},
    {"id":3, "name":"Chi"},
    {"id":4, "name":"Thor"},
    {"id":5, "name":"Clive"},
    {"id":6, "name":"Hicks"},
    {"id":7, "name":"Devin"},
    {"id":8, "name":"Kate"},
    {"id":9, "name":"Klein"},
]

interests = [
    (0,"Hadoop"),(0,"Big Data"),(0,"HBase"),(0,"Java"),(0,"Spark"),(0,"Storm"),(0,"Cassandra"),
    (1,"NoSQL"),(1,"MongoDB"),(1,"Cassandra"),(1,"HBase"),(1,"Postgres"),(2,"Python"),(2,"scikit-learn"),(2,"scipy"),
    (2,"numpy"),(2,"statsmodel"),(2,"pandas"),(3,"r"),(3,"python"),(3,"statistics"),
    (3,"regression"),(3,"probability"),(4,"machine learning"),(4,"decision trees"),(4,"regression"),(4,"libsm"),(5,"python"),(5,"R"),
    (5,"C++"),(5,"Java"),(5,"Haskell"),(5,"programming language"),(6,"statistics"),(6,"mathematics"),
    (6,"thoery"),(7,"machine learning"),(7,"scikit-learn"),(7,"mahout"),(7,"neural networks"),
    (8,"neural networks"),(8,"deep learning"),(8,"Big Data"),(8,"artificial intelligence"),
    (9,"Hadoop"),(9,"Java"),(9,"MapReduce"),(9,"Big Data")]

friendship_pairs = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

#making a friendship dict where user_id is the key and an empty list is being stored as the value. 
friendships = {user["id"]: [] for user in users}
#print(friendships)
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

#print(friendships)

def number_of_friends(user):
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users) # Iterating over users dict and passing user meaning every single user with ID and Key to to number_of_friend function 
#print(total_connections)

num_users = len(users)
avg_connections = total_connections/num_users

# Create a list of user_id and num of friends. 
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]


num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse = True)

"""key=lambda id_and_friends: id_and_friends[1]: This is a sorting key, which tells Python how to sort the list. 
The lambda function is used to extract the second element (id_and_friends[1]) 
from each tuple (user_id, number_of_friends) in the list. 
The second element represents the number of friends."""

#print(num_friends_by_id) # Each pair is user ID and number od friends.


# to know frnds of frnds. 
def friends_of_frnds(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id and foaf_id not in friendships[user_id]
        )
#print("Friends of friends")
#print(friends_of_frnds(users[0]))

def data_scientist_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]

user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
#print(user_ids_by_interest)

interest_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interest_by_user_id[user_id].append(interest)

#print(interest_by_user_id)



#finding out who has the most interest in common (my own try)
"""
comm = defaultdict(list)

def common_interest(user):
    user_id = user["id"]
    for userids in user_ids_by_interest.values():
        
        if user_id in userids:
            for id in userids:
                if id != user_id:
                    comm[id].append(user_id)
    return comm
            
print(common_interest(users[9]))    
"""

def most_common_interest(user):
    return Counter(
        interested_user_id
        for interest in interest_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )
#print("Most Common Interest")
#print(most_common_interest(users[0]))

interest_Counts = {interest: [] for interest in user_ids_by_interest}

for interest in user_ids_by_interest:
    interest_Counts[interest].append(len(user_ids_by_interest[interest]))

#print(dict(sorted(interest_Counts.items(), key=lambda item:item[1], reverse = True))) 


# Read more in chapter 23

words_and_counts = Counter(word for user, interest in interests for word in interest.lower().split()) 

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)